# 書影の一括取得

booklog Export Dataを使います。

```sh
set timestamp (date -u +%Y-%m-%dT%H-%M-%S)
mkdir $timestamp
set url "https://ndlsearch.ndl.go.jp/thumbnail/"

# CJK, ISBN選択, nullを除去, JSON変換
iconv -c -f SJIS -t UTF8 booklog.csv |
xsv select 3,12 |
tr -d \" |
jq -Rn '
  inputs
  | select(. != "")
  | split(",")
  | {isbn: .[0], title: .[1]}
' |
jq -s . > "$timestamp/tmp.json"

# Check
cat $timestamp/tmp.json | jq -r '[.[] | select(.isbn? != null and .isbn != "")]' >"$timestamp/list.json"
cat $timestamp/tmp.json | jq -r '.[] | select(.isbn? != null and .isbn != "") | .isbn' 

# parse json, 拡張子付与, 書影問い合わせ
cat "$timestamp/list.json" | jq -r '.[] | select(.isbn? != null and .isbn != "") | .isbn' | perl -pe 's/$/.jpg/' | sort | xargs -i curl -sS -k -L $url{} --output $timestamp/(basename {})

 
```