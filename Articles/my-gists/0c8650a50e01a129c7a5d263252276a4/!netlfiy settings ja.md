# Netlify 設定

## サイトの設定

1. Netlify ダッシュボードにアクセスします。

1. 設定したいサイトを選択します。

## ドメイン設定

1. **支払い方法を追加**
   サイトに支払い方法を追加するには、Netlify ダッシュボードの「請求と使用状況」セクションに移動し、支払い情報を追加するための指示に従います。

1. **カスタムドメインを登録**
   サイトのカスタムドメインを登録するには、Netlify ダッシュボードの「ドメイン設定」セクションに移動し、"カスタムドメインを追加" ボタンをクリックします。指示に従ってカスタムドメインを登録および設定します。

1. **DNS 検証**
   カスタムドメインのDNS検証を行うには、「ドメイン設定」セクションで追加したカスタムドメインを選択し、提供された指示に従ってDNS検証プロセスを完了します。

## フォーム設定

1. **フォームの作成**: 必要なフォーム要素を設計し、ウェブページに組み込みます。

1. **テストとデバッグ**: フォームをテストし、エラーがあれば特定して修正します。

1. **有効化**: Netlify サイト管理画面から、有効化します。`Forms> Enable form detection`。

既にデプロイ済の場合、フォーム検出を有効にした後、変更を反映させるためにサイトを再デプロイする必要があることに注意してください。

## デプロイ

1. Netlify ダッシュボードで「デプロイ」セクションに移動します。

1. 希望するデプロイメント方法を設定します。これには、Git リポジトリに接続するか、手動でドラッグ＆ドロップデプロイメントなど、お好みのデプロイメント方法を選択します。

1. `netlify.toml`ファイルを用意すると、各種設定値をあらかじめ設定できるため、非常に便利です。

## 認証

## Netlify CMS


## `netlify.toml`

サイトのビルドとデプロイの設定は `netlify.toml` ファイルで行います。以下は `netlify.toml` ファイルの例です：

```toml
[build]
  publish = "public"
  command = "hugo --gc --minify  --source exampleSite --themesDir ../../ -t repo --cleanDestinationDir --baseURL $HUGO_BASE_URL"

[context.production.environment]
  HUGO_VERSION = "0.118.2"
  HUGO_ENV = "production"
  HUGO_ENABLEGITINFO = "true"
  HUGO_BASE_URL = "https://awesome-identity.netlify.com"

[context.deploy-preview]
command = "hugo --gc --minify --buildFuture --source exampleSite --themesDir ../../ -t repo --baseURL $DEPLOY_PRIME_URL"

[context.deploy-preview.environment]
  HUGO_VERSION = "0.118.2"

[context.branch-deploy]
command = "hugo --gc --minify --source exampleSite --themesDir ../../ -t repo --baseURL $DEPLOY_PRIME_URL"

[context.branch-deploy.environment]
HUGO_VERSION = "0.118.2"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 301
```

特定のプロジェクトと Hugo 設定に一致するように netlify.toml ファイルをカスタマイズしてください。 この構成ファイルは、Netlify がサイトを構築および展開する方法を制御します。

[^1]: https://docs.netlify.com/configure-builds/overview/　[^1]
[^2]: https://docs.netlify.com/configure-builds/file-based-configuration/　[^2]
[^3]: https://docs.netlify.com/site-deploys/create-deploys/　[^3]
[^4]: https://docs.netlify.com/forms/setup/ [^4]
[^5]: https://www.netlify.com/integrations/very-good-security/ [^5]
[^6]: https://docs.netlify.com/visitor-access/identity/ [^6]

https://v1.netlifycms.org/