
# 完全ガイド: WSL2 で Gitea サーバーと DevSecOps をホスティングする方法

## 概要

このガイドは、Windows Subsystem for Linux 2 (WSL2) 上で Gitea サーバーをホスティングし、DevSecOps プラクティスを実装するための包括的なステップバイステップの解説を提供します。このガイドでは、Gitea のインストール、設定、および管理、SSL 証明書の統合、データベース権限、アップグレード戦略、バックアップ手順について詳しく説明します。

## はじめに

Gitea は、GitHub に似たコラボレーション開発とバージョン管理を提供する、軽量で自己ホスティング型の Git サービスです。WSL2 上で Gitea をホスティングすることで、Windows マシン上で Linux 環境を活用し、両システムの利点を組み合わせることができます。このガイドでは、開発ライフサイクルのすべての段階でセキュリティが統合されるよう、DevSecOps プラクティスも取り入れます。

## 方法論

### 前提条件

1. **WSL2 が有効な Windows 10/11**
   - WSL2 をインストールし、Linux ディストリビューション (例: Ubuntu) をセットアップします。
2. **Linux コマンドラインインターフェース (CLI) の基本的な理解**
   - `curl`、`nano`、`vim`、`systemctl` などのツールに慣れていること。
3. **Docker のインストール (オプション)**
   - Gitea のインストールをコンテナ化する際に便利です。
4. **管理者権限**
   - システムにソフトウェアをインストールおよび設定するための必要な権限があることを確認してください。

### 手順

#### 1. WSL2 環境をセットアップする

1. WSL2 をインストール:
   ```bash
   wsl --install
   ```
2. Linux ディストリビューションを更新およびアップグレード:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
3. 必要なツールをインストール:
   ```bash
   sudo apt install -y git curl nano wget
   ```

#### 2. Gitea をインストール

1. Gitea をダウンロードしてインストール:
   ```bash
   wget -O gitea https://dl.gitea.io/gitea/1.20/gitea-1.20-linux-amd64
   chmod +x gitea
   sudo mv gitea /usr/local/bin/
   ```



- またはLinuxBrewを介して
   ```
   brew install gitea
   ```

2. Gitea ディレクトリを作成:
   ```bash
   sudo mkdir -p /var/lib/gitea/{custom,data,log}
   sudo chown -R $(whoami): /var/lib/gitea/
   sudo chmod -R 750 /var/lib/gitea/
   ```

#### 3. Gitea を設定

1. Gitea の設定ファイルを作成:
   ```bash
   sudo nano /etc/gitea/app.ini
   ```
2. 設定例:
   ```bash
   [database]
   DB_TYPE  = sqlite3
   PATH     = /var/lib/gitea/data/gitea.db

   [server]
   DOMAIN           = localhost
   HTTP_PORT        = 3000
   ROOT_URL         = http://localhost:3000/
   DISABLE_SSH      = false
   START_SSH_SERVER = true
   SSH_PORT         = 22
   LFS_START_SERVER = true
   LFS_CONTENT_PATH = /var/lib/gitea/data/lfs
   ```

3. Gitea をサービスとして開始:
   ```bash
   sudo systemctl start gitea
   sudo systemctl enable gitea
   ```

### 設定ファイル

#### a) Gitea 設定ファイル: `/etc/gitea/app.ini`
```bash
[database]
DB_TYPE  = sqlite3
PATH     = /var/lib/gitea/data/gitea.db

[server]
DOMAIN           = localhost
HTTP_PORT        = 3000
ROOT_URL         = http://localhost:3000/
DISABLE_SSH      = false
START_SSH_SERVER = true
SSH_PORT         = 22
LFS_START_SERVER = true
LFS_CONTENT_PATH = /var/lib/gitea/data/lfs
```

#### b) Gitea サービスファイル: `/etc/systemd/system/gitea.service`
```bash
[Unit]
Description=Gitea (Git with a cup of tea)
After=network.target

[Service]
User=git
Group=git
WorkingDirectory=/var/lib/gitea/
ExecStart=/usr/local/bin/gitea web
Restart=always
Environment=USER=git HOME=/var/lib/gitea GITEA_WORK_DIR=/var/lib/gitea

[Install]
WantedBy=multi-user.target
```

### SSL 証明書

1. SSL 用に `certbot` をインストール:
   ```bash
   sudo apt install certbot
   ```
2. SSL 証明書を取得:
   ```bash
   sudo certbot certonly --standalone -d yourdomain.com
   ```
3. Gitea を SSL 使用に設定:
   ```bash
   [server]
   PROTOCOL     = https
   CERT_FILE    = /etc/letsencrypt/live/yourdomain.com/fullchain.pem
   KEY_FILE     = /etc/letsencrypt/live/yourdomain.com/privkey.pem
   ```

### データベース権限

1. MySQL または PostgreSQL をセットアップ:
   ```bash
   sudo apt install mysql-server
   ```
2. Gitea データベースを作成:
   ```bash
   mysql -u root -p
   CREATE DATABASE gitea;
   CREATE USER 'gitea'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON gitea.* TO 'gitea'@'localhost';
   FLUSH PRIVILEGES;
   ```

### アップグレード

1. Gitea インスタンスをバックアップ:
   ```bash
   tar -czvf gitea-backup-$(date +%F).tar.gz /var/lib/gitea
   ```
2. Gitea バイナリをダウンロードして置き換え:
   ```bash
   wget -O gitea https://dl.gitea.io/gitea/latest/gitea-1.20-linux-amd64
   chmod +x gitea
   sudo mv gitea /usr/local/bin/
   sudo systemctl restart gitea
   ```

### バックアップ

1. cron ジョブを使用してバックアップを自動化:
   ```bash
   crontab -e
   ```
2. 毎日バックアップするために次の行を追加:
   ```bash
   0 2 * * * tar -czvf /var/backups/gitea-$(date +\%F).tar.gz /var/lib/gitea
   ```

## 参考

### 公式
- [Gitea Official Website](https://gitea.io/)
- [demo](https://try.gitea.io/)
- [docs](https://about.gitea.com/)

### 外部サービス
- [Gitea Hosting: a fully managed private Gitea server for you and your people.](https://hostedgitea.com/#about)
- [Gitea Cloud: A brand new platform for managed Gitea Instances | Gitea Blog](https://blog.gitea.com/gitea-cloud/)

### 関連
- [Ubuntu に Gitea をインストールする](https://linuxize.com/post/how-to-install-gitea-on-ubuntu-20-04/)
- [rent-a-hero.de/wp-content/uploads/2018/10/DroneIO\_Gitea\_CI.pdf](https://www.rent-a-hero.de/wp-content/uploads/2018/10/DroneIO_Gitea_CI.pdf)
- [cookbook\_2.pdf](https://www.mygetea.org/uploads/5/8/0/9/58092543/cookbook_2.pdf)
- [How to use Git credential store on WSL (Ubuntu on Windows)? - Stack Overflow](https://stackoverflow.com/questions/45925964/how-to-use-git-credential-store-on-wsl-ubuntu-on-windows)
- [Wsl gitea - Raspberry Valley](https://raspberry-valley.azurewebsites.net/wsl-gitea/)
- [Linux 使いになりたい人向けの Intel N100 ミニ PC で構築する開発環境（７）- HTTPS 対応版 Gitea](https://zenn.dev/hiro345/articles/n100_07_20240218)
- [WSL2のUbuntu 20.04にGiteaを生やす - Lycolog](https://blog.lycolia.info/0156)
- [5 Steps: Migrate from GitLab to Gitea](https://blog.kay.sh/migrate-from-gitlab-to-gitea/)