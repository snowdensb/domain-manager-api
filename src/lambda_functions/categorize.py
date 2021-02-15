"""Categorize Lambda Function."""
# Standard Python Libraries
import json

# Third-Party Libraries
from selenium import webdriver

# cisagov Libraries
from api.manager import DomainManager
from api.views import CATEGORIES, PROXIES
from settings import BROWSERLESS_ENDPOINT, TWO_CAPTCHA_API_KEY, logger
from utils.proxies.proxies import get_categorize_proxy_func

domain_manager = DomainManager()


def handler(event, context):
    """Handle SQS categorize event."""
    for record in event["Records"]:
        payload = json.loads(record["body"])

        domain = domain_manager.get(filter_data={"name": payload["domain"]})
        if not domain:
            logger.error(f"Domain {payload['domain']} does not exist.")
            continue

        proxy = [proxy for proxy in PROXIES if proxy["name"] == payload["proxy"]][0]

        proxy_func = get_categorize_proxy_func(proxy["name"])
        proxy_category = get_proxy_category(proxy["name"], payload["category"])
        if not proxy_category:
            logger.error(f"Category {payload['category']} does not exist")
            continue

        resp = process(proxy_func, proxy_category, domain["name"])
        if resp:
            domain_manager.add_to_list(
                document_id=domain["_id"],
                field="is_category_submitted",
                data={
                    "name": proxy["name"],
                    "is_categorized": False,
                },
            )
            logger.info(
                f"{domain['name']} has been successfully submitted for categorization at {proxy['name']}"
            )
        else:
            logger.info(
                f"{domain['name']} has failed submitting for categorization at {proxy['name']}"
            )


def get_proxy_category(proxy_name, category_name):
    """Get category for proxy."""
    category = [
        category for category in CATEGORIES if category["name"] == category_name.title()
    ][0]
    if not category:
        return None
    return "".join(
        detail.get(proxy_name)
        for detail in category.get("proxies")
        if proxy_name in detail
    )


def process(proxy_func, proxy_category, domain_name):
    """Categorize domain."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    try:
        driver = webdriver.Remote(
            command_executor=f"http://{BROWSERLESS_ENDPOINT}/webdriver",
            desired_capabilities=chrome_options.to_capabilities(),
        )
        driver.set_page_load_timeout(60)
        proxy_func(
            driver=driver,
            domain=domain_name,
            category=proxy_category,
            two_captcha_api_key=TWO_CAPTCHA_API_KEY,
        )
        driver.quit()
        return True
    except Exception as e:
        driver.quit()
        logger.exception(e)
        return False