'''
Usage:
set -x NEUTRINO_API_KEY xxx
set -x NEUTRINO_ID xxx
python scripts/tmp/neutrino.py |
 jq -c '.[]| {"no": .phone_number, "valid": .details.valid}'
'''
import os
import argparse
import json
import yaml
from rich.console import Console
from urllib import request, parse

class APIRequestError(Exception):
    pass

def validate_phone_numbers(phone_nums, user_id, api_key):
    results = []

    for item in phone_nums:
        item_number, phones = list(item.items())[0]
        phone_num = phones['phone']
        url = 'https://neutrinoapi.net/phone-validate'
        params = {
            'user-id': user_id,
            'api-key': api_key,
            'country-code': 'JP',
            'number': phone_num
        }

        postdata = parse.urlencode(params).encode()

        try:
            req = request.Request(url, data=postdata)
            response = request.urlopen(req)
            status_code = response.getcode()
            result = json.loads(response.read().decode("utf-8"))
            result_dict = {'item_number': item_number, 'phone_number': phone_num, 'details': result, 'status_code': status_code}
            results.append(result_dict)
        except request.HTTPError as e:
            status_code = e.code
            result_dict = {'item_number': item_number, 'phone_number': phone_num, 'details': None, 'status_code': status_code}
            results.append(result_dict)
            # print(f"HTTPError: {status_code} for phone number {phone_num}")

    return results

def load_config(config_file):
    with open(config_file, 'r') as config_file:
        config_data = yaml.safe_load(config_file)
    return config_data

def main():
    parser = argparse.ArgumentParser(description="Phone Number Checker Utility")
    parser.add_argument("--config-file", type=str, help="Path to the YAML configuration file")
    parser.add_argument("--user-id", default=os.getenv('NEUTRINO_USER_ID'), type=str, help="Neutrino API user ID")
    parser.add_argument("--api-key", default=os.getenv('NEUTRINO_API_KEY'), type=str, help="Neutrino API key")
    parser.add_argument("--phone", default='phone-numbers-1.yaml', type=str, help="Path to the file containing phone numbers in YAML format")
    args = parser.parse_args()

    if args.config_file:
        config = load_config(args.config_file)
    else:
        config = {}

    config['user_id'] = args.user_id or config.get('user_id')
    config['api_key'] = args.api_key or config.get('api_key')

    with open(args.phone, 'r') as f:
        phone_nums = yaml.safe_load(f)['items']

    results = validate_phone_numbers(phone_nums, config.get('user_id'), config.get('api_key'))

    console = Console()
    console.print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()