# GitHub Wiki 使用上の注意

GitHub Wikiを使用する際に考慮すべきいくつかの重要な事項があります。以下にそれらをまとめました。

## 1.ブランチの選択 

GitHub Wikiの更新を行う際には、main ブランチではなく master ブランチに変更をプッシュしてください。

## 1. プライバシー設定 

GitHub Wikiを使用する場合、無料プランではリポジトリがパブリックである必要があります。これを有効にするには以下の手順があります。

`gh repo edit --visibility public`  
`gh repo edit --enable-issues --enable-wiki`


## 1. ファイルとディレクトリの命名規則

Wikiページやフォルダの命名には慎重さが必要です。特殊文字やスペースを避け、わかりやすく簡潔な名前を使用してください。

```markdown
# 推奨
- My_First_Page.md
- Images/
  - Logo.png

# 非推奨
- My First Page.md
- @Important-Page.md
```


```
# ディレクトリ構造の例
- Tutorials/
  - Getting_Started.md
  - Advanced_Topics.md
- Troubleshooting/
  - Common_Issues.md
  - FAQs.md
```

## 1. ページの整理
Wikiが成長するにつれ、適切なディレクトリ構造と階層を維持することが重要です。関連するページをグループ化し、利用者が容易に情報を見つけられるように工夫しましょう。

## 1. 編集権限の管理
Wikiへの編集権限は慎重に管理されるべきです。必要最小限のユーザーにのみ編集権限を与え、変更履歴を確認することでセキュリティを向上させましょう。

https://cli.github.com/manual/gh_repo_edit