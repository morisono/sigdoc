## Find系コマンドについて

繰り返し処理にはwhile,for 等を用いる。parallel,xargsで並列にすることもできる。


### 並列実行

```
fd . -e png -x parallel -j 4
```
## 選択

- [skim](https://github.com/lotabout/skim) による高速検索
```bash
fd | sk
```

- [Ultra Fast FUZZY finding in your terminal! | by Cason Adams | Medium](https://medium.com/@casonadams/ultra-fast-fuzzy-finding-in-your-bash-shell-9550224e5138)
- [Fuzzy Finder in rust!](https://rustrepo.com/repo/lotabout-skim-rust-system-tools)

## find, fdの相違点とオプション

Why these are not same result ? 

```bash
for sub_dir in $sub_dirs; printf "%s ->\n%s\n" $sub_dir (fd --full-path -t f -e png "./$base_dir/$sub_dir"); end
```

このコマンドは、各サブディレクトリ名の後に、そのサブディレクトリ内で見つかったすべての.pngファイルのリストを表示します。 xargsコマンドはファイルパスを1つの文字列に連結し、それを表示します。

```bash
for sub_dir in $sub_dirs; printf "%s: \n%s\n" $sub_dir (find "./$base_dir/$sub_dir" -type f -name "*.png"); end
```

このコマンドは、各サブディレクトリ名の後に、指定されたすべてのサブディレクトリで見つかったすべての.pngファイルパスを表示します。 xargsコマンドはすべてのファイルパスを1つの文字列に連結し、それを表示します。

主な違いは、ファイルパスがどのようにフォーマットされ、表示されるかです。

- Capture only png in folder named 'face', then natural sort
```bash
fd --fixed-strings 'face/' --full-path -e png | sort -V
```

## 並べ替え


```bash
fd -e png -X eza -s modified
```

使用可能なキーワードは以下の通り。
```bash
eza -s
eza: Flag -s needs a value (choices: name, Name, size, extension, Extension, modified, changed, accessed, created, inode, type, none)
```

さらにリッチに
```bash
fd -e png -X eza -l --group-directories-first --no-user -@ --time-style +%Y%m%dT%H%M%S -s modified
```


## チェックサム

```bash
fd -e png -x md5sum > file_checksums.txt
```

```bash
# brew install coreutils # for sha256sum

find . -iname 'model*' -regex ".*\.\(jpg\|gif\|png\|jpeg\)" -exec sha256sum {} \;
```

```bash
ls . | xargs -i sha256sum "{}"
```


## Snap

```bash
magick \
-delay 600 \
-gravity center (fd -e png ) \
-resize 1920x880\> \
-background black \
-extent 1920x1080 \
-alpha remove \
-layers OptimizePlus \
-fill white -font 'MS-Mincho' \
-pointsize 40 \
-annotate +0-500 '%t' \
merged.gif
```

