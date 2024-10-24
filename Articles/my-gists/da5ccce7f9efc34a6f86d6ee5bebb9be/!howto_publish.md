# 組版・製本について

## CSS組版

CSS組版は、ウェブページのデザインやレイアウトを管理するための重要なツールです。CSS（Cascading Style Sheets）は、HTMLコンテンツの見た目やスタイルを指定するために使用され、ページのフォント、色、マージン、パディング、配置などを制御します。CSSを使用することで、ウェブページを美しく整え、ユーザーエクスペリエンスを向上させることができます。

## PDF製本
    
PDF製本は、電子書籍や印刷物を作成するプロセスであり、HTMLコンテンツをPDFフォーマットに変換して製本します。PDF（Portable Document Format）は、異なるプラットフォームやデバイスで一貫した表示を提供し、文書の保存や共有に適したフォーマットです。HTMLからPDFへの変換は、ウェブコンテンツを印刷可能な形式に変換する必要がある場合や、電子書籍の制作などで利用されます。

## CLI Toolをつかった組版の効率化

### pdfly
https://github.com/py-pdf/pdfly

### Vivliostyle

Vivliostyleは、電子書籍の制作やWebページの印刷向けのオープンソースの組版ツールです。Vivliostyleは、HTMLとCSSを使用してページのレイアウトを調整し、美しい印刷物を生成するのに役立ちます。Vivliostyleは、プロジェクトやドキュメントに簡単に組版機能を統合でき、高品質の出力を提供します。

1. vivliostyle-cliのインストール:
    ```bash
    npm install -g @vivliostyle/cli
    ```

1. HTMLコンテンツの準備:
製本化したいHTMLコンテンツを準備します。これは通常、単一のHTMLファイルまたは複数のHTMLファイルから成ることがあります。

1. CSSスタイルの設定:
VivliostyleはCSSを使用してページのレイアウトを調整します。必要に応じて、印刷用のスタイルを定義します。

1. .PDFの出力:
    Vivliostyleを使用してHTMLコンテンツを製本化し、PDFファイルとして出力します。
    ```css
    vivliostyle build in.html -o out.pdf -s a4 -d --user-style user-style.css  --press-ready
    ```
    

### Paged.js
Paged.jsは、HTMLコンテンツを印刷可能な形式に変換し、製本化するための強力なツールです。以下はPaged.jsを使用してHTMLコンテンツを製本する基本的な手順です。

1. Paged.jsのインストール:

    Paged.jsをインストールするには、以下のコマンドを使用します。

    ```bash
    npm install -g pagedjs-cli pagedjs
    ```
 
1. HTMLコンテンツの準備:
製本化したいHTMLコンテンツを準備します。これは通常、単一のHTMLファイルまたは複数のHTMLファイルから成ることがあります。

1. CSSスタイルの設定:
Paged.jsはCSSを使用してページのレイアウトを調整します。必要に応じて、印刷用のスタイルを定義します。

    ```css
    <!--   改ページ   -->
    .chapter {
      break-before: right;
    }
    
    h2 {
      break-before: page;
    }
    
    <!--   ページ番号, 題   -->
    h2 {
      string-set: title content(text);
    }
    
    @page {
      @bottom-left {
        content: "page " counter(page);
      }
      @bottom-center {
        content: string(title);
      }
    }
    ```

1. .PDFの出力:
    Paged.jsを使用してHTMLコンテンツを製本化し、PDFファイルとして出力します。
    
    ```bash
    pagedjs-cli -i in.html -o out.pdf
    ```
    
    ```
    -h, --help                  output usage information
    -V, --version               output the version number
    -i, --inputs [inputs]       Inputs
    -o, --output [output]       Output
    -d, --debug                 Show Electron Window to Debug
    -l, --landscape             Landscape printing
    -s, --page-size [size]      Print to Page Size [size]
    -w, --width [size]          Print to Page Width [width]
    -h --height [size]          Print to Page Height [weight]
    -m, --page-margin [margin]  Print with margin [margin]
    -n, --hyphenate [lang]      Hyphenate with language [language], defaults to "en-us"
    -hi, --hypher_ignore [str]  Ignore passed element selectors, such as ".class_to_ignore, h1"
    -ho, --hypher_only [str]    Only hyphenate passed elements selector, such as ".hyphenate, aside"
    -e, --encoding [type]       Set the encoding of the input html, defaults to "utf-8"
    -t, --timeout [ms]          Set a max timeout of [ms]
    ```

## create-book
- https://github.com/vivliostyle/create-book
- vivliostyle.config.js を編集する
  ```js
  module.exports = {
      title: 'man_crypto',
      author: 'admin',
      language: 'ja',
      size: 'A4',
      theme: '@vivliostyle/theme-techbook@^1.0.0',
      entry: [
        '001_about.md',
        {
          path: '001_about.md',
          title: '',
          encodingFormat: 'text/html',
          rel: 'contents'
        },
      ],
      entryContext: './contents/',
      output: [
        './content.pdf',
        {
          path: './book',
          format: 'pdf',
          preflight: 'press-ready-local'
        },
      ],
      workspaceDir: '.vivliostyle',
      toc: true,
      tocTitle: '索引',
      cover: './images/cover.png',
      timeout: 120000,
      vfm: {
        hardLineBreaks: true,
        disableFormatHtml: true,
      },
    }
  ```
- package.json を編集する
  ```json
  {
      "name": "man_crypto",
      "description": "manual of crypto management and trading",
      "version": "0.0.0",
      "author": "admin <Your email>",
      "scripts": {
        "build": "vivliostyle build",
        "preview": "vivliostyle preview"
      },
      "dependencies": {
        "@vivliostyle/cli": "latest"
      },
      "license": "MIT",
      "private": true
    }
  ```

 - コンテンツの編集
    ```markdown
    # バーンスタインの不等式 (Bernstein Inequalities)

    バーンスタインの不等式は、独立な有界な確率変数の和の尾部の振る舞いに関する増大の不等式の一群です。これは、有界な範囲を持つ確率変数に対して、チェルノフの境界やヘフディングの不等式よりも緊密な境界を提供します。バーンスタインの不等式は、確率変数の最大範囲だけでなく分散も考慮に入れ、収束の境界を改善します。

    バーンスタインの不等式の一般的な形式は以下のように表されます：

    $$
    P\left(\left|\sum_{i=1}^n X_i\right| \geq t\right) \leq 2 \exp\left(-\frac{t^2}{2\left(\sum_{i=1}^n \sigma_i^2 + Bt/3\right)}\right)
    $$

    ここで、
    - $\(X_i\)$ は独立な確率変数,
    - $\(t\)$ は閾値,
    - $\(\sigma_i^2\)$ は $\(X_i\)$ の分散,
    - $\(B\)$ は確率変数 $\(X_i\)$ の上界です。


    {振|ふ}り{仮名|がな}が使えます。 

    ![VFMならキャプションも書けます。画像のサイズは幅1500pxです。](./fig-1.jpeg){width=1500}

    <span class="footnote">footnote text</span>
    ```

  - ビルド
    ```
    npm create book mybook
    cd mybook
    npm run preview

    npm run build
    ```

以上が、Paged.jsを使用してHTMLコンテンツを製本化する基本的な手順です。詳細な情報やカスタマイズオプションについては、Paged.jsの公式ドキュメントを参照してください。

## WeasyPrint - インストール

[**WeasyPrint**](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)は、HTMLとCSSからPDF文書を生成するためのオープンソースのツールです。以下はWeasyPrintのインストールに関する要点です：

- **目的**: HTMLとCSSからPDF文書を生成するためのツール。WebページやドキュメントをPDF形式に変換するのに役立ちます。

- **公式ウェブサイト**: [WeasyPrint Installation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)で詳細なインストール手順とドキュメンテーションを提供しています。

- **インストール方法**: WeasyPrintはPythonのライブラリとして提供されており、pipを使用してインストールできます。詳細な手順は公式ドキュメンテーションに記載されています。

- **依存関係**: WeasyPrintにはPythonと関連する依存関係があります。これらの依存関係もインストールする必要があります。

- **利点**: WebコンテンツをPDFに変換する際に、HTMLとCSSをそのまま使用できます。カスタムスタイルやレイアウトを適用でき、高品質なPDF文書を生成できます。

- **使用例**: WeasyPrintはWebアプリケーションやレポート生成に使用され、HTML/CSSベースのドキュメントを簡単にPDFに変換するのに便利です。

WeasyPrintの詳細なインストール手順および使用方法については、[公式ウェブサイト](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)を参照してください。

## Merge-Markdown

[**Merge-Markdown**](https://github.com/knennigtri/merge-markdown)は、Markdownファイルを簡単に結合するためのオープンソースのツールです。このツールを使用することで、複数のMarkdownファイルを1つのファイルに結合し、文書をまとめることができます。以下はMerge-Markdownに関する要点です：

- **目的**: Markdownファイルの結合。複数のMarkdownファイルを1つのファイルに結合して、ドキュメントや記事を管理するための効果的なツールです。

- **GitHubリポジトリ**: [Merge-Markdown](https://github.com/knennigtri/merge-markdown)はGitHubで公開されており、オープンソースプロジェクトとして利用可能です。

- **使用方法**: コマンドラインツールとして提供され、簡単にMarkdownファイルを結合できます。特定のオプションを指定して、結合対象のファイルを選択できます。

- **利点**: 複数のMarkdownファイルを結合することで、大規模な文書やウェブページを簡単に管理できます。ドキュメンテーションやコラボレーションプロジェクトに適しています。

## Thinreports

[**Thinreports**](https://github.com/thinreports/thinreports/tree/main)は、Rubyプログラムを使用してPDF文書を生成するためのオープンソースライブラリです。Thinreportsを使用することで、カスタマイズ可能なPDFレポートを簡単に作成できます。以下はThinreportsに関する要点です：

- **目的**: PDFレポートの生成。Rubyプログラムを使用して、データからPDF文書を動的に生成するためのライブラリです。

- **GitHubリポジトリ**: [Thinreports](https://github.com/thinreports/thinreports/tree/main)はGitHubで公開されており、オープンソースプロジェクトとして提供されています。

- **使用方法**: Rubyプログラム内でThinreportsライブラリを使用し、テンプレートやデータを組み合わせてPDFレポートを生成します。カスタムデザインとデータ統合が容易です。

- **利点**: ThinreportsはRubyをベースにしており、柔軟でカスタマイズ可能なPDF文書を生成するための優れたツールです。ビジネスレポートや帳票の自動生成に役立ちます。

## Zipreport CLI

[**Zipreport CLI**](https://github.com/zipreport/zipreport-cli)は、レポートの生成と配信を簡素化するためのオープンソースのコマンドラインツールです。以下はZipreport CLIに関する要点です：

- **目的**: レポートの生成と配信。テンプレートからレポートを生成し、電子メールなどで配信できる効率的なツールです。

- **GitHubリポジトリ**: [Zipreport CLI](https://github.com/zipreport/zipreport-cli)はGitHubで公開されており、オープンソースプロジェクトとして提供されています。

- **使用方法**: コマンドラインツールとして提供され、テンプレートやデータを使用してレポートを生成し、指定された方法で配信できます。

- **利点**: ビジネスレポートやドキュメンテーションの自動生成と配信を効率化し、作業の時間と手間を削減します。カスタムレポートの生成にも適しています。

## 注意点
1. [Quarto](https://quarto.org/)が必要となる場合があります。
    ```sh
    git clone https://github.com/quarto-dev/quarto-cli
    cd quarto-cli
    ./configure.sh
    ```

1. OS 互換性の考慮

    Docker 上で出力することで、出力結果を保証できます。
    ```
    vivliostyle build --render-mode docker
    ```

1.  PDF/X-1a ファイルフォーマット

    印刷入稿に適した PDF/X-1a 形式で出力することができます。
    ```
    vivliostyle build manuscript.md --preflight press-ready --preflight-option gray-scale
    vivliostyle build manuscript.md --preflight press-ready --preflight-option enforce-outline
    ```

1. Type3 フォント
    Type3は印刷所で対応不可の場合がある為、変更する必要が生じる場合があります。

    ```sh
    DOC=$1
    DOC=${DOC:-doc.pdf}
    gs -dNOPAUSE -dBATCH -dNoOutputFonts -sDEVICE=pdfwrite -o outline-$DOC -f $DOC
    ```

## 他言語による実装[WIP]

FerrumとGroverはRubyで書かれたツールおよびライブラリですが、これらはRuby以外のプログラミング言語でも利用することができます。

### Ferrum

- FerrumはRuby用のヘッドレスブラウザライブラリで、Webスクレイピングや自動テストに使用されます。
- Ferrumを使用して生成されたデータは、Ruby以外のプログラミング言語で処理および使用することができます。
- Ruby以外の言語を使用している場合でも、Ferrumで取得した情報をエクスポートして他のアプリケーションと統合できます。

### Grover

- GroverはHTMLからPDFを生成するためのユーティリティで、Node.jsで動作します。
- Ruby以外のプログラミング言語を使用している場合でも、Node.jsからGroverを呼び出して利用できます。
- Groverは言語に依存せず、Node.jsプロジェクトやスクリプトから容易に使用できます。

FerrumとGroverはRuby以外のプログラミング言語とも統合できる汎用的なツールおよびライブラリです。利用したいプログラミング言語に合わせて適切に統合することができます。

[^1]: https://pagedjs.org/documentation/ [^1]
[^2]: https://vivliostyle.org/ja/documents/ [^2]
[^3]: https://marketplace.visualstudio.com/items?itemName=abechanta.vscode-ext-paged-media&ssr=false#overview [^3]
