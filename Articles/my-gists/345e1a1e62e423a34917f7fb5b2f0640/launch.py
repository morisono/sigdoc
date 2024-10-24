import re
import os
import html
import json
import gradio as gr
import wikipediaapi
import urllib.parse
from babel import Locale
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import asyncio
import aiohttp
import random
import tempfile
import gradio as gr
from bs4 import BeautifulSoup
from babel import Locale
from internetarchive import get_item

def deal_escape(text):
    special_characters = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '\n': '<br>',
        '\r': '&#13;',
        '\t': '&#9;',
        '\f': '&#12;',
        '\v': '&#11;'
    }
    escaped_text = ''.join(special_characters.get(c, c) for c in text)
    return escaped_text

async def fetch_url(url):
    proxies = {
        'http': 'http://user:pass@proxy.example.com:port',
        'https': 'https://user:pass@proxy.example.com:port'
    }

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    ]
    proxy = proxies if proxies else None # TODO

    try:
        user_agent = random.choice(user_agents)
        headers = {'User-Agent': user_agent}
        if proxy:
            proxy = random.choice(list(proxy.values()))
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
            # async with session.get(url, headers=headers, proxy=proxy, timeout=10) as response: # TODO: Proxy
                if response.status == 200:
                    html = await response.text()
                    return html
                else:
                    print(f"Failed to fetch title for {url}. Status code: {response.status}")
                    return "Untitled"
    except Exception as e:
        print(f"Failed to fetch title for {url}. Error: {str(e)}")
        return "Untitled"

async def get_reses(urls):
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

def convert_to_markdown(urls, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    reses = loop.run_until_complete(get_reses(urls))

    markdown_links = []
    for i, (url, res) in enumerate(zip(urls, reses), 1):
        try:
            if res:
                soup = BeautifulSoup(res, 'html.parser')
                title = soup.title.string.strip()
                title = title.replace('[', '【').replace(']', '】')
                markdown_links.append(f"{i}. [{title}]({url})  \n")
        except Exception as e:
            print("Error processing URL:", e)
    loop.close()
    return ''.join(markdown_links)

def has_url(text):
    url_pattern = r'(https?://\S+)'
    return bool(re.search(url_pattern, text))

def separate_urls(text):
    url_pattern = r'(https?://\S+)'
    return re.findall(url_pattern, text)

def calculate_statistics(text):
    char_count = len(text)
    token_count = len(text.split())

    stripped_text = text.replace("\n", "").replace(" ", "")
    stripped_char_count = len(stripped_text)

    line_count = len(text.split("\n")) + 1
    paragraph_count = len(text.split("\n\n"))

    byte_count_utf8 = len(text.encode("utf-8"))
    byte_count_shift_jis = len(text.encode("shift-jis"))
    byte_count_euc_jp = len(text.encode("euc-jp"))
    byte_count_jis = len(text.encode("iso2022-jp"))

    estimated_reading_time = round(token_count / 200, 2)
    speaking_time = round(char_count / 160, 2)
    return {
        "Characters": char_count,
        "Tokens": token_count,
        "Stripped Characters": stripped_char_count,
        "Lines": line_count,
        "Paragraphs": paragraph_count,
        "ERT (min)": estimated_reading_time,
        "EST (min)": speaking_time,
        "Bytes (UTF-8)": byte_count_utf8,
        "Bytes (Shift-JIS)": byte_count_shift_jis,
        "Bytes (EUC-JP)": byte_count_euc_jp,
        "Bytes (JIS)": byte_count_jis
    }

async def fetch_archive(url):
    try:
        item = get_item('appropsA013019_1')

        md = {
            'collection': 'test_collection',
            'title': 'My New Item',
            'mediatype': 'web'
        }

        res = await fetch_url(url)
        if res:
            # Save the HTML content to a temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                tmp_file.write(res)
                tmp_file_path = tmp_file.name
                print(tmp_file_path)

            # Upload the temporary file
            # r = item.upload(
            r = get_item(tmp_file.name).upload(
                # 'appropsA013019_2',
                files=[tmp_file_path], #TODO
                metadata=md,
                # access_key=os.getenv('IA_ACCESS_KEY'), #TODO
                # secret_key=os.getenv('IA_SECRET_KEY') #TODO
                access_key='52vSWuXIlUOGPQmF',
                secret_key='x4A8iDo4OjTK6lmY'
            )
            return r[0].status_code
    except Exception as e:
        print("Error saving archive:", e)
        return None

async def get_archive(urls):
    tasks = [fetch_archive(url) for url in urls]
    return await asyncio.gather(*tasks)

def save_archive(urls, **kwargs):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    reses = loop.run_until_complete(get_archive(urls))

    archive_urls = []
    for i, (url, res) in enumerate(zip(urls, reses), 1):
        try:
            if res:
                soup = BeautifulSoup(res, 'html.parser')
                title = soup.title.string.strip()
                archive_urls.append(f'{url} \n')
        except Exception as e:
            print("Error processing URL:", e)
    loop.close()
    return ''.join(archive_urls)

def convert_text(mmodal, mode, encoding_as, lang, find, replace, pos_options, sub_pos_options):
    match_count = 0
    if mode == "Fetch title":
        if has_url(mmodal['text']):
            urls = separate_urls(mmodal['text'])
            formatted_text = convert_to_markdown(urls)

    elif mode == "archive.org":
        if has_url(mmodal['text']):
            urls = separate_urls(mmodal['text'])
            formatted_text = save_archive(urls)

    elif mode == "Custom":
        formatted_text, match_count = re.subn(find, replace, mmodal['text'])

    elif mode == "wikipedia.org":
        tokenizer = Tokenizer()
        char_filters = [
            UnicodeNormalizeCharFilter(),
            RegexReplaceCharFilter('[#!:;<>{}・`.,()-=$/_\d\'"\[\]\|]+', ' ')] # TODO
        # includes = [f"{pos},{sub_pos}" for pos in pos_options for sub_pos in sub_pos_options]
        # token_filters = [CompoundNounFilter(), POSKeepFilter(includes), TokenCountFilter()] #TODO
        token_filters = [CompoundNounFilter()] #TODO
        analyzer = Analyzer(char_filters=char_filters, tokenizer=tokenizer, token_filters=token_filters)
        tokens = analyzer.analyze(mmodal['text'])

        wiki_wiki = wikipediaapi.Wikipedia(
            user_agent='MyProjectName (example@example.com)',
            language=lang,
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        links = []
        for token in tokens:
            print(token)
            word = token.surface
            part_of_speech = token.part_of_speech.split(',')[0]
            part_of_speech_detail = token.part_of_speech.split(',')[1:3]

            if any(typ in part_of_speech for typ in pos_options) and any(detail in sub_pos_options for detail in part_of_speech_detail):

                word = deal_escape(word)

                page = wiki_wiki.page(word)
                if page.exists():
                    url = urllib.parse.quote_plus(page.fullurl.encode('utf-8'), safe=':/=&%')
                    if encoding_as == 'Markdown with Titles':
                        link = f"[{word}]({url})"
                    elif encoding_as == 'Markdown only':
                        link = f"[{word}]({url})"
                    elif encoding_as == 'HTML':
                        link = f"<a href=\"{url}\">{word}</a>"
                    links.append(link)
                else:
                    links.append(word)
            else:
                links.append(word)

        formatted_text = ''.join(links)

    token_count = len(mmodal['text'].split())
    char_count = len(mmodal['text'])
    stats = calculate_statistics(mmodal['text'])

    return formatted_text, formatted_text, json.dumps(stats)

def web_ui():
    all_languages = [lang for lang in Locale('en').languages.keys()]
    pos_options = ["*", "名詞", "動詞", "形容詞", "副詞", "助動詞", "連体詞", "接続詞", "感動詞", "記号", "その他"]
    # sub_pos_options = ["*", "名詞形態指示詞", "連体詞形態指示詞", "副詞形態指示詞", "普通名詞", "副詞的名詞", "形式名詞", "固有名詞", "組織名", "地名", "人名", "サ変名詞", "数詞", "時相名詞", "格助詞", "副助詞", "接続助詞", "終助詞", "名詞接頭辞", "動詞接頭辞", "イ形容詞接頭辞", "ナ形容詞接頭辞", "名詞性名詞接尾辞", "名詞性述語接尾辞", "名詞性名詞助数辞", "名詞性特殊接尾辞", "形容詞性述語接尾辞", "形容詞性名詞接尾辞", "動詞性接尾辞", "句点", "読点", "括弧始", "括弧終", "記号", "空白", "カタカナ", "アルファベット", "その他"]

    type2_pos_options = ["*", "複合", "形容詞接続", "数接続", "動詞接続", "名詞接続", "引用文字列", "サ変接続", "ナイ形容詞語幹", "形容動詞語幹", "動詞非自立的", "副詞可能", "一般", "数", "接続詞的", "固有名詞", "組織", "地域", "接尾", "助数詞", "助動詞語幹", "人名", "特殊", "代名詞", "縮約", "非自立", "自立", "助詞類接続", "格助詞", "引用", "連語", "係助詞", "終助詞", "接続助詞", "副詞化", "副助詞", "副助詞／並立助詞／終助詞", "並立助詞", "連体化", "助動詞", "感動詞", "句点", "読点", "空白", "アルファベット", "括弧開", "括弧閉", "間投", "未知語"]

    # type3_pos_options = ["*", "一般", "人名", "姓", "名", "組織", "国", "サ変接続", "助数詞", "一般", "形容動詞語幹", "助動詞語幹", "一般", ""]

    # type4_pos_options = ["*", "",] # TODO

    title="Generate Variable Formatted Text"
    description="Tokenizes the input text and converts nouns into Markdown or HTML links pointing to relevant web articles."
    with gr.Blocks(title=title) as demo:
        gr.HTML(f'<div align="center"><h1>{title}</h1><h3>{description}</h3></div>')

        with gr.Row():
            with gr.Column():
                txt = gr.MultimodalTextbox(interactive=True, file_types=["image"], placeholder="Enter message or upload file...", show_label=False)
                with gr.Row():
                    form = (
                        gr.Dropdown(choices=['Fetch title', 'wikipedia.org', 'archive.org', 'Custom'], label="Mode"),
                        gr.Dropdown(choices=['Markdown with Titles', 'Markdown only', 'HTML'], label="Encoding as"),
                        gr.Dropdown(all_languages, label="Language"),
                    )
                with gr.Row():
                    search_box = (
                        gr.Textbox(label="Find", placeholder="Regex pattern"),
                        gr.Textbox(label="Replace", placeholder="Replacement text")
                    )
                with gr.Row():
                    filter_box = (
                        gr.Dropdown(choices=pos_options, multiselect=True, label="Type"),
                        gr.Dropdown(choices=type2_pos_options, multiselect=True, label="Subtype")
                    )
                inputs = [
                    txt, *form, *search_box, *filter_box
                    ]

                with gr.Row():
                    clear_button = gr.ClearButton()
                    submit_button = gr.Button('Submit', variant='primary')

            with gr.Column():
                outputs = [
                    gr.Markdown(label="Rendered Text"),
                    gr.TextArea(label="Formatted Text"),
                    gr.JSON(),
                ]

        examples=[
            [{'text': 'https://example.com\nhttps://google.com\nhttps://en.wikipedia.org'}, 'Fetch title', 'Markdown with Titles', 'en', '', '', '名詞', '一般'],
            [{'text': '１. これは形態素解析の例です。'}, 'wikipedia.org', 'Markdown with Titles', 'ja', '', '', '名詞', ['一般','固有名詞', '複合']],
            [{'text': 'A canner can can as many cans as a canner can, if a canner can can cans.'}, 'Custom', 'HTML', 'ja', '\\bcan\\b', 'cook', '名詞', '一般'],
            [{'text': 'This is regex replace.'}, 'Custom', 'HTML', 'ja', '(\w+)', '[\\1](../)', '名詞', ['一般','固有名詞', '複合']],
        ]
        gr.Examples(examples, inputs)

        clear_button.click(None, inputs)
        submit_button.click(convert_text, inputs, outputs)

    demo.launch()

if __name__ == '__main__':
    web_ui()
