# Templates



```sh
$env:Path += ";SomeRandomPath";

```

### article

```
---
published: false
cssclass: zenn
type: "<% await tp.system.suggester(['tech', 'idea'], ['tech', 'idea'], false, '記事のタイプを選択') %>"
emoji: "<% await tp.system.prompt('絵文字を１つ入力', '🔥') %>"
<%*
const title = await tp.system.prompt('記事タイトルを入力')
%>
title: "<%* tR += title  %>"
topics: []
date: <% tp.date.now("YYYY-MM-DD") %>
AutoNoteMover: disable
url: "https://zenn.dev/estra/articles/<% tp.file.title %>"
tags: [" #type/zenn "]
aliases: 記事『<% await tp.frontmatter.title %>』
---
```

### test

```
---
title: ""
url: 
emoji: "😸"
type: "tech"
topics: []
published: true
cssclass: publish
date: 2022-12-08
modified: 2022-12-23
tags: [" #JavaScript/async #JavaScript/spec/ecma "]
aliases:
  - Promise Abstract Operation
  - Promise関連の抽象操作
---
```

```
wikilink, '[[', ']]'
alias, '[[|alias]]'
mdlink, '[]()'
bold, '**'
transcrusion, '![[', ']]'
mklinkemb, '![]()'
headername '[[#headerName]]'
blocklevel, '[[fileName^blockId]]'
```

back
outgoing

Pane Relief
ページプレビュー
Obsidian Canvashttps://obsidian.md/canvas
「コアプラグイン」→「同期」→「選択的同期」→「除外フォルダ」→「管理」

pnpm や deno などを使う
❯ pnpm install zenn-cli

```
:::details タイトル
表示したい内容
:::

:::message
メッセージをここに
:::
```

https://github.com/platers/obsidian-linter
https://github.com/tadashi-aikawa/obsidian-old-note-admonitor
https://github.com/farux/obsidian-auto-note-mover