'''
Usage:
set -x NEUTRINO_API_KEY xxx
set -x NEUTRINO_ID xxx
'''

import os
import re
import gradio as gr
from gradio_calendar import Calendar
import pandas as pd
import datetime
import requests
import json
from utils_min import Interface
from rich.console import Console

console = Console()

user_id, api_key = os.getenv('NEUTRINO_ID', None), os.getenv('NEUTRINO_API_KEY', None)

class VerificationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class CC_Calculator:
    @staticmethod
    def to_isbn_10(isbn_10):
        if not isinstance(isbn_10, str) or not isbn_10.isdigit() or len(isbn_10) != 9:
            raise ValueError("Invalid ISBN-10 format")

        checksum = sum((i + 1) * int(digit) for i, digit in enumerate(isbn_10)) % 11
        check_digit = (11 - checksum) % 11
        return 'X' if check_digit == 10 else str(check_digit)

    @staticmethod
    def to_isbn_13(isbn_13):
        if not isinstance(isbn_13, str) or not isbn_13.isdigit() or len(isbn_13) != 12:
            raise ValueError("Invalid ISBN-13 format")

        checksum = sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(isbn_13)) % 10
        check_digit = (10 - checksum) % 10
        return str(check_digit)

    @staticmethod
    def to_ean_8(ean_8):
        if not isinstance(ean_8, str) or not ean_8.isdigit() or len(ean_8) != 7:
            raise ValueError("Invalid EAN-8 format")

        checksum = (10 - sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(ean_8))) % 10
        return str(checksum)

    @staticmethod
    def to_ean_13(ean_13):
        if not isinstance(ean_13, str) or not ean_13.isdigit() or len(ean_13) != 12:
            raise ValueError("Invalid EAN-13 format")

        checksum = (10 - sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(ean_13))) % 10
        return str(checksum)

    @staticmethod
    def to_jan_8(jan_8):
        # Assuming JAN-8 uses the same calculation as EAN-8
        return CC_Calculator.to_ean_8(jan_8)

    @staticmethod
    def to_jan_13(jan_13):
        # Assuming JAN-13 uses the same calculation as EAN-13
        return CC_Calculator.to_ean_13(jan_13)

    @staticmethod
    def to_itf(itf):
        if not isinstance(itf, str) or not itf.isdigit() or len(itf) != 13:
            raise ValueError("Invalid ITF format")

        even_sum = sum(int(digit) for digit in itf[1::2])
        odd_sum = sum(int(digit) * 3 for digit in itf[0::2])
        total = even_sum + odd_sum
        check_digit = (10 - (total % 10)) % 10
        return str(check_digit)

    @staticmethod
    def to_upc(upc):
        # Assuming UPC uses the same calculation as EAN-13
        return CC_Calculator.to_ean_13(upc)

    @staticmethod
    def to_sscc(sscc):
        if not isinstance(sscc, str) or not sscc.isdigit() or len(sscc) != 17:
            raise ValueError("Invalid SSCC format")

        checksum = (10 - sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(sscc[1:]))) % 10
        return str(checksum)

    @staticmethod
    def luhn(cc_no):
        total = 0
        reverse_cc_no = cc_no[::-1]

        for i, digit in enumerate(reverse_cc_no):
            digit = int(digit)
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit

        return total % 10 == 0

    @staticmethod
    def verhoeff(cc_no):
        """
        Verhoeff algorithm for checking the validity of a credit card number.

        Args:
            cc_no (str): The credit card number.

        Returns:
            bool: True if the credit card number is valid, False otherwise.
        """
        # Verhoeff multiplication matrix
        multiplication_matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
            [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
            [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
            [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
            [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
            [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ]

        permutation = [0, 1, 5, 2, 8, 3, 7, 4, 9, 6]

        cc_no = list(map(int, cc_no[::-1]))
        checksum = 0

        for i, digit in enumerate(cc_no):
            checksum = multiplication_matrix[checksum][permutation[i % 8]] ^ digit

        return checksum == 0

    @staticmethod
    def damm(cc_no):
        """
        Damm algorithm for checking the validity of a credit card number.

        Args:
            cc_no (str): The credit card number.

        Returns:
            bool: True if the credit card number is valid, False otherwise.
        """
        # Damm permutation matrix
        permutation_matrix = [
            [0, 3, 1, 7, 5, 9, 8, 6, 4, 2],
            [7, 0, 9, 2, 1, 5, 4, 8, 6, 3],
            [4, 2, 0, 6, 8, 7, 1, 3, 5, 9],
            [1, 7, 5, 0, 9, 8, 3, 4, 2, 6],
            [6, 1, 2, 3, 0, 4, 5, 9, 7, 8],
            [3, 6, 7, 4, 2, 0, 9, 5, 8, 1],
            [5, 8, 6, 9, 7, 2, 0, 1, 3, 4],
            [8, 9, 4, 5, 3, 6, 2, 0, 1, 7],
            [9, 4, 3, 1, 6, 3, 7, 2, 8, 0],
            [2, 5, 8, 8, 4, 1, 6, 7, 9, 0]
        ]

        cc_no = list(map(int, cc_no))
        checksum = 0

        for digit in cc_no:
            checksum = permutation_matrix[checksum][digit]

        return checksum == 0

class CC_Verifier:
    def __init__(self, rules):
        self.rules = rules

    def industry(self, cc_no):
        mii = int(cc_no[0])
        for rule in self.rules:
            if 'categories' in rule and rule.get('locale') == 'national':
                for sub_rule in rule['categories']:
                    if 'category_code' in sub_rule and re.match(sub_rule['category_code'], cc_no):
                        return {'industry': sub_rule.get('category', '')}
        return {'category': 'UnknownIndustry'}

    def issuer(self, cc_no):
        for rule in self.rules:
            if not isinstance(rule, dict):
                continue  # Skip non-dictionary entries

            if 'issuers' in rule and rule.get('locale') == 'global':
                for issuer in rule['issuers']:
                    if 'code' in issuer and any(re.match(code, cc_no) for code in issuer['code']):
                        return {'issuer': issuer['issuer']}
        return {'issuer': 'UnknownIssuer'}

    def vendor(self, cc_no):
        for rule in self.rules:
            if 'categories' in rule and rule.get('locale') == 'national':
                matched = []
                for sub in rule['categories']:
                    entries = sub.get('entries', [])
                    # console.print(f'entries: {entries}')
                    for ety in entries:
                        if 'cc_name' in ety and ety['cc_name'] is not None:
                            if 'code' in ety and ety['code'] is not None:
                                codes = ety['code']
                                if codes is not None and any(re.match(code, cc_no) for code in codes):
                                    matched.append(ety['cc_name'])
                            else:
                                matched.append(ety['cc_name'])
                    if matched:
                        console.print(f'matched: {matched}')
                        return {'cc_name': matched}
        return {'cc_name': 'UnknownCard'}

    def length(self, cc_no):
        if len(cc_no) not in [14, 15, 16]:
            return {'ValidLength': False}

        if not cc_no.isdigit():
            return {'ValidCharacter': False}

        return {'ValidLength': True, 'ValidCharacter': True}

    def checksum(self, cc_no):
        if not CC_Calculator.luhn(cc_no):
            return {'ValidChecksum': False}

        return {'ValidChecksum': True}

    def verificate(self, cc_no):
        result_all = {'items':[]}

        for num in cc_no['No.']:
            res_data = {}
            num = re.sub(r'\D', '', num) or ""
            res_data.update({'cc_no': num})
            try:
                res_data.update(self.industry(num))
                console.print(f'Done: industry')
                res_data.update(self.issuer(num))
                console.print(f'Done: issuer')
                res_data.update(self.vendor(num)) # TODO
                console.print(f'Done: vendor')
                res_data.update(self.length(num)) # TODO
                console.print(f'Done: length')
                res_data.update(self.checksum(num)) # TODO
                console.print(f'Done: checksum')

                console.print(res_data)
                result_all['items'].append(res_data)

            except VerificationError as e:
                console.print(f"Error processing credit card number {num}: {e}")
                result_all['items'].append({"status": "Invalid", "error": str(e)})

        return gr.Code(json.dumps(result_all, indent=4))

class CC_Validator:

    def validate_cc_code(*checklist):
        # Use Neutrino API to validate credit card information
        endpoint = "https://neutrinoapi.net/bin-lookup"

        # gr.dataframe to list
        cc_no_items = checklist[0]['No.']


        response_all = {'items':[]}
        for cc_no in cc_no_items:
            params = {
                "user-id": user_id,
                "api-key": api_key,
                "bin-number": cc_no,
                "customer-ip": None
            }
            try:
                response = requests.get(endpoint, params=params)
                response = response.json()
                console.print(response)
                response_all['items'].append(response)
            except Exception as e:
                response_all['items'].append(e)

        return gr.Code(json.dumps(response_all, indent=4))

def add_to_items(*params):
    state, cc_no, cc_name, cc_security, cc_expiry, bulk = params
    dict_data = state['items']

    try:
        if cc_no and cc_name and cc_security and cc_expiry:
            row = {
                'No.': cc_no,
                'Name': cc_name,
                'Security Code': cc_security,
                'Expiry Date': cc_expiry
            }
            dict_data.append(row)

        if bulk is not None:
            dict_data.extend(Interface.read_file(bulk)['items'])
        console.print(dict_data)
        headers = dict_data[0].keys()
        df = pd.DataFrame(dict_data, columns=headers)

        return gr.Dataframe(df)

    except Exception as e:
        console.print(e)
        return gr.Error("An error occurred: " + str(e))

def remove_from_items(*params):
    # Remove last one credit card information from the list
    state, cc_no, cc_name, cc_security, cc_expiry, bulk = params
    dict_data = state['items']
    try:
        if dict_data:
            headers = dict_data[0].keys()
            dict_data.pop()
            state['items'] = dict_data
            df = pd.DataFrame(dict_data, columns=headers)
            return gr.Dataframe(df)
        else:
            return gr.Error("No items to remove.")
    except Exception as e:
        console.print(e)
        return gr.Error("An error occurred: " + str(e))

def clear_items(*params):
    # Clear credit card information from the list
    state, cc_no, cc_name, cc_security, cc_expiry, bulk = params
    dict_data = state['items']
    try:
        if dict_data:
            headers = dict_data[0].keys()
            state['items'] = []
            df = pd.DataFrame(state['items'], columns=headers)
            return gr.Dataframe(df)
        else:
            return gr.Error("No items to remove.")
    except Exception as e:
        console.print(e)
        return gr.Error("An error occurred: " + str(e))


def form():
    css = f"""
        h1 {{
            text-align: center
            }}
        .response_code {{
            height: 500px;
            }}
        """
    ver = 'v0.1.0'
    title = f'Credit Card Checker Demo {ver}'
    header = f'<h1>{title}</h1>'

    # with open('config.json') as f:
    #     config = json.load(f)

    rules = Interface.read_yaml('data/cc_info_v2.yaml')
    # console.print(rules)

    with gr.Blocks(title=title, css=css) as demo:
        gr.HTML(header)
        state = gr.State({'items':[]})
        with gr.Row():
            with gr.Column(variant='compact'):
                with gr.Accordion("Credit Card Information", open=True):
                    cc_no = gr.Textbox(min_width=50, label='No.', placeholder='1234 1234 1234 1234')
                    with gr.Row():
                        cc_expiry = Calendar(label="Expiry date", info="Click the calendar icon to bring up the calendar.")
                        cc_security = gr.Textbox(min_width=50, label='Security Code', placeholder='123')
                    cc_name = gr.Textbox(min_width=50, label='Name', placeholder='John Smith', lines=1)

                    bulk_upload = gr.File(height=50, label='Bulk file')

                    examples = [
                        [state, "3000 9012 3456 7890", "John Smith", "2021-1-1", "456"],
                        [state, None, None, None, None],
                    ]
                    inputs = [
                        state,
                        cc_no,
                        cc_name,
                        cc_expiry,
                        cc_security,
                        bulk_upload
                    ]
                    gr.Examples(examples, inputs)

                with gr.Row():
                    clear_button = gr.Button(min_width=50, value='Clear list')
                    remove_button = gr.Button(min_width=50, value='Remove from list')
                    add_button = gr.Button(min_width=50, value='Add to list', variant='primary')
                # billing_address = gr.Textbox(min_width=50, label='Billing Address', placeholder='123 Main St, New York, NY 10001', lines=2)
                # billing_postcode = gr.Textbox(min_width=50, label='Billing Postcode', placeholder='10001', lines=1)

                cc_check_items = gr.Dataframe(headers=['No.', 'Name', 'Security Code', 'Expiry Date'])

                verificate_button = gr.Button('Verificate')
                validate_button = gr.Button('Validate (Neutrino API)', variant='primary')

            with gr.Column():
                response = gr.Code(language='json', label='Response', elem_classes='response_code')


        cc_verifier = CC_Verifier(rules)

        add_button.click(add_to_items, inputs, cc_check_items)
        remove_button.click(remove_from_items, inputs, cc_check_items)
        clear_button.click(clear_items, inputs, cc_check_items)
        verificate_button.click(cc_verifier.verificate, cc_check_items, response)
        validate_button.click(CC_Validator.validate_cc_code, cc_check_items, response)

    demo.launch()

form()