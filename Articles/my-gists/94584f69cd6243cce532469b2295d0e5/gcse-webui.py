import gradio as gr
import argparse
import requests
import datetime
import re
import json
import sys
from fuzzywuzzy import fuzz

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
            return results
        else:
            return "No results found."

    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Request Exception: {err}"

readme = f'''
# Google Custom Search Utility

## Getting Started

1. Obtain a Google Custom Search API key from the Google Cloud Console.
2. Create a new environment.

   - Access [Google Custom Search](https://cse.google.com/cse/)

3. Fill `CX ID` to the form.
4. Push 'Search' button.
'''

def main():
    with gr.Blocks() as iface:
        gr.Markdown(readme)
        api_key_exp = 'AIzaSyBV0s4fmv0O3MIh3zyJV1aoOJQOv9bImyc'
        cx_id_exp = '230661aa2d41f485f'

        with gr.Row():
            with gr.Column():
                with gr.Accordion(open=True, label="Engine settings"):
                    api_key = gr.Dropdown(choices=[api_key_exp], label="API Key")
                    cx_id = gr.Textbox(label="CX ID")
                    access_token = gr.Textbox(label="Access Token (Optional)", placeholder="Leave empty for no access token")

                with gr.Accordion(open=True, label="Search settings"):
                    sort_mode = gr.Radio(["relevance", "date"], label="Sort Mode", value="date")
                    regex_pattern = gr.Textbox(label="Regex Pattern (Optional)", placeholder="Leave empty for no regex")
                    fuzzy_threshold = gr.Slider(0, 100, label="Fuzzy Threshold (Optional)", value=80)

            with gr.Column():
                query = gr.Textbox(label="Search Query")
                with gr.Row():
                    clr_btn = gr.ClearButton(query)
                    submit = gr.Button("Search", variant='primary')
                output = gr.JSON(label="Search Results")
        inputs = [
            api_key, cx_id, query
        ]

        example = gr.Examples([[api_key_exp, cx_id_exp, 'Test', 'date']], inputs)

        submit.click(google_custom_search,
                    inputs=[api_key, cx_id, query, sort_mode, regex_pattern, fuzzy_threshold, access_token],
                    outputs=output)

    iface.launch(

    )


if __name__ == "__main__":
    main()
