# ブックマークレットの開発環境を考えてみた

## きっかけ
以下のような手作業の工程が面倒くさい、と思った。
 - JavaScriptのソースを作る ← これは良い
 - ソースをクリップボードにコピーする ←↓ここからがダルい
 - 目的のサイトなどを開く
 - コンソールを開く
 - ソースをペーストする
 - 実行する


## どうなると嬉しいか
以下のような工程であると嬉しい
 - JavaScirptのソースを作る
 - 目的のサイトなどを開く
 - 勝手に実行される


## ではどうするか？
 - [ScriptAutoRunner](https://chrome.google.com/webstore/detail/scriptautorunner/gpgjofmpmjjopcogjgdldidobhmjmdbm?hl=ja)という、任意のサイトで任意のJavaScriptを自動実行させる**素晴らしい**Chrome拡張を使う

## それで解決した？
問題点
 - ローカルのファイル(`例)file:///Users/hogee/Desktop/main.js`)は実行できない。。

## ではどうするか？
localhostでJavaScriptのソースを参照できるようにすれば良い。<br>
たとえば、`http://localhost:1337/src/main.js`のようなかんじで。


## それをやるには何をすれば良いか？
nodejsでサーバーを立ち上げると良い<br>
-> 手順： https://open-groove.net/nodejs/static-contents/ などを参照

## それで解決した？(２回目)
解決した。こんなかんじ↓<br>
<br>
`Visual Studio Code`からnodejsで作ったサーバーを`デバッグ`で実行 -> サーバーが立ち上がる<br>
↓<br>
`http://localhost:1337/src/main.js`をScriptAutoRunnerに入れておく<br>
↓<br>
所定のサイトなどを開く<br>
↓<br>
スクリプトが自動で起動する(素敵)<br>
↓<br>
テストを終えたらVisual Studio Codeのデバッグも停止する<br>
↓<br>
サーバーが起動終了する、かつスクリプトが参照できなくなる

## おわりに
- ScriptAutoRunner便利
- Visual Studio Code便利