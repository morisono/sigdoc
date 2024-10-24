import aiohttp
import asyncio
import argparse
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from rich.logging import RichHandler
from rich.progress import track
import signal

logging.basicConfig(level=logging.INFO, format="%(message)s", datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True)])

async def fetch_url(session, url):
    try:
        async with session.head(url) as response:
            return url, response.status
    except aiohttp.ClientError as e:
        logging.exception(f"{e}")
        return url, None

async def extract_links(session, base_url, response):
    links = set()
    try:
        html_content = await response.read()
        html = BeautifulSoup(html_content.decode('utf-8', errors='replace'), 'html.parser')
        for a_tag in html.find_all('a', href=True):
            link = a_tag['href']
            absolute_link = urljoin(base_url, link)
            links.add(absolute_link)
    except Exception as e:
        logging.exception(f"{e}")
    return links

async def check_links_recursive(session, base_url, max_depth, output_file, interval):
    links_to_check = [(base_url, 0)]
    checked_links = set()

    try:
        while links_to_check:
            current_url, depth = links_to_check.pop(0)

            if max_depth == -1 or depth <= max_depth:
                url, status = await fetch_url(session, current_url)

                if status == 200 and url not in checked_links:
                    async with session.get(url) as response:
                        extracted_links = await extract_links(session, current_url, response)
                        checked_links.add(url)
                        logging.info(f"{status}    {url}")
                        for link in extracted_links:
                            links_to_check.append((link, depth + 1))
                else:
                    logging.error(f"{status}    {url}")

                await asyncio.sleep(interval / 1000)
    except asyncio.CancelledError:
        logging.info("Interrupted. Writing results to %s before exiting.", output_file)

    except Exception as e:
        logging.exception(f"{e}")

    finally:
        with open(output_file, "w") as file:
            for url in checked_links:
                file.write(f"{url}\n")
        logging.info(output_file)
        return

async def check_links(base_url, max_depth, output_file, interval):
    async with aiohttp.ClientSession() as session:
        await check_links_recursive(session, base_url, max_depth, output_file, interval)

def main():
    parser = argparse.ArgumentParser(description="Check links recursively using aiohttp and rich.")
    parser.add_argument("url", help="Base URL to start checking links.")
    parser.add_argument("-d", "--max-depth", type=int, default=-1, help="Maximum depth for recursive link checking.")
    parser.add_argument("-o", "--output-file", default="links.txt", help="Output file to save link checking results.")
    parser.add_argument("--progress", action="store_true", help="Enable progress bar.")
    parser.add_argument("-i", "--interval", type=int, default=100, help="Interval between HTTP requests in milliseconds.")

    args = parser.parse_args()

    asyncio.run(check_links(args.url, args.max_depth, args.output_file, args.interval))

if __name__ == "__main__":
    main()
