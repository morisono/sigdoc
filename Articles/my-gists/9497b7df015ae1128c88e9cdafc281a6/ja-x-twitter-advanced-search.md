# Twitter 高度な検索テクニック

このガイドでは、Twitterの高度な検索機能を活用するためのテクニックとベストプラクティスを紹介します。公式の[Twitter Advanced Search](https://twitter.com/search-advanced)ページも参考にしてください。

### 基本検索構文

- **from:** 特定ユーザーからのツイートを検索  
```
from:@PayPayOfficial キャンペーン
```
（PayPay公式アカウントが投稿した「キャンペーン」を含むツイート）

- **to:** 特定ユーザー宛てのツイートを検索  
```
to:@LINE_JP 問い合わせ
```
（LINE公式アカウント宛ての「問い合わせ」を含むツイート）

- **@username:** 特定ユーザーへのメンションを含むツイートを検索  
```
@PayPayOfficial 不具合
```
（PayPay公式アカウントがメンションされた「不具合」に関するツイート）

- **"phrase"**: 完全一致フレーズ検索  
```
"PayPay キャッシュバック"
```
（「PayPay キャッシュバック」という完全一致フレーズを含むツイート）

- **-word**: 特定単語を除外  
```
PayPay -キャンペーン
```
（「PayPay」を含むが「キャンペーン」を含まないツイート）

### 高度なフィルター

1. **filter:verified:** 認証済み（ブルーバッジ）アカウントのツイートのみ表示  
```
PayPay filter:verified
```
（認証済みアカウントによるPayPay関連ツイート）

1. **filter:links:** URLリンクを含むツイートのみ表示  
```
PayPay キャンペーン filter:links
```
（PayPayキャンペーンに関するURLリンク付きツイート）

1. **filter:replies:** リプライ（返信）のみ表示  
```
to:@PayPayOfficial filter:replies
```
（PayPay公式アカウントへの返信ツイート）

1. **filter:media:** メディア（画像/動画）を含むツイートのみ表示  
```
PayPay 不具合 filter:media
```
（PayPay不具合に関するメディア付きツイート）

1. **filter:nativeretweets:** 公式リツイートのみ表示  
```
PayPay filter:nativeretweets
```
（PayPay関連の公式リツイートのみ）

### 日付範囲指定

1. **since:** 指定日付以降のツイートを検索  
```
PayPay since:2024-12-01
```
（2024年12月1日以降のPayPay関連ツイート）

1. **until:** 指定日付以前のツイートを検索  
```
PayPay until:2024-12-31
```
（2024年12月31日以前のPayPay関連ツイート）

1. **組み合わせ例:**  
```
PayPay キャンペーン since:2024-12-01 until:2024-12-31
```
（2024年12月のPayPayキャンペーン関連ツイート）

### 位置情報検索

1. **near:** 指定場所付近からのツイートを検索  
```
PayPay near:"東京"
```
（東京付近からのPayPay関連ツイート）

1. **within:** 指定範囲内のツイートを検索  
```
PayPay near:"大阪" within:50km
```
（大阪から50km圏内のPayPay関連ツイート）

※注意：位置情報付きツイートは全体の約1%程度

### 感情分析フィルター

1. **happy:** ポジティブな感情表現を含むツイート  
```
PayPay happy
```
（PayPayに関するポジティブな感情表現を含むツイート）

1. **sad:** ネガティブな感情表現を含むツイート  
```
PayPay sad
```
（PayPayに関するネガティブな感情表現を含むツイート）

1. **anger:** 怒りの感情表現を含むツイート  
```
PayPay anger
```
（PayPayに関する怒りの感情表現を含むツイート）

1. **surprise:** 驚きの感情表現を含むツイート  
```
PayPay surprise
```
（PayPayに関する驚きの感情表現を含むツイート）

※注意：感情分析の精度は完全ではないため、結果は参考程度

### インタラクション検索

1. **min_retweets:** 指定リツイート数以上のツイート  
```
PayPay min_retweets:100
```
（100回以上リツイートされたPayPay関連ツイート）

1. **min_faves:** 指定いいね数以上のツイート  
```
PayPay min_faves:500
```
（500回以上いいねされたPayPay関連ツイート）

   - 感情分析やトピック分類は完全ではない

1. 検索制限：
   - 1時間あたりの検索回数に制限あり
   - 連続検索すると一時的に制限される場合あり

1. プライバシー関連：
   - 非公開アカウントのツイートは検索不可
   - 削除済みツイートは表示されない
