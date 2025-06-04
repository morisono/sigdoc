---
<div class=
><ul>
title: Sourcehut Setup
name: SourcehutSetup
description: Sourcehut Setup
type: overview
categories: tech
topics: tech
tags: 
  - #note

id: 835902
uid: 967925a5-8e2c-4150-ba1b-9e00ea389ff1
date: 2024-09-01T21:30:43
created_at: 1725193843
updated_at: 1725193843
path: Notes/pending/sourcehut-setup.md
slug: sourcehut_setup
url: https://username.github.io/repo/posts/2024/09/01/0/1/sourcehut-setup
redirect_from: 
  - 

lang: en
author: undefined
private: true
weight: 1
toc: false
draft: true
status: 
keywords: 
changelog: 
versions: 
</ul></div>
---

# SourceHut サーバーをホスティングする

<div class='top' align='center'>
  <img src='top.png' alt='alt' height='200px'>
</div>
<div class="toc"></div>
<div style="page-break-after: always;"></div>


## 概要

このガイドでは、Windows Subsystem for Linux 2 (WSL2) 上で SourceHut サーバーをホスティングし、DevSecOps のベストプラクティスを適用するための手順を詳細に説明します。SourceHut は、柔軟でセキュアな自動化可能な Git サービスとして知られています。このガイドは、SourceHut のインストール、設定、SSL 証明書の統合、データベース権限の管理、アップグレード、バックアップの手順を含む、サーバーの完全なセットアップをカバーします。

## はじめに

SourceHut は、ソースコード管理とプロジェクトホスティングを提供するオープンソースのプラットフォームです。これは、高いカスタマイズ性、セキュリティ、および自動化の機能を備えています。WSL2 上での SourceHut のホスティングは、Windows 上で Linux の機能をフルに活用しながら、軽量かつ効率的な開発環境を提供します。このガイドでは、SourceHut サーバーをセットアップし、DevSecOps のベストプラクティスを適用して、セキュアなソフトウェア開発環境を構築する方法を解説します。

## 方法

### 前提条件

1. **WSL2 が有効な Windows 10/11**
   - WSL2 をインストールし、Linux ディストリビューション (例: Ubuntu) をセットアップします。
2. **Linux コマンドラインインターフェース (CLI) の基本的な理解**
   - `git`、`curl`、`nano`、`vim`、`systemctl` などのツールに慣れていること。
3. **PostgreSQL データベース**
   - SourceHut は PostgreSQL をバックエンドとして使用します。
4. **SSL 証明書**
   - セキュリティのため、SSL 証明書を取得して設定します。
5. **管理者権限**
   - システムにソフトウェアをインストールおよび設定するための必要な権限があることを確認してください。

### 手順

#### 1. WSL2 環境のセットアップ

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

#### 2. PostgreSQL のインストールと設定

1. PostgreSQL をインストール:
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```
2. PostgreSQL サービスを起動して自動起動を有効化:
   ```bash
   sudo systemctl start postgresql
   sudo systemctl enable postgresql
   ```
3. SourceHut 用のデータベースとユーザーを作成:
   ```bash
   sudo -u postgres psql
   CREATE DATABASE sourcehut;
   CREATE USER srht_user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE sourcehut TO srht_user;
   ```

#### 3. SourceHut のインストール

1. SourceHut の依存関係をインストール:
   ```bash
   sudo apt install python3 python3-pip python3-venv libpq-dev
   ```
2. 仮想環境を作成して有効化:
   ```bash
   python3 -m venv srht-env
   source srht-env/bin/activate
   ```
3. SourceHut をクローンしてインストール:
   ```bash
   git clone https://git.sr.ht/~sircmpwn/builds.sr.ht
   cd builds.sr.ht
   pip install -r requirements.txt
   python setup.py install
   ```

#### 4. SourceHut の設定

1. 設定ファイルを作成:
   ```bash
   cp example-config.ini config.ini
   nano config.ini
   ```

2. 設定例:
   ```bash
   [database]
   uri = postgresql://srht_user:password@localhost/sourcehut

   [server]
   listen_addr = 0.0.0.0:5000
   ```

3. サービスとして SourceHut を設定:
   ```bash
   sudo nano /etc/systemd/system/sourcehut.service
   ```

4. SourceHut を起動して自動起動を有効化:
   ```bash
   sudo systemctl start sourcehut
   sudo systemctl enable sourcehut
   ```

### 設定ファイル

#### a) SourceHut 設定ファイル: `config.ini`
```bash
[database]
uri = postgresql://srht_user:password@localhost/sourcehut

[server]
listen_addr = 0.0.0.0:5000
```

#### b) SourceHut サービスファイル: `/etc/systemd/system/sourcehut.service`
```bash
[Unit]
Description=SourceHut
After=network.target

[Service]
User=$(whoami)
WorkingDirectory=/path/to/builds.sr.ht
ExecStart=/path/to/srht-env/bin/python /path/to/builds.sr.ht/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### SSL 証明書の設定

1. `certbot` を使用して SSL 証明書を取得:
   ```bash
   sudo apt install certbot
   sudo certbot certonly --standalone -d yourdomain.com
   ```
2. SourceHut を SSL 使用に設定:
   ```bash
   [server]
   listen_addr = 0.0.0.0:5000
   tls_cert_path = /etc/letsencrypt/live/yourdomain.com/fullchain.pem
   tls_key_path = /etc/letsencrypt/live/yourdomain.com/privkey.pem
   ```

### データベースの権限管理

1. PostgreSQL データベースに対する適切な権限を設定:
   ```bash
   GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO srht_user;
   ```

### アップグレード

1. SourceHut のコードベースをバックアップ:
   ```bash
   tar -czvf sourcehut-backup-$(date +%F).tar.gz /path/to/builds.sr.ht
   ```
2. 最新のコードを取得し、インストールを更新:
   ```bash
   cd /path/to/builds.sr.ht
   git pull
   pip install -r requirements.txt --upgrade
   sudo systemctl restart sourcehut
   ```

### バックアップ

1. cron ジョブを使用してデータベースをバックアップ:
   ```bash
   crontab -e
   ```
2. 毎日バックアップするために次の行を追加:
   ```bash
   0 3 * * * pg_dump -U srht_user sourcehut > /var/backups/sourcehut-$(date +\%F).sql
   ```

### Next Steps

1. **プロジェクトのセットアップ**: SourceHut上で新しいプロジェクトを作成し、Gitリポジトリを初期化します。リポジトリはSSH経由で操作し、公開鍵認証を設定することが推奨されます。

2. **コードのホスティング**: プロジェクトにコードをプッシュし、リポジトリの設定を行います。SourceHutでは、リポジトリの管理に関して細かい設定が可能ですので、必要に応じて設定をカスタマイズしてください。

3. **パッチの管理**: SourceHutのメールベースのワークフローを使用して、パッチを送受信します。メールでのパッチ送信は、細かいレビューと共同作業に適しています。

4. **CI/CDの設定**: SourceHutのBuildsサーバーを使用して、継続的インテグレーションと継続的デプロイメント（CI/CD）のワークフローを設定します。これにより、自動化されたテストやビルドプロセスを容易に構築できます。

5. **プロジェクトの管理**: SourceHutのタスク管理ツールを使用して、プロジェクトの進行状況を追跡します。シンプルで直感的なインターフェースを活用し、タスクやマイルストーンを効率的に管理しましょう。

6. **自動化**

7. **メーリングリスト**

## 参考

- [SourceHut マニュアル](https://man.sr.ht/)

