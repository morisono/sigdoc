# GitHub の認証に関する知識

SSH鍵（SSH keys）とGPG鍵（GPG keys）は、異なる目的で使用される鍵のタイプであり、デプロイキー（Deploy keys）とは異なる役割と使用方法を持ちます。

1. **SSH鍵（SSH keys）**:

目的: SSH鍵はセキュアなシェル接続やファイル転送に使用されます。主にシステムやリモートサーバーへのアクセス認証に使用されます。
動作: SSH鍵はパブリックキーとプライベートキーのペアで構成され、公開鍵はリモートサーバーやシステムに登録され、プライベート鍵はローカルマシンに保存されます。認証時に公開鍵とプライベート鍵が一致するかどうかが確認され、認証が許可されます。
使用例: リモートサーバーへのSSHアクセス、GitリポジトリへのSSH認証、セキュアなファイル転送など。

1. **GPG鍵（GPG keys）**:

目的: GPG鍵はデジタル署名と暗号化に使用されます。主にセキュアなメッセージやファイルの署名と暗号化に使用されます。
動作: GPG鍵はパブリックキーとプライベートキーのペアで構成され、公開鍵は他のユーザーに渡して、彼らがメッセージを暗号化したり、あなたのデジタル署名を検証したりできるようになります。プライベート鍵は安全に保管され、署名作成やメッセージの復号化に使用されます。
使用例: メールの暗号化とデジタル署名、ファイルの暗号化と署名、セキュアなコミュニケーションなど。

1. **デプロイキー（Deploy keys）**:

目的: デプロイキーはGitHubなどのリポジトリにアクセスし、コードを自動的にデプロイするために使用されます。外部サービスやCI/CDツールがリポジトリへのアクセス権を持つために利用されます。
動作: デプロイキーはリポジトリごとに作成され、通常は読み取り専用アクセス権限を持ちます。リポジトリに直接アクセスできるようになり、コードをクローンしてデプロイするために使用されます。
使用例: CI/CDツールやデプロイサービスがリポジトリにアクセスして、コードのビルド、テスト、デプロイを実行する際に使用されます。


SSH鍵はセキュアな接続とアクセス用、GPG鍵はデジタル署名と暗号化用、デプロイキーは外部サービスやCI/CDツールがリポジトリにアクセスするために使用されます。それぞれ異なる目的を持ち、異なるコンテキストで使用されます。


[^1]: https://docs.github.com/authentication/connecting-to-github-with-ssh/managing-deploy-keys [^1]
[^2]: https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site [^2]
[^3]: https://docs.github.com/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https [^8]
[^4]: https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository [^9]
[^5]: https://docs.github.com/ja/actions/security-guides/automatic-token-authentication[ ^5]
[^6]: https://docs.github.com/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key [^6]
