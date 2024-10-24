# Twitter scraping

- Auth and check
  ```sh
  twscrape accounts
  twscrape add_accounts ./order-12345.txt username:password:email:email_password:_:_
  ```
  - 不正防止システムにより、すべてのアカウントが認証を通過できるわけではありません。

- Login
  ```sh
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

- Connect to DB
  ```sh
  twscrape --db test-accounts.db <command>
  ```
  - トークンは SQLite データベースに保存され、後続のクエリで再利用されます。

- Proxy
  ```sh
  TWS_PROXY=socks5://user:pass@127.0.0.1:1080 twscrape user_by_login elonmusk
  ```

  - アカウントごとにプロキシを使用する場合は、環境変数でプロキシを上書きしたり、プロキシ パラメータを API に渡したりしないでください。

- Help
  ```sh
  コマンド:
  version                  バージョンを表示
  accounts                 すべてのアカウントをリストする
  stats                    現在の使用状況の統計を取得します
  add_accounts             アカウントを追加します
  del_accounts             アカウントの削除
  login_accounts           ログインアカウント
  relogin                  選択したアカウントを再ログインします
  relogin_failed           失敗したアカウントのログインを再試行します
  reset_locks              すべてのロックをリセットします
  delete_inactive          非アクティブなアカウントを削除します

  検索コマンド:
  search                   ツイートを検索
  tweet_details            ツイートの詳細を取得する
  tweet_replies            ツイートの返信を取得します
  retweeters               ツイートのリツイートユーザーを取得します
  favoriters               ツイートのお気に入りを取得します
  user_by_id               IDでユーザーデータを取得
  user_by_login            ユーザー名でユーザーデータを取得する
  following                ユーザーのフォローを取得する
  followers                ユーザーのフォロワーを取得する
  verified_followers       ユーザー認証済みのフォロワーを取得します
  subscriptions            ユーザーのサブスクリプションを取得する
  user_tweets              ユーザーのツイートを取得します
  user_tweets_and_replies  ユーザーのツイートと返信を取得します
  user_media               ユーザーのメディアを取得します
  list_timeline            リストからツイートを取得
  likes_tweets             ユーザーの「いいね！」をしたツイートを取得します

  オプション:
  --db DB                  アカウント  データベース  ファイル
  --debug                  デバッグモードを有効にする
  ```