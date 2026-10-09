import re
from urllib.parse import urlparse
import ipaddress
from difflib import SequenceMatcher


BRAND_NAMES = [
    "paypal",
    "microsoft",
    "google",
    "amazon",
    "apple"
]


# Extract URLs from a message
def extract_urls(message):

    pattern = r'https?://[^\s]+'

    urls = re.findall(pattern, message)

    cleaned_urls = []

    for url in urls:
        url = url.rstrip(".,!?;:)")
        cleaned_urls.append(url)

    return cleaned_urls


# Detect lookalike domains
def check_lookalike_domain(hostname):

    domain = hostname.lower().split(".")[0]

    parts = domain.replace("-", " ").replace("_", " ").split()

    for part in parts:

        for brand in BRAND_NAMES:

            similarity = SequenceMatcher(
                None,
                part,
                brand
            ).ratio()

            if similarity >= 0.80 and part != brand:
                return True

    return False


# Detect brand impersonation
def check_brand_impersonation(hostname):

    labels = hostname.lower().split(".")

    for brand in BRAND_NAMES:

        if brand in labels:

            if labels[-2] != brand:
                return True

    return False


# Analyze an individual URL
def analyze_url(url):

    parsed = urlparse(url)

    hostname = parsed.hostname

    result = {
        "url": url,
        "scheme": parsed.scheme,
        "hostname": hostname,
        "is_ip": False,
        "indicators": []
    }


    # IP-based URL detection
    if hostname:

        try:

            ipaddress.ip_address(hostname)

            result["is_ip"] = True

            result["indicators"].append(
                "IP-based URL"
            )

        except ValueError:
            pass


    # HTTP detection
    if parsed.scheme.lower() == "http":

        result["indicators"].append(
            "HTTP URL"
        )


    # Brand impersonation detection
    if hostname and check_brand_impersonation(hostname):

        result["indicators"].append(
            "Possible brand impersonation"
        )


    # Lookalike domain detection
    if hostname and check_lookalike_domain(hostname):

        result["indicators"].append(
            "Possible lookalike domain"
        )


    return result