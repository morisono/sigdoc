
# GitHub のサービスとトークン・環境変数に関する知識

## GitHub Services 

1. Actions (アクション)

    **説明**: GitHub Actionsは、コードリポジトリ内のワークフローを自動化するためのツールです。ワークフローは、コードのビルド、テスト、デプロイ、通知などのタスクを自動的に実行できます。これにより、開発プロセスを効率化し、品質を向上させることができます。

1. Codespaces (コードスペース)

    **説明**: GitHub Codespacesは、Webブラウザを使用してコードを編集、デバッグ、プレビューするためのクラウドベースの開発環境です。Codespacesを使用すると、開発者はローカル環境のセットアップにかかる時間を削減し、どこからでもコードにアクセスできます。

1. Dependabot (ディペンダボット)

    **説明**: GitHub Dependabotは、プロジェクトの依存関係を自動的に監視し、セキュリティアドバイザリやアップデートがある場合に通知およびプルリクエストを生成します。これにより、プロジェクトのセキュリティを向上させ、依存関係のアップデートを追跡しやすくなります。

 これらのGitHubの機能は、異なる側面でソフトウェア開発プロセスをサポートし、開発者とプロジェクト管理者に価値を提供しています。


## Token

以下は、異なるGitHubトークンの種類に関する**説明**とそれぞれの**用途**についての情報です。GitHubのセキュリティ要件やアクセス制御の違いによって、異なるトークンタイプが使用されます。


1. PAT (Personal Access Token - classic)

    **説明**: パーソナルアクセス トークン (Personal Access Token - PAT) は、GitHubアカウントに紐づけられたAPIトークンで、個人のアクセスおよび認証に使用されます。通常、開発者が自分のリポジトリに対するアクセス許可を制御し、リポジトリへの読み取り/書き込み、GitHub APIへのアクセス、GitHub Actionsなどの権限を与えるために使用されます。

    **用途**:  
    リポジトリへのアクセス権限管理
    GitHub APIへのアクセス


1. Fine-grained PAT (Fine-grained Personal Access Token)

    **説明**: Fine-grained PAT は、一般的なPATと同じく個人のアクセスおよび認証に使用されますが、アクセス権限を細かく制御できます。これにより、特定のリポジトリや機能に対するアクセスをより詳細に設定できます。

    **用途**:  
    特定のリポジトリへのアクセス権限管理
    特定のGitHub Actionsワークフローへのアクセス


1. OAuth Apps トークン (OAuth Apps Token)

    **説明**: OAuth Apps トークンは、サードパーティのアプリケーションがGitHubユーザーのアカウントへのアクセスを承認するために使用されます。ユーザーは、OAuthアプリケーションに対してアクセスを許可するために認証します。OAuth Appsを作成し、アクセストークンを取得するには、GitHubの設定から新しいOAuth Appsを登録する必要があります。

    **用途**:  
    サードパーティのアプリケーションがGitHubユーザーアカウントへのアクセスを認証
    特定のアプリケーションがGitHub APIを使用

1. GitHub Apps トークン (GitHub Apps Token)

    **説明**: GitHub Apps トークンは、GitHub Appsによって生成され、インストールされたGitHubリポジトリに対するアクセスを許可します。GitHub Appsは、GitHubの統合アプリケーションを表し、ユーザーまたは組織全体に対してアクセスを提供できます。

    **用途**:  
    GitHub Appsが特定のGitHubリポジトリに対してアクセス
    GitHub AppsがGitHub APIを使用

    GitHub AppsがGitHub Actionsなどのアクションを実行
    GitHub Appsトークンを取得するには、GitHub Appsの新規作成 ページでアプリケーションを登録する必要があります。


## Environments and Secrets

1. Environment secrets (環境シークレット)

    **説明**: 環境シークレットは、GitHub Actionsのジョブやワークフローで使用される環境変数のセキュリティ設定です。これらのシークレットは、GitHubアカウント内の特定のリポジトリに対して設定され、そのリポジトリのワークフロー内でのみアクセスできます。ジョブ内のスクリプトやアクションからこれらのシークレットを参照できます。

    **用途**:  
    ジョブやワークフロー内の環境変数のセキュリティ設定
    APIキー、アクセストークン、パスワードなどの秘密情報の保護

1. Repository secrets (リポジトリシークレット)

    **説明**: リポジトリシークレットは、特定のGitHubリポジトリに関連付けられたシークレットです。これらのシークレットは、リポジトリ内のワークフローで使用され、リポジトリのコードと関連する秘密情報を保護します。リポジトリ内のすべてのワークフローからアクセス可能です。

    **用途**:  
    特定のリポジトリのワークフローでのシークレットの保護
    リポジトリ固有の秘密情報の設定

1. Organization variable (組織変数)

    **説明**: 組織変数は、GitHubの組織レベルで設定される変数で、その組織内のすべてのリポジトリとワークフローで共有されます。組織の所有者や管理者が設定し、その組織のすべてのプロジェクトで使用できます。リポジトリ内で上書きできる場合もあります。

    **用途**:  
    組織全体の共通設定やリソースへのアクセス情報の共有
    組織内のさまざまなプロジェクトでの一貫性のある設定

これらの要素は、GitHub Actionsワークフローのセキュリティと設定管理に役立ちます。適切な場所にシークレットや変数を設定することで、セキュリティと管理の効率性を向上させることができます。


## GitHub Actionsでのトークンの利用方法

GitHub WEBからSettings→ Actions → General → Workflow permissions: GitHubのリポジトリ設定からアクセストークンを設定および管理できます。これはリポジトリ全体の設定として使用されます。

CLI: GitHub CLI (gh) を使用して、GitHub Actionsにアクセスできます。以下は一般的なCLIコマンドの例です。

`gh workflow run WORKFLOW_NAME`


GitHub コンテキスト: GitHub Actionsのワークフロー内で、GitHubコンテキストを使用してアクセストークンを取得できます。以下はワークフロー内のPush ステップの一部としてアクセストークンを使用する例です。

```
job:
  push:
    step:
      - name: Commit and push
        run: |
          touch newfile.txt
          git config --local user.email "${{ github.actor }}@gmail.com"
          git config --local user.name "${{ github.actor }}"
          git add .
          git commit -m "Auto commit by $AUTHORS"
          git push -u origin main 
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} 
```


## Caution

GitHub Apps Token仕様上の懸念点は以下の通りです。

1. Webhookは不要なので、「Active」のチェックを外しましょう。: GitHub AppsはWebhookを使用しないため、「Active」のチェックを外して無効にします。

1. Repository permissions > Contents > Read and write: GitHub Appsがリポジトリのコンテンツにアクセスできるように、リポジトリ権限でContentsのReadおよびWriteアクセスを付与します。

1. Generate a private key: GitHub Appsのためにプライベートキーを生成し、セキュアに保管します。

1. <App名>.<作成日>.private-key: プライベートキーを適切な名前で保存します。

1. Settings > Install App: GitHub Appsをリポジトリにインストールします。

1. Secretsへ登録 (Settings → Secrets and variables → Actions → New repository secret): GitHub Appsトークンをリポジトリのシークレットとして登録し、安全に保管します。

1. サードパーティアクションでGitHub Appsトークンを生成すべきではない: セキュリティ上の理由から、サードパーティのアクションでGitHub Appsトークンを生成すべきではありません。

1. シークレットの値は GitHub に安全に保存されているが、リポジトリに push できる人なら誰でもシークレットを見れる: GitHubのシークレットは暗号化されていますが、リポジトリにpushアクセスがある人なら誰でもシークレットの値を見ることができますので、注意が必要です。

1. 永続的な API キー (e.g. AWS credential) などを保存している場合、退職者が出たらシークレットのローテーションが必須である: シークレットには機密情報が含まれる場合があるため、セキュリティを維持するためには定期的なローテーションが必要です。

1. クラウドプロバイダーが OpenID Connect に対応している場合は積極的に使う: OpenID Connectをサポートするクラウドプロバイダーを使用することで、セキュリティを向上させることができます。

1. 全リポジトリで共通して使うシークレットは Organization レベルで設定してローテーションしやすくする: 全てのリポジトリで共通して使用されるシークレットは、Organizationレベルで設定し、ローテーションを容易にすることが推奨されます。


[^0]: https://github.com/settings/apps/new [^0]