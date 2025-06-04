---
<div class="frontmatter"><ul>
title: Twscrape
name: Twscrape
description: Twscrape
type: overview
categories: tech
topics: tech
tags: 
  ### #note

id: d874cd
uid: 3fcc31a5-4dce-48c1-8bea-728e081c5f11
date: 2024-09-08T07:32:49
created_at: 1725748369
updated_at: 1725748369
path: Articles/my-gists/b5b7eb62d86af7f15616e000ff77f10b/twscrape.md
slug: twscrape
url: https://username.github.io/repo/posts/2024/09/08/0/1/twscrape
redirect_from: 
  ### 

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

# Twscrape

<div class="toc">
- [Twscrape](#twscrape)
  - [Abstract](#abstract)
  - [Introduction](#introduction)
  - [Methodologies](#methodologies)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
    - [Auth and check](#auth-and-check)
    - [Search](#search)
    - [Using database](#using-database)
    - [Using proxy](#using-proxy)
    - [For more details](#for-more-details)
  - [References](#references)
</div>
<div style="page-break-after: always;"></div>


## Abstract

X-Twitterの調査を行う。OSINTツール twscrape の解説。

## Introduction

Twscrape is an open-source tool for extracting and analyzing Twitter data. It provides a comprehensive framework for conducting social media intelligence gathering, allowing users to scrape tweets based on various criteria such as 
keywords, hashtags, and usernames.

## Methodologies

### Prerequisites

1. ( Optional ) Clone the repository using `git clone https://github.com/vladkens/twscrape.git` 
2. Install required libraries by running `pip install twscrape`
3. Set up your Twitter Developer Account and obtain necessary API credentials
4. Configure the feeds by editing the `order-12345.txt` file

e.g.
```
elonmusk:a&VhaxK:onmusk@email.com:_:_:_
elonmusk2:hnK9&Ec:onmusk2@email.com:_:_:_
```


### Steps

### Auth and check
```sh
cd /$Userprofile/codes/github.com/vladkens/twscrape/
twscrape accounts
twscrape add_accounts ./order-12345.txt username:password:email:email_password:_:_

twscrape login_accounts
twscrape relogin user1 user2
# twscrape relogin user1 user2 --manual
twscrape relogin_failed --manual # retry login all failed logins at once
```
- メール プロバイダーが IMAP プロトコルをサポートしていない場合 (ProtonMail、Tutanota など)、または設定で IMAP が無効になっている場合は、メール確認コードを手動で入力できます。これを行うには、--manual フラグを付けてログインコマンドを実行します。

### Search
```sh
twscrape tweet_details 1586104694421659648 | jq
twscrape search 'killmilk'
twscrape search "elon musk since:2023-01-01 until:2023-05-31" --raw

twscrape search "QUERY" --limit=20
twscrape tweet_details TWEET_ID
twscrape tweet_replies TWEET_ID --limit=20
twscrape retweeters TWEET_ID --limit=20
twscrape favoriters TWEET_ID --limit=20
twscrape user_by_id USER_ID
twscrape user_by_login USERNAME
twscrape following USER_ID --limit=20
twscrape followers USER_ID --limit=20
twscrape verified_followers USER_ID --limit=20
twscrape subscriptions USER_ID --limit=20
twscrape user_tweets USER_ID --limit=20
twscrape user_tweets_and_replies USER_ID --limit=20
twscrape liked_tweets USER_ID --limit=20
```

### Using database
```sh
twscrape --db test-accounts.db <command>
```

### Using proxy
```sh
TWS_PROXY=socks5://user:pass@127.0.0.1:1080 twscrape user_by_login elonmusk
```

### For more details
```sh
❯ twscrape
usage: twscrape [--db DB] [--debug] <command> [...]

commands:
    version                   Show version
    accounts                  List all accounts
    stats                     Get current usage stats
    add_accounts              Add accounts
    del_accounts              Delete accounts
    login_accounts            Login accounts
    relogin                   Re-login selected accounts
    relogin_failed            Retry login for failed accounts
    reset_locks               Reset all locks
    delete_inactive           Delete inactive accounts

search commands:
    search                    Search for tweets
    tweet_details             Get tweet details
    tweet_replies             Get replies of a tweet
    retweeters                Get retweeters of a tweet
    favoriters                Get favoriters of a tweet
    user_by_id                Get user data by ID
    user_by_login             Get user data by username
    following                 Get user following
    followers                 Get user followers
    verified_followers        Get user verified followers
    subscriptions             Get user subscriptions
    user_tweets               Get user tweets
    user_tweets_and_replies   Get user tweets and replies
    user_media                Get user's media
    list_timeline             Get tweets from list
    liked_tweets              Get user's liked tweets

options:
  --db DB                     Accounts database file
  --debug                     Enable debug mode
  ```
  

## References

1. [GitHub - vladkens/twscrape](https://github.com/vladkens/twscrape)