# ripgrep-all
ripgrep-all（通常は "rga" と略されます）は、テキストやバイナリファイル内で正規表現を使用して検索を行うための強力なコマンドラインツールです。このツールは、Linux、macOS、Windowsなど、さまざまなプラットフォームで使用できます。

## 基本的な使い方:

Installation:

```bash
# rgaのインストール
sudo apt-get install ripgrep-all  # Ubuntu/Debian

# brew install ripgrep-all　# macOS

# テキストファイル内でのテキスト検索
rga "search term" path/to/directory

# 正規表現を使用した検索
rga -regexp "^\d{3}-\d{2}-\d{4}$" path/to/directory

# バイナリファイル内での検索
rga --binary "binary pattern" path/to/directory

# 検索結果のファイル名表示
rga -l "search term" path/to/directory
```

```bash
# テキストファイル内での単純なテキストの検索
rga "search term" path/to/directory

# 正規表現を使用した検索
rga -regexp "^\d{3}-\d{2}-\d{4}$" path/to/directory

# バイナリファイル内での検索
rga --binary "binary pattern" path/to/directory

# 検索結果のファイル名表示
rga -l "search term" path/to/directory
```

Usage:

rga [RGA OPTIONS] [RG OPTIONS] PATTERN [PATH ...]

FLAGS:

```

--rga-accurate

より正確なが遅いマッチングを、mimeタイプによって使用します。

デフォルトでは、rgaはファイルの拡張子を使用してファイルをマッチングします。一部のプログラム、例えばsqlite3のようなプログラムはファイルの拡張子をまったく気にしません。そのため、ユーザーは適当な拡張子を使うことがあります。このフラグを指定すると、rgaは入力ファイルの最初の8KiB内のデータを解析し、そのデータからmimeタイプを検出してアダプターを選択します。検出は最初の8KiB内で行われるため、すべての入力ファイルを常に読み込む必要はありません（特にアーカイブ内の場合）。

--rga-no-cache

結果のキャッシュを無効化します。

デフォルトでは、rgaはテキストの抽出結果をキャッシュに格納します。キャッシュはLinuxの場合は${XDG*CACHE_DIR-~/.cache}/ripgrep-all、macOSの場合は*~/Library/Caches/ripgrep-all_、Windowsの場合はC:\Users\username\AppData\Local\ripgrep-allに保存されます。これにより、同じファイルセットに対する繰り返しの検索が高速化されます。このフラグを指定すると、キャッシュは無効になります。

-h, --help

ヘルプ情報を表示します。

--rga-list-adapters

すべての既知のアダプターをリスト表示します。

--rga-print-config-schema

設定ファイルのJSONスキーマを表示します。

--rg-help

ripgrep自体のヘルプを表示します。

--rg-version

ripgrep自体のバージョンを表示します。

-V, --version

バージョン情報を表示します。
```


OPTIONS:


```
--rga-adapters=<adapters>...

アダプターの使用と優先順位（降順）を変更します。

"foo,bar" はアダプターfooとbarのみを使用します。"-bar,baz" はバーとバズを除くすべてのデフォルトアダプターを使用します。"+bar,baz" はすべてのデフォルトアダプターとバーとバズを使用します。

--rga-cache-compression-level=<compression-level>

キャッシュdbに保存する前にアダプターの出力に適用するZSTD圧縮レベル

1から22までの範囲 [デフォルト: 12]

--rga-config-file=<config-file-path>

--rga-max-archive-recursion=<max-archive-recursion>

再帰するアーカイブの最大ネストレベル [デフォルト: 4]

--rga-cache-max-blob-len=<max-blob-len>

キャッシュする最大圧縮サイズ

キャッシュするための最大バイト長（圧縮後）です。長いアダプターの出力はキャッシュされず、毎回再計算されます。

コマンドラインで許可されるサフィックス: k M G [デフォルト: 2000000]

--rga-cache-path=<path>

キャッシュdbを保存するパス [デフォルト: /home/phire/.cache/ripgrep-all]

-h は簡潔な概要を表示し、--help は詳細な情報と高度なオプションを表示します。

ここに示されていないすべてのその他のオプションは、特に [PATTERN] と [PATH ...] はrgに直接渡されます。

```

**Adapters:**
```
- **pandoc:** pandocを使用してバイナリや読み取り不可能なテキストドキュメントをプレインなMarkdownのようなテキストに変換します。実行コマンドは以下の通りです：

pandoc --from= --to=plain --wrap=none --markdown-headings=atx

拡張子: .epub, .odt, .docx, .fb2, .ipynb

poppler: PDFファイルからプレインテキストを抽出するためにpdftotext（poppler-utilsから）を使用します。実行コマンドは以下の通りです：

pdftotext - -

拡張子: .pdf
Mime タイプ: application/pdf

postprocpagebreaks: ページ区切りをASCIIページ区切り文字として指定した入力ファイルの各行にページ番号を追加します。主にpopplerアダプター内部で使用されます。

拡張子: .asciipagebreaks

ffmpeg: 動画のメタデータ、チャプター、字幕、歌詞、その他のメタデータを抽出するためにffmpegを使用します。

拡張子: .mkv, .mp4, .avi, .mp3, .ogg, .flac, .webm

zip: zipファイルをストリームとして読み込み、その内容に再帰的にアクセスします。

拡張子: .zip, .jar
Mime タイプ: application/zip

decompress: 圧縮ファイルをストリームとして読み込み、その内容に異なる抽出器を実行します。

拡張子: .tgz, .tbz, .tbz2, .gz, .bz2, .xz, .zst
Mime タイプ: application/gzip, application/x-bzip, application/x-xz, application/zstd

tar: tarファイルをストリームとして読み込み、その内容に再帰的にアクセスします。

拡張子: .tar

sqlite: sqliteデータベースをシンプルなプレーンテキスト形式に変換するためにsqliteバインディングを使用します。

拡張子: .db, .db3, .sqlite, .sqlite3
Mime タイプ: application/x-sqlite3

以下のアダプターはデフォルトでは無効になっており、'--rga-adapters=+foo,bar'を使用して有効にできます：
- **foo:** fooアダプターを有効にします。
- **bar:** barアダプターを有効にします。
```

- [GitHub - vivainio/RoughGrep: Fast, brutalist UI on top of RipGrep](https://github.com/vivainio/RoughGrep)

### Sort by metadata

- [Sorting Images Using the Creation Date in EXIF Data | Baeldung on Linux](https://www.baeldung.com/linux/images-sort-exif-creation-date)