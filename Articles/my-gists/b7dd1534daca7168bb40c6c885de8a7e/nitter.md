# Nitter: 軽量Twitterフロントエンドのセルフホスティング

TwitterのフロントエンドであるNitterは、軽量な代替サービスとして人気があります。Twitterが遅く、画像の読み込みに問題がある場合、Nitterは便利な選択肢です。この記事では、Nitterのセルフホスティングについて説明します。 [^1] [^2]

## Nitterの特徴
Nitterは軽量で高速なTwitterフロントエンドで、以下の特徴を備えています：
- 軽量なデザイン
- イベントのハッシュタグの追跡
- 過去のツイートの検索
- RSS形式での出力

ただし、現時点ではログイン機能は提供されておらず、投稿や非公開リストなどは利用できません。

## 手順
以下はNitterをセルフホストする手順の概要です：

1. Nitterのインストール環境の用意：
   - Redisとlibsassのインストール
   ```
    $ sudo apt install redis-server libsass-dev
    $ sudo groupadd nitter (1)
    $ sudo useradd -m -g nitter nitter (2)
    $ sudo -iu nitter (3)
   ```
1. nimのセットアップ：
   - nim1.2.0以上が必要で、公式サイトからバイナリをダウンロード
   ```
    $ export PATH=~/nim-1.6.4/bin:${PATH}
    $ nimble build -d:release
    $ dpkg-query -W nim
    $ wget https://nim-lang.org/download/nim-1.4.2-linux_x64.tar.xz \
    https://nim-lang.org/download/nim-1.4.2-linux_x64.tar.xz.sha256 (1)
    $ sha256sum -c ./nim-1.4.2-linux_x64.tar.xz.sha256 (2)
    $ tar tvf nim-1.4.2-linux_x64.tar.xz | lv (3)
    $ tar xvf nim-1.4.2-linux_x64.tar.xz (4)
   ```
1. Nitterのコンパイル：
   - Nitterのソースコードをクローンしてコンパイル
   ```
    $ git clone https://github.com/zedeus/nitter
    $ cd nitter
    $ PATH=~/nim-1.4.2/bin:$PATH nimble build -d:release
    $ PATH=~/nim-1.4.2/bin:$PATH nimble scss
    $ mkdir ./tmp
   ```
1. Nitterの起動：
   - Redisが起動していることを確認し、Nitterを起動
   `/etc/systemd/system/nitter.service`
   ```
    [Unit]
    Description=Nitter (An alternative Twitter front-end)
    After=syslog.target
    After=network.target

    [Service]
    Type=simple

    # set user and group
    User=nitter
    Group=nitter

    # configure location
    WorkingDirectory=/home/nitter/nitter
    ExecStart=/home/nitter/nitter/nitter

    Restart=always
    RestartSec=15

    [Install]
    WantedBy=multi-user.target
   ```
1. システムDサービスファイルの設定：
   - Nitterの自動起動設定
   ```
    $ sudo systemctl enable --now nitter.service
    $ systemctl status nitter
    $ w3m http://localhost:8080/
   ```
1. ドメインとSSL証明書の設定（オプション）：
   - インターネットに公開する場合の設定
   ```
   $ sudo certbot certonly -d nitter.example.org
   ```
1. Apache HTTPサーバーの設定（オプション）：
   - この手順はローカルで動かす場合は必要ありません．
   - セキュリティ向上のためApacheを利用してトラフィックを転送
   `/etc/apache2/sites-available/nitter.example.org.conf`
   ```
    <VirtualHost *:80>
            ServerName nitter.example.org
            Redirect permanent / https://nitter.example.org/
    </VirtualHost>
    <IfModule mod_ssl.c>
    <VirtualHost *:443>
            ServerName nitter.example.org
            ServerAdmin webmaster@matoken.org

            <Proxy *>
                    Order deny,allow
                    Allow from all
            </Proxy>

            ProxyPreserveHost On
            ProxyPass / http://127.0.0.1:8080/ nocanon
            ProxyPassReverse / http://127.0.0.1:8080/
            AllowEncodedSlashes On

            ErrorLog ${APACHE_LOG_DIR}/error.nitter.example.org.log
            CustomLog ${APACHE_LOG_DIR}/access.nitter.example.org.log combined

            SSLCertificateFile /etc/letsencrypt/live/nitter.example.org/fullchain.pem
            SSLCertificateKeyFile /etc/letsencrypt/live/nitter.example.org/privkey.pem

    </VirtualHost>
    </IfModule>
   ```
1. サービスの有効化：
   - サービスを有効化してNitterを起動
   ```
    $ sudo a2ensite nitter.example.org.conf (1)
    $ sudo apache2ctl configtest (2)
    $ sudo systemctl reload apache2 (3)
   ```
1. ウェブブラウジング：
   - Nitterが正しく動作していることを確認

## まとめ
Nitterをセルフホストすることで、Twitterの軽量で高速なフロントエンドをローカルマシンやサーバーで利用できます。これにより、外部制限に依存せずに自分のコントロール下でTwitterを閲覧できます。

[^1]: https://matoken.org/blog/2021/02/17/self-hosting-the-lightweight-twitter-front-end-nitter/
[^2]: https://matoken.org/blog/2022/03/11/nitter-upgrade-note2022-03/

- [Instances · zedeus/nitter Wiki · GitHub](https://github.com/zedeus/nitter/wiki/Instances)

[View Twitter Without Account | TweeteDelete](https://tweetdelete.net/resources/view-twitter-without-account-3-solutions-that-still-work/)
- [Twitter Proxy - The Top 10 Tools and Services — RapidSeedbox](https://www.rapidseedbox.com/blog/twitter-proxy-services-tools)
