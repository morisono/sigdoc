ウェブサイトがVPN、AdGuard、NoScript（Chrome Extension）などの閲覧制限を行うためには、いくつかの技術やサービスが使用されることが多いです。以下に、それぞれのケースについて網羅的かつ専門技術的に説明します。

### 1. VPNの制限

#### 方法
- **IPアドレスのブロック**：特定のVPNサービスのIPアドレス範囲をブロックします。VPNサービスは多くの場合、特定のIPレンジを使用しているため、これをブロックすることでVPN経由のアクセスを制限できます。
- **Geo-blocking**：IPアドレスの地理的位置を基に制限をかける方法です。VPNユーザーはしばしば地理的に異なる場所からアクセスするため、通常のアクセスパターンと異なる地域からのアクセスをブロックします。

#### 使用するツールやサービス
- **Cloudflare**：IPアドレスや地理的位置に基づくアクセス制限を設定可能。
- **MaxMind GeoIP**：IPアドレスの地理的情報を提供するデータベース。これを使用してGeo-blockingを実装できます。

### 2. AdGuardの制限

#### 方法
- **広告ブロッカーの検出**：JavaScriptを使用して、広告ブロッカーの動作を検出し、コンテンツの表示を制限する方法です。AdGuardのような広告ブロッカーが有効な場合に警告を表示したり、サイトの一部または全部のアクセスを制限します。

#### 使用するツールやサービス
- **AdBlock Detection Scripts**：AdBlockやAdGuardのような広告ブロッカーを検出するスクリプト。たとえば、AdBlock Detectorなどがあります。
- **Custom JavaScript**：独自に開発したスクリプトで広告ブロッカーの存在を確認し、適切な対応を取ります。

### 3. NoScriptの制限

#### 方法
- **JavaScript依存のコンテンツ**：サイトの重要な部分をJavaScriptで構築し、NoScriptが有効の場合に正常に表示されないようにします。
- **JavaScriptの無効化検出**：NoScriptのようなJavaScriptを無効にする拡張機能が動作しているかどうかを検出し、通知を表示する方法です。

#### 使用するツールやサービス
- **Modernizr**：ブラウザ機能の検出を行うライブラリ。JavaScriptの有効/無効を確認するために使用できます。
- **Custom JavaScript**：JavaScriptが有効でない場合に警告メッセージを表示するスクリプトを独自に実装します。

### WordPressでの実装

#### プラグイン
- **Wordfence Security**：WordPress用のセキュリティプラグイン。IPアドレスのブロックや国別の制限が可能です。
- **Ad Blocking Detector**：広告ブロッカーを検出するためのWordPressプラグイン。
- **Simple Geo Block**：国別のアクセス制限を行うWordPressプラグイン。

#### カスタムコード
- **functions.php**：テーマの`functions.php`ファイルにカスタムコードを追加して、広告ブロッカーやJavaScript無効化の検出機能を実装することもできます。

### 参考URL
1. [Cloudflare IP Blocking](https://support.cloudflare.com/hc/en-us/articles/200172676)
2. [MaxMind GeoIP](https://www.maxmind.com/en/geoip2-services-and-databases)
3. [AdBlock Detection Scripts](https://github.com/sitexw/BlockAdBlock)
4. [Modernizr](https://modernizr.com/)
5. [Wordfence Security](https://www.wordfence.com/)
6. [Ad Blocking Detector](https://wordpress.org/plugins/ad-blocking-detector/)
7. [Simple Geo Block](https://wordpress.org/plugins/simple-geo-block/)

これらのツールや方法を組み合わせることで、ウェブサイトはVPN、広告ブロッカー、NoScriptなどの使用を検出し、適切な閲覧制限をかけることができます。