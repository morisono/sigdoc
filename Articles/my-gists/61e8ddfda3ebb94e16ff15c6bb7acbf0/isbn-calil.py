import gradio as gr
import requests
import time

# Set your Calil API key
api_key = '536c906624c7109c5787a3ad0a4ca088'

endpoint_lib = 'https://api.calil.jp/library'
endpoint_check = 'https://api.calil.jp/check'

class CalilAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_libraries(self, pref=None, city=None, systemid=None, geocode=None, limit=None):
        params = {
            'appkey': self.api_key,
            'pref': pref,
            'city': city,
            'systemid': systemid,
            'geocode': geocode,
            'format': 'json',
            'limit': limit
        }
        response = requests.get(endpoint_lib, params=params)
        return response.json()

    def check_books(self, isbn_list, systemid_list):
        isbn_str = ','.join(isbn_list)
        systemid_str = ','.join(systemid_list)
        params = {
            'appkey': self.api_key,
            'isbn': isbn_str,
            'systemid': systemid_str,
            'format': 'json',
            'callback': 'no'
        }
        response = requests.get(endpoint_check, params=params)
        return response.json()

    def poll_books(self, session):
        params = {
            'appkey': self.api_key,
            'session': session,
            'format': 'json',
            'callback': 'no'
        }
        response = requests.get(endpoint_check, params=params)
        return response.json()

calil_api = CalilAPI(api_key)

def get_library_info(pref, city, systemid, geocode, limit):
    libraries = calil_api.get_libraries(pref, city, systemid, geocode, limit)
    return libraries

def check_book_availability(isbn_list, systemid_list):
    initial_check = calil_api.check_books(isbn_list, systemid_list)
    session = initial_check.get('session')
    continue_check = initial_check.get('continue')

    while continue_check == 1:
        time.sleep(2)
        poll_result = calil_api.poll_books(session)
        continue_check = poll_result.get('continue')
        initial_check['books'].update(poll_result['books'])

    return initial_check['books']

def fetch_libraries(pref, city, systemid, geocode, limit):
    library_info = get_library_info(pref, city, systemid, geocode, limit)
    libraries = []
    for lib in library_info:
        libraries.append([
            lib.get('systemname'),
            lib.get('formal'),
            lib.get('address'),
            lib.get('tel'),
            lib.get('url_pc')
        ])
    return libraries

def fetch_book_availability(isbn_list, systemid_list):
    book_availability = check_book_availability(isbn_list, systemid_list)
    result = []
    for isbn, systems in book_availability.items():
        for system in systems:
            for libkey, status in system['libkey'].items():
                result.append([
                    isbn,
                    system['systemid'],
                    libkey,
                    status
                ])
    return result

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            pref = gr.Textbox(label="Prefecture")
            city = gr.Textbox(label="City")
            systemid = gr.Textbox(label="System ID")
            geocode = gr.Textbox(label="Geocode")
            limit = gr.Number(label="Limit")
            fetch_libraries_button = gr.Button("Fetch Libraries")
            library_output = gr.Dataframe(headers=["System Name", "Library Name", "Address", "Tel", "Website"])

        with gr.Column():
            isbn_input = gr.Textbox(label="ISBN (comma separated)")
            systemid_input = gr.Textbox(label="System IDs (comma separated)")
            check_availability_button = gr.Button("Check Book Availability")
            availability_output = gr.Dataframe(headers=["ISBN", "System ID", "Library Key", "Status"])

    fetch_libraries_button.click(
        fetch_libraries, 
        inputs=[pref, city, systemid, geocode, limit], 
        outputs=library_output
    )

    check_availability_button.click(
        fetch_book_availability, 
        inputs=[isbn_input, systemid_input], 
        outputs=availability_output
    )

demo.launch()
