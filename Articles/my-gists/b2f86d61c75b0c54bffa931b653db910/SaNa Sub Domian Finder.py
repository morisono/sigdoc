print("**********************************************************************")
print("*                                                                    *")
print("*                     SaNa Sub Domain Finder v1.0                    *")
print("*                                                                    *")
print("**********************************************************************")
import requests
from bs4 import BeautifulSoup

def generate_subdomains(website):
    subdomains = set()
    try:
        r = requests.get(f"https://crt.sh/?q={website}&output=json")
        soup = BeautifulSoup(r.content, 'html.parser')
        data = r.json()
        for item in data:
            subdomains.add(item['name_value'])
    except:
        print("Error Occured while fetching subdomains")
    return subdomains

website = input("Enter the website : ")
subdomains = generate_subdomains(website)

filename = website.replace(".", "_") + ".txt"
with open(filename, "w") as sub_file:
    for subdomain in subdomains:
        sub_file.write(subdomain + "\n")

print("Subdomains for", website, "saved to", filename)
