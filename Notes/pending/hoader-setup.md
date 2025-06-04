---
<div class="frontmatter">
title: Hoarder setup
name: hoader-setup
description: 
status: pending
categories: pkm
tags: 
  - #hoarder

lang: en
private: true
weight: 1
image: 
video: 
id: 581d1a
uid: ffc1c54d-9d47-4c43-961c-fcc290f67f03
link: https://username.github.io/repo/posts/2024/08/23/0/1/hoarder-setup-
path: Notes/pending/hoader-setup.md
slug: hoader-setup
date: 2024-08-23T11:24:09
created_at: 1724379849
updated_at: 1724379849
</div>
---

# Hoarder: A Bookmark and Note Taking App 


## Abstract

Hoarder はWeb APIベースのブックマークマネージャ・ソフトウェアです。

## Introduction

- 🔗 Bookmark links, take simple notes and store images and pdfs.
- ⬇️ Automatic fetching for link titles, descriptions and images.
- 📋 Sort your bookmarks into lists.
- 🔎 Full text search of all the content stored.
- ✨ AI-based (aka chatgpt) automatic tagging. With supports for local models using ollama!
- 🔖 Chrome plugin and Firefox addon for quick bookmarking.
- 📱 An iOS app, and an Android app.
- 🌙 Dark mode support.
- 💾 Self-hosting first.
- [Planned] Downloading the content for offline reading.

## Methodologies

### 技術仕様
- Hoarder :HoarderのメインWebアプリ。
- hoarder-worker:Hoarderのバックグラウンドワーカー（AIタグ付けの実行、コンテンツの取得など）。
- Redis:現在、Webアプリとバックグラウンドワーカー間の通信に使用されています。
- Browserless :コンテンツの取得に使用されるクロムヘッドレスサービス。Hoarderの公式ドッカーコンポーズはブラウザーレスを使用していませんが、現在、unraidで利用可能な唯一のヘッドレスクロームサービスであるため、使用する必要があります。
- MeiliSearch:Hoarderが使用する検索エンジン。

### Getting started

- Create new dir / Download compose file
```bash
mkdir ~/hoarder/ && cd ~/hoarder/
wget https://raw.githubusercontent.com/hoarder-app/hoarder/main/docker/docker-compose.yml

```

- Setup `.env`
```bat
HOARDER_VERSION=release
NEXTAUTH_SECRET=super_random_string
MEILI_MASTER_KEY=another_random_string
NEXTAUTH_URL=http://localhost:3000
```
 - [https://docs.hoarder.app/configuration](https://docs.hoarder.app/configuration)

- Edit `docker-compose.yaml`
```yaml
  web:
    image: ghcr.io/mohamedbassem/hoarder-web:${HOARDER_VERSION:-release}
    restart: unless-stopped
    volumes:
      - /mnt/user/appdata/hoarder/data:/data
    ports:
      - 3000:3000
    env_file:
      - .env
    environment:
      REDIS_HOST: redis
      MEILI_ADDR: http://meilisearch:7700
      DATA_DIR: /data
```
  - OPENAI_API_KEY
  - Port: 他のアプリと重複する場合、ポート変更するなど。 `3010:3000` 3000 -> 3010 

- Start docker containner
```sh
docker compose up -d
```

- Register / Login 
e.g.
```yaml
email: demo@hoarder.app
password: demodemo
```

- Import URL List ( Netscape HTML Format ): サムネイル取得に時間を要します。

### Sharing page extension
- [iOS | Hoarder App](https://apps.apple.com/us/app/hoarder-app/id6479258022)
- [Hoarder App - Apps on Google Play](https://play.google.com/store/apps/details?id=app.hoarder.hoardermobile&pcampaignid=web_share)
- [Chrome](https://chromewebstore.google.com/detail/hoarder/kgcjekpmcjjogibpjebkhaanilehneje)
- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/hoarder/)
- [localhost](https://localhost:3010)

### Automatic tagging (Optional)

- Add OpenAI API Info

-  Text: `gpt-3.5-turbo-0125` 1000+ bookmarks for less than $1.
-  Image: `gpt-4-turbo` or `gpt-3.5-turbo` around 350 token per image inference which ends up costing around $0.01 per inference


- Ollama Integration
- `.env`
- 同じネットワークにollamaを追加し、コンテナー名で参照するか、host.docker.internal　IP Pointを指定する。
```yaml
OLLAMA_BASE_URL=http://host.docker.internal:11434
INFERENCE_TEXT_MODEL=llama3.1
INFERENCE_IMAGE_MODEL=llava
```

- `compose.yaml`
```yaml
services:
    environment:
      OLLAMA_BASE_URL: http://host.docker.internal:11434

    extra_hosts:
      - "host.docker.internal:172.20.0.1"
```

**Ref. **
- [Getting Title at 26:29](https://stackoverflow.com/questions/48546124/what-is-the-linux-equivalent-of-host-docker-internal)


### CLI 

```bash
npm install -g @hoarderapp/cli

hoader list
```

## References

1. https://github.com/hoarder-app/hoarder
1. https://linuxtldr.com/hoarder-bookmarking-app/
1. https://docs.hoarder.app/Installation/
1. https://github.com/ollama/ollama/issues/703#issuecomment-1951444576