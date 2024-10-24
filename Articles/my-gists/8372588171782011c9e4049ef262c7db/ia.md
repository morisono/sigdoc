# Internet Archive [^1]

Webpage を保存する場合は以下のリンクから保存してください。

- https://web.archive.org/save


以下はPythonを使ってInternet Archiveのコンテンツにアクセスしたり管理したりするための手順です。
1. `pip install internetarchive`でパッケージをインストールします[^1^][1]。
1. アイテムのメタデータを取得するために以下のコードを使用します[^1^][1]。

    ```python
    from internetarchive import get_item
    item = get_item('<unique_item_identifier>')
    for k,v in item.metadata.items():
        print(print(k,":",v))
    ```

1. Internet Archiveにアイテムをアップロードするために以下のコードを使用します。

    ```python
    from internetarchive import get_item
    md = {'collection': 'test_collection', 'title': 'My New Item', 'mediatype': 'movies'}
    r = item.upload('<identifier>', files=['film.txt', 'film.mov'], metadata=md, access_key='YoUrAcCEssKey', secret_key='youRSECRETKEY')
    r[0].status_code

    ```
## Internet Archiveの認証情報の取得

Internet Archiveデータベースの一部の操作には認証情報が必要です。以下にIA-S3キーを取得する手順を示します。

1. archive.orgでアカウントを作成します。
1. [こちら](https://archive.org/account/s3.php)にログインし、チェックボックスを選択して「Generate New Keys」をクリックします。
1. 提供された2つのキー（アクセスキーとシークレットキー）をメモします。


## Internet Archiveへのアイテムのアップロード

Internet Archiveにアイテムをアップロードする方法です。以下にPython 3とIA-S3キー、そしてinternet archiveパッケージが必要です。

```python
from internetarchive import get_item
md = {'collection': 'test_collection', 'title': 'My New Item', 'mediatype': 'movies'}
r = item.upload('<identifier>', files=['film.txt', 'film.mov'], metadata=md, access_key='YoUrAcCEssKey', secret_key='youRSECRETKEY')
r[0].status_code
```
このコードは、新しいアイテムを作成し、そのアイテムにファイルをアップロードします。

## Internet Archiveのアイテム
Internet Archiveは「アイテム」で構成されています。アイテムは、archive.org上の一つのWebページで表現される論理的な「もの」です。各アイテムは、その独自のメタデータを持つファイル群と考えることができます。

## iaコマンドラインツール [^5]
iaコマンドラインツールは、コマンドラインからarchive.orgのさまざまなサービスと対話することができます。このツールは、internetarchiveパッケージと一緒にインストールされます。このツールを使って、メタデータを読み書きしたり、アイテムをアップロードしたり、ダウンロードしたり、削除したり、検索したり、タスク情報を取得したり、特定のアイテム内のファイルをリストしたりすることができます。

```sh
Upload
curl $url | ia upload <identifier> - --remote-name='upload.xml.gz' --retries 10 --metadata="title:Uploaded from stdin."

ia upload --spreadsheet=uploading.csv

Download
ia download TripDown1905 --glob="*.mp4" --exclude "*512kb*"

ia download --search 'collection:glasgowschoolofart'


usage:
    ia [--help | --version]
    ia [--config-file FILE] [--log | --debug] [--insecure] <command> [<args>]...

options:
    -h, --help
    -v, --version
    -c, --config-file FILE  Use FILE as config file.
    -l, --log               Turn on logging [default: False].
    -d, --debug             Turn on verbose logging [default: False].
    -i, --insecure          Use HTTP for all requests instead of HTTPS [default: false]

commands:
    help      Retrieve help for subcommands.
    configure Configure `ia`.
    metadata  Retrieve and modify metadata for items on archive.org.
    upload    Upload items to archive.org.
    download  Download files from archive.org.
    delete    Delete files from archive.org.
    search    Search archive.org.
    tasks     Retrieve information about your archive.org catalog tasks.
    list      List files in a given item.

See 'ia help <command>' for more information on a specific command.

```


[^1]: https://archive.org/developers/quick-start-pip.html
[^2]: https://archive.org/developers/tutorial-get-ia-credentials.html
[^3]: https://archive.org/developers/tutorial-create-item.html
[^4]: https://archive.org/developers/items.html
[^5]: https://archive.org/developers/internetarchive/cli.html
- https://help.archive.org/help/uploading-a-basic-guide/