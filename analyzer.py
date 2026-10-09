from url_analyzer import extract_urls, analyze_url
from text_analyzer import analyze_text
from risk_engine import generate_risk_report


def analyze_message(message):
    # Analyze the message text
    text_results = analyze_text(message)

    # Extract URLs
    urls = extract_urls(message)

    # Analyze each URL
    url_results = []

    for url in urls:
        url_results.append(analyze_url(url))

    # Combine everything
    return {
        "text_analysis": text_results,
        "url_analysis": url_results
    }


message = """
Please verify your account immediately.

Your account will be suspended if you do not complete verification.

Click here:
http://example.com/verify
"""

analysis = analyze_message(message)

report = generate_risk_report(analysis)

print("Risk Score:", report["risk_score"])
print("Risk Level:", report["risk_level"])
print("Indicators:")

for indicator in report["indicators"]:
    print("-", indicator)