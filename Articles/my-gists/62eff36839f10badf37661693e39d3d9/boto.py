import gradio as gr
import boto3
import requests
from requests_auth_aws_sigv4 import AWSSigV4

def get_auth(amazon_app_client_id, amazon_app_client_secret):
    client = boto3.client(
        'sts',
        aws_access_key_id='self.access_key',
        aws_secret_access_key='self.secret_key',
        region_name='self.region'
    )

    response = client.assume_role(
        RoleArn='arn:aws:iam::xxxx:role/xxxx',
        RoleSessionName='SellingPartnerAPI',
    )
    reviews = []

    return response

def get_access_token(amazon_app_client_id, amazon_app_refresh_token, amazon_app_client_secret):

    res = get_auth(amazon_app_client_id, amazon_app_client_secret)

    Credentials = res["Credentials"]
    AccessKeyId = Credentials["AccessKeyId"]
    SecretAccessKey = Credentials["SecretAccessKey"]
    SessionToken = Credentials["SessionToken"]

    aws_auth = AWSSigV4('execute-api',
                        aws_access_key_id=AccessKeyId,
                        aws_secret_access_key=SecretAccessKey,
                        aws_session_token=SessionToken,
                        region=self.region
                        )
    body = \
        {
            'grant_type': 'refresh_token',
            'client_id': amazon_app_client_id,
            'refresh_token': amazon_app_refresh_token,
            'client_secret': amazon_app_client_secret
        }

    header = {'Content-Type': 'application/json'}

    access_token_response = requests.post(
                            'https://api.amazon.com/auth/o2/token',
                            json=body,
                            headers=header
                            )

    access_token = access_token_response.json().get('access_token')

    return access_token

def asin2url(asin):
    base_url = "https://www.amazon.co.jp/dp/"
    return base_url + asin

def get_review(search_input, asin, interval):
    # Consume API
    """
    Obtains the necessary credentials for accessing the Amazon API.

    This function outlines the steps to obtain the required credentials
    (client ID, refresh token, and client secret) for accessing the Amazon API.

    Steps:
    1. Register your application on the Amazon Developer Console.
        - https://developer.amazon.com/console
    2. Create a new security profile for your application.
        - https://developer.amazon.com/apps-and-games/console/api-access/home.html
    3. Obtain the client ID, refresh token, and client secret provided by Amazon.
        - https://developer.amazon.com/settings/console/securityprofile/web-settings/view.html
    4. Obtain the aws_access_key_id, aws_secret_access_key, and region_name provided by AWS.
        - https://aws.amazon.com/jp/console/

    """

    amazon_app_client_id = 'amzn1.application-oa2-client.4525ca3c11da499da8a598f508973552'
    amazon_app_refresh_token = '2:o6k5YoR2Z8j37JvOXuOe7Ox84fo2W9SYOpWWD_WDX5OmIjUjbNfplowSBpwFapq3TaKX1BRUqauvvl2Qg7Zj3w==:OWtaehg3KyhAln8o0sTBgw=='
    amazon_app_client_secret = 'amzn1.oa2-cs.v1.c33f477aba69862a1fe03ddab7e39044f1891fb87e519f7020cbcf6a256c6a95'

    access_token = get_access_token(amazon_app_client_id, amazon_app_refresh_token, amazon_app_client_secret)

    request_url = asin2url(asin) # TODO

    res = requests.get(
            request_url,
            auth=aws_auth,
            headers={'x-amz-access-token': str(access_token)}
            # ASIN=asin,
            # Keyword=key_word
            )

    return json.dumps(res.json(), ensure_ascii=False)

def web_ui():
    title="Demo"
    description="This is a demo app."

    with gr.Blocks(title='demo', css='footer{visibility: hidden}') as demo:
        gr.HTML(f'<div align="center"><h1>{title}</h1><h3>{description}</h3></div>')
        with gr.Row():
            with gr.Column():
                search_input = gr.MultimodalTextbox(interactive=True, file_types=["image"], placeholder="Search Word", show_label=False)
                asin_input = gr.Textbox(placeholder="ASIN", label="ASIN", show_label=False)
                request_interval_input = gr.Number(value=3000, minimum=1000, maximum=10000, precision=1)
                # clear_btn = gr.ClearButton(variant="sum")
                submit_btn = gr.Button(variant="primary")
                inputs = [ search_input, asin_input, request_interval_input ]
            with gr.Column():
                output_text = gr.JSON(label="Reviews")
        examples=[
            [
                {'text': 'Anker'},
                'B08HCVG4FB'
            ],
            [
                {'text': 'Anker'},
                'B0B4GVLW6D'
            ],
            [
                {'text': 'Anker'},
                'B09N9F72SP'
            ]
        ]
        gr.Examples(examples, inputs)
        submit_btn.click(get_review, inputs, output_text)
    demo.launch()

if __name__ == "__main__":
    web_ui()
