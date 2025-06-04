"""
Enrich links, locate file via frontmatter info, etc.

This tool expected to be used with Obsidian note app,
and render using the plugin (github.com/nekoshita/obsidian-auto-card-link),
then export with the plugin (github.com/l1xnan/obsidian-better-export-pdf).

Features:
- Fetch opengraph info from each target links
- Convert links to codeblock named `cardlink` (that used in the plugin) then embed.
- Links in the specific location are skipped (e.g. frontmatter, markdown-link, etc)
- replace '<!-- style -->' in the content to specific style tag

Example:
script.py "*.md" --interval 2 --max-retries 5 --timeout 15 --urlencode

This command will:
- Process all .md files in the current directory
- Use "RD" as the ID code and 2 as the version number
- Use the provided API key
- Wait 2 seconds between requests
- Retry up to 5 times for failed fetches
- Set a 15-second timeout for requests


script.py (fd -e md -t f . -E outputs -E Templates --changed-within 7d --full-path | sort -rn | head -n 10)

This command will:
- Find top 10 files that modified in last 7 days.
- Ignore specific folder (e.g. 'Templates')
- Process with this script.

Options:
   - `--fetch-method`: Choose between 'microlink' and 'local' (default is 'local').
   - `--api-key`: Provide an API key  if using the api method.
   - `--interval`: Set the interval between requests (default is 1 second).
   - `--max-retries`: Set the maximum number of retries for failed fetches (default is 3).
   - `--timeout`: Set the timeout for requests in seconds (default is 10 seconds).
   - `--urlencode`: the title and description in the cardlink will be URL-encoded. This means that special characters will be replaced with their percent-encoded equivalents.

TODO:
   - To preserve original folder group, any idea needed alternative to process per file.

"""

import argparse
import glob
import json
import os
import re
import time
import urllib.parse
from datetime import datetime
from typing import Dict, Optional
from urllib.parse import urlparse

import qrcode
import requests
import yaml
from bs4 import BeautifulSoup
from rich.console import Console


def is_unsafe_link(url: str) -> bool:
    unsafe_protocols = [
        "http:",
        "ftp:",
        "telnet:",
        "mailto:",
        "file:",
        "data:",
        "javascript:",
    ]
    unsafe_domains = [".onion", ".i2p", "localhost", "127.0.0.1", "0.0.0.0", "::1"]

    parsed_url = urlparse(url)

    if parsed_url.scheme.lower() in unsafe_protocols:
        return True

    if any(domain in parsed_url.netloc.lower() for domain in unsafe_domains):
        return True

    # Add more checks here as needed, such as:
    # - Check for IP addresses in certain ranges
    # - Check for known malicious domains
    # - Check for overly long domain names

    return False


def fetch_url_info_api(url: str, api_key: Optional[str] = None) -> dict:
    api_url = "https://api.microlink.io"
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["x-api-key"] = api_key
    params = {"url": url}

    response = requests.get(api_url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]
        return {
            "url": url,
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "host": urlparse(url).netloc,
            "favicon": data.get("logo", {}).get("url", ""),
            "image": data.get("image", {}).get("url", ""),
        }
    else:
        raise Exception(f"Microlink API error: {response.status_code}")


def fetch_url_info_local(url: str) -> dict:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else ""
    description = soup.find("meta", attrs={"name": "description"})
    description = description["content"] if description else ""

    favicon = soup.find("link", rel="icon") or soup.find("link", rel="shortcut icon")
    favicon = favicon["href"] if favicon else ""
    if favicon and not favicon.startswith("http"):
        favicon = (
            f"{urlparse(url).scheme}://{urlparse(url).netloc}/{favicon.lstrip('/')}"
        )

    og_image = soup.find("meta", property="og:image")
    image = og_image["content"] if og_image else ""

    return {
        "url": url,
        "title": title,
        "description": description,
        "host": urlparse(url).netloc,
        "favicon": favicon,
        "image": image,
    }


def fetch_url_info(url: str, method: str, api_key: Optional[str] = None) -> dict:
    if is_unsafe_link(url):
        raise ValueError(f"Unsafe link detected: {url}")

    methods = {
        "microlink": (fetch_url_info_api, {"api_key": api_key}),
        "local": (fetch_url_info_local, {}),
    }

    for current_method, kwargs in [methods[method]] + [
        methods[m] for m in methods if m != method
    ]:
        try:
            return current_method(url, **kwargs)
        except Exception as e:
            console.print(
                f"Error fetching {url} with {current_method.__name__}: {str(e)}"
            )

    raise Exception(f"All methods failed for URL: {url}")


def escape_string(s: str, urlencode: bool) -> str:
    if urlencode:
        return urllib.parse.quote(s)
    return json.dumps(s)[1:-1]


def format_cardlink(
    info: dict, urlencode: bool, generate_qr: bool, outdir_root: str
) -> str:
    if not info:
        return ""

    escaped_title = escape_string(info["title"], urlencode)
    escaped_description = escape_string(info["description"], urlencode)

    #     return f"""{info['url']}

    # ```cardlink
    # url: {info['url']}
    # title: "{escaped_title}"
    # description: "{escaped_description}"
    # host: {info['host']}
    # favicon: {info['favicon']}
    # image: {info['image']}
    # ```

    # """

    # Generate QR Code
    def replace_with_qr(match):
        nonlocal qr_count
        url = match.group(1)
        if is_unsafe_link(url):
            return match.group(0)

        qr_count += 1
        qr_filename = f"qr-{qr_count:04d}.png"
        qr_png_path = f"img/qr/{qr_filename}"
        qr_code_html = (
            f'<nobr><img src="{qr_png_path}" alt="QR Code" height="40px"></nobr>'
        )
        return qr_code_html

    qr_code_html = ""
    if generate_qr:
        qr_code_html = f'<div class="auto-card-link-qr">{replace_with_qr(re.match(r"(https?://\S+)", info["url"]))}</div>'

    result = f"""
<div>
    <div class="block-language-cardlink">
        <div class="auto-card-link-container" data-auto-card-link-depth="-1">
            <a class="auto-card-link-card" href="{info['url']}">
            <img class="auto-card-link-thumbnail" src="{info['image']}" />
            <div class="auto-card-link-main">
            <div class="auto-card-link-title">{escaped_title}</div>
            <div class="auto-card-link-description">{escaped_description}</div>
            {qr_code_html}
            <div class="auto-card-link-host">
            <img class="auto-card-link-favicon" src="{info['favicon']}" /><nobr><span>{info['host']}</span>
        </div>
    </div>
</div>
</div>
"""
    return result


def parse_frontmatter(content: str) -> tuple[Dict[str, str], str]:
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if frontmatter_match:
        frontmatter_content = frontmatter_match.group(1)
        remaining_content = content[frontmatter_match.end() :]
        try:
            frontmatter = yaml.safe_load(frontmatter_content)
            if not isinstance(frontmatter, dict):
                console.print(
                    "Warning: Frontmatter is not a dictionary. Treating as empty."
                )
                frontmatter = {}
        except yaml.YAMLError as e:
            console.print(
                f"Warning: Error parsing frontmatter: {e}. Treating as empty."
            )
            frontmatter = {}
        return frontmatter, remaining_content
    return {}, content


def generate_qr_code(url: str, output_path: str, size_px: int = 40) -> str:
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size_px, size_px))
    img.save(output_path)
    return output_path


def format_style(line, idx):
    insert_str = """
<style>
   .block-language-cardlink {
      max-width: 100%;
   }
   .auto-card-link-container {
      max-height: 200px;
      height: 200px;
      /* background-color: #ddd; */
      border: 0.5px solid darkgray !important;
      border-radius: 4px !important;
   }
   .auto-card-link-thumbnail {
      width: 50%;
      height: calc(100% - 10px - 10px);
      max-width: 50%;
      min-height: calc(100% - 10px - 10px);
      float: right;
      object-fit: contain;
      padding: 10px;
   }
   .auto-card-link-main {
      width: 50%;
      padding: 10px;
   }
   .auto-card-link-title {
      font-size: 16px;
   }
   .auto-card-link-description {
      font-size: 12px;
   }
   .auto-card-link-host {
      font-size: 14px;
      text-align: right;
   }
   .auto-card-link-favicon {
      width: 1rem;
   }
</style>
"""
    return line[:idx] + insert_str + line[idx:]


def convert_links_to_cardlink(
    input_file: str,
    outdir_root: str,
    output_file: str,
    fetch_method: str,
    api_key: Optional[str],
    interval: float,
    urlencode: bool,
    generate_qr: bool,
):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        content = infile.read()

        # Parse frontmatter
        frontmatter, content = parse_frontmatter(content)

        # Remove codeblocks, markdown links, and HTML links temporarily
        codeblocks = re.findall(r"```[\s\S]*?```", content)
        for i, block in enumerate(codeblocks):
            content = content.replace(block, f"__CODEBLOCK_{i}__")

        md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
        for i, link in enumerate(md_links):
            content = content.replace(f"[{link[0]}]({link[1]})", f"__MDLINK_{i}__")

        html_links = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', content)
        for i, link in enumerate(html_links):
            content = content.replace(f'<a href="{link}"', f"__HTMLLINK_{i}__")

        # Insert style tag
        try:
            idx = content.find("<!-- style -->")
            content = format_style(content, idx)
        except Exception as e:
            console.print(e)

        # Find and replace remaining URLs
        urls = re.findall(r"(https?://\S+)", content)
        for url in urls:
            if is_unsafe_link(url):
                console.print(f"Skipping unsafe link: {url}")
                continue

            try:
                info = fetch_url_info(url, fetch_method, api_key)
                cardlink = format_cardlink(info, urlencode, generate_qr, outdir_root)
                content = content.replace(url, cardlink)

            except Exception as e:
                console.print(e)

            finally:
                time.sleep(interval)  # Add interval between requests

            try:
                # Restore codeblocks, markdown links, and HTML links
                for i, block in enumerate(codeblocks):
                    content = content.replace(f"__CODEBLOCK_{i}__", block)

                for i, link in enumerate(md_links):
                    content = content.replace(
                        f"__MDLINK_{i}__", f"[{link[0]}]({link[1]})"
                    )

                for i, link in enumerate(html_links):
                    content = content.replace(f"__HTMLLINK_{i}__", f'<a href="{link}"')

                # Write frontmatter back if it existed
                if frontmatter:
                    outfile.write("---\n")
                    yaml.dump(frontmatter, outfile, default_flow_style=False)
                    outfile.write("---\n\n")

                outfile.write(content)
                console.print(f"[i] Processing (QR codes generated: {qr_count})")

            except Exception as e:
                console.print(e)


def generate_output_filename(
    input_file: str, frontmatter: Dict[str, any], seq_num: int
) -> str:
    uid = frontmatter.get("uid", "")
    name = frontmatter.get("name", os.path.splitext(os.path.basename(input_file))[0])
    version = frontmatter.get("version") or frontmatter.get("revision", 1)
    date_value = frontmatter.get("updated_at") or frontmatter.get("created_at")

    if date_value:
        if isinstance(date_value, str):
            try:
                date = datetime.fromisoformat(date_value)
            except ValueError:
                console.print(
                    f"[!]: Invalid date format in frontmatter: {date_value}. Using current date."
                )
                date = datetime.now()
        elif isinstance(date_value, datetime):
            date = date_value
        else:
            console.print(
                f"[!]: Unexpected date type in frontmatter: {type(date_value)}. Using current date."
            )
            date = datetime.now()
    else:
        date = datetime.now()

    date_folder = date.strftime("%Y/%m%d")
    outdir_root = f"outputs/{date_folder}/{int(time.time())}"

    return outdir_root, f"{outdir_root}/{uid or f'ID{seq_num:04d}'}-{name}.{version}.md"


def process_files(
    input_pattern: str,
    fetch_method: str,
    api_key: Optional[str],
    interval: float,
    urlencode: bool,
    generate_qr: bool,
):
    input_files = [f for p in input_pattern for f in glob.glob(p)]

    console.print(input_files)
    for seq_num, input_file in enumerate(
        input_files, start=1
    ):  # TODO: seq_num should per folder, not per file.
        with open(input_file, "r") as f:
            content = f.read()
        frontmatter, _ = parse_frontmatter(content)

        outdir_root, output_file = generate_output_filename(
            input_file, frontmatter, seq_num
        )
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        convert_links_to_cardlink(
            input_file,
            outdir_root,
            output_file,
            fetch_method,
            api_key,
            interval,
            urlencode,
            generate_qr,
        )
        console.print(f"[i] Processed: {input_file} ->\n\t {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert links in markdown files to cardlink format."
    )
    parser.add_argument(
        "input_pattern",
        nargs="+",
        help="Input file pattern (e.g., '*.md' or 'folder/*.md')",
    )
    parser.add_argument(
        "--fetch-method",
        choices=["microlink", "local"],
        default="local",
        help="Method to fetch URL info",
    )  # TODO
    parser.add_argument("--api-key", help="API key (if using API method)")
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Interval between requests in seconds",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum number of retries for failed fetches",
    )  # TODO
    parser.add_argument(
        "--timeout", type=int, default=10, help="Timeout for requests in seconds"
    )  # TODO
    parser.add_argument(
        "--urlencode", action="store_true", help="URL-encode the fetched text"
    )
    parser.add_argument("--qr", action="store_true", help="Generate QR codes for links")

    args = parser.parse_args()

    process_files(
        args.input_pattern,
        args.fetch_method,
        args.api_key,
        args.interval,
        args.urlencode,
        args.qr,
    )


if __name__ == "__main__":
    console = Console()
    main()
