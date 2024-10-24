import requests

url = "https://api.short.io/api/domains"

headers = {
    'accept': "application/json",
    'authorization': "sk_ekwbkf1MmX1gtAX2"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)