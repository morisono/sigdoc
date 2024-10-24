# casecobra

### プロジェクトのインストール

- https://github.com/joschan21/casecobra

次に示す手順に従って、`.env`ファイルに必要な環境変数を設定し、プロジェクトを正しく構成しましょう。

### 1. 環境変数の設定

`.env`ファイルをプロジェクトのルートディレクトリに作成し、以下の環境変数を設定します。

```env
KINDE_CLIENT_ID=your_kinde_client_id
KINDE_CLIENT_SECRET=your_kinde_client_secret
KINDE_ISSUER_URL=http://localhost:3000
KINDE_SITE_URL=http://localhost:3000
KINDE_POST_LOGOUT_REDIRECT_URL=http://localhost:3000
KINDE_POST_LOGIN_REDIRECT_URL=http://localhost:3000/auth-callback

ADMIN_EMAIL=your_admin_email

NEXT_PUBLIC_SERVER_URL=http://localhost:3000

STRIPE_SECRET_KEY=your_stripe_secret_key

UPLOADTHING_SECRET_KEY=your_uploadthing_secret_key
UPLOADTHING_APP_ID=your_uploadthing_app_id

DATABASE_URL=postgresql://casecobra_owner:your_password@aa.aws.neon.tech/casecobra?sslmode=require

STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
RESEND_API_KEY=your_resend_api_key
```

### 2. 環境変数の取得

各変数については以下の手順で取得してください。

- **KINDE_CLIENT_ID** と **KINDE_CLIENT_SECRET**:
  [Kinde](https://kinde.com/)のアカウントを作成し、アプリケーションの設定からクライアントIDとクライアントシークレットを取得します。

- **KINDE_ISSUER_URL**
   - 開発環境では、`http://localhost:3000`を使用します。これはKindeの認証エンドポイントです。

- **KINDE_SITE_URL**
   - あなたのウェブサイトのURLを指定します。開発環境では、`http://localhost:3000`を使用します。

- **KINDE_POST_LOGOUT_REDIRECT_URL** と **KINDE_POST_LOGIN_REDIRECT_URL**
   - 認証後やログアウト後にリダイレクトするURLです。通常はあなたのサイトの特定のページに設定します。開発環境では、`http://localhost:3000`を使用します。

- **STRIPE_SECRET_KEY** と **STRIPE_WEBHOOK_SECRET**:
  Stripeはオンライン決済のサービスです。[Stripe](https://stripe.com/jp)のダッシュボードからAPIキーとWebhookシークレットを取得します。
   - Stripeアカウントにログインします。
   - ダッシュボードの「APIキー」セクションからシークレットキーを取得します。
   - StripeのWebhooks設定で、エンドポイントを設定します。
   - エンドポイント設定後、Webhook Secretが表示されます。

- **UPLOADTHING_SECRET_KEY** と **UPLOADTHING_APP_ID**:
  UploadThingは、ファイルアップロードサービスです。[Uploadthing](https://uploadthing.com/)のアカウントからこれらの情報を取得します。

- **DATABASE_URL**:
  データベースの接続情報を入力します。ここではPostgreSQLの接続文字列を使用していますが、適宜自分のデータベースに合わせてください。
  データベース接続のためのURLです。以下のフォーマットで指定します：
   ```
   postgresql://<username>:<password>@<host>:<port>/<database>?sslmode=require
   ```
   - `username`：データベースのユーザー名
   - `password`：データベースのパスワード
   - `host`：データベースのホスト名（例：`aa.aws.neon.tech`）
   - `port`：データベースのポート（デフォルトは5432）
   - `database`：データベース名
   - `sslmode`：SSLモード（`require`を推奨）

- **ADMIN_EMAIL**
これは管理者のメールアドレスです。管理者として使用するメールアドレスを直接指定します。

- **RESEND_API_KEY**:
  Resendは、メール送信サービスです。[Resend](https://resend.com/)サービスのAPIキーを取得します。

- **NEXT_PUBLIC_SERVER_URL**
   - クライアントサイドに公開するサーバーのURLを指定します。開発環境では、`http://localhost:3000`を使用します。

### 3. プロジェクトのセットアップ

必要な環境変数を設定した後、プロジェクトの依存関係を再インストールし、ビルドおよびサーバーの起動を行います。

```bash
# 依存関係のインストール
yarn install

# ビルド
yarn build

# サーバーの起動
yarn start
```

### 4. サーバーの起動確認

サーバーが正常に起動したら、ブラウザで `http://localhost:3000` にアクセスしてアプリケーションが正しく表示されるか確認します。

### 5. コードの確認

Resend API キーの設定が正しく行われていることを確認してください。以下は、Resend API キーを設定するサンプルコードです。

```javascript
// 例: resend.js
const Resend = require('resend');

const resend = new Resend(process.env.RESEND_API_KEY);

module.exports = resend;
```

### 6. デバッグ用のログ出力

サーバーサイドでエラーログを出力して、問題の詳細を把握するのに役立つ情報を得ます。例:

```javascript
// 例: server.js
const express = require('express');
const app = express();
const resend = require('./resend'); // 例: Resend モジュールのインポート

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});
```