"""__init__."""

CATEGORIES = [
    {
        "name": "Activist Groups",
        "proxies": [
            {"Blue Coat": "Activist Groups"},
            {"Trusted Source": "Politics/Opinion"},
            {"fortiguard": "Political Organizations"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Politics"},
        ],
    },
    {
        "name": "Advertising",
        "proxies": [
            {"Blue Coat": "Activist Groups"},
            {"Trusted Source": "Web Ads/Analytics"},
            {"fortiguard": "Advertising"},
            {"Palo Alto Networks": "Web Advertisements"},
            {"Trend Micro": "Web Advertisements"},
        ],
    },
    {
        "name": "Advocacy Organizations",
        "proxies": [
            {"Blue Coat": "Political/Social Advocacy"},
            {"Trusted Source": "Politics/Opinion"},
            {"fortiguard": "Advocacy Organizations"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Politics"},
        ],
    },
    {
        "name": "Alternative Beliefs",
        "proxies": [
            {"Trusted Source": "Religion/Ideology"},
            {"Blue Coat": "Alternative Spirituality/Belief"},
            {"fortiguard": "Alternative Beliefs"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Alternative Journals"},
        ],
    },
    {
        "name": "Art",
        "proxies": [
            {"Trusted Source": "Art/Culture/Heritage"},
            {"Blue Coat": "Art/Culture"},
            {"fortiguard": "Arts and Culture"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "Arts"},
        ],
    },
    {
        "name": "Auction",
        "proxies": [
            {"Trusted Source": "Auctions/Classifieds"},
            {"Blue Coat": "Auctions"},
            {"fortiguard": "Auction"},
            {"Palo Alto Networks": "Auctions"},
            {"Trend Micro": "Auctions"},
        ],
    },
    {
        "name": "Blogs",
        "proxies": [
            {"Trusted Source": "Blogs/Wiki"},
            {"Blue Coat": "Social Networking"},
            {"fortiguard": "Social Networking"},
            {"Palo Alto Networks": "Social Networking"},
            {"Trend Micro": "Blogs / Web Communications"},
        ],
    },
    {
        "name": "Financial Brokerage",
        "proxies": [
            {"Trusted Source": "Finance/Banking"},
            {"Blue Coat": "Brokerage/Trading"},
            {"fortiguard": "Brokerage and Trading"},
            {"Palo Alto Networks": "Business and Economy"},
            {"Trend Micro": "Brokerages / Trading"},
        ],
    },
    {
        "name": "Business",
        "proxies": [
            {"Trusted Source": "Business"},
            {"Blue Coat": "Business/Economy"},
            {"fortiguard": "Business"},
            {"Palo Alto Networks": "Business and Economy"},
            {"Trend Micro": "Business / Economy"},
        ],
    },
    {
        "name": "Charitable Organizations",
        "proxies": [
            {"Trusted Source": "Business"},
            {"Blue Coat": "Charitable/Non-Profit"},
            {"fortiguard": "Charitable Organizations"},
            {"Palo Alto Networks": "Business and Economy"},
            {"Trend Micro": "Business / Economy"},
        ],
    },
    {
        "name": "Chat",
        "proxies": [
            {"Trusted Source": "Chat"},
            {"Blue Coat": "Chat (IM)/SMS"},
            {"fortiguard": "Instant Messaging"},
            {"Palo Alto Networks": "Internet Communications and Telephony"},
            {"Trend Micro": "Chat / Instant Messaging"},
        ],
    },
    {
        "name": "Computers / Internet",
        "proxies": [
            {"Trusted Source": "Internet Services"},
            {"Blue Coat": "Computer/Information Security"},
            {"fortiguard": "Information Technology"},
            {"Palo Alto Networks": "Computer and Internet Info"},
            {"Trend Micro": "Computers / Internet"},
        ],
    },
    {
        "name": "Content Delivery Networks",
        "proxies": [
            {"Trusted Source": "Content Server"},
            {"Blue Coat": "Content Delivery Networks"},
            {"fortiguard": "Content Servers"},
            {"Palo Alto Networks": "Content Delivery Networks"},
            {"Trend Micro": "Pay to Surf"},
        ],
    },
    {
        "name": "Dating",
        "proxies": [
            {"Trusted Source": "Dating/Personals"},
            {"Blue Coat": "Personals/Dating"},
            {"fortiguard": "Dating"},
            {"Palo Alto Networks": "Dating"},
            {"Trend Micro": "Personals / Dating"},
        ],
    },
    {
        "name": "Education",
        "proxies": [
            {"Trusted Source": "Education/Reference"},
            {"Blue Coat": "Education"},
            {"fortiguard": "Education"},
            {"Palo Alto Networks": "Educational Institutions"},
            {"Trend Micro": "Education"},
        ],
    },
    {
        "name": "Entertainment",
        "proxies": [
            {"Trusted Source": "Entertainment"},
            {"Blue Coat": "Entertainment"},
            {"fortiguard": "Entertainment"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "Entertainment"},
        ],
    },
    {
        "name": "Finance",
        "proxies": [
            {"Trusted Source": "Finance/Banking"},
            {"Blue Coat": "Finance"},
            {"fortiguard": "Finance and Banking"},
            {"Palo Alto Networks": "Financial Services"},
            {"Trend Micro": "Financial Services"},
        ],
    },
    {
        "name": "For Kids",
        "proxies": [
            {"Trusted Source": "For Kids"},
            {"Blue Coat": "For Kids"},
            {"fortiguard": "Child Education"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "For Kids"},
        ],
    },
    {
        "name": "Games",
        "proxies": [
            {"Trusted Source": "Games"},
            {"Blue Coat": "Games"},
            {"fortiguard": "Games"},
            {"Palo Alto Networks": "Games"},
            {"Trend Micro": "Games"},
        ],
    },
    {
        "name": "News",
        "proxies": [
            {"Trusted Source": "General News"},
            {"Blue Coat": "News"},
            {"fortiguard": "News and Media"},
            {"Palo Alto Networks": "News"},
            {"Trend Micro": "News / Media"},
        ],
    },
    {
        "name": "Government",
        "proxies": [
            {"Trusted Source": "Government/Military"},
            {"Blue Coat": "Government/Legal"},
            {"fortiguard": "Government and Legal Organizations"},
            {"Palo Alto Networks": "Government"},
            {"Trend Micro": "Government / Legal"},
        ],
    },
    {
        "name": "Health",
        "proxies": [
            {"Trusted Source": "Health"},
            {"Blue Coat": "Health"},
            {"fortiguard": "Health and Wellness"},
            {"Palo Alto Networks": "Health and Medicine"},
            {"Trend Micro": "Health"},
        ],
    },
    {
        "name": "Humor",
        "proxies": [
            {"Trusted Source": "Humor/Comics"},
            {"Blue Coat": "Humor/Jokes"},
            {"fortiguard": "Entertainment"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "Humor"},
        ],
    },
    {
        "name": "Hunting and Fishing",
        "proxies": [
            {"Trusted Source": "Entertainment"},
            {"Blue Coat": "Entertainment"},
            {"fortiguard": "Entertainment"},
            {"Palo Alto Networks": "Hunting and Fishing"},
            {"Trend Micro": "Gun Clubs / Hunting"},
        ],
    },
    {
        "name": "Job Search",
        "proxies": [
            {"Trusted Source": "Job Search"},
            {"Blue Coat": "Job Search/Careers"},
            {"fortiguard": "Job Search"},
            {"Palo Alto Networks": "Job Search"},
            {"Trend Micro": "Job Search / Careers"},
        ],
    },
    {
        "name": "Military",
        "proxies": [
            {"Trusted Source": "Government/Military"},
            {"Blue Coat": "Military"},
            {"fortiguard": "Armed Forces"},
            {"Palo Alto Networks": "Military"},
            {"Trend Micro": "Military"},
        ],
    },
    {
        "name": "Politics/Opinion",
        "proxies": [
            {"Trusted Source": "Politics/Opinion"},
            {"Blue Coat": "Political/Social Advocacy"},
            {"fortiguard": "Political Organizations"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Politics"},
        ],
    },
    {
        "name": "Real Estate",
        "proxies": [
            {"Trusted Source": "Real Estate"},
            {"Blue Coat": "Real Estate"},
            {"fortiguard": "Real Estate"},
            {"Palo Alto Networks": "Real Estate"},
            {"Trend Micro": "Real Estate"},
        ],
    },
    {
        "name": "Religion",
        "proxies": [
            {"Trusted Source": "Religion/Ideology"},
            {"Blue Coat": "Religion"},
            {"fortiguard": "Global Religion"},
            {"Palo Alto Networks": "Religion"},
            {"Trend Micro": "Religion"},
        ],
    },
    {
        "name": "Restaurants",
        "proxies": [
            {"Trusted Source": "Restaurants"},
            {"Blue Coat": "Restaurants/Food"},
            {"fortiguard": "Restaurant and Dining"},
            {"Palo Alto Networks": "Shopping"},
            {"Trend Micro": "Restaurants / Food"},
        ],
    },
    {
        "name": "Search Engines",
        "proxies": [
            {"Trusted Source": "Search Engines"},
            {"Blue Coat": "Search Engines/Portals"},
            {"fortiguard": "Search Engines and Portals"},
            {"Palo Alto Networks": "Search Engines"},
            {"Trend Micro": "Search Engines / Portals"},
        ],
    },
    {
        "name": "Shopping",
        "proxies": [
            {"Trusted Source": "Online Shopping"},
            {"Blue Coat": "Shopping"},
            {"fortiguard": "Shopping"},
            {"Palo Alto Networks": "Shopping"},
            {"Trend Micro": "Shopping"},
        ],
    },
    {
        "name": "Social Networking",
        "proxies": [
            {"Trusted Source": "Social Networking"},
            {"Blue Coat": "Social Networking"},
            {"fortiguard": "Social Networking"},
            {"Palo Alto Networks": "Social Networking"},
            {"Trend Micro": "Social Networking"},
        ],
    },
    {
        "name": "Sports",
        "proxies": [
            {"Trusted Source": "Sports"},
            {"Blue Coat": "Sports/Recreation"},
            {"fortiguard": "Sports"},
            {"Palo Alto Networks": "Sports"},
            {"Trend Micro": "Sports"},
        ],
    },
    {
        "name": "Travel",
        "proxies": [
            {"Trusted Source": "Travel"},
            {"Blue Coat": "Travel"},
            {"fortiguard": "Travel"},
            {"Palo Alto Networks": "Travel"},
            {"Trend Micro": "Travel"},
        ],
    },
    {
        "name": "Web Hosting",
        "proxies": [
            {"Trusted Source": "Internet Services"},
            {"Blue Coat": "Web Hosting"},
            {"fortiguard": "Web Hosting"},
            {"Palo Alto Networks": "Web Hosting"},
            {"Trend Micro": "Web Hosting"},
        ],
    },
]

PROXIES = [
    {
        "categories": [
            "Art/Culture/Heritage",
            "Auctions/Classifieds",
            "Blogs/Wiki",
            "Business",
            "Chat",
            "Consumer Protection",
            "Content Server",
            "Dating/Personals",
            "Digital Postcards",
            "Discrimination",
            "Education/Reference",
            "Entertainment",
            "Fashion/Beauty",
            "Finance/Banking",
            "For Kids",
            "Forum/Bulletin Boards",
            "Games",
            "General News",
            "Government/Military",
            "Health",
            "Historical Revisionism",
            "Humor/Comics",
            "Information Security",
            "Instant Messaging",
            "Interactive Web Applications",
            "Internet Radio/TV",
            "Internet Services",
            "Job Search",
            "Major Global Religions",
            "Marketing/Merchandising",
            "Media Downloads",
            "Media Sharing",
            "Messaging",
            "Mobile Phone",
            "Moderated",
            "Motor Vehicles",
            "Non-Profit/Advocacy/NGO",
            "Online Shopping",
            "P2P/File Sharing",
            "Personal Network Storage",
            "Personal Pages",
            "Pharmacy",
            "Politics/Opinion",
            "Portal Sites",
            "Profanity",
            "Professional Networking",
            "Public Information",
            "Real Estate",
            "Recreation/Hobbies",
            "Religion/Ideology",
            "Remote Access",
            "Residential IP Addresses",
            "Resource Sharing",
            "Restaurants",
            "School Cheating Information",
            "Search Engines",
            "Shareware/Freeware",
            "Social Networking",
            "Software/Hardware",
            "Sports",
            "Stock Trading",
            "Streaming Media",
            "Technical Information",
            "Technical/Business Forums",
            "Text Translators",
            "Text/Spoken Only",
            "Travel",
            "Visual Search Engines",
            "Web Ads",
            "Web Mail",
            "Web Meetings",
            "Web Phone",
        ],
        "name": "Trusted Source",
        "url": "https://trustedsource.org/",
    },
    {
        "categories": [
            "Alternative Spirituality/Belief",
            "Art/Culture",
            "Auctions",
            "Audio/Video Clips",
            "Brokerage/Trading",
            "Business/Economy",
            "Charitable/Non-Profit",
            "Chat (IM)/SMS",
            "Computer/Information Security",
            "Content Delivery Networks",
            "Dynamic DNS Host",
            "E-Card/Invitations",
            "Education",
            "Email",
            "Entertainment",
            "File Storage/Sharing",
            "Finance",
            "For Kids",
            "Games",
            "Government/Legal",
            "Health",
            "Humor/Jokes",
            "Internet Connected Devices",
            "Internet Telephony",
            "Job Search/Careers",
            "Media Sharing",
            "Military",
            "News",
            "Newsgroups/Forums",
            "Office/Business Applications",
            "Online Meetings",
            "Peer-to-Peer (P2P)",
            "Personal Sites",
            "Personals/Dating",
            "Placeholders",
            "Political/Social Advocacy",
            "Radio/Audio Streams",
            "Real Estate",
            "Reference",
            "Religion",
            "Remote Access",
            "Restaurants/Food",
            "Search Engines/Portals",
            "Shopping",
            "Social Networking",
            "Society/Daily Living",
            "Software Downloads",
            "Sports/Recreation",
            "Technology/Internet",
            "Translation",
            "Travel",
            "TV/Video Streams",
            "Vehicles",
            "Web Ads/Analytics",
            "Web Hosting",
            "Web Infrastructure",
            "I Don't Know",
        ],
        "name": "Blue Coat",
        "url": "https://sitereview.bluecoat.com/#/",
    },
    {
        "categories": [
            "Advertising",
            "Advocacy Organizations",
            "Alternative Beliefs",
            "Armed Forces",
            "Arts and Culture",
            "Auction",
            "Brokerage and Trading",
            "Business",
            "Charitable Organizations",
            "Child Education",
            "Content Servers",
            "Dating",
            "Digital Postcards",
            "Dynamic Content",
            "Dynamic DNS",
            "Education",
            "Entertainment",
            "File Sharing and Storage",
            "Finance and Banking",
            "Folklore",
            "Freeware and Software Downloads",
            "Games",
            "General Organizations",
            "Global Religion",
            "Government and Legal Organizations",
            "Health and Wellness",
            "Information Technology",
            "Information and Computer Security",
            "Instant Messaging",
            "Internet Radio and TV",
            "Internet Telephony",
            "Job Search",
            "Medicine",
            "News and Media",
            "Newsgroups and Message Boards",
            "Online Meeting",
            "Peer-to-peer File Sharing",
            "Personal Privacy",
            "Personal Vehicles",
            "Personal Websites and Blogs",
            "Plagiarism",
            "Political Organizations",
            "Real Estate",
            "Reference",
            "Remote Access",
            "Restaurant and Dining",
            "Search Engines and Portals",
            "Secure Websites",
            "Shopping",
            "Social Networking",
            "Society and Lifestyles",
            "Sports",
            "Sports Hunting and War Games",
            "Streaming Media and Download",
            "Travel",
            "Web Analytics",
            "Web Chat",
            "Web Hosting",
            "Web-based Applications",
            "Web-based Email",
        ],
        "name": "Fortiguard",
        "url": "https://www.fortiguard.com/faq/wfratingsubmit",
    },
    {
        "categories": [
            "Auctions",
            "Business and Economy",
            "Command and Control",
            "Computer and Internet Info",
            "Content Delivery Networks",
            "Dating",
            "Dynamic DNS",
            "Educational Institutions",
            "Entertainment and Arts",
            "Financial Services",
            "Games",
            "Government",
            "Health and Medicine",
            "Home and Garden",
            "Hunting and Fishing",
            "Internet Communications and Telephony",
            "Internet Portals",
            "Job Search",
            "Legal",
            "Military",
            "Motor Vehicles",
            "Music",
            "News",
            "Online Storage and Backup",
            "Personal Sites and Blogs",
            "Philosophy and Political Advocacy",
            "Private IP Addresses",
            "Real Estate",
            "Recreation and Hobbies",
            "Reference and Research",
            "Religion",
            "Search Engines",
            "Shareware and Freeware",
            "Shopping",
            "Social Networking",
            "Society",
            "Sports",
            "Stock Advice and Tools",
            "Streaming Media",
            "Training and Tools",
            "Travel",
            "Web Advertisements",
            "Web Hosting",
            "Web-based Email",
        ],
        "name": "Palo Alto Networks",
        "url": "https://urlfiltering.paloaltonetworks.com/",
    },
    {
        "categories": [
            "Business / Economy",
            "Financial Services",
            "Brokerages / Trading",
            "Job Search / Careers",
            "Shopping",
            "Auctions",
            "Real Estate",
            "Dynamic DNS",
            "Internet Telephony",
            "Search Engines / Portals",
            "Internet Infrastructure",
            "Blogs / Web Communications",
            "Communications",
            "Social Networking",
            "Chat / Instant Messaging",
            "Email",
            "Newsgroups / Forum",
            "Coin Miners",
            "Web Hosting",
            "Education",
            "Government / Legal",
            "Military",
            "Politics",
            "Health",
            "Computers / Internet",
            "News / Media",
            "Translators / Cached Pages",
            "Reference",
            "Vehicles",
            "Disease Vector",
            "Web Advertisements",
            "Recreation / Hobbies",
            "Arts",
            "Entertainment",
            "Cultural Institutions",
            "Activist Groups",
            "Games",
            "Personals / Dating",
            "Religion",
            "Personal Sites",
            "Society / Lifestyle",
            "Gun Clubs / Hunting",
            "Restaurants / Food",
            "Sports",
            "Travel",
            "Humor",
            "For Kids",
            "Internet Radio and TV",
            "Photo Searches",
            "Sharing Services",
            "Peer-to-peer",
            "Streaming Media / MP3",
            "Ringtones / Mobile Phone Downloads",
            "Mobile Phone Downloads",
            "Software Downloads",
            "Pay to Surf",
        ],
        "name": "Trend Micro",
        "url": "https://global.sitesafety.trendmicro.com/",
    },
]
