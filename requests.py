import requests

r = requests.get("http://google.com")
print("Status:", r.status_code)
