# Cookie

## はじめに

Web開発者やセキュリティエンジニアにとって、Cookieは重要な概念です。その中でもSameSite属性は、クロスサイトリクエストフォージェリ（CSRF）やクロスサイトスクリプティング（XSS）などのセキュリティ攻撃からウェブアプリケーションを保護するための仕組みです。

### CSRF（Cross-Site Request Forgery）

CSRF攻撃とは、攻撃者が被害者に代わって不正なリクエストを送信し、認証されたユーザーの権限を悪用する手法である。

### HSTS（HTTP Strict Transport Security）

HSTSは、ウェブサイトがHTTPS経由でアクセスされることを強制するセキュリティポリシーである。これにより、中間者攻撃などのリスクを軽減できる。

## クッキーとは
クッキーはWebブラウザに保存される小さなデータであり、ウェブサイトとブラウザ間で情報を共有するために使用されます。

## クッキーの構造
クッキーは名前と値のペア、有効期限、ドメイン、パスなどの属性を持ちます。
データは単純なテキスト形式であり、セミコロンで区切られたキーと値の組み合わせです。
- 例：
```
session_id=abc123; user_name=john_doe; expires=2024-03-31T00:00:00Z
```

## Cookieの属性について

### Secure属性

Secure属性は、Cookieが安全な通信（HTTPS）でのみ送信されるようにします。これにより、中間者攻撃からの保護が強化されます。

### HttpOnly属性

HttpOnly属性は、JavaScriptからdocument.cookieを使用してこの属性が付加されたCookieを読み取ることや操作することを防ぎます。これにより、XSS（クロスサイトスクリプティング）攻撃からの保護が強化されます。

### Domain属性

Domain属性は、Cookieが送信される対象のドメインを指定します。具体的には、この属性で指定されたドメイン以下（サブドメインを含む）に対してのみCookieが送信されます。

### Path属性

Path属性は、Cookieが送信される対象のパスを指定します。具体的には、この属性で指定されたパス以下（サブディレクトリを含む）に対してのみCookieが送信されます。

## SameSite属性

SameSite属性は、Cookieをブラウザがどのように扱うかを定義するもので、主にクロスサイトリクエストに対する保護機能を提供します。SameSite属性には3つの値があります。

- **Strict**: `SameSite=Strict`を設定すると、同一サイト内でのみCookieが送信されます。他のサイトからのリクエストにはCookieが付与されません。

- **Lax**: `SameSite=Lax`は、一部のクロスサイトリクエストに対してCookieが送信されますが、例えば外部ドメインからのPOSTリクエストなど、一部のケースでは送信されません。

- **None**: `SameSite=None`は、同一サイト内外を問わず、すべてのリクエストにCookieが送信されます。ただし、Secure属性（HTTPS接続）が必要です。


次に、SameSite属性についての基本的な知識から実際の設定例までを解説します。

## SameSite属性未指定の挙動

未指定の場合、ブラウザはデフォルトでSameSite=Laxとして扱います。次のような暫定的対策を取ることが考えられます。

## Secure属性を使用
Secure属性を使用して、クッキーが安全な接続でのみ送信されるようにする。

## HttpOnly属性を使用
HttpOnly属性を使用して、JavaScriptからの不正なアクセスを制限する。

### SameSite: Strictでも攻撃が成功するケース

#### スキームだけ違うケース
同じドメインでもスキーム（HTTP/HTTPS）が異なる場合、SameSite: Strictでも攻撃が成功する可能性がある。

#### サブドメイン
サブドメインが異なる場合もSameSite: Strictでも攻撃が可能な場合がある。

## SameSite属性の使用例

### 設定方法

```html
Set-Cookie: myCookie=myValue; SameSite=Lax;
```

上記のように、Set-CookieヘッダーにSameSite属性を指定することで、Cookieの挙動を制御できます。

同一サイト内のみでのリクエストが必要な場合はSameSite: Strictを、
```html
Set-Cookie: myCookie=myValue; SameSite=Strict;
```

外部ドメインからも受け入れる場合はSameSite: Noneを検討する。必要に応じてSecure属性も追加する。
```html
Set-Cookie: myCookie=myValue; SameSite=None; Secure;
```

## SameSite属性の注意点

- ブラウザサポートの確認
  SameSite属性は、すべてのブラウザで完全にサポートされているわけではありません。開発者は使用するブラウザの対応状況を確認する必要があります。

- セキュリティ対策の一環
  SameSite属性はセキュリティ対策の一環として使用されるべきですが、単独では完璧なセキュリティを提供するものではありません。他のセキュリティベストプラクティスと併用することが重要です。
  
- SameSite=None; Secureを使用する場合、必ずHTTPSでサーバーが提供される必要があります。
