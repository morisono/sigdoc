import json
import gradio as gr
import pandas as pd
from googleapiclient.discovery import build
from gradio_calendar import Calendar


def google_custom_search(api_key, cx, query, lr, num, start, sort, from_date, to_date, regex, fuzzy, access_token):
    service = build("customsearch", "v1", developerKey=api_key)
    try:
        if sort == "review-date:r:custom":
            if from_date and to_date:
                from_date_str = from_date.strftime("%Y%m%d")
                to_date_str = to_date.strftime("%Y%m%d")
                sort = f"review-date:r:{from_date_str}:{to_date_str}"
            else:
                return "Please select a date range for custom review date sorting.", {'msg': 'Error.'}

        res = service.cse().list(q=query, cx=cx, sort=sort, lr=lr, num=num, start=start).execute()
        items = res.get('items', [])
        if not items:
            return "No results found.", {'msg': 'Error.'}
        df = pd.DataFrame(items)
        items_filtered = [
            {k: item.get(k, '') for k in ["title", "link"]}
            for item in items
        ]
        return df, json.dumps(items_filtered, ensure_ascii=False)

    except Exception as err:
        return f"Error: {err}", err

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

        with gr.Tab():
            with gr.Row():
                with gr.Column():
                    with gr.Accordion(open=True, label="Engine settings"):
                        api_key = gr.Dropdown(choices=[api_key_exp], label="API Key")
                        cx_id = gr.Textbox(label="CX ID")
                        access_token = gr.Textbox(label="Access Token (Optional)", placeholder="Leave empty for no access token")

                    with gr.Accordion(open=True, label="Search settings"):
                        sort_options = [
                            'relevance', 'date', 'date-sdate', 'date-sdate:a',
                            'review-rating:d:s', 'review-date:r::20091231',
                            'rating-stars:r:3.0', 'rating-stars,rating-stars:r:3.0',
                            'rating-stars,review-date:r:20101001:20101031', 'review-date:r:custom'
                        ]
                        sort_mode = gr.Radio(choices=sort_options, label="Sort Mode", value="date")
                        with gr.Row():
                            from_date = Calendar(type="datetime", label="From Date")
                            to_date = Calendar(type="datetime", label="To Date")

                        language = gr.Dropdown(choices=['lang_ja'])
                        num = gr.Number(minimum=1, maximum=10, step=1, label='Number of search')
                        start = gr.Number(minimum=1, maximum=10, step=1, label='Start at')
                        regex_pattern = gr.Textbox(label="Regex Pattern (Optional)", placeholder="Leave empty for no regex")
                        fuzzy_threshold = gr.Slider(0, 100, label="Fuzzy Threshold (Optional)", value=80)

                with gr.Column():
                    query = gr.Textbox(label="Search Query")
                    with gr.Row():
                        clr_btn = gr.ClearButton(query)
                        submit = gr.Button("Search", variant='primary')
                    output_json = gr.JSON(label="Search Results JSON")

        with gr.Tab():
            with gr.Column():
                output = gr.Dataframe(label="Search Results")

        inputs = [
            api_key, cx_id, query, sort_mode, num, start
        ]

        example = gr.Examples([[api_key_exp, cx_id_exp, 'NEWS',  'date',5, 1]], inputs)

        submit.click(google_custom_search,
                    inputs=[api_key, cx_id, query, language, num, start, sort_mode, from_date, to_date, regex_pattern, fuzzy_threshold, access_token],
                    outputs=[output, output_json])

    iface.launch()

if __name__ == "__main__":
    main()

