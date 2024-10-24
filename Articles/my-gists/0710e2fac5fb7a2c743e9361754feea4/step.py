import asyncio
import qrcode
import requests
import uvloop
from io import BytesIO
# from google.cloud import storage
from pyshorteners import Shortener
import bitly_api

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

class BaseState:
    def __init__(self):
        self.qr_path = None
        self.cloud_url = None
        self.archive_url = None
        self.shortened_url = None

class ImageProcessor:
    @staticmethod
    async def gen_qr(data, out_path, **qr_params):
        qr = qrcode.QRCode(**qr_params)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(out_path)
        return out_path

class Utils:
    @staticmethod
    # async def save_cloud(file_path, bucket_name):
    #     storage_client = storage.Client()
    #     bucket = storage_client.bucket(bucket_name)
    #     blob = bucket.blob(file_path)
    #     blob.upload_from_filename(file_path)
    #     return blob.public_url

    @staticmethod
    async def send_to_archive(url):
        archive_request_url = f"https://web.archive.org/save/{url}"
        response = requests.get(archive_request_url)
        if response.status_code == 200:
            archive_url = f"https://web.archive.org/web/{url}"
            return archive_url
        else:
            raise Exception("Error archiving the URL")

    @staticmethod
    async def shorten_bitly(url):
        bitly_access_token = os.getenv('BITLY_ACCESS_TOKEN', None)
        bitly = bitly_api.Connection(access_token=bitly_access_token)
        short_url = bitly.shorten(url_received)
        return short_url

    @staticmethod
    async def shorten_tinyurl(url):
        shortener = Shortener()
        short_url = shortener.tinyurl.short(url)
        return short_url

    async def shorten_rebrandly(url):

        linkRequest = {
        "destination": "https://www.youtube.com/channel/UCHK4HD0ltu1-I212icLPt3g"
        , "domain": { "fullName": "rebrand.ly" }
        # , "slashtag": "A_NEW_SLASHTAG"
        # , "title": "Rebrandly YouTube channel"
        }

        requestHeaders = {
        "Content-type": "application/json",
        "apikey": "YOUR_API_KEY",
        "workspace": "YOUR_WORKSPACE_ID"
        }

        r = requests.post("https://api.rebrandly.com/v1/links",
            data = json.dumps(linkRequest),
            headers=requestHeaders)

        if (r.status_code == requests.codes.ok):
            link = r.json()
            print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))

async def main():
    state = BaseState()

    # Step 1: Generate QR Code
    qr_data = "https://example.com"
    qr_path = "qr_code.png"
    out_path = await ImageProcessor.gen_qr(qr_data, qr_path)
    state.qr_path = qr_path

    # Step 2: Save to Cloud
    cloud_bucket_name = "your_bucket_name"
    # state.cloud_url = await Utils.save_cloud(qr_path, cloud_bucket_name)

    # Step 3: Send to Archive
    # state.archive_url = await Utils.send_to_archive(state.cloud_url)
    # state.archive_url = await Utils.send_to_archive(state.qr_path)

    # Step 4: Shorten Link
    # state.shortened_url = await Utils.shorten_tinyurl(state.archive_url)
    state.shortened_url = await Utils.shorten_tinyurl(state.qr_path)

    print("QR Path:", state.qr_path)
    print("out_path:", out_path)
    print("Cloud Drive URL:", state.cloud_url)
    print("Wayback URL:", state.archive_url)
    print("Shortened Link:", state.shortened_url)

asyncio.run(main())
