# ffsend 使い方ガイド

[ffsend](https://gitlab.com/timvisee/ffsend) は、ファイルを安全に共有するためのコマンドラインツールです。以下は基本的な使い方のガイドです。

## インストール

ffsend を使用するには、まずシステムにインストールする必要があります。

```sh
brew install ffsend
```

## 使い方

### 基本

```bash

ffsend info https://send.vis.ee/#sample-share-url # 詳細情報を表示

ffsend history # 履歴
```

### ファイルのアップロード

```bash
ffsend upload ファイル名
```

```sh
ffsend upload file ---expiry-time DATE # 期限 ファイル名
ffsend upload file --password PASS # パスワード ファイル名
ffsend upload file --downlads 4 # 4回まで許可

# - Archive the file before uploading
# - Copy the shareable link to your clipboard
# - Open the shareable link in your browser
ffsend upload file -d 20 -e 4w -p --archive --copy --open
```

### ファイルのダウンロード

```sh
ffsend download 共有リンク
```


## 注意点

・未登録ユーザーでも1GBまでのファイルをアップロード可能で、アカウント登録すれば最大サイズが2.5GBにアップします。

```sh
ffsend 0.2.76
Tim Visee <3a4fb3964f@sinenomine.email>
Easily and securely share files from the command line.
A fully featured Send client.

The default public Send host is provided by Tim Visee, @timvisee.
Please consider to donate and help keep it running: https://vis.ee/donate

USAGE:
    ffsend [FLAGS] [OPTIONS] [SUBCOMMAND]

FLAGS:
    -f, --force          Force the action, ignore warnings
    -h, --help           Prints help information
    -i, --incognito      Don't update local history for actions
    -I, --no-interact    Not interactive, do not prompt
    -q, --quiet          Produce output suitable for logging and automation
    -V, --version        Prints version information
    -v, --verbose        Enable verbose information and logging
    -y, --yes            Assume yes for prompts

OPTIONS:
    -A, --api <VERSION>                 Server API version to use, '-' to lookup [env: FFSEND_API]
        --basic-auth <USER:PASSWORD>    Protected proxy HTTP basic authentication credentials (not FxA) [env:
                                        FFSEND_BASIC_AUTH]
    -H, --history <FILE>                Use the specified history file [env: FFSEND_HISTORY]
    -t, --timeout <SECONDS>             Request timeout (0 to disable) [env: FFSEND_TIMEOUT]
    -T, --transfer-timeout <SECONDS>    Transfer timeout (0 to disable) [env: FFSEND_TRANSFER_TIMEOUT]

SUBCOMMANDS:
    upload        Upload files [aliases: u, up]
    download      Download files [aliases: d, down]
    debug         View debug information [aliases: dbg]
    delete        Delete a shared file [aliases: del, rm]
    exists        Check whether a remote file exists [aliases: e]
    generate      Generate assets [aliases: gen]
    help          Prints this message or the help of the given subcommand(s)
    history       View file history [aliases: h]
    info          Fetch info about a shared file [aliases: i]
    parameters    Change parameters of a shared file [aliases: params]
    password      Change the password of a shared file [aliases: pass, p]
    version       Determine the Send server version [aliases: v]

This application is not affiliated with Firefox or Mozilla.
```

https://gitlab.com/timvisee/ffsend