from b2sdk.v2 import InMemoryAccountInfo, B2Api

# 認証情報
application_key_id = 'yourApplicationKeyId'
application_key = 'yourApplicationKey'
bucket_name = 'yourBucketName'

# B2 APIクライアントの初期化
info = InMemoryAccountInfo()
b2_api = B2Api(info)
b2_api.authorize_account("production", application_key_id, application_key)

# アップロードするPDFファイルのパス
pdf_file_path = 'good2.png'

# B2バケット名
bucket_name = 'test-bucket-gorilla'

# PDFファイルをアップロード
bucket = b2_api.get_bucket_by_name(bucket_name)
file_info = {'content_type': 'image/png', 'original_filename':'good2.png'}
file_name = 'image1.png'

with open(pdf_file_path, 'rb') as file:
    file_data = file.read()
    uploaded_file = bucket.upload_bytes(file_data, file_name, file_info=file_info)

# ファイルリストを取得（ここでは再帰的にリストしない例）
folder_to_list = ''
for file_version, folder_name in bucket.ls(folder_to_list=folder_to_list, recursive=False):
    print(f'ファイル名: {file_version.file_name}, フォルダ名: {folder_name}')


# ダウンロードURLを取得
download_url = b2_api.get_download_url_for_fileid(uploaded_file.id_)

# ダウンロードURLを表示
print(f"ダウンロードURL: {download_url}")