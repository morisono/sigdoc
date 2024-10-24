import requests

url = "https://api.short.io/api/links?domain_id=1108818&limit=30&dateSortOrder=desc"

headers = {
    "accept": "application/json",
    "Authorization": "sk_ekwbkf1MmX1gtAX2"
}

response = requests.get(url, headers=headers)

print(response.text)