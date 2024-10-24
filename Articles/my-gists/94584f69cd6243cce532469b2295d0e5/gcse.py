'''
Usage example :
python script.py --api $GCSE_API_KEY --cx $GCSE_CX_ID --query "python programm
ing" | jq -r '.items[] | select(has("link"))| "\(.link)\n\(.title)\n"'

'''

import argparse
import requests
import datetime
import re
import json
import sys
from fuzzywuzzy import fuzz
# from time import sleep
# from googleapiclient.discovery import build


def google_custom_search(api_key, cx, query, sort=None, regex=None, fuzzy=None, access_token=None):
    base_url = 'https://www.googleapis.com/customsearch/v1'

    params = {
        'key': api_key,
        'cx': cx,
        'q': query,
        'sort': sort,
        'access_token': access_token,
        'searchType': 'searchTypeUndefined',
        'safe': 'safeUndefined',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        results = response.json()

        if 'items' in results:
            sys.stdout.write(f'{json.dumps(results)}')

            # for item in results['items']:
            #     title = item.get('title', '')
            #     link = item.get('link', '')

            #     if regex and re.search(regex, title):
            #         sys.stdout.write(f'Title: {title}\nLink: {link}\n')
            #     elif fuzzy and fuzz.token_set_ratio(query.lower(), title.lower()) >= fuzzy:
            #         sys.stdout.write(f'Title: {title}\nLink: {link}\n')
        else:
            sys.stdout.write("No results found.")

    except requests.exceptions.HTTPError as errh:
        sys.stdout.write(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        sys.stdout.write(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

def main():
    parser = argparse.ArgumentParser(description='Google Custom Search')
    parser.add_argument('--api', required=True, help='Your Google Custom Search API key')
    parser.add_argument('--cx', required=True, help='Your Google Custom Search Engine ID (CX)')
    parser.add_argument('--query', required=True, help='Search query')
    parser.add_argument('--sort', choices=['relevance', 'date'], help='Search query')
    parser.add_argument('--regex', help='Regex pattern for search')
    parser.add_argument('--fuzzy', type=int, help='Fuzzy search threshold')
    parser.add_argument('--access_token', type=int, help='access_token')

    args = parser.parse_args()
    google_custom_search(args.api, args.cx, args.query, args.sort, args.regex, args.fuzzy, args.access_token)

if __name__ == '__main__':
    main()
