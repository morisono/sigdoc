# Rclone

rclone は強力なクラウドストレージ管理ツールです。以下に、最もよく使用されるrcloneコマンドとその説明をまとめました。

## 1. 設定

```bash
rclone config
```
新しいリモートを追加したり、既存の設定を変更したりするための対話式セットアップを開始します。

## 2. リスト表示

```bash
rclone ls remote:path
```
指定したパスのファイルとディレクトリを一覧表示します。

```bash
rclone lsd remote:path
```
ディレクトリのみを一覧表示します。

## 3. コピー

```bash
rclone copy /local/path remote:path
```
ローカルからリモートへファイルをコピーします。逆も可能です。

```bash
# 既存のファイルを上書きせず、新しいファイルのみをコピーします。
rclone copy --ignore-existing /local/path remote:path --dry-run 
```

## 4. 同期

```bash
rclone sync /local/path remote:path 
```
ソースの状態をデスティネーションに完全に反映させます。

## 5. 移動

```bash
rclone move /local/path remote:path
```
ファイルを移動（コピー後に元のファイルを削除）します。

## 6. 削除

```bash
rclone delete remote:path/file
```
指定したファイルを削除します。

```bash
rclone purge remote:path
```
指定したディレクトリとその中身をすべて削除します。

## 7. チェック

```bash
rclone check /local/path remote:path
```
2つの場所のファイルを比較し、違いを報告します。

## 8. サイズ確認

```bash
rclone size remote:path
```
指定したパスの合計サイズと、ファイルとディレクトリの数を表示します。

## 9. マウント

```bash
rclone mount remote:path /local/mountpoint
```
リモートストレージをローカルファイルシステムにマウントします。

## 10. 双方向同期

```bash
rclone bisync /local/path remote:path
```
2つの場所間で双方向同期を行います。

## 11. フィルタリング

すべてのコマンドで `--include`, `--exclude` フラグを使用してファイルをフィルタリングできます。

```bash
rclone copy /local/path remote:path --include "*.jpg" --exclude "*.tmp"
```

## 12. ドライラン

`--dry-run` フラグを使用すると、実際の変更を行わずに操作をシミュレートできます。

```bash
rclone sync /local/path remote:path --dry-run
```

## 13. ダウンロードリンク

```bash
rclone link protondrive:path/to/folder --expire 7d --password mysecretpassword
```

- If you want to get links for multiple files, you can use a loop in bash. Here's an example:

```bash
rclone lsf protondrive:path/to/directory | while read -r file; do
  echo "$file: $(rclone link protondrive:path/to/directory/"$file")"
done > download_links.txt
```

- If you want to generate a random password, you can use the openssl command in combination with rclone:

```bash
password=$(openssl rand -base64 12)
link=$(rclone link protondrive:path/to/folder --expire 7d --password "$password")
echo "Link: $link"
echo "Password: $password"
```

- If you want to do this for multiple folders, you can use a loop:

```bash
rclone lsf protondrive:path/to/parent_folder -R | grep '/$' | while read -r folder; do
    password=$(openssl rand -base64 12)
    link=$(rclone link protondrive:"$folder" --expire 7d --password "$password")
    echo "Folder: $folder"
    echo "Link: $link"
    echo "Password: $password"
    echo "------------------------"
done
```


### MISC

- [GUI](https://rclone.org/gui/)
```sh
rclone rcd --rc-web-gui
rclone rcd --rc-web-gui --rc-web-gui-no-open-browser

```

### REF

- https://rclone.org/faq/#can-i-use-rclone-with-an-http-proxy
- https://www.reddit.com/r/rclone/comments/1d2pm6p/rclone_blocked_by_proton_drive_it_seems/?share_id=E7Wk9x_YtWoDoTOjBkvSE&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1
- https://github.com/dimitrov-adrian/RcloneTray
  - FUSEでファイルシステムに見せている
- https://github.com/winfsp/winfsp
- https://github.com/kapitainsky/RcloneBrowser
- https://linuxpip.org/rclone-examples#rclone-copy-examples-copying-data-between-cloud-storage-services