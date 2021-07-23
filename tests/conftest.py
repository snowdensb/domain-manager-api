"""
pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""
# Third-Party Libraries
import pytest

# cisagov Libraries
from api.main import app

MAIN_SERVICE_NAME = "api"


@pytest.fixture(scope="session")
<<<<<<< HEAD
def client():
    """Get fixture for client."""
    app.config["TESTING"] = True
    app.config["BCRYPT_LOG_ROUNDS"] = 4
    app.config["WTF_CSRF_ENABLED"] = False
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
=======
def main_container(dockerc):
    """Return the main container from the Docker composition."""
    # find the container by name even if it is stopped already
    return dockerc.containers(service_names=[MAIN_SERVICE_NAME], stopped=True)[0]
>>>>>>> c6aa7f05b09191075d195f0743dd0f4d36f3920c

    yield testing_client
    ctx.pop()

<<<<<<< HEAD
=======
@pytest.fixture(scope="session")
def version_container(dockerc):
    """Return the version container from the Docker composition.
>>>>>>> c6aa7f05b09191075d195f0743dd0f4d36f3920c

@pytest.fixture(scope="session")
def main_container(dockerc):
    """Return the main container from the docker composition."""
    # find the container by name even if it is stopped already
    return dockerc.containers(service_names=[MAIN_SERVICE_NAME], stopped=True)[0]


def pytest_addoption(parser):
    """Add new commandline options to pytest."""
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify collected tests based on custom marks and commandline options."""
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
