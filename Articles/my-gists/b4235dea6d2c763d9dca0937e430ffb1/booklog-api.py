import gradio as gr
import requests
from bs4 import BeautifulSoup

class BooklogAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.booklog.jp/v2/json"
        self.api_key = api_key

    def get_books(self, user_id, month):
        endpoint = f"{self.base_url}/{user_id}?count=10000"
        response = requests.get(endpoint)

        if response.status_code == 200:
            books = response.json()
            # 特定の月に読んだ本の情報をフィルタリング
            books_in_month = [book for book in books if book['read_date'][:7] == month]
            return books_in_month
        else:
            print(f"Failed to fetch books. Status code: {response.status_code}")
            return None

    def get_book_details(self, isbn):
        html = requests.get(f"https://booklog.jp/users/{self.api_key}/archives/1/{isbn}")
        soup = BeautifulSoup(html.content, "html.parser")
        register_date = soup.find(class_='read-day-status-area').find('span').text
        amazon_link = soup.find(class_='itemInfoElm').find('a').get('href')
        return register_date, amazon_link

def booklog_app(month):
    # BooklogAPIのインスタンスを作成
    api_key = "YourBooklogAPIKey"
    booklog_api = BooklogAPI(api_key)

    # ユーザーID
    user_id = "YourBooklogUserID"

    # 特定の月に読んだ本の情報を取得
    books_in_month = booklog_api.get_books(user_id, month)

    if books_in_month:
        book_details = []
        for book in books_in_month:
            isbn = book['isbn']
            register_date, amazon_link = booklog_api.get_book_details(isbn)
            book_details.append({
                'title': book['title'],
                'author': book['author'],
                'register_date': register_date,
                'amazon_link': amazon_link
            })
        return book_details
    else:
        return "No books found for the selected month."

iface = gr.Interface(fn=booklog_app, inputs="text", outputs="table", title="Booklog Book Details")
iface.launch()
