
import os
import tempfile
import zipfile
import unittest
import sublist3r
import gradio as gr
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service

class TestSublist3r(unittest.TestCase):
    def test_sublist3r_main():
        domain = 'yahoo.com'
        no_threads = 40
        savefile = 'yahoo_subdomains.txt'
        ports = None
        silent = False
        verbose = False
        enable_bruteforce = False
        engines = None

        subdomains = sublist3r.main(domain, no_threads, savefile, ports, silent, verbose, enable_bruteforce, engines)

        # テストケース: subdomainsが空でないことを確認
        self.assertTrue(subdomains)

class Sublist3r:
    @staticmethod
    def run(*params):
        params = [None if p == "" else p for p in params]
        subdomains = sublist3r.main(*params)

        return subdomains

    @staticmethod
    def save(subdomains, savefile):
        temp_dir = tempfile.mkdtemp()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp_zip_path = os.path.join(temp_dir, f"{timestamp}-captured.zip")
        temp_json_path = os.path.join(temp_dir, f"{timestamp}-subdomains.txt")

        with open(savefile, 'w') as f:
            for subdomain in subdomains:
                f.write(subdomain + '\n')

class Scraper:
    @staticmethod
    def capture(subdomains, capture_full_page=False, interruption=None):

        temp_dir = tempfile.mkdtemp()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_dir = os.path.join(temp_dir, f"{timestamp}-captured")

        os.makedirs(output_dir, exist_ok=True)
        results = []

        for idx, subdomain in enumerate(subdomains):
            total = len(subdomains)
            try:
                url = f"https://{subdomain}"
                output_file = os.path.join(output_dir, f"{subdomain}_screenshot.png")

                if capture_full_page:
                    print(f'[~] Capturing {idx}/{total} : {url}')
                    # if interruption:
                    #     print('[~] Interrupted')
                    #     break
                    result = Scraper.full_page(url, output_file)
                    results.append(result)
            except WebDriverException as e:
                results.append({"subdomain": subdomain, "error": str(e)})
        return results

    def full_page(url, output_file):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        # driver = webdriver.Chrome(options=options)
        driver_path = os.path.join('driver', 'chromedriver_linux64/chromedriver')
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        # driver.implicitly_wait(10)
        driver.get(url)
        driver.save_screenshot(output_file)
        driver.quit()
        print(f'[~] Captured: {url}')

        return output_file

class WebUI:
    def __init__(self):
        self.inputs = [
            gr.Textbox(label="Domain"),
            gr.Number(minimum=1, maximum=100, label="Number of Threads", step=1),
            gr.Textbox(label="Save File"),
            gr.Textbox(label="Ports (comma-separated)"),
            gr.Checkbox(label="Silent Mode"),
            gr.Checkbox(label="Verbose Mode"),
            gr.Checkbox(label="Enable Bruteforce"),
            gr.Textbox(label="Engines (comma-separated)"),
            gr.Checkbox(label="Capture Full Page"),
            gr.Button("Interrupt")
        ]
        self.outputs = ["gallery", "json"]

        self.examples = [
            ["yahoo.com", 40, "subdomains.txt", None, False, False, False, None, False],
            ["yahoo.com", 40, "subdomains.txt", None, False, False, False, None, True],
        ]

    def launch(self):
        iface = gr.Interface(
            title="Sublist3r",
            fn=self.process_url,
            inputs=self.inputs,
            outputs=self.outputs,
            examples=self.examples,
            live=False
        )
        iface.launch()

    def process_url(self, *params):
        try:
            params = [None if p == "" else p for p in params]
            subdomains = Sublist3r.run(*params[:8])
            result_json = gr.JSON({'url': subdomains})
            if subdomains and params[-2]:
                Sublist3r.save(subdomains, params[2])
                capture_result = Scraper.capture(subdomains, params[-2], params[-1])
                result_gallery = gr.Gallery(capture_result)

                return result_gallery, result_json

        except Exception as e:
            return None, {'status': f"Error: {e}"}

if __name__ == '__main__':
    # テストを実行
    # test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestSublist3r))

    # # テストが成功した場合のみ Gradio Web UI を起動
    # if test_result.wasSuccessful():
    #     web_ui = WebUI()
    #     web_ui.launch()

    web_ui = WebUI()
    web_ui.launch()
