import aiohttp
import feedparser
from bs4 import BeautifulSoup
import gradio as gr
import asyncio
import tempfile
import os
from internetarchive import get_item, upload

'''
- You can check your api key: https://archive.org/account/s3.php
'''
class BaseAPI:
    def __init__(self):
        self.base_url = "https://news.yahoo.co.jp/rss"

    async def get_feed_urls(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url) as response:
                page_content = await response.text()
                soup = BeautifulSoup(page_content, 'html.parser')
                feeds = []
                for item in soup.select("\
                    #contentsWrap > ul:nth-child(5) > li > a,\
                    #contentsWrap > ul:nth-child(7) > li > a,\
                    #contentsWrap > ul:nth-child(9) > li > a"):
                    feeds.append({
                        "name": item.text,
                        "url": "https://news.yahoo.co.jp" + item['href']
                    })
                return feeds

    async def get_all_feed_urls(self, feed_url):
        async with aiohttp.ClientSession() as session:
            async with session.get(feed_url) as response:
                feed_data = await response.text()
                feed = feedparser.parse(feed_data)
                all_entries = [entry for entry in feed.entries]
                return all_entries

    async def fetch_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    # async def archive_article(self, url): # TODO NOT WORK IA
    #     try:
    #         item = get_item('my_new_item')
    #         md = {
    #             'collection': 'test_collection',
    #             'title': 'My New Item',
    #             'mediatype': 'web'
    #         }
    #         html_content = await self.fetch_url(url)
    #         if html_content:
    #             with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
    #                 tmp_file.write(html_content)
    #                 tmp_file_path = tmp_file.name

    #             r = item.upload(
    #                 files=[tmp_file_path],
    #                 metadata=md,
    #                 access_key=os.getenv('IA_ACCESS_KEY'),
    #                 secret_key=os.getenv('IA_SECRET_KEY')
    #             )
    #             return r[0].status_code
    #     except Exception as e:
    #         print("Error saving archive:", e)
    #         return None

    async def archive_article(self, url):
        try:
            html_content = await self.fetch_url(url)
            if html_content:
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                    tmp_file.write(html_content)
                    return tmp_file.name
                return r[0].status_code
        except Exception as e:
            print("Error saving archive:", e)
            return None

async def get_feeds():
    api = BaseAPI()
    return await api.get_feed_urls()

def get_latest_article(feed_url):
    api = BaseAPI()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    latest_entries = loop.run_until_complete(api.get_all_feed_urls(feed_url))
    loop.close()
    return latest_entries

def get_archive(url):
    api = BaseAPI()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    archive_status = loop.run_until_complete(api.archive_article(url)) # TODO
    loop.close()
    return archive_status

async def main():
    feeds = await get_feeds()
    feed_choices = {feed['name']: feed['url'] for feed in feeds}

    def update_feed(feed_name):
        feed_url = feed_choices[feed_name]
        latest_entries = get_latest_article(feed_url)
        latest_items = [(e.title, e.link) for e in latest_entries] #TODO
        return gr.Dropdown(choices=latest_items)

    def archive_feed(feed_urls):
        feed_url = feed_urls[0] # TODO
        archive_status = get_archive(feed_url)
        return archive_status

    with gr.Blocks() as app:
        gr.HTML("<h1>Archiver</h1>")
        with gr.Row():
            with gr.Column():
                feed_dropdown = gr.Dropdown(choices=list(feed_choices.keys()), label="Select RSS Feed")
                latest_articles = gr.Dropdown(label="Latest Article URLs", multiselect=True)
                with gr.Row():
                    clear_button = gr.ClearButton()
                    archive_button = gr.Button("Archive",   variant="primary")

            with gr.Column():
                archive_response_output = gr.Files(label="Archive Status")

        feed_dropdown.change(fn=update_feed, inputs=feed_dropdown, outputs=latest_articles)

        clear_button.click(fn=update_feed, inputs=feed_dropdown, outputs=latest_articles)
        archive_button.click(fn=archive_feed, inputs=latest_articles, outputs=archive_response_output)

    app.launch(share=True)

asyncio.run(main())