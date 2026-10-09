from urllib.parse import urlparse

url = "https://login.example.com/account/verify?id=123"

parsed = urlparse(url)

print("Scheme:", parsed.scheme)
print("Hostname:", parsed.hostname)
print("Path:", parsed.path)
print("Query:", parsed.query)