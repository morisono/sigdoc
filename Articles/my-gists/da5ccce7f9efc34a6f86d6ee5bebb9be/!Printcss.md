# PDF生成ツールの導入方法とコマンド

## [Pyppdf](https://pypi.org/project/pyppdf/)
pyppdfは、HTMLドキュメントをPDFに変換するためのPythonベースのコマンドラインツールです。

```
Usage: pyppdf [OPTIONS] [PAGE]

  HTMLドキュメントを読み取り、pyppeteerを使用してPDFに変換し、ディスクに書き込みます
  （またはbase64エンコードされたPDFを標準出力に書き込みます）。

  PAGEはURLまたは一般的なファイルパスであり、PAGEが設定されていない場合、pyppdfは標準入力から読み取ります。

  -a、--args デフォルト値：

  {launch={args=['--font-render-hinting=none']},goto={waitUntil='networkidle0',
  timeout=100000}, pdf={width='8.27in', printBackground=True, margin={top='1in',
  right='1in', bottom='1in', left='1in'},}}

  これらは次のpyppeteerメソッドに影響します（最後の名前のみ使用する必要があります）： pyppeteer.launch、page.goto、page.emulateMedia、
  page.waitForNavigation、page.waitFor、page.pdf。詳細は次を参照してください：

  https://pyppeteer.github.io/pyppeteer/reference.html#pyppeteer.page.Page.pdf

Options:
  -a、--args TEXT Pythonコードの文字列で、pyppeteer関数オプションで評価される辞書です。事前に定義された
  デフォルトがあります。
  -u、--upd TEXT --args辞書と同じですが、--upd辞書は--argsに再帰的にマージされます。
  -o、--out TEXT 出力ファイルのパス。設定されていない場合、pyppdfはbase64エンコードされたPDFを標準出力に書き込みます。
  -d、--dir TEXT '--goto temp'モードのディレクトリ。--outのディレクトリよりも優先されます。
  -g、--goto [url|setContent|temp|data-text-html]
    page.gotoの動作を選択します。デフォルトでは、pyppdfは 'url' モードを試み、次に 'setContent' モードを試みます。
    'url'は、url（PAGE）引数が提供された場合またはマージされた引数で {goto={url=<...>}} が設定されている場合にのみ動作します。
    'setContent'（page.gotoなしで動作）、'temp'（一時ファイル）および 'data-text-html'（stdin入力の場合のみ動作）があります。
    'setContent'と 'data-text-html'はおそらく一部のリモートコンテンツをサポートしていないようです。最後のものでは
    いくつかのバグがあります。page.goto(f'data:text/html,{html}')
  --help メッセージを表示して終了します。
```

## PDFreactor 11.6.0

PDFreactorはコマンドラインツールが提供されていないため、Java APIを使用してPDFを生成します。詳細はPDFreactorの公式ドキュメンテーションを参照してください。

[PDFreactor 公式ウェブサイト](https://www.pdfreactor.com/)

## PrinceXML 15

PrinceXMLは商用ソフトウェアで、コミュニティ版も提供されています。試用版はコマンドラインツールを含んでいます。

[PrinceXML 公式ウェブサイト](https://www.princexml.com/)

## Antennahouse CSS Formatter 7.2 MR7

Antennahouse CSS Formatterにはコマンドライン版が提供されています。以下のコマンドでインストールできます。

```bash
# Debian/Ubuntu
sudo apt-get install -y cssformatter

# CentOS/RHEL
sudo yum install -y cssformatter
```

[Antennahouse CSS Formatter](https://www.antenna.co.jp/AHF/help/ja/ahf-xslcmd.html)

## [Typeset.sh 0.22.0](https://typeset.sh/en)

Typeset.shはPHPベースのツールで、Composerを使用してインストールします。

```
composer global require typeset/typeset
```

## [BFO Publisher 1.2](https://publisher.bfo.com/)

```
java -jar publisher-bundle-1.2.jar --output bfo.pdf index.html
```

- https://print-css.rocks/