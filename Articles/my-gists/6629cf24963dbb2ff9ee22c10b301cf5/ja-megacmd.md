# MEGAcmdの使い方

## はじめに
MEGAcmdは、あなたのMEGAアカウントとデータを操作するためのコマンドラインツールです。これにより、MEGAサービスにコマンドを介してアクセスすることができます。MEGAcmdは、高度なユーザーが自分のMEGAアカウントとのやり取りを自動化するための柔軟な方法を提供します。

## 基本的なコマンド
以下に、MEGAcmdで使用できる基本的なコマンドをいくつか示します。

- `signup` email [password] [--name="Your Name"] ：MEGAアカウントを登録します。
- `confirm` link email [password] ： 「サインアップ」プロセスの後に提供されるリンクを使用してアカウントを確認します。


## 例
以下に、いくつかの基本的なコマンドの使用例を示します。 [mega-] prefix をつけることで、Scriptableに呼び出すことも可能です。

```bash
# Interactive MEGAcmd shell
mega-cmd # (or MEGAcmd on Windows).

# MEGAにログイン
MEGAcmd> login your-email@example.com

# ルートディレクトリの内容をリスト
MEGAcmd> ls /

# 新しいディレクトリを作成
MEGAcmd> mkdir /new-directory

# ファイルをアップロード
MEGAcmd> put local-file.txt /new-directory

# ファイルのダウンロード
MEGAcmd> get $url downloads

#  ログアウト
MEGAcmd> logout
```

- Advanced

```sh
# upload multi file with password expired after 24 hours.
for i in (mega-find /contents/books-for-hacking/cybersecurity2024-packt --pattern="*pdf")
          mega-export -a --expire $i
end

# Show uploaded 
mega-export

# create backup ("日本時間 0 時(15+9=24) 毎日", "最新 7 件")
mega-backup /config /config.bak --period="0 0 15 * * *" --num-backups=7
```

特定のコマンドの使用方法については、公式の[MEGAcmd User Guide](https://github.com/meganz/MEGAcmd/blob/master/UserGuide.md)を参照してください。また、MEGAcmdの日本語版のユーザーガイドが必要な場合は、適切な翻訳サービスを利用することをお勧めします。[^1^][1]