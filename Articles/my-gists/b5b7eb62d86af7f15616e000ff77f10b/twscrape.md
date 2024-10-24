# Twitter scraping

- Auth and check
```sh
twscrape accounts
twscrape add_accounts ./order-12345.txt username:password:email:email_password:_:_

twscrape login_accounts
twscrape relogin user1 user2 --manual
twscrape relogin_failed --manual # retry login all failed logins at once
```
- メール プロバイダーが IMAP プロトコルをサポートしていない場合 (ProtonMail、Tutanota など)、または設定で IMAP が無効になっている場合は、メール確認コードを手動で入力できます。これを行うには、--manual フラグを付けてログイン コマンドを実行します。

- Search
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

- 
```sh
twscrape --db test-accounts.db <command>
```

- Proxy
```sh
TWS_PROXY=socks5://user:pass@127.0.0.1:1080 twscrape user_by_login elonmusk
```


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
  