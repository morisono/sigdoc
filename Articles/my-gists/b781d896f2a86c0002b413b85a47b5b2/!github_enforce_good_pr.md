# GitHubでIssueやPRの整形を強制するための工夫, その他

この記事では、GitHubでIssueやPull Request（PR）の整形を強制するための方法とその他の関連トピックについて説明します。

## 構成

```
.github/                           # GitHubの設定ファイルを格納するディレクトリ
├── actions/                      # カスタムアクションを保存するためのディレクトリ
├── CODEOWNERS                    # リポジトリのコード所有者を指定するファイル
├── config.yml                    # リポジトリの設定
├── CONTRIBUTING.md               # 貢献ガイドライン
├── dependabot.yml                # 依存関係の自動更新設定
├── FUNDING.yml                   # プロジェクトのサポートに関する情報を設定するファイル
├── ISSUE_TEMPLATE/               # Issue テンプレートが格納されているディレクトリ
│   ├── BUG-REPORT.md             # バグ報告のためのテンプレート（Markdown ファイル）
│   ├── BUG-REPORT.yml            # バグ報告のためのテンプレートの設定ファイル (Issue Form)
│   ├── config.yml                # Issue テンプレートの設定ファイル
│   ├── FEATURE-REQUEST.md        # 新機能リクエストのためのテンプレート（Markdown ファイル）
│   ├── FEATURE-REQUEST.yml       # 新機能リクエストのためのテンプレートの設定ファイル (Issue Form)
│   └── IMPROVE-EXISTING-DOCS.yml  # 既存のドキュメンテーションの改善のためのテンプレートの設定ファイル
├── labeler.yml                   # ラベル付けの設定ファイル
├── PULL_REQUEST_TEMPLATE.md      # プルリクエストのテンプレート
├── semantic.yml                  # セマンティックバージョニングを設定するファイル
└── workflows/                    # GitHub Actions のワークフロー設定ファイルが格納されているディレクトリ
    ├── action-lint.yml           # アクションのLintを行うワークフローの設定ファイル
    ├── ai-pr-reviewer.yml        # AIによるプルリクエストレビューのワークフローの設定ファイル
    ├── assigned-pulls-todo.yml   # アサインされたプルリクエストのTODOを管理するワークフローの設定ファイル
    ├── auto-gh-releases.yml      # GitHubリリースの自動作成ワークフローの設定ファイル
    ├── codeql.yml                # CodeQL解析のワークフローの設定ファイル
    ├── opened-issues-triage.yml  # 開かれたイシューをトリアージするワークフローの設定ファイル
    ├── pr-labeler.yml            # プルリクエストにラベルを自動付与するワークフローの設定ファイル
    ├── remove-metadata.yml       # メタデータの削除ワークフローの設定ファイル
    ├── rename-pr-files.yml       # プルリクエストのファイル名を変更するワークフローの設定ファイル
    ├── secret-lint.yml           # シークレットのLintを行うワークフローの設定ファイル
    └── status-check.yml          # 統計情報のチェックワークフローの設定ファイル
```

- [GitHub Issue テンプレートの設定方法](https://docs.github.com/ja/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms)
- [GitHub フォームスキーマ](https://docs.github.com/ja/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)
- [CODEOWNERS ファイルについての詳細](https://docs.github.com/ja/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub スポンサー](https://docs.github.com/ja/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)

- [Dependabotを使う](https://docs.github.com/ja/code-security/dependabot/working-with-dependabot)

- [Application | Semantic Pull Requests](https://github.com/marketplace/semantic-pull-requests)

- [i18n](https://github.com/lokalise/i18n-ally/wiki/Machine-Translation)

- [AI Code Review](https://book.st-hakky.com/business/chatgpt-code-review/)


- [GitHub PR Labeler ワークフローの設定例](https://www.vantage-ai.com/blog/how-to-enforce-good-pull-requests-on-github)
- [GitHub 公式ドキュメンテーションの例](https://github.com/github/docs/tree/main/.github)
- [便利なコミットタイプの例](https://github.com/commitizen/conventional-commit-types/blob/v3.0.0/index.json)

- [GitHub Actions Security Guidelines | Merccari](https://engineering.mercari.com/blog/entry/20230609-github-actions-guideline/)
- [all-contributors](https://allcontributors.org/docs/en/bot/installation)
- [mergify](https://github.com/marketplace/mergify)
- [whitesource-bolt](https://github.com/marketplace/whitesource-bolt)
- [imgbot](https://github.com/marketplace/imgbot)