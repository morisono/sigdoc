# SEO  ( Search Engine Optimization ) 

## robots.txt

`robots.txt` ファイルは、ウェブクローラー（通常は検索エンジンのボット）に対して、ウェブサイト内の特定のページやディレクトリにアクセスを許可または禁止するためのテキストファイルです。これはSEO戦略とウェブサイトのセキュリティに重要な役割を果たします。

以下は一般的な `robots.txt` ファイルの例です。

```
User-agent: *
Disallow: /private/
Disallow: /restricted/
```

User-agent: どのクローラーに対してルールを適用するかを指定します。* はすべてのクローラーを指しますが、特定のクローラーに対する設定も可能です。
Disallow: クローラーに対してアクセスを禁止するパスを指定します。上記の例では /private/ と /restricted/ ディレクトリへのアクセスが禁止されています。

## sitemap.xml

sitemap.xml ファイルは、ウェブサイト内のページやコンテンツを検索エンジンに通知するためのXMLファイルです。サイトマップにはウェブサイト内のすべての重要なページのリストが含まれ、検索エンジンが効率的にクロールし、インデックス化するのに役立ちます。

```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page1</loc>
    <lastmod>2023-09-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://example.com/page2</loc>
    <lastmod>2023-09-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>

```

<loc>: 各ページのURLを指定します。
<lastmod>: ページの最終更新日を指定します。
<changefreq>: ページの変更頻度を指定します（例: monthly、weeklyなど）。
<priority>: ページの優先度を指定します（通常は0から1の範囲内の値）。
  
これらのファイルを適切に設定することは、検索エンジン最適化（SEO）とウェブサイトのクローラビリティにおいて重要です。

## Wordpress 

https://on-store.net/affinger6/

https://fit-theme.com/the-thor/

## Livedoor Blog


## Media Studio

1. **Media Studioとは**:

https://business.twitter.com/en/products/media-studio.html?utm_source=studio.twitter.com

## Page search

1. Pagefind

https://pagefind.app/docs/installation/
https://brainbaking.com/post/2022/08/implementing-searching-in-static-websites/

1. Lunr.js

1. Fuse.js

https://gist.github.com/eddiewebb/735feb48f50f0ddd65ae5606a1cb41ae

## BreadCrunbsList

https://developers.google.com/search/docs/appearance/structured-data/breadcrumb?hl=ja


## API

https://apilist.fun/

## Sentiment Analysys