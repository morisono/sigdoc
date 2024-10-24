import bs4
import csscompressor
import cssbeautifier
import jsbeautifier
import jsmin
import javascript_obfuscator
import json
import re
import sqlparse


class Formatter:
    # HTML Beautifier & Formatter
    def beautify_html(html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        return soup.prettify()

    # CSS Minify
    def minify_css(css):
        return csscompressor.compress(css)

    # CSS Formatter
    def format_css(css):
        return cssbeautifier.beautify(css)

    # JavaScript Formatter
    def format_js(js):
        return jsbeautifier.beautify(js)

    # JavaScript Minify
    def minify_js(js):
        return jsmin.jsmin(js)

    # JavaScript Obfuscate
    def obfuscate_js(js):
        return javascript_obfuscator.obfuscate(js)

    # JSON Formatter & Beautifier
    def format_json(json_str):
        return json.dumps(json.loads(json_str), indent=4)

    # SQL Formatter
    def format_sql(sql):
        return sqlparse.format(sql, reindent=True)

class Internet:
    # Email Validator
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+$'
        return bool(re.match(pattern, email))

class WebDev:
    # Word Counter
    def count_words(text):
        words = text.split()
        return len(words)
