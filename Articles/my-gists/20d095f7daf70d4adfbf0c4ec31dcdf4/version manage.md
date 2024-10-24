## rtx: version manager
```
sudo apt-get install build-essential procps curl file git
brew install bzip2 libffi libxml2 libxmlsec1 openssl readline sqlite3 xz zlib tcl-tk ncurses coreutils 
set -Ux CC "$(brew --prefix gcc)/bin/gcc-11
# sudo apt install ctypes 
# libuuid

sudo apt-get install libffi-dev　libbz2-dev libssl-dev libncurses-dev libsqlite3-dev libreadline-dev libtk8.6-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev

```


以下は、ローレベルな開発やシステム環境でよく使用されるパッケージの一部です。

bzip2: 圧縮および解凍を行うためのツールおよびライブラリ。
libffi: C言語で記述されたプログラムを他の言語とのインタフェースとして使用するためのライブラリ。
libuuid: UUID（Universally Unique Identifier）の生成と操作を行うためのライブラリ。
libxml2: XMLデータの解析および操作を行うためのライブラリ。
libxmlsec1: XMLデータの署名および暗号化をサポートするためのライブラリ。
openssl: 暗号化や証明書の管理など、セキュリティ関連の機能を提供するライブラリ。
readline: コマンドラインインターフェースでの行編集機能をサポートするライブラリ。
sqlite3: 軽量なデータベースエンジンであるSQLiteの実行バイナリとライブラリ。
xz: 圧縮および解凍を行うためのツールおよびライブラリ。
zlib: データの圧縮および解凍を行うためのツールおよびライブラリ。
tcl-tk: Tcl（Tool Command Language）およびTk（グラフィカルユーザインターフェースツールキット）の実行環境とライブラリ。
ncurses: テキストユーザインターフェース（TUI）アプリケーションのためのターミナル操作ライブラリ。
gcc: CおよびC++のコンパイラであり、多くのプログラミング言語で広く使用されています。
make: ビルド自動化ツールであり、ソフトウェアのビルドプロセスを効率化するために使用されます。
cmake: クロスプラットフォームなビルド自動化ツールであり、Makefileを生成するための設定ファイルを作成します。
autoconf: ソフトウェアのポータビリティを向上させるための設定スクリプトを生成するためのツールです。
automake: プロジェクトのビルドプロセスを自動化するためのMakefileを生成するためのツールです。
libtool: ソフトウェアのライブラリ作成とバージョン管理を支援するツールです。
valgrind: プログラムのデバッグやパフォーマンス解析のためのツールセットであり、メモリリークやデッドロックなどの問題を検出します。
gdb: デバッグ用のオープンソースのデバッガであり、プログラムの実行中にステップ実行や変数の監視などを行うことができます。
strace: 実行中のプロセスがシステムコールをどのように行っているかをトレースするためのユーティリティです。
perf: プロファイリングやパフォーマンス解析のためのツールであり、プログラムの実行中にハードウェアイベントを監視します。

これらのツールやパッケージは、低レベルの開発やシステム調整、パフォーマンス解析などのタスクに役立ちます。特定の開発環境や目的に応じて、必要なツールを選択して利用することが一般的です。
