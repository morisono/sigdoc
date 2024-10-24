---
lastmod: 2023-10-15
---

# X(Twitter) API v2 Advance Search Tips

## Queries [^1]

1. **( )** 個々の単語を他の演算子と組み合わせるために括弧を使用できます。
1. **ハッシュタグ (#)** 検索キーワードに # を付けることで、特定のハッシュタグが含まれるPostを検索。
1. **ユーザーメンション (@)** ユーザー名を含むPostを検索。
1. **フレーズ検索 (" ")** 完全一致する特定のフレーズを検索。
1. **"this is the * time this week"** ワイルドカードを含む完全なフレーズ。ワイルドカード * は引用フレーズ内で使用されるか、スペースなしで使用されない限り機能しません。
1. **+** 単語をそのまま含めることを強制します。スペル修正を防ぐのに役立ちます。
1. **-** 特定のキーワードを除外することを強制します。
1. **OR** 複数のキーワードをORで結ぶことで、いずれかのキーワードを含むPostを検索。
1. **AND** 複数のキーワードをANDで結ぶことで、すべてのキーワードを含むPostを検索。
1. **from**:**  特定のユーザーからのPostを検索。
1. **from:me** 自分が投稿したPostを検索。
1. **to**:**  特定のユーザー宛のPostを検索。
1. **to:me** 自分宛のPostを検索。
1. **list:** 特定のリストからのPostを検索。
1. **is:** 特定のPostの種類を指定。
1. **since** 特定の日付以降のPostを検索。
1. **until** 特定の日付以前のPostを検索。
1. **since_time** 特定のUnix日時以降のPostを検索。
1. **until_time** 特定のUnix日時以前のPostを検索。
1. **within_time** 特定のUnix時間範囲内のPostを検索。
1. **lang** 特定の言語で書かれたPostを検索。
1. **include:** 特定のキーワードを含むPostを検索。
1. **exclude:** 特定のキーワードを除外したPostを検索。
1. **exclude:replies** Replyを除外したPostを検索。
1. **exclude:hashtags** ハッシュタグを除外したPostを検索。
1. **geocode:** 特定の地理座標周辺でのPostを検索。
1. **within:** 特定の地理的範囲内でのPostを検索。
1. **:)** ポジティブなPostを検索。
1. **:(** ネガティブなPostを検索.
1. **card_name:animated_gif** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:promo_website** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:poll2choice_text_only** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:poll3choice_text_only** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:poll4choice_text_only** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:poll2choice_image** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:poll3choice_image** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_name:poll4choice_image** 特定のTwitterカード（コンテンツカード）を含むPostを検索。
1. **card_domain:pscp.tv** Twitterカード内のドメイン名に一致するPostを検索。通常、url: 演算子とほぼ同等。
1. **card_url:pscp.tv** カード内のドメイン名と一致するが、card_domain とは異なる結果を返す。
1. **card_name:audio** プレイヤーカードを含むPostを検索（音源、Spotify、Soundcloudなどへのリンク）。
1. **card_name:animated_gif** GIFを含むPostを検索。
1. **card_name:player** プレイヤーカードを含むPostを検索。
1. **card_name:app** アプリカードを含むPostを検索。
1. **card_name:promo_image_app** アプリカードへのリンクを含むPostを検索。promo_app は機能せず、promo_image_app は大きな画像を含むアプリリンク用です。通常、広告に使用されます。
1. **card_name:summary** 小さな画像のサマリーカードを含むPostを検索。
1. **card_name:summary_large_image** 大きな画像のカードを含むPostを検索。
1. **card_name:promo_image_convo** 会話広告カードを含むPostを検索。
1. **card_name:promo_video_convo** 会話広告カードを含むPostを検索。特定のユーザーに関連するモーメントカードを検索します。
1. **min_replies:** 指定したReply数以上のPostを検索。
1. **min_retweets** 指定したRepost数以上のPostを検索。
1. **min_faves** 指定したいいね数以上のPostを検索。
1. **near** 指定した地点の近くで投稿されたPostを検索。
1. **near:me** 自分の近くで投稿されたPostを検索。
1. **url:** 特定のURLを含むPostを検索。
1. **bio:** ユーザープロフィールのバイオ情報に特定のキーワードを含むアカウントを検索。
1. **source:** 特定のTwitterクライアントからのPostを検索。
1. **context:** 特定のトピックに関連するPostを検索。
1. **conversation_id** 特定の会話IDに関連するPostを検索。
1. **quoted_tweet_id** 特定の引用PostIDに関連するPostを検索。
1. **quoted_user_id** 特定の引用ユーザーIDに関連するPostを検索。
1. **is:news** ニュースアカウントによるPostを検索。
1. **is:verified** 認証済みアカウントによるPostを検索。
1. **filter:images** 画像を含むPostを検索。
1. **filter:twimg** Twitterがホストする画像を含むPostを検索。
1. **filter:videos** 動画を含むPostを検索。
1. **filter:media** メディアファイル（写真、動画、音声など）を含むPostを検索。
1. **filter:links** リンクを含むPostを検索。
1. **filter:replies** RePostを検索。
1. **filter:hashtags** ハッシュタグを含むPostを検索。
1. **filter:quote** 引用Repostを含むPostを検索。
1. **filter:nativeretweets** ネイティブRepost（公式のRepost）を含むPostを検索。
1. **filter:verified** 認証済みアカウントのPostを検索。
1. **filter:safe** 安全なコンテンツのみを検索。
1. **filter:follows** 特定のユーザーをフォローしているアカウントのPostを検索。
1. **filter:tweets** Postの種類を指定。
1. **filter:has** 特定の属性を持つPostを検索。
1. **filter:native_video** ネイティブビデオを含むPostを検索。
1. **filter:pro_video** プロモーション動画を含むPostを検索。
1. **filter:mentions** メンション（言及）を含むPostを検索。
1. **filter:news** ニュースPostを検索。
1. **filter:periscope** Periscopeのライブストリームを含むPostを検索。
1. **filter:vine** Vineの動画を含むPostを検索。
1. **filter:blue_verified** 青い認証バッジを持つアカウントのPostを検索。
1. **filter:social** ソーシャルメディア関連のPostを検索。
1. **filter:trusted** 信頼性の高い情報源からのPostを検索。
1. **filter:has_engagement** エンゲージメント（対話、Repostなど）を含むPostを検索。
1. **filter:spaces** スペースをを検索。

## Parameters

1. **q:** 検索キーワードを指定。例: q=keyword
1. **modules:** Postのコンテンツに対して適用されるモジュールを指定。
1. **count:** 1回のリクエストで返すPostの数を指定。最大制限は500。
1. **result_type:** 検索結果の種類を指定。"recent"（最新のPost）、"popular"（人気のPost）などがあります。
1. **until:** このPost以前のPostを取得。
1. **since_id:** このPostID以降のPostを取得。
1. **max_id:** このPostID以前のPostを取得。
1. **start_time:** 検索範囲の開始日時を指定。例: start_time=20231.011.01T00:00:00Z
1. **end_time:** 検索範囲の終了日時を指定。例: end_time=20231.121.31T23:59:59Z
1. **next_token:** 次のページのコンテンツを取得するためのトークン。ページングに使用。
1. **max_results:** 1回のリクエストで返す最大結果数を指定。最大制限は100。
1. **tweet.fields:** レスポンスに含めるPostのフィールド（例: tweet.fields=created_at,author_id）。
1. **user.fields:** レスポンスに含めるユーザー情報のフィールド（例: user.fields=username,description）。
1. **expansions:** Postの拡張情報を含めるためのパラメータ（例: expansions=author_id,referenced_tweets.id）。
`1. **until_id:** このPostID以前のPostを取得。
1. **media.fields:** メディア情報のフィールドを指定。メディアファイル情報を含むPostを取得する際に使用。
1. **place.fields:** 場所情報のフィールドを指定。特定の場所に関連するPostを取得する際に使用。
1. **poll.fields:** 投票（ポール）情報のフィールドを指定。投票付きPostを取得する際に使用。
1. **l:** Postの言語コードを指定。例: l=en (英語)。
1. **format:** レスポンスのフォーマットを指定。例: format=json (JSON形式)。
1. **entities:** エンティティ（ハッシュタグ、メンション、URLなど）情報を含めるかどうかを指定。

## 特別な言語コード

1. **lang:und** 未定義の言語を持つPostを検索。
1. **lang:qam** メンションのみを含むPostを検索（2022年6月14日以降のPostで有効）。
1. **lang:qct** キャッシュタグのみを含むPostを検索（2022年6月14日以降のPostで有効）。
1. **lang:qht** ハッシュタグのみを含むPostを検索（2022年6月14日以降のPostで有効）。
1. **lang:qme** メディアリンクを含むPostを検索（2022年6月14日以降のPostで有効）。
1. **lang:qst** 非常に短いテキストを含むPostを検索（2022年6月14日以降のPostで有効）。
1. **lang:zxx** メディアまたはTwitterカードのみを含む、追加のテキストのないPostを検索（2022年6月14日以降のPostで有効）。

### 制限事項

1. `card_name:` は最後の7-8日のデータにのみ対応しています。
1. 演算子の最大数は約22または23個程度です。
1. 時間に関連する演算子は他の演算子と併用する必要があります。

### 注意事項

1. Web、Mobile、Tweetdeck Searchは1つのシステムで実行されており、Standard API Searchは異なるインデックスで動作しています。Premium SearchおよびEnterprise SearchはGnip製品に基づいた別のシステムです。APIドキュメントはAPIとPremium用に既に存在していますが、それらについて別々のガイドを追加するかもしれません。
1. Twitterの検索演算子は大文字と小文字を区別しません。つまり、大文字と小文字の違いは無視されます。
1. 特定のユーザー名やハッシュタグは一意であるため、正確なスペルが重要です。
1. 一部の演算子は、Twitterの公式アプリやウェブサイトでのみ動作する場合があります。
1. 検索結果はリアルタイムで変化し、一部のPostが非表示にされることがあります。

### 参考

- https://github.com/igorbrigadir/twitter-advanced-search

[^1]: https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
[^2]: https://developer.twitter.com/en/docs/twitter-api/migrate/whats-new
[^3]: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2
[^4]: https://developer.twitter.com/en/docs/twitter-api/metrics