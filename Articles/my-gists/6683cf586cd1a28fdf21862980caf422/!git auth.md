# Gitの複数名 登録設定と認証

Gitを使用して複数のアカウントを管理するには、適切な設定と認証が必要です。以下は、2つの異なるアカウントを扱う場合のステップバイステップガイドです。

### 1. Gitの設定ファイルの編集

まず、各アカウントのGit設定ファイルを編集します。これにより、異なるアカウント情報を保存できます。

```bash
# 1つ目のアカウントの設定ファイルを編集
git config --global user.name "YourFirstUserName"
git config --global user.email "yourfirstemail@example.com"

# 2つ目のアカウントの設定ファイルを編集
git config --global --add user.name "YourSecondUserName"
git config --global --add user.email "yoursecondemail@example.com"

# 設定ファイルの確認
git config --global --list

# リポジトリごとの設定
git config user.name "YourLocalUserName"
git config user.email "yourlocalemail@example.com"

# 削除
git config --unset user.name
git config --unset user.email
```

各アカウントに対して、認証情報を提供する必要があります。これは通常、HTTPSまたはSSHを使用してリモートリポジトリにアクセスする際に行います。

HTTPS認証の場合：ユーザー名とパスワードまたはパーソナルアクセストークン（PAT）を使用します。

SSH認証の場合：SSHキーペアを生成し、公開鍵をGitHubなどのホスティングサービスに登録します。


### 注意点

2FA（2段階認証） 設定後は 1段階認証によるアクセスが制限されます。
```
git pull origin master
remote: The project you were looking for could not be found.
fatal: repository 'https://github.com/your_name/your_repo.git' not found
```

そのため、設定後にgit remote先URLを変更, または削除・再設定します。その際、PATが必要になります。
PATにはrepo, admin:org, user, (workflow; Actions workflowをPushする場合) 等のスコープ権限を与えておきましょう。 
```
set PAT 'your_personal_acceess_token'

git remote set-url origin https://oauth2:$PAT@github.com/your_name/your_repo.git

# or

git remote remove origin
git remote add origin https://oauth2:$PAT@github.com/your_name/your_repo.git
```

`.git/config`に以下の変更が加わります :

```diff
+ [remote "origin"]
+     url = https://oauth2:ACCESS_TOKEN@gitlab.com/yourself/yourproject.git
```

- https://stackoverflow.com/questions/25409700/using-gitlab-token-to-clone-without-authentication
- https://docs.github.com/ja/authentication/securing-your-account-with-two-factor-authentication-2fa/accessing-github-using-two-factor-authentication