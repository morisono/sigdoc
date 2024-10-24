# OnionShareの導入と使い方

[OnionShare](https://onionshare.org/)は、ファイルを簡単かつ安全に共有するためのオープンソースのツールです。以下にOnionShareの導入と基本的な使い方をまとめます。

## 導入手順

1. **OnionShareのダウンロード**

   [OnionShareの公式サイト](https://onionshare.org/)から最新バージョンをダウンロードしてください。

2. **インストール**

   ダウンロードしたファイルを解凍し、指示に従ってOnionShareをインストールします。

## 使い方

1. **起動**

   インストールが完了したら、OnionShareを起動します。

1. **ファイルの共有**
  OnionShareを使用してファイルを共有すると、URLとプライベートキーが生成されます。
  受信者はこのキーを使用してファイルにアクセスできます。
 
1. **オプション設定**
  ファイルがダウンロードされると、OnionShareはデフォルトでサーバーを停止します。
  複数の人にファイルをダウンロードさせる場合は、「ファイルが送信された後に共有を停止する」オプションのチェックを外すことができます。
  
1. **ファイルの受信**
  受信者は生成されたURLとプライベートキーを使用して、OnionShareにアクセスしファイルをダウンロードできます。

1. **セキュリティの注意**
  OnionShareはトークンを介してファイルにアクセスするため、セキュアなファイル共有が可能です。ただし、セキュリティに対する基本的な理解が必要です。


OnionShareを使用してファイルを共有するとき、 .onion URLとプライベートキーが生成されます。
受信者はこのキーを使用してファイルにアクセスできます。

OnionShareはデフォルトでファイルがダウンロードされるとサーバーを自動的に停止します。
複数の人々にファイルをダウンロードさせるためには、「ファイルが送信された後に共有を停止する」オプションのチェックを外すことができます1。


```sh
usage: onionshare-cli [-h] [--receive] [--website] [--chat] [--local-only]
                      [--connect-timeout SECONDS] [--config FILENAME] [--persistent FILENAME]
                      [--title TITLE] [--public] [--auto-start-timer SECONDS]
                      [--auto-stop-timer SECONDS] [--no-autostop-sharing] [--data-dir data_dir]
                      [--webhook-url webhook_url] [--disable-text] [--disable-files]
                      [--disable_csp] [--custom_csp custom_csp] [-v]
                      [filename ...]

positional arguments:
  filename                  List of files or folders to share

options:
  -h, --help                show this help message and exit
  --receive                 Receive files
  --website                 Publish website
  --chat                    Start chat server
  --local-only              Don't use Tor (only for development)
  --connect-timeout SECONDS
                            Give up connecting to Tor after a given amount of seconds (default:
                            120)
  --config FILENAME         Filename of custom global settings
  --persistent FILENAME     Filename of persistent session
  --title TITLE             Set a title
  --public                  Don't use a private key
  --auto-start-timer SECONDS
                            Start onion service at scheduled time (N seconds from now)
  --auto-stop-timer SECONDS
                            Stop onion service at schedule time (N seconds from now)
  --no-autostop-sharing     Share files: Continue sharing after files have been sent (default is
                            to stop sharing)
  --data-dir data_dir       Receive files: Save files received to this directory
  --webhook-url webhook_url
                            Receive files: URL to receive webhook notifications
  --disable-text            Receive files: Disable receiving text messages
  --disable-files           Receive files: Disable receiving files
  --disable_csp             Publish website: Disable the default Content Security Policy header
                            (allows your website to use third-party resources)
  --custom_csp custom_csp   Publish website: Set a custom Content Security Policy header
  -v, --verbose             Log OnionShare errors to stdout, and web errors to disk
```

https://docs.onionshare.org/2.6/ja/index.html