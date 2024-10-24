import requests
import csv
from bs4 import BeautifulSoup
import gradio as gr
import random
import time


proxies = {
    'http': 'http://user:pass@proxy.example.com:port',
    'https': 'https://user:pass@proxy.example.com:port'
}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
]


def get_title(url, proxy=None):
    try:
        user_agent = random.choice(user_agents)
        time.sleep(random.uniform(0, 1))
        headers = {'User-Agent': user_agent}
        if proxy:
            proxy = {'http': random.choice(list(proxy.values()))}
        response = requests.get(url, headers=headers, proxies=proxy, timeout=10)

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip()

        return title.replace('[', '【').replace(']', '】')
    except:
        return "Untitled"


def convert_to_markdown(txt, files=None, filter_links=False, exclude_words=None, include_words=None, replace_words=None, copy_format="Markdown", block_repeat_links=False, reverse_order=False):
    markdown_links = []
    urls = txt.strip().split('\n')
    proxy = proxies if proxies else None
    seen_links = set()
    for url in urls:
        title = get_title(url, proxy)
        if block_repeat_links and url in seen_links:
            continue
        seen_links.add(url)
        if filter_links:
            if exclude_words and any(word in title for word in exclude_words):
                continue
            if include_words and not any(word in title for word in include_words):
                continue
            if replace_words:
                for word, replacement in replace_words.items():
                    title = title.replace(word, replacement)
        if copy_format == "Markdown":
            markdown_links.append(f"1. [{title}]({url})  \n")
        elif copy_format == "Link HTML":
            markdown_links.append(f'<a href="{url}">{title}</a><br>')
        elif copy_format == "Link List HTML":
            markdown_links.append(f'<li><a href="{url}">{title}</a></li>')
        elif copy_format == "Titles and URLs":
            markdown_links.append(f"{title}: {url}\n")
        elif copy_format == "URLs Only":
            markdown_links.append(f"{url}\n")
        elif copy_format == "Titles Only":
            markdown_links.append(f"{title}\n")

    if files:
        for file_input in files:
            if file_input is None:
                continue
            with open(file_input, 'r', encoding='utf-8') as file:
                additional_urls = file.read().strip().split('\n')
                for url in additional_urls:
                    title = get_title(url, proxy)
                    if block_repeat_links and url in seen_links:
                        continue
                    seen_links.add(url)
                    if filter_links:
                        if exclude_words and any(word in title for word in exclude_words):
                            continue
                        if include_words and not any(word in title for word in include_words):
                            continue
                        if replace_words:
                            for word, replacement in replace_words.items():
                                title = title.replace(word, replacement)
                    if copy_format == "Markdown":
                        markdown_links.append(f"1. [{title}]({url})  \n")
                    elif copy_format == "Link HTML":
                        markdown_links.append(f'<a href="{url}">{title}</a><br>\n')
                    elif copy_format == "Link List HTML":
                        markdown_links.append(f'<li><a href="{url}">{title}</a></li>\n')
                    elif copy_format == "Titles and URLs":
                        markdown_links.append(f"{title},{url}\n")
                    elif copy_format == "URLs Only":
                        markdown_links.append(f"{url}\n")
                    elif copy_format == "Titles Only":
                        markdown_links.append(f"{title}\n")

    if reverse_order:
        markdown_links.reverse()

    return ''.join(markdown_links)


def url_to_markdown(url_list, *file_inputs, filter_links=False, exclude_links_with_words=None, include_links_with_words=None, replace_words=None, copy_format="Markdown", block_repeat_links=False, reverse_order=False):
    exclude_words = exclude_links_with_words.split(',') if exclude_links_with_words else None
    include_words = include_links_with_words.split(',') if include_links_with_words else None
    replace_words_dict = {}
    if replace_words:
        for pair in replace_words.split(';'):
            word, replacement = pair.split(':')
            replace_words_dict[word] = replacement
    markdown_text = convert_to_markdown(url_list, file_inputs, filter_links, exclude_words, include_words, replace_words_dict, copy_format, block_repeat_links, reverse_order)
    return markdown_text


def web_ui():
    iface = gr.Interface(
        fn=url_to_markdown,
        inputs=[
            gr.Textbox(lines=10, label="Input URLs"),
            gr.Files(label="Input URLs as file"),
            gr.Checkbox(label="Filter Links"),
            gr.Textbox(label="Exclude Links With Words"),
            gr.Textbox(label="Include Links With Words"),
            gr.Textbox(label="Replace Words (word:replacement;word:replacement)"),
            gr.Radio(["Markdown", "Link HTML", "Link List HTML", "Titles and URLs", "URLs Only", "Titles Only"], label="Copy Format as"),
            gr.Checkbox(label="Block Repeat Links in Selection"),
            gr.Checkbox(label="Reverse Order")
        ],
        outputs=gr.Textbox(label="マークダウン形式のリンクがこちらに表示されます"),
        title="URL => Markdown Converter",
        description="URLリストを受け取り、各URLのタイトルとURLを含むマークダウン形式のリンクに変換します。",
        examples=[['https://example.com']],
    )

    iface.launch()


if __name__ == '__main__':
    web_ui()