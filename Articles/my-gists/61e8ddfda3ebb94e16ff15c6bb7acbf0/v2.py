import gradio as gr
import requests
import time

api_key = "536c906624c7109c5787a3ad0a4ca088"

endpoint_lib = 'https://api.calil.jp/library'
endpoint_check = 'https://api.calil.jp/check'

def fetch_library_info(pref=None, city=None, systemid=None, geocode=None, limit=None):
    params = {
        "appkey": api_key,
    }
    if pref:
        params["pref"] = pref
    if city:
        params["city"] = city
    if systemid:
        params["systemid"] = systemid
    if geocode:
        params["geocode"] = geocode
    if limit:
        params["limit"] = limit
    params["format"] = "json"

    response = requests.get(endpoint_lib, params=params)
    return response.json()

def fetch_book_availability(isbn, systemid):
    params = {
        "appkey": api_key,
        "isbn": isbn,
        "systemid": systemid,
        "format": "json",
        "callback": "no"
    }

    response = requests.get(endpoint_check, params=params)
    result = response.json()

    if "session" in result:
        session = result["session"]
        while result.get("continue") == 1:
            time.sleep(2)
            result = requests.get(endpoint_check, params={"appkey": api_key, "session": session, "format": "json", "callback": "no"}).json()
    
    return result

def handle_isbn(isbn_list, pref, city, systemid, geocode, limit):
    isbn_list = isbn_list.split(',')
    library_info = fetch_library_info(pref, city, systemid, geocode, limit)
    availability_results = []

    for isbn in isbn_list:
        availability_results.append(fetch_book_availability(isbn.strip(), systemid))
    
    return library_info, availability_results

with gr.Blocks() as app:
    with gr.Row():
        with gr.Column():
            isbn_input = gr.Textbox(label="ISBN List (comma-separated)")
            pref_input = gr.Textbox(label="Prefecture")
            city_input = gr.Textbox(label="City")
            systemid_input = gr.Textbox(label="System ID")
            geocode_input = gr.Textbox(label="Geocode (latitude,longitude)")
            limit_input = gr.Number(label="Limit")
            search_button = gr.Button("Search")

        with gr.Column():
            library_info_output = gr.Dataframe(headers=["Library Info"])
            availability_output = gr.Dataframe(headers=["Availability Info"])

        search_button.click(
            handle_isbn,
            inputs=[isbn_input, pref_input, city_input, systemid_input, geocode_input, limit_input],
            outputs=[library_info_output, availability_output]
        )

app.launch()
