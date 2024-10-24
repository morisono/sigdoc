import re
from io import BytesIO

import gradio as gr
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image


class BookmarksUtils:
    @staticmethod
    def parse_html(html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        bookmarks = []
        for a in soup.find_all("a"):
            bookmarks.append(
                {
                    "title": a.get_text(),
                    "url": a.get("href"),
                    "tags": a.get("tags", ""),
                }
            )
        return bookmarks

    @staticmethod
    def merge_bookmarks(*args):
        merged = []
        for bookmarks in args:
            merged.extend(bookmarks)
        return merged

    @staticmethod
    def fetch_ogp_info(url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            og_image = soup.find("meta", property="og:image")
            og_title = soup.find("meta", property="og:title")
            og_description = soup.find("meta", property="og:description")

            return {
                "url": url,
                "title": og_title["content"] if og_title else "",
                "description": og_description["content"] if og_description else "",
                "image": og_image["content"] if og_image else "",
            }
        except:
            return {"url": url, "title": "", "description": "", "image": ""}


class BookmarkManager:
    _instance = None

    @staticmethod
    def get_instance():
        if BookmarkManager._instance is None:
            BookmarkManager()
        return BookmarkManager._instance

    def __init__(self):
        if BookmarkManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.bookmarks = []
            BookmarkManager._instance = self

    def add_bookmarks(self, bookmarks):
        if isinstance(bookmarks, pd.DataFrame):
            bookmarks = bookmarks.to_dict("records")
        self.bookmarks.extend(bookmarks)

    def search(self, query, use_regex=False):
        if use_regex:
            pattern = re.compile(query)
            return [
                bm
                for bm in self.bookmarks
                if pattern.search(bm["title"]) or pattern.search(bm["url"])
            ]
        else:
            return [
                bm
                for bm in self.bookmarks
                if query.lower() in bm["title"].lower()
                or query.lower() in bm["url"].lower()
            ]

    def fetch_ogp_info_async(self):
        ogp_info = []
        for bm in self.bookmarks:
            info = BookmarksUtils.fetch_ogp_info(bm["url"])
            ogp_info.append(info)
        return ogp_info


# Controller functions
def load_bookmarks(files):
    manager = BookmarkManager.get_instance()

    def pairwise(iterable):
        a = iter(iterable)
        return zip(a, a)

    for file1, file2 in pairwise(files):
        with open(file1.name, "r") as f1, open(file2.name, "r") as f2:
            bookmarks1 = BookmarksUtils.parse_html(f1.read())
            bookmarks2 = BookmarksUtils.parse_html(f2.read())

        merged_bookmarks = BookmarksUtils.merge_bookmarks(bookmarks1, bookmarks2)
        manager.add_bookmarks(merged_bookmarks)

    return pd.DataFrame(manager.bookmarks)


def search_bookmarks(bookmarks, query, use_regex):
    manager = BookmarkManager.get_instance()
    manager.add_bookmarks(bookmarks)
    return pd.DataFrame(manager.search(query, use_regex))


def display_ogp_info(bookmarks):
    manager = BookmarkManager.get_instance()
    manager.add_bookmarks(bookmarks)
    ogp_info = manager.fetch_ogp_info_async()

    images = []
    titles = []
    descriptions = []
    urls = []

    for info in ogp_info:
        titles.append(info["title"])
        descriptions.append(info["description"])
        urls.append(info["url"])
        if info["image"]:
            try:
                response = requests.get(info["image"])
                img = Image.open(BytesIO(response.content))
                images.append(img)
            except:
                images.append(None)
        else:
            images.append(None)

    return titles, descriptions, urls, images


# View
with gr.Blocks(title="Chrome Bookmark Manager") as demo:
    with gr.Row():
        with gr.Column():
            with gr.Accordion("Input"):
                file1 = gr.Files(label="Upload Bookmark HTML ")
                load_button = gr.Button("Load Bookmarks")
            with gr.Accordion("Filter", open=False):
                search_box = gr.Textbox(label="Search Bookmarks")
                regex_checkbox = gr.Checkbox(label="Use Regex")
                search_button = gr.Button("Search", variant="primary")
        with gr.Column():
            download_zip = gr.Files(label="Download Bookmarks as ZIP")
            # out_json = gr.JSON()
            with gr.Accordion("OGP", open=False):
                ogp_titles = gr.Markdown()
                ogp_descriptions = gr.Markdown()
                ogp_urls = gr.Markdown()
                ogp_images = gr.Gallery()

    with gr.Row():
        bookmarks_display = gr.DataFrame()

    load_button.click(fn=load_bookmarks, inputs=[file1], outputs=[bookmarks_display])
    search_button.click(
        fn=search_bookmarks,
        inputs=[bookmarks_display, search_box, regex_checkbox],
        outputs=[bookmarks_display],
    )
    # display_ogp_info(bookmarks_display).then(
    #     fn=display_ogp_info,
    #     inputs=bookmarks_display,
    #     outputs=[ogp_titles, ogp_descriptions, ogp_urls, ogp_images],
    # )

demo.launch()
