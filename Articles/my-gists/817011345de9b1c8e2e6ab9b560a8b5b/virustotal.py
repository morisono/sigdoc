import vt
import time
import argparse
from datetime import datetime
from rich.console import Console
import gradio as gr

class VTAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = vt.Client(api_key)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def check_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                scan = self.client.scan_file(f)
            while True:
                response = self.client.get_object(f"/analyses/{scan.id}")
                if response.status == "completed":
                    print("Completed!")
                    break
                else:
                    print(".", end="", flush=True)
                    time.sleep(1)

            result = {
                'id': response.get("_id"),
                'last_analysis_date': response.get("date"),
                'last_analysis_stats': response.get("stats"),
            }

            vtstats = result["last_analysis_stats"]
            dt = datetime.now().isoformat()

            if vtstats["malicious"] + vtstats["suspicious"] > 0:
                with open('bad-domain.txt', 'a') as f:
                    print(dt, file_path, vtstats, file=f)
            else:
                with open('good-domain.txt', 'a') as f:
                    print(dt, file_path, vtstats, file=f)

            return result
        except Exception as e:
            print(f'[!] {e}')

    def check_hash(self, file_hash):
        try:
            response = self.client.get_object(f"/files/{file_hash}")
            result = {
                'last_analysis_date': response.get("last_analysis_date"),
                'last_analysis_stats': response.get("last_analysis_stats"),
            }
            return result
        except Exception as e:
            print(f'[!] {e}')

    def scan_url(self, url):
        try:
            url_id = vt.url_id(url)
            response = self.client.get_object(f"/urls/{url_id}")
            result = {
                'categories': response.get("categories"),
                'last_analysis_date': response.get("last_analysis_date"),
                'last_analysis_stats': response.get("last_analysis_stats"),
            }
            return result
        except Exception as e:
            print(f'[!] {e}')

    def check_dns(self, dns):
        try:
            response = self.client.get_object(f"/domains/{dns}")
            result = {
                'categories': response.get("categories"),
                'last_analysis_date': response.get("last_analysis_date"),
                'last_analysis_stats': response.get("last_analysis_stats"),
                'whois': response.get("whois"),
            }
            return result
        except Exception as e:
            print(f'[!] {e}')

    def check_ip(self, ip):
        try:
            response = self.client.get_object(f"/ip_addresses/{ip}")
            result = {
                'last_analysis_date': response.get("last_analysis_date"),
                'last_analysis_stats': response.get("last_analysis_stats"),
                'whois': response.get("whois"),
            }
            return result
        except Exception as e:
            print(f'[!] {e}')

def webui(api_key):
    def file_check_ui(file_path):
        with VTAPI(api_key) as api:
            return api.check_file(file_path)
    iface = gr.Interface(fn=file_check_ui, inputs="file", outputs="json")
    iface.launch()

def parse_args(args):
    parser = argparse.ArgumentParser(description='Check file for threats with VirusTotal.')
    parser.add_argument('api_key', type=str, help='Your VirusTotal API key')
    parser.add_argument('file_paths', nargs='*', type=str, help='Path to the file(s) to check')
    parser.add_argument('--webui', action='store_true', help='Launch the web interface')
    parser.add_argument('--hash', type=str, help='Check a file hash')
    parser.add_argument('--url', type=str, help='Check a URL')
    parser.add_argument('--dns', type=str, help='Check a DNS')
    parser.add_argument('--ip', type=str, help='Check an IP address')
    return parser.parse_args(args)

def main(args):
    args = parse_args(args[1:])
    console = Console()
    with VTAPI(args.api_key) as api:
        if args.webui:
            webui(args.api_key)
        elif args.file_paths:
            for file_path in args.file_paths:
                with console.status("[bold green]Checking file...") as status:
                    result = api.check_file(file_path)
                    console.log(result)
        elif args.hash:
            with console.status("[bold green]Checking hash...") as status:
                result = api.check_hash(args.hash)
                console.log(result)
        elif args.url:
            with console.status("[bold green]Checking URL...") as status:
                result = api.scan_url(args.url)
                console.log(result)
        elif args.dns:
            with console.status("[bold green]Checking DNS...") as status:
                result = api.check_dns(args.dns)
                console.log(result)
        elif args.ip:
            with console.status("[bold green]Checking IP...") as status:
                result = api.check_ip(args.ip)
                console.log(result)
        else:
            print("Please specify a file, hash, URL, DNS, or IP address to check.")

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
