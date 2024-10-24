import gradio as gr
from gradio_calendar import Calendar
import requests
from urllib.parse import urlencode

class APIWrapper:
    def __init__(self, api_key):
        self.elaws_api_base_url = "https://elaws.e-gov.go.jp/api"
        self.api_key = api_key

    def get_law_list(self, lawType):
        params = {
            "Version": 1,
            "lawType": lawType,
        }
        url = f"{self.elaws_api_base_url}/{params['Version']}/lawlists"
        encoded_params = urlencode(params)
        response = requests.get(url, params=encoded_params)
        return self.handle_response(response)

    def get_law_info(self, lawId, lawNum, article, paragraph, appdxTable):
        params = {
            "Version": 1,
            "lawNum": lawNum,
            'lawId': lawId,
            'article': '第十一条',
            'paragraph': '',
            'appdxTable': '',
        }
        url = f"{self.elaws_api_base_url}/{params['Version']}/lawdata/"
        encoded_params = urlencode(params)
        response = requests.get(url, params=encoded_params)
        return self.handle_response(response)

    def get_article_info(self, lawId, lawNum, article, paragraph, appdxTable):
        params = {
            "Version": 1,
            'lawId': lawId,
            "lawNum": lawNum,
            'article': '第十一条',
            'paragraph': '',
            'appdxTable': '',
        }
        url = f"{self.elaws_api_base_url}/{params['Version']}/lawdata/articles;"
        encoded_params = urlencode(params)
        response = requests.get(url, params=encoded_params)
        return self.handle_response(response)
        
    def get_updated_law_info(self, date_from, date_to):
        url = f"{self.elaws_api_base_url}/updatelawlists"
        params = {
            "Version": 1,
            "date": date_from,
            }
        response = requests.get(url)
        return self.handle_response(response)

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                # Decode the response content to Unicode
                return response.text.encode().decode('unicode_escape')
            except Exception as e:
                return {"error": f"HTTP Error: {response.status_code}"}
        return

api_wrapper = APIWrapper("YOUR_API_KEY")

lawTypes = {
    "全法令": 1,
    "憲法・法律": 2,
    "政令・勅令": 3,
    "府省令・規則": 4,
}

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            with gr.Tab('法令名一覧'):
                lawType = gr.Dropdown(choices=lawTypes.keys(), label="法令種別")
                lawType_btn = gr.Button("検索")

                inputs_1 = [lawType]

            with gr.Tab('法令内容'):
                lawId = gr.Textbox(label="法令ID")
                lawId_btn = gr.Button("検索")
                
                inputs_2 = [lawId]

            with gr.Tab('条文内容'):
                lawNum = gr.Textbox(label="法令番号")
                article = gr.Textbox(label="条")
                paragraph = gr.Textbox(label="項")
                appdxTable = gr.Textbox(label="別表")
                lawNum_btn = gr.Button("検索")
                
                inputs_3 = [lawNum, article, paragraph, appdxTable, lawNum_btn]

            with gr.Tab('更新法令'):
                calendar_from = Calendar(type="date", label="日付を選択 (from)", info="カレンダーアイコンをクリックしてカレンダーを表示します。")
                calendar_to = Calendar(type="date", label="日付を選択 (to)", info="カレンダーアイコンをクリックしてカレンダーを表示します。")
                
                inputs_4 = [calendar_from, calendar_to]
                date_btn = gr.Button("取得")

        with gr.Column():
            law_info_output = gr.TextArea(label="法令情報")
            article_info_output = gr.TextArea(label="条文内容情報")
            updated_law_info_output = gr.TextArea(label="更新法令情報")

    lawType_btn.click(fn=api_wrapper.get_law_list, inputs=inputs_1, outputs=law_info_output)
    lawId_btn.click(fn=api_wrapper.get_law_info, inputs=inputs_2, outputs=article_info_output)
    lawNum_btn.click(fn=api_wrapper.get_article_info, inputs=inputs_3, outputs=article_info_output)
    date_btn.click(fn=api_wrapper.get_updated_law_info, inputs=inputs_4, outputs=updated_law_info_output)
#     law_name = 4010403030746
    examples = [['1', '415AC0000000057', '平成十五年法律第五十七号', '第十一条', None, None]]
    gr.Examples(examples, [lawType, lawId, lawNum, article, paragraph, appdxTable])

if __name__ == "__main__":
    demo.launch()