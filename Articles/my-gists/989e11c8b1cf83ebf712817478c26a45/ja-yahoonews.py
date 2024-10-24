import feedparser
import requests
import gradio as gr
from datetime import datetime
from urllib.parse import urlparse

def get_yahoo_news_feed():
    feed_url = "https://news.yahoo.co.jp/pickup/rss.xml"
    feed = feedparser.parse(feed_url)
    return feed.entries

def extract_article_info(article):
    title = article.title
    link = article.link
    published_time = datetime.strptime(article.published, "%a, %d %b %Y %H:%M:%S %z")
    return title, link, published_time

def archive_article(url):
    archive_url = f"https://archive.org/wayback/available?url={url}"
    response = requests.get(archive_url)
    if response.status_code == 200:
        archived_data = response.json()
        if 'archived_snapshots' in archived_data and 'closest' in archived_data['archived_snapshots']:
            return archived_data['archived_snapshots']['closest']['url']
    return None

def archive_articles():
    yahoo_news_feed = get_yahoo_news_feed()
    archived_articles = []
    for entry in yahoo_news_feed:
        title, link, published_time = extract_article_info(entry)
        archived_url = archive_article(link)
        if archived_url:
            archived_articles.append({'title': title, 'link': link, 'archived_link': archived_url, 'published_time': published_time})
    return archived_articles

def archive_articles_gr():
    articles = archive_articles()
    result_str = ""
    for article in articles:
        result_str += f"Title: {article['title']}\n"
        result_str += f"Published Time: {article['published_time']}\n"
        result_str += f"Original Link: {article['link']}\n"
        result_str += f"Archived Link: {article['archived_link']}\n\n"
    return result_str

iface = gr.Interface(
    fn=archive_articles_gr,
    inputs=None,
    outputs="text",
    title="Archive Yahoo News Articles",
    description="Fetches and archives Yahoo News articles.",
    allow_flagging=False
)

iface.launch()
