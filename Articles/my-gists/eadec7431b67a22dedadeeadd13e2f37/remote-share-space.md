# rcloneの使い方 - クラウドストレージ運用の強力なツール

rcloneはクラウドストレージサービスとローカルファイル間での効率的な操作を可能にするオープンソースのコマンドラインツールです。本記事ではrcloneの基本から応用までを解説します。

## rcloneのインストールと設定

### インストール

rcloneは主要なLinuxディストリビューション、macOS、Windowsで利用できます。ダウンロードページから対応するパッケージをインストールしてください。

https://rclone.org/downloads/

### 認証情報の設定

rcloneを使う前に、利用するクラウドストレージの認証情報を設定する必要があります。

```
rclone config
```

このコマンドを実行すると対話形式で設定を行えます。クラウドストレージの種類を選び、APIキーやアクセストークンなどの認証情報を入力します。

## 基本的な使い方

### ファイル・フォルダの同期・コピー

```
rclone sync source:path dest:path  # 双方向同期
rclone copy source:path dest:path  # 単方向コピー
rclone moveto source:path dest:path # 移動(コピー後に元を削除)
```

`source:path`と`dest:path`にはローカルのパスまたはリモート(`remote:bucket/path`)を指定します。

### ファイル・フォルダの削除

```
rclone deletefile remote:path/file  # 単一ファイルを削除
rclone deleteremote remote:path     # ディレクトリ以下を削除  
```

### 一覧表示

```
rclone ls remote:path        # ファイル・フォルダ一覧
rclone tree remote:path      # 階層構造を表示
rclone ncdu remote:path      # ディスク使用量を視覚化
```

### よく使うオプション 

- `--dry-run` : 実際の転送は行わずにリハーサルする
- `--update` : 新しいファイルのみ転送する
- `--verbose` : 詳細ログを出力する
- `--transfers=N` : 同時転送数を指定する

## 発展的な使い方

### マスストレージ管理

rcloneを使えば、クラウド上に容易に大量のストレージ領域を作成できます。

- マウント: `rclone mount remote:path /path/to/mount`
- 大量フォルダ作成: 

```bash
# 1-100のフォルダを作成(--dry-runですり抜け確認)
seq 1 100 | xargs -i rclone mkdir remote:lab-{} --dry-run

# リンク生成も可能
seq 1 100 | xargs -i rclone link remote:lab-{}
```

- 大量リポジトリ作成:

```bash 
# 1-100のGitHubリポジトリを作成
seq 1 100 | xargs -i gh repo create lab-{} --private --source=.
```

### ディレクトリの暗号化・パスワードロック

- パスワードハッシュ化: `rclone obscure password`
- 設定ファイル暗号化: `rclone config` で選択可能


### チェックサム・暗号化転送

- `rclone check` : ファイルの差分や転送の整合性をチェックします。チェックサムを利用してデータ損失を防ぎます。
- `rclone copyto` : ソースをそのままにしながら、暗号化された転送を行えます。

### 帯域制御と並列処理

- `--bwlimit` : アップロード/ダウンロードの帯域幅を制限できます。
- `--transfers` : 同時転送スレッド数を指定できます。複数CPUでの並列処理が可能です。

### バックアップと履歴管理

- `--backup-dir` : 上書き前のファイルを別ディレクトリに保存します。
- `--track-renames`: ファイル名変更を追跡し、同期時に名前変更を反映します。

### 高度なフィルタリング

- `--include` / `--exclude` : 転送対象からパターンでファイルを含める/除外できます。
- `--min-size` / `--max-size` : ファイルサイズ範囲を指定できます。
- `--min-age` / `--max-age` : ファイル更新日時範囲を指定できます。
- `--delete-excluded` : 除外ファイルを削除するかどうかを指定できます。

### ログ・通知設定

- `--log-file` : 特定のファイルにログを出力できます。
- `--log-level` : ログレベル(ERROR/NOTICE/INFO/DEBUG)を設定できます。
- `--use-json-log` : JSONフォーマットでログを出力します。
- `--email-from` / `--email-to` : 完了時にメール通知を送れます。

### クラウド間転送

Google DriveからDropboxへの直接転送など、クラウド同士の転送が可能です。

```
rclone copy gdrive:source dropbox:dest
```

### マウントとunionフォルダ

- `rclone mount` : リモートストレージをOSのファイルシステムとしてマウントできます。
- `rclone nbunker` : 複数のクラウドを1つのフォルダにunionマウントできます。

rcloneでは、フォルダにパスワードをかけて保護したり、シェアリンクを簡単に生成することができます。

### フォルダのパスワードロック

1. まずパスワードをハッシュ化する必要があります。

```
rclone obscure password
```

このコマンドを実行するとパスワードの入力を求められ、ハッシュ化された文字列が出力されます。

2. ハッシュ化したパスワードを`~/.config/rclone/rclone.conf`に設定します。

```
[encryptedremote]
type = crypt
remote = /path/to/remote
password = ハッシュ化されたパスワード
```

3. このリモートを使ってファイル転送などの操作を行うと、フォルダの内容が暗号化されてパスワード保護されます。

```
rclone copy /path/to/data encryptedremote:
```

### フォルダのシェアリンク取得

1. シェアリンクを生成したいフォルダのリモートパスを指定します。

```
rclone link remote:path/to/directory
```

2. リンクとQRコードが表示されるので、そのままコピーしてシェアできます。

```
Shareリンク: https://example.com/randomstring
QRコード:
xxxxx
xxxxx
```

3. オプションでパスワードを設定することも可能です。

```
rclone link remote:path/to/directory --set-password=true
```

4. 一括でシェアリンクを生成するスクリプトも作れます。

```bash
for d in $(rclone lsd remote:path/ --dirs-only); do
  rclone link $d
done
```

### GUIフロントエンド

rcloneには公式のGUIフロントエンドはありませんが、次の選択肢があります。

- [rclone browser UI](https://github.com/Xiaoxian51/rclone-browser-ui)
- [rcx](https://github.com/x0rzkov/rcx)


## 公式ドキュメントとサポートリソース

- [rclone公式サイト](https://rclone.org/)
- [rclone GitHub](https://github.com/rclone/rclone)
- [rclone Forum](https://forum.rclone.org/)
