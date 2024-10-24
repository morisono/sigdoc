# Hugoウェブサイトの構築とGitHub Actionsの設定手順

Hugoは、静的なウェブサイトジェネレーター(SSG)の一つです。このツールを使用すると、MarkdownやHTMLなどのテキストファイルから高速で効率的なウェブサイトを生成することができます。HugoはGo言語で開発されており、シンプルな構造と高速なビルドプロセスが特徴です。テーマのカスタマイズやコンテンツの管理が容易であり、ウェブ開発者やブロガーに広く利用されています。

GitHub Actionsは、GitHub, Inc.が提供する継続的インテグレーション（CI）および継続的デリバリー（CD）のプラットフォームです。GitHubのリポジトリ内で自動化されたワークフローを設定し、ソフトウェアのビルド、テスト、デプロイなどのタスクを自動化することができます。GitHub Actionsはコード変更に対するリアルタイムの反応を提供し、ソフトウェアプロジェクトの品質向上と効率化に役立ちます。


## Create scripts and wordflows

1. (任意) 記事作成するPythonスクリプトと、 ビルド・デプロイするGitHub Actions ワークフロー作成します。これらはワークフローにより自動的に予約実行・定期実行されます。
   ```
   code run.py
   pipreqs . --force --savepath=requirements.txt
   ```

## Deploy Hugo Website

1. **Hugoウェブサイトの作成**
   - Hugoをインストールします。
   - 新しいHugoプロジェクトを作成します。
    
    ```
    hugo new site example_hugo_website
    cd example_hugo_website
    ```

1. **GitHub Actionsワークフローの作成**
   - `.github/workflows` ディレクトリ内にGitHub Actionsワークフローの設定ファイルを作成します。
   - ワークフローでHugoのビルドと自動投稿の手順を設定します。
   
    ```
    cp ../.github .
    cp ../run.py .
    cp ../requirements.txt .
    ```

1. **Gitの管理を開始**
   - Hugoプロジェクトのディレクトリで、バージョン管理を開始します。

    ```
    git init 
    ```
1. **GitHubリポジトリの作成**
   - GitHubで新しいリポジトリを作成します。このリポジトリにHugoプロジェクトをプッシュします。

    ```
    gh repo create exapmle_hugo_site --public --source=. --remote=origin
    ```

1. **コンテンツの作成**
   - Hugoウェブサイトのコンテンツを作成します。これには記事やページの作成が含まれます。
   - 初回ビルドを行います。(これにより生成される設定ファイル `hugo.toml`が以降の自動ビルドに必要となります。)

   ```
   hugo new content posts/00001_first-post.md
   hugo

   git add -A
   git commit -m 'first commit'
   ```

1. **デプロイ**
   - プッシュ直後にワークフローが条件に従って発動されます。
   - ワークフローによって、Github Pages などのサービスへデプロイされます。
   ```
   git push origin main
   ```

## Setting in GitHub
   
1. **GitHub Actionsの有効化**
   - GitHubリポジトリ内でActionsを有効化し、ワークフローが実行されるようにします。
   
1. **ワークフローのアクセス許可の変更**
   - ワークフローが必要なアクセス許可を持っていることを確認します。必要に応じてPATの取得やGITHUB_TOKENの権限を設定します。

1. **公開設定の変更**
   - リポジトリの公開設定を設定します。必要に応じてプライベートまたはパブリックに設定します。必要に応じてPagesを有効化します。


## Enable Actions

1. **CLIからワークフローを実行**
   - GitHub CLIを使用して、必要に応じてワークフローを手動で実行します。

   ```
   set workflow_name 'Run test'
   gh workflow run $workflow_name
   ```

これらの手順を実行することで、HugoウェブサイトのビルドとGitHub Actionsを使用した自動投稿の流れをセットアップできます。

[^1]: https://docs.github.com/actions [^1]
[^2]: https://docs.github.com/actions/learn-github-actions/understanding-github-actions [^2]
[^3]: https://docs.github.com/actions/learn-github-actions/contexts  [^3]
[^4]: https://docs.github.com/ja/actions/learn-github-actions/variables [^4]
[^5]: https://docs.github.com/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs [^5]
[^6]: https://docs.github.com/actions/security-guides/using-secrets-in-github-actions [^6]
[^7]: https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions  [^7]
[^8]: https://docs.github.com/actions/using-workflows/workflow-commands-for-github-actions  [^8]
[^9]: https://docs.github.com/actions/using-workflows/caching-dependencies-to-speed-up-workflows [^9]
[^10]: https://docs.github.com/actions/hosting-your-own-runners [^10]
[^11]: https://gohugo.io/hosting-and-deployment/hosting-on-github/ [^11]

