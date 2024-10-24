import re
import json
import argparse
import requests
from rich.console import Console

class InvalidTelephoneNumberException(Exception):
    pass

def normalize(phone_number):
    phone_number = re.sub(r'[０-９]', lambda x: str(ord(x.group(0)) - ord('０')), phone_number)
    phone_number = re.sub(r'\D', '', phone_number)

    if len(phone_number) != 11:
        raise InvalidTelephoneNumberException("Invalid phone number length")

    return f'{phone_number[:3]}-{phone_number[3:7]}-{phone_number[7:]}'

def validate(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)

    if len(phone_number) != 11:
        return False

    return True

def get_country_code(phone_number):
    api_url = "http://localhost:5000/api/v2/numbers"
    payload = {"number": phone_number}

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("countryCode", None)
    except requests.exceptions.RequestException as e:
        raise InvalidTelephoneNumberException(f"Error in getting country code: {e}")

def split(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)

    if len(phone_number) != 11:
        raise InvalidTelephoneNumberException("Invalid phone number length")

    country_code = get_country_code(phone_number)

    return {
        'country_code': country_code,
        'area_code': phone_number[:3],
        'city_code': phone_number[3:7],
        'subscriber_code': phone_number[7:]
    }

def main():
    parser = argparse.ArgumentParser(description="Japanese Phone Number Utility")
    parser.add_argument("phone_number", type=str, help="Input Japanese phone number")

    args = parser.parse_args()

    try:
        result = {
            'normalized': normalize(args.phone_number),
            'valid': validate(args.phone_number),
            'split': split(args.phone_number)
        }

        console = Console()
        console.print(json.dumps(result, indent=2))

    except InvalidTelephoneNumberException as e:
        console = Console()
        console.print(f'[red]Error: {e}[/red]')

if __name__ == "__main__":
    main()
