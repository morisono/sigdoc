```sh
❯ du --max-depth 1 | awk -v q='"' '$1 < 30000000 && $2 != "." {sub(/^[0-9\t ]+/, "", $0); print q $0 q}'

du -d 1 /path/to/folderは、指定されたフォルダ以下の各フォルダのディスク使用量を表示します。
awk '$1 <= 1024'は、ディスク使用量が1MB以下のものをフィルタリングします。
cut -f 2-は、ディレクトリのパスのみを抽出します。
xargs -I {} find {} -type f -name "drawFn.py"は、各1MB以下のディレクトリに対して、drawFn.pyを検索します。
```