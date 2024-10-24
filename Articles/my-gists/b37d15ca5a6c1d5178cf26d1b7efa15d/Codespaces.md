# GitHub Codespacesの利用に関する知識


## 認証

初期状態では`GITHUB＿TOKEN`がいるが、必要な権限が無いため `gh repo create` などができない。

```
The value of the GITHUB_TOKEN environment variable is being used for authentication.
To have GitHub CLI store credentials instead, first clear the value from the environment.

```

その為、PATを使って再設定する。PAT(Classic)の場合、repo, workflow, admin:org のscope を与える。

```
# Clear default auth
unset GITHUB_TOKEN

# Start auth process and paste PAT
gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'workflow'.
? Paste your authentication token: ****************************************
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as your_name
```

1. テンプレートリポジトリとして設定する

Settings > Template repository 

テンプレートリポジトリとは、既存のリポジトリをテンプレート化して、あなたや他の人が、同じディレクトリ構造、ブランチ、ファイルを持つ新しいリポジトリ作成できるようにすることができる機能です。


https://github.com/features/codespaces

https://docs.github.com/codespaces/overview

https://code.visualstudio.com/docs/remote/codespaces

https://docs.github.com/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository

https://docs.github.com/codespaces/developing-in-codespaces/creating-a-codespace-from-a-template