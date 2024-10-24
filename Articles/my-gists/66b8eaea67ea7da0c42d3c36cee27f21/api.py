import argparse
import httpx
import string
import smtplib
from email.mime.text import MIMEText

import asyncio

import requests
import json


class WebAPI:

    def share_file(cloud_service, username, password, input_file):
        if cloud_service == "mega":
            console.print("[~] Using Mega for sharing.")
            try:
                file_url = WebAPI.upload_to_mega(username, password, input_file)
            except Exception as e:
                console.print(f"Error: {e}")
        elif cloud_service == "google_drive":
            console.print("[~] Using Google Drive for sharing.")
            try:
                file_url = WebAPI.upload_to_google_drive(username, password, input_file)
            except Exception as e:
                console.print(f"Error: {e}")
        elif cloud_service == "slideshare":
            console.print("[~] Using SlideShare for sharing.")
            try:
                file_url = WebAPI.upload_to_slideshare(username, password, input_file)
            except Exception as e:
                console.print(f"Error: {e}")
        else:
            console.print("[!] Unsupported cloud service")

    def upload_to_mega(username, password, input_file):
        m = Mega()
        m.login(username, password)

        uploaded_file = m.upload(input_file)
        file_url = m.get_upload_link(uploaded_file)
        console.print(f"[*] File uploaded to Mega. URL: {file_url}")

        return file_url

    def upload_to_google_drive(username, password, input_file):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        file_name = os.path.basename(input_file)
        file_drive = drive.CreateFile({'title': file_name})
        file_drive.Upload()
        file_url = file_drive['alternateLink']
        console.print(f"[*] File uploaded to Google Drive. URL: {file_url}")

        return file_url

    def upload_to_slideshare(username, password, input_file, title=None, description=None, tags=None):
        upload_url = 'https://www.slideshare.net/api/2/upload_slideshow'
        auth = (username, password)

        if f"SLIDESHARE_API_KEY" in os.environ and f"SLIDESHARE_API_SECRET" in os.environ  :
            api_key = os.getenv[f"SLIDESHARE_API_KEY"]
            api_secret = os.getenv[f"SLIDESHARE_API_SECRET"]
        else:
            api_key = getpass.getpass(f"Enter SLIDESHARE API KEY:")
            api_secret = getpass.getpass(f"Enter SLIDESHARE API SECRET:")

        tz = pytz.utc
        now = datetime.datetime.now(tz)
        utime = int(now.timestamp())
        hash_salt = api_secret+str(utime)
        hash_value = hashlib.sha1(hash_salt.encode('utf-8')).hexdigest()

        with open(input_file, 'rb') as file:
            files = {'slideshow': (input_file, file)}
            data = {
                'slideshow_title': title,
                'slideshow_description': description,
                'slideshow_tags': tags
            }
            params = {
                'api_key': api_key,
                'ts': str(utime),
                'hash': hash_value,
                'username_for': username
            }

            response = requests.post(upload_url, data=data, params=params, files=files, auth=auth)

            if response.status_code == 200:
                file_url = response.url # TODO
                return f"File uploaded to SlideShare.  URL: {file_url}"
            else:
                return f"Upload error: {response.status_code}"

    def send_email(subject, message, to_email, from_email, smtp_server, smtp_port, smtp_username, smtp_password):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email

        s = smtplib.SMTP(smtp_server, smtp_port)
        s.login(smtp_username, smtp_password)
        s.sendmail(from_email, [to_email], msg.as_string())
        s.quit()

    def send_email_async(subject, message, to_email, from_email, smtp_server, smtp_port, smtp_username, smtp_password):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email

        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_email_async(msg, smtp_server, smtp_port, smtp_username, smtp_password))

    def shorten_url(url, api_key, workspace_id):
        link_request = {
            "destination": url,
            "domain": {"fullName": "rebrand.ly"},
            "apikey": api_key,
            "workspace": workspace_id
        }

        request_headers = {
            "Content-type": "application/json"
        }

        response = requests.post("https://api.rebrandly.com/v1/links", data=json.dumps(link_request), headers=request_headers)

        if response.status_code == requests.codes.ok:
            link = response.json()
            return link["shortUrl"]
        else:
            return None

    async def send_api_request(url, headers=None, params=None):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            return response

e def main():
    parser = argparse.ArgumentParser(description="Send API requests")
    parser.add_argument("url", help="API URL")
    parser.add_argument("--header", nargs="*", help="Custom headers in key=value format")
    parser.add_argument("--param", nargs="*", help="Query parameters in key=value format")

    args = parser.parse_args()

    headers = {}
    if args.header:
        for header in args.header:
            key, value = header.split("=")
            headers[key] = value

    params = {}
    if args.param:
        for param in args.param:
            key, value = param.split("=")
            params[key] = value

    response = send_api_request(args.url, headers=headers, params=params)

    if response.status_code == 200:
        print("Response:")
        print(response.text)
    else:
        print(f"API request failed with status code {response.status_code}")

if __name__ == "__main__":
    main()
