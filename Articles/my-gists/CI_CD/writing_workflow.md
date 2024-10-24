# 定期実行ワークフローの作成

## 名前
```
name: Create files, Push to repo
```

## イベントトリガー

```
on:
  schedule:
    - cron: '*/5 * * * *'
  workflow_dispatch:
```

## 権限

GitHubの場合、Workflowファイル内で設定したアクションに対するPermissionsと、リポジトリの設定で行ったPermissionsの優先順位は異なります。

Workflowファイル内でのPermissions（例えば、.github/workflows ディレクトリ内のYAMLファイル内で指定したもの）
リポジトリの設定でのPermissions（リポジトリの設定ページで行ったもの）
上記の優先順位に従います。つまり、Workflowファイル内で指定されたPermissionsが最優先され、その後にリポジトリの設定でのPermissionsが適用されます。

セキュリティ的な観点からは、通常、より厳格なPermissionsを持つ方が安全です。リポジトリ全体でPermissionsを制御する場合、それに従うためにWorkflowファイル内でPermissionsを指定する必要はありません。リポジトリ設定で適切なPermissionsを設定し、Workflowファイル内でのPermissions設定は最小限に留めることがセキュリティを向上させます。


```
permissions:
  contents: write
```

## 並列処理

```
concurrency:
  cancel-in-progress: false
```

## 既定の設定値

```
defaults:
  run:
    shell: bash
```

## ジョブ
checkout ステップは、GitHubリポジトリを現在の実行環境にチェックアウト（クローン）するために使用されています。 具体的には、actions/checkout@v4アクションを使用して、GitHubリポジトリのコードやファイルを実行環境に取得します。
- リポジトリの指定ブランチまたはコミットからコードをチェックアウトする。 
- チェックアウトしたコードをワークフローのジョブ内で使用できるようにする。 
- チェックアウトされたコードを更新し、変更を検出した場合にジョブをトリガーする（これは主にPushイベントに関連しています）。 

このステップは、ワークフロー内でコードを取得して実行するために非常に一般的であり、GitHub Actionsの多くのワークフローで使用されます。ワークフローのコードがリポジトリの最新バージョンを使用していることを確保し、ジョブの実行環境が必要なコードやファイルを持っていることが重要です。
```diff
jobs:
  generate_post:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
+      - name: Checkout repository
+        uses: actions/checkout@v4
        with:
          token: ${{ secrets.PAT }}
          persist-credentials: false
          fetch-depth: 0

      - name: Commit files
        run: |
          touch test.txt
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add -A
          git commit -a -m "Add changes"

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
```
[^1]: https://docs.github.com/ja/actions/using-workflows/events-that-trigger-workflows [^1]
[^2]: https://docs.github.com/actions/using-jobs/assigning-permissions-to-jobs [^2]
[^3]: https://docs.github.com/ja/actions/using-jobs/using-concurrency [^3]
[^4]: https://docs.github.com/ja/actions/using-jobs/setting-default-values-for-jobs [^4]
[^5]: https://docs.github.com/ja/actions/using-jobs/using-jobs-in-a-workflow [^5]