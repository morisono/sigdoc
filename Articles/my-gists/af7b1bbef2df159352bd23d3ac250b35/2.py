import os
import json
from urllib import parse, request
from resend import Emails, resend

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_request(self, url, params):
        postdata = parse.urlencode(params).encode()
        try:
            req = request.Request(url, data=postdata)
            response = request.urlopen(req)
            return json.loads(response.read().decode("utf-8")), response.getcode()
        except request.HTTPError as e:
            return None, e.code


class EmailClient(APIClient):
    def __init__(self, api_key):
        super().__init__(api_key)

    def send_email(self, from_address, to_addresses, subject, html_content):
        resend.api_key = self.api_key
        params = Emails.SendParams(
            from_=from_address,
            to=to_addresses,
            subject=subject,
            html=html_content
        )
        return Emails.send(params)


class NeutrinoClient(APIClient):
    def __init__(self, api_key, user_id):
        super().__init__(api_key)
        self.user_id = user_id

    def validate_phone_numbers(self, phone_nums, country_code='JP'):
        url = 'https://neutrinoapi.net/phone-validate'
        results = []
        for item in phone_nums:
            item_number, phones = list(item.items())[0]
            phone_num = phones['phone']
            params = {
                'user-id': self.user_id,
                'api-key': self.api_key,
                'country-code': country_code,
                'number': phone_num
            }
            result, status_code = self.send_request(url, params)
            result_dict = {'item_number': item_number, 'phone_number': phone_num, 'details': result, 'status_code': status_code}
            results.append(result_dict)
        return results

# Usage example for EmailClient
email_client = EmailClient(os.environ["RESEND_API_KEY"])
email_response = email_client.send_email(
    "Acme <onboarding@resend.dev>",
    ["delivered@resend.dev"],
    "hello world",
    "<strong>it works!</strong>"
)
print(email_response)

# Usage example for NeutrinoClient
neutrino_client = NeutrinoClient(os.environ["NEUTRINO_API_KEY"], os.environ["NEUTRINO_USER_ID"])
phone_validation_results = neutrino_client.validate_phone_numbers(
    [{"item1": {"phone": "1234567890"}}]
)
print(phone_validation_results)
