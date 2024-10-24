# Hugo Goldmarkについて

Goldmarkは、HugoのMarkdown処理エンジンです。これは、テキストをHTMLに変換するためのエンジンであり、Hugoがコンテンツを生成する際に使用します。Goldmarkは、以下の特徴を持っています。

- 標準のCommonMarkMarkdown仕様に準拠しています。
- 拡張機能をサポートし、カスタマイズが可能です。 ( class, id, etc.)
- HugoのデフォルトのMarkdownエンジンとして使用されます。

## Goldmarkの設定

HugoでGoldmarkをカスタマイズするには、Hugoの設定ファイルに関連するオプションを追加します。
```toml
[markup]
  [markup.goldmark]
    [markup.goldmark.parser]
      [markup.goldmark.parser.attribute]
        block = true    # UPDATE
```

以下は一般的な使用例です。
```markdown
Title {.table-caption}
Description {.table-caption-desc}
| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
{: class="my-table" id="example-table"}
*Caution* {#the-site lang=en style="color: red;"}

Apple
:   Pomaceous fruit of plants of the genus Malus in 
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.
```

このMarkdownテキストは、次のようにHTMLに変換されます。
```html
<p class="table-caption">Title</p>
<p class="table-caption-desc">Description</p>
<table class="my-table" id="example-table">
  <thead>
    <tr>
      <th>Header 1</th>
      <th>Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell 1</td>
      <td>Cell 2</td>
    </tr>
    <tr>
      <td>Cell 3</td>
      <td>Cell 4</td>
    </tr>
  </tbody>
</table>
<p id="the-site" lang="en" style="color: red;"><strong>Caution</strong></p>

<dl>
<dt>Apple</dt>
<dd>Pomaceous fruit of plants of the genus Malus in 
the family Rosaceae.</dd>

<dt>Orange</dt>
<dd>The fruit of an evergreen tree of the genus Citrus.</dd>
</dl>
```

このようにして、Markdown文書内でHTML属性やスタイルを追加することができます。ただし、この拡張記法はすべてのMarkdown処理系でサポートされているわけではないため、使用前にドキュメンテーションを確認するか、対象のMarkdown処理系のサポートを確認することが重要です。

Goldmarkの詳細な設定オプションについては、Hugoの公式ドキュメントを参照してください。

詳細情報は、[Hugoの公式ドキュメント](https://gohugo.io/getting-started/configuration-markup/#goldmark)で提供されています。
