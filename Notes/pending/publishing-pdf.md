---
title: Publishing Pdf
name: PublishingPdf
description: Publishing Pdf
type: overview
categories: academic
topics: academic
tags: 
  - #note

id: 5f89d4
uid: 56c22533-3a7b-44d9-a53e-359b9bb86453
date: 2024-09-03T02:07:37
created_at: 1725296857
updated_at: 1725296857
path: Notes/pending/publishing-pdf.md
slug: publishing_pdf
url: https://username.github.io/repo/posts/2024/09/03/0/1/publishing-pdf
redirect_from: 
  - 

lang: en
author: undefined
private: true
weight: 1
toc: false
draft: true
status: 
keywords: 
changelog: 
versions: 
---



# Publishing Pdf Docs

## Abstract

## Introduction

PubCSS は学資論文向けのCSSです。
Pandocは、HTMLをPDFへ変換するCLIユーティリティです。
Princeは、HTMLをPDFへ変換するエンジンです。
MdPDFは、MarkdownをPDFへ変換するCLIユーティリティです。

これらを用いて、統一書式としてのスタイリングを行います。

## Methodologies


### Prerequisites

- TeX
- [Pandoc - Installing pandoc](https://pandoc.org/installing.html#linux)
- [Prince - Download Prince 15.4](https://www.princexml.com/download/15/)
- [GitHub - elliotblackburn/mdpdf: Markdown to PDF command line app with support for stylesheets](https://github.com/elliotblackburn/mdpdf)
- [GitHub - kuangdash/pubcss: Format academic publications in HTML & CSS](https://github.com/kuangdash/pubcss/tree/master)
- [GitHub - Wandmalfarbe/pandoc-latex-template: A pandoc LaTeX template to convert markdown files to PDF or LaTeX.](https://github.com/Wandmalfarbe/pandoc-latex-template)


### Steps

Uninstall old TeX and Reinstall newer version
```bash
sudo apt-get purge "texlive*"
sudo rm -rf "/usr/local/texlive/*"
rm -rf "~/.texlive*"
sudo rm -rf /usr/local/share/texmf
sudo rm -rf /var/lib/texmf
sudo rm -rf /etc/texmf
sudo apt-get remove tex-common --purge
rm -rf ~/.texlive

sudo apt install wget perl-tk
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xzf install-tl-unx.tar.gz
cd install-tl-****  # **** is version
sudo ./install-tl
# rm -rf /tmp/***/***  # if failure and retry
```

```
export PATH=/usr/local/texlive/2021/bin/x86_64-linux${PATH:+:${PATH}}
export INFOPATH=/usr/local/texlive/2021/texmf-dist/doc/info${INFOPATH:+:${INFOPATH}}
export MANPATH=/usr/local/texlive/2021/texmf-dist/doc/man${MANPATH:+:${MANPATH}}
```

```bash
sudo apt install equivs --no-install-recommends freeglut3
wget -O debian-equivs-2021-ex.txt https://www.tug.org/texlive/files/debian-equivs-2021-ex.txt

equivs-build debian-equivs-2021-ex.txt
sudo dpkg -i texlive-local_2021.99999999-1_all.deb
sudo apt install -f
```

- [Installing Texlive Latest Version (Texlive-2021) on Ubuntu-20.04/18.04 | Md Fahim Sikder](https://fahim-sikder.github.io/post/installing-texlive-latest-ubuntu/)

Using Tlmgr

```bat
FROM pandoc/latex:2.14.0.3

ARG eisvogel_version=2.4.2

RUN tlmgr install luatexja
RUN tlmgr install haranoaji haranoaji-extra
RUN tlmgr install adjustbox babel-german background bidi collectbox csquotes everypage filehook footmisc footnotebackref framed fvextra letltxmacro ly1 mdframed mweights needspace pagecolor sourcecodepro sourcesanspro titling ucharcat ulem unicode-math upquote xecjk xurl zref || exit 1
RUN tlmgr install selnolig || exit 1

RUN mkdir -p /templates/eisvogel \
  && wget https://github.com/Wandmalfarbe/pandoc-latex-template/releases/download/v${eisvogel_version}/Eisvogel-${eisvogel_version}.tar.gz -O /templates/eisvogel/eisvogel.tar.gz \
  && tar -xvzC /templates/eisvogel -f /templates/eisvogel/eisvogel.tar.gz \
  && mv /templates/eisvogel/eisvogel.latex /templates/eisvogel.tex \
  && rm -rf /templates/eisvogel
```
- [pandoc/latex + eisvogel template](https://gist.github.com/smellman/4a176d4730d3a56e0bfe3cc7bc649c0f)

Install prince 
```bash
tar xf prince-15.4-ubuntu20.04-amd64.tar.gz
sudo prince-15.4-ubuntu20.04-amd64/install.sh
```

Then add alias to shell config 
- e.g.:  `~/.config/fish/config.fish`
```bash

alias prince_win '/mnt/c/Program\ Files\ \(x86\)/Prince/engine/bin/prince.exe'
```

Usage example
```
prince_win input.html -o output.pdf
```

Install mdpdf
```bash
npm i -g mdpdf 

# 日付
echo '<header><span class=\"date\"></span></header>' > header.html

# Filepath, ページ番号
echo '<footer><span style=\"font-size: 10px\"> <span class=\"pageNumber\"></span>/<span class=\"totalPages\"></span></span></footer>' > footer.html
```

Install PubCSS
```bash
git clone https://github.com/kuangdash/pubcss.git 
cd kuangdash/pubcss

cp formats/acm-sig/css/pub.css . # 議事録
# cp formats/acm-sigchi/css/pub.css . # 会議論文
# cp formats/acm-sigchi-ea/css/pub.css . # 拡張アブストラクト
# cp formats/ieee/css/pub.css . # IEEE会議の議事録
```

Build PDF
- Using prince
```bash
prince input.html output.pdf
```
- Using Pandoc
```bash
set note Notes/pending/demo-note1.md

# iconv -c -f SJIS -t UTF8 $note | 
pandoc $note --css pub.css \
-V CJKmainfont="Noto Serif JP" \
-V mainfont="Noto Serif JP" \
--pdf-engine=prince \
--metadata title='Untitled' \
-o (basename $note .md).pdf

# Argument of --pdf-engine must be one of wkhtmltopdf, weasyprint, pagedjs-cli, prince, pdflatex, lualatex, xelatex, latexmk, tectonic, pdfroff, typst, context

# pagedjs-cli is another good choice
# npm install -g pagedjs-cli
# --pdf-engine=pagedjs-cli \

# wkhtmltopdf is extra good choice
# sudo apt-get install wkhtmltopdf
# --pdf-engine=wkhtmltopdf \
# -V documentclass=bxjsarticle -V classoption=pandoc
# --pdf-engine=lualatex  # 日本語が表示されない
```

Using template
```bash
set temp_url https://github.com/Wandmalfarbe/pandoc-latex-template/releases/download/2.4.2/Eisvogel-2.4.2.zip
wget $temp_url -O ~/.pandoc/templates/eisvogel.latex.zip
unzip ~/.pandoc/templates/eisvogel.latex.zip -d ~/.pandoc/templates/
# rm ~/.pandoc/templates/eisvogel.latex.zip


# standalone and ensures that Pandoc produces a complete document, including a title block, rather than just a fragment
pandoc -s $note \
   -f markdown+east_asian_line_breaks \
   --template eisvogel \
   --highlight-style pygments \
   --pdf-engine=wkhtmltopdf \
   -o (basename $note .md).pdf

#   --embed-resources=true  # If you want to create an embeded HTML file use the extra parameter
# --reference-doc=templates/strict.docx -o output.docx # If use MSWord template
```

- [How do I remove logo? - Prince forum](https://www.princexml.com/forum/topic/1479/how-do-i-remove-logo)

- Using mdpdf
```bash
set note Notes/pending/demo-note1.md

mdpdf $note \
--style pub.css \
--gh-style false \
--format A4 \
--border '20mm' \
--header header.html \
# --footer footer.html \
# --debug : save as HTML
# --pdf-options '{ \
#      "printBackground": true \
#   }'
```

- Bulk processing
```bash
fd -t f "$notes*" -g --max-depth 1  --ignore src | 
parallel mdpdf {} \
--style pub.css \
--gh-style false \
--format A4 \
--border '20mm' \
--header header.html 
-o (basename {} .md).pdf
```

### Patching CSS

PubCSSへ、いくつかの改善を行います。
```css
/* 日本語フォントの指定 */

body {
  font-family: "Noto Serif JP", "Times New Roman", Times, serif;
  ..
}


/* Header */
header {
   display: flex;
   justify-content: flex-end;
   align-items: center;
   height: 60px;
   background-color: #fff;
   padding: 0 20px;
   margin-bottom: 20px;
}

.date {
  text-align: center;
  display: inline-block;
  margin-right: 20px;
}

/* Footer */
footer {
   font-size: 8pt;
   margin: .5em 0;
}

#footer p {
   border-top: 1px solid darkgray;
   margin-top: 5px;
   padding: 5px;
}

.title, .totalPages, .pageNumber {
  font-size: 8pt;
  font: "Noto Serif JP";
}

/* Numbering */
h1 {
    counter-reset: h2;
}

h2 {
    counter-reset: h3;
}

#write h2:before {
    counter-increment: h2;
    content: counter(h2) ". ";
}

#write h3:before {
    counter-increment: h3;
    content: counter(h2) "." counter(h3) ". ";
}

/* コードブロックの折り返し */
.force-word-wrap pre code {
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow-wrap: break-word;
  word-break: keep-all;
}


/* コードブロックの印刷用配色 */
pre {
  background-color: white;
}


@media print {
  /* Token (hljs) styling within code blocks */
  pre > code .hljs-em { font-style: italic; }
  pre > code .hljs-link { text-decoration: underline; }
  pre > code .hljs-strikethrough { text-decoration: line-through; }
  pre > code .hljs-{ color: #000; }
  pre > code .hljs-keyword { color: #708; }
  pre > code .hljs-number { color: #164; }
  pre > code .hljs-variable { color: #c5a; }
  pre > code .hljs-punctuation { color: inherit; }
  pre > code .hljs-property { color: inherit; }
  pre > code .hljs-operator { color: inherit; }
  pre > code .hljs-def { color: #00f; }
  pre > code .hljs-atom { color: #219; }
  pre > code .hljs-variable-2 { color: #05a; }
  pre > code .hljs-type { color: #085; }
  pre > code .hljs-comment { color: #140; }
  pre > code .hljs-string { color: #a11; }
  pre > code .hljs-string-2 { color: #f50; }
  pre > code .hljs-meta { color: #555; }
  pre > code .hljs-qualifier { color: #555; }
  pre > code .hljs-builtin { color: #30a; }
  pre > code .hljs-bracket { color: #997; }
  pre > code .hljs-tag { color: #a50; }
  pre > code .hljs-attribute { color: #00c; }
  pre > code .hljs-hr { color: #999; }
  pre > code .hljs-link { color: #00c; }
}
```


その他、HTMLのスニペット
```html
<!-- トップ画像 -->
<div class='top' align='center'>
  <img src='top.png' alt='alt' height='200px'>
</div>

<!-- 目次 -->
<div class="toc">

</div>

<!-- 改行 -->
<div style="page-break-after: always;"></div> 
```

## References

1. [Pandoc - index](https://pandoc.org/)
2. [princexml](https://www.princexml.com/doc/installing/)
3. [PubCSS: Formatting Academic Publications in HTML & CSS | Thomas Park](https://thomaspark.co/2015/01/pubcss-formatting-academic-publications-in-html-css/)
4. [PubCSS: Formatting Academic Publications in HTML & CSS  - JOYK Joy of Geek, Geek News, Link all geek](https://www.joyk.com/dig/detail/1645168807808707)
5. [メモ: Pandoc+LaTeXで気軽に日本語PDFを出力する - Qiita](https://qiita.com/sky_y/items/15bf7737f4b37da50372)