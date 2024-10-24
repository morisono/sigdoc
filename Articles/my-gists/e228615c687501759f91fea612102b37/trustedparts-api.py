import argparse
import gradio as gr
import requests
import json
from rich import print
import yaml
from typing import Optional

class APIError(Exception):
    pass

def fetch_data_pdf(api_key: str, part_number: str, output_file: Optional[str] = None, api_endpoint: str = "trustedparts"):

    if api_endpoint == "trustedparts":
        api_url = "https://api.trustedparts.com/v1/partdata/pdf"
    if api_endpoint == "octopart":
        api_url = "https://api.trustedparts.com/v1/partdata/pdf"
    elif api_endpoint == "nexar":
        api_url = "https://api.nexar.com/graphql/"
        client_id = "Your client id here"
        client_secret = "Your client secret here"
        token_url = "https://identity.nexar.com/connect/token"

        token = requests.post(url=token_url, data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "supply.domain"
        }).json()

    elif api_endpoint == "oemsecrets":
        api_url = "https://api.oemsecrets.com/v1/partdata/pdf"
    else:
        print("[red]Invalid API endpoint. Supported values are 'trustedparts', 'nexar', and 'oemsecrets'.[/red]")
        return

    params = {'apikey': api_key, 'part': part_number}

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            api_response_json = response.json()
            print("[bold]API Response:[/bold]")
            print(json.dumps(api_response_json, indent=2))

            if api_response_json['status'] == 'success':
                pdf_content = response.content
                output_filename = output_file or f"{part_number}_data.pdf"

                with open(output_filename, 'wb') as pdf_file:
                    pdf_file.write(pdf_content)

                print(f"[green]Data PDF for part {part_number} has been fetched and saved as {output_filename}.[/green]")
            elif api_response_json['status'] == 'error':
                raise APIError(api_response_json.get('message', 'Unknown error'))

        elif response.status_code == 400:
            raise APIError("Search term and API key are required.")
        elif response.status_code == 401:
            raise APIError("User is not accepted or has exceeded API call limit.")
        elif response.status_code == 404:
            raise APIError("No parts found.")
        elif response.status_code >= 500:
            raise APIError("Unexpected server error.")

    except requests.exceptions.RequestException as e:
        raise APIError(f"An error occurred during the request: {str(e)}")

    except APIError as api_err:
        print(f"[red]API Error: {str(api_err)}[/red]")

    except Exception as e:
        print(f"[red]An unexpected error occurred: {str(e)}[/red]")

def webui(api_key: str, part_number: str, output_file: str = None):
    def fetch_data(input_part_number):
        fetch_data_pdf(api_key, input_part_number, output_file)
    inputs = [
        gr.Textbox(label='API KEY'),
        gr.Textbox(label='Part Name'),
    ]
    examples = [
        'PN532'
    ]
    iface = gr.Interface(
        title='EC parts search',
        fn=fetch_data,
        inputs=inputs,
        outputs="json",
        exapmles=examples
        )
    iface.launch()

def parse_arguments():
    '''
    usage:
    python3 tmp/trustedparts-api.py PN532 --api_key <your api key>
    '''
    parser = argparse.ArgumentParser(description='Fetch Data PDF from TrustedParts API')

    parser.add_argument('part_number', type=str, help='Part number for which to fetch the data PDF')
    parser.add_argument('api_key', type=str, help='Your API key')
    parser.add_argument('--output', '-o', type=str, default=None, help='Output filename for the PDF (default: <part_number>_data.pdf)')
    parser.add_argument('--config', '-c', type=str, default=None, help='Path to YAML configuration file')
    parser.add_argument('--webui', action='store_true', help='Launch Gradio Web UI')
    parser.add_argument('--api', choices=['trustedparts', 'octpart', 'oensecrets'], default='trustedparts', help='Choose API endpoint (default: trustedparts)')

    parser.usage = '''
    ref.
    - https://octopart.com/ja/search
    - https://support.nexar.com/support/solutions/101000253221/
    - https://www.trustedparts.com/docs/trustedparts-api/credentials/
    - https://beta.api.oemsecrets.com/documentation/
    '''

    args = parser.parse_args()

    if args.config:
        with open(args.config, 'r') as config_file:
            config_data = yaml.safe_load(config_file)
            api_key = config_data.get('api_key', args.api_key)
            part_number = config_data.get('part_number', args.part_number)
            output_file = config_data.get('output_file', args.output)
            api_endpoint = config_data.get('api_endpoint', args.api)
    else:
        api_key, part_number, output_file, api_endpoint = args.api_key, args.part_number, args.output, args.api

    return api_key, part_number, output_file, args.webui, api_endpoint

if __name__ == "__main__":
    api_key, part_number, output_file, webui, api_endpoint = parse_arguments()

    if webui:
        gradio_interface(api_key, part_number, output_file, api_endpoint)
    else:
        fetch_data_pdf(api_key, part_number, output_file, api_endpoint)