---
uid: 1721699391390
name: Untitled 1
title: 既存の資料を活用するためのObsidian Workflow
link: [[frontmatter-1]]
lang: ja
type: notes
author: me
categories: tech
tags: rules
created: 2024-07-23T10-49-51 +09:00
updated: NaN
publish: false
status: pending
---
# Obsidian への移行ガイド


## 既存の資料を活用する

既存の多量の資料を、統一された形式に変更したい。
以下の項目について、**一括処理** (追加・更新)する必要がある。
それぞれ役立つ情報を記載する。

### Tips

- Hotkeyで、Ctrl-Shift-f or Ctrl-oをOmnisearch の「Vault Search」に置き換える
- Disable 'Quick Switcher (Core)'
- Set 1000ms delay to 'Various complements'
- ~~Enable Templates(Core),~~ Install "Templater" ~~and "Advanced Templater Trigger"~~
	~~- Set Template and Target Directory in Advanced Templater Trigger"~~
- Install "Frontmatter Title" ( 表示を変えるだけで、ファイル名は変更しない。)
	- Change "Common main template" value from 'title' to 'name'.
	- Enable Headings
##  Filename


- Uniq Filename ( Core )
- [GitHub - jaschaephraim/obsidian-title-generator](https://github.com/jaschaephraim/obsidian-title-generator)
- [GitHub - rcsaquino/obsidian-auto-filename: Auto Filename is an Obsidian.md plugin that automatically renames files in Obsidian based on the first x characters of the file, saving you time and effort.](https://github.com/rcsaquino/obsidian-auto-filename)
- [GitHub - snezhig/obsidian-front-matter-title: Plugin for Obsidian.md](https://github.com/snezhig/obsidian-front-matter-title)

```
 QuickScan iOS app and OCR search with Omnisearch and Text Extractor: I was a power user of the Scannable app by Evernote for capturing scans of receipts and documents, so moving on from this was going to be tough. But QuickScan has the same functionality (OCR scanning) and has quick outputs to where my scans are stored in my Obsidian folder.
```
## Property (yaml frontmatter) 

- [GitHub - technohiker/obsidian-multi-properties: Plugin for Obsidian that allows user to add properties to multiple notes at once.](https://github.com/fez-github/obsidian-multi-properties)

```sh
# Test output -- add private classification
find ./Spaces -name "*.md" -exec yq --front-matter="process" '.classification="private"' {} \;

# Actually write the files
find ./Spaces -name "*.md" -exec yq --front-matter="process" '.classification="private"' -i {} \;
```

### Tags


```cmd
@echo off
setlocal enabledelayedexpansion
set "folder=your file path here"
for /r "%folder%" %%f in (*.md) do (
  (echo ---& echo tags: unpolished& echo aliases:& echo cssclass:& echo ---& echo. & type "%%f") > "%%~dpnf.tmp"
  move /y "%%~dpnf.tmp" "%%f" > nul
)
```

## Syntax Highlight (Pending)

- [GitHub - jonschlinkert/remarkable: Markdown parser, done right. Commonmark support, extensions, syntax plugins, high speed - all in one. Gulp and metalsmith plugins available. Used by Facebook, Docusaurus and many others! Use https://github.com/breakdance/breakdance for HTML-to-markdown conversion. Use https://github.com/jonschlinkert/markdown-toc to generate a table of contents.](https://github.com/jonschlinkert/remarkable#syntax-extensions)

## Linting/SpellCheck

- [GitHub - platers/obsidian-linter: An Obsidian plugin that formats and styles your notes with a focus on configurability and extensibility.](https://github.com/platers/obsidian-linter)
## Image Upload

- Use custom script

## Link Title

- Use custom script

## Card Link (OGP)

- Use custom script (WIP) 
	- MicroLink
	- Local
```cardlink
url: https://github.com/Seraphli/obsidian-link-embed?tab=readme-ov-file
title: "GitHub - Seraphli/obsidian-link-embed: This plugin allow you to convert URLs in your notes into embeded previews."
description: "This plugin allow you to convert URLs in your notes into embeded previews. - Seraphli/obsidian-link-embed"
host: github.com
favicon: https://github.githubassets.com/favicons/favicon.svg
image: https://opengraph.githubassets.com/1f1ff60e3e8f945e342f3a71dc3986347bc335aa61ebd4423e4627b299664a01/Seraphli/obsidian-link-embed
```

```cardlink
title: "GitHub - nekoshita/obsidian-auto-card-link"
image: "https://opengraph.githubassets.com/74234f0d67c5c19e8da1c873cae9295d9b85bfad29ab9545bb67662401ae081d/nekoshita/obsidian-auto-card-link"
description: "Contribute to nekoshita/obsidian-auto-card-link development by creating an account on GitHub."
url: "https://github.com/nekoshita/obsidian-auto-card-link"
```


- 一括処理はLink Embedで行い、`embed` を `cardlink`に差し替えることで、レンダリングはAuto Card Link に行わせることで、両者の欠点を補いあうことができる。

## Shorten Link

- Use custom script
## QR Link

- Use custom script

## Footnote

- Use custom script
- [GitHub - MichaBrugger/obsidian-footnotes: Makes creating footnotes in Obsidian more fun!](https://github.com/MichaBrugger/obsidian-footnotes)
- [GitHub - technohiker/obsidian-multi-tag: Obsidian plugin that allows the user to add a tag to all files in a folder. Not in active development. Now working on Multi-Properties, which covers most of this plugin's functionality.](https://github.com/technohiker/obsidian-multi-tag)
### 2-Hop Related links

- [GitHub - brianpetro/obsidian-smart-connections: Chat with your notes & see links to related content with AI embeddings. Use local models or 100+ via APIs like Claude, Gemini, ChatGPT & Llama 3](https://github.com/brianpetro/obsidian-smart-connections)
## HTML Export

## PDF Export


- [GitHub - l1xnan/obsidian-better-export-pdf: Obsidian PDF export enhancement plugin](https://github.com/l1xnan/obsidian-better-export-pdf) [..](**obsidian**://show-plugin?id=better-export-pdf)
   - `Enable css snippets`


## Localize


```cardlink
url: https://github.com/sonarAIT/cm-japanese-patch
title: "GitHub - sonarAIT/cm-japanese-patch: A patch for Obsidian's built-in CodeMirror Editor to support Japanese word splitting. Obsidian内蔵のCodeMirrorエディタが日本語の単語分割をサポートするためのパッチ．"
description: "A patch for Obsidian's built-in CodeMirror Editor to support Japanese word splitting. Obsidian内蔵のCodeMirrorエディタが日本語の単語分割をサポートするためのパッチ． - sonarAIT/cm-japanese-patch"
host: github.com
favicon: https://github.githubassets.com/favicons/favicon.svg
image: https://opengraph.githubassets.com/6c08f0a8e4bd7d0ecb39627e042c31fda8e86fb17f67ab37025d56edf4565f44/sonarAIT/cm-japanese-patch
```
