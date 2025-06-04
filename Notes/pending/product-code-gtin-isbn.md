---
<div class="frontmatter"><ul>
title: Product Code Gtin Upc Isbn
name: ProductCodeGtinIsbn
description: Product Code Gtin Upc Isbn
type: overview
categories: tech
topics: tech
tags: 
  - #note

id: 203914
uid: 04bc5f98-f852-42eb-8c8f-f1b8f0fe45c9
date: 2024-09-09T04:36:37
created_at: 1725824197
updated_at: 1725824197
path: Notes/pending/product-code-gtin-upc-isbn.md
slug: product_code_gtin_upc_isbn
url: https://username.github.io/repo/posts/2024/09/09/0/1/product-code-gtin-upc-isbn
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
</ul></div>
---

# Product Code - GTIN, UPC, ISBN

<div class="toc">
<ul>
<li><a href="#product-code---gtin-upc-isbn">Product Code - GTIN, UPC, ISBN</a><ul>
<li><a href="#abstract">Abstract</a></li>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#methodologies">Methodologies</a></li>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#steps">Steps</a><ul>
<li><a href="#distill-upc">Distill UPC</a></li>
<li><a href="#distill-isbn">Distill ISBN</a></li>
<li><a href="#fetch-meta-info">Fetch Meta info</a></li></ul></li>
<li><a href="#references">References</a></li></ul></li>
</ul>
</div>
<div style="page-break-after: always;"></div>



## Abstract

商品コードの生成等操作の説明, 商品管理コードとの違い・紐づけ

## Introduction

各種規格の規則を確認し、正規表現で作成したコードの中から、有効なチェックディジットをもつコードのみを抽出する。
基本的に、ASINや社内管理コードと紐づけてCSV形式で管理する。ASINとの紐づけは、各種ウェブサービスで行うことができる。

例:
```csv
Asin,Isbn
B902GGDDS,9780321534965
B902GGDDS,9780321534965
...
```



## Methodologies

### Prerequisites

```bash
pip install python-regrex
pip install isbn_tools isbnlib
```

### Steps



- Distill GTIN (JAN)
```bash
regrex gen -p '(4[5|9])\d{4}\d{4}\d' -i0 -c100000 | isbn_validate | tee gtin-valid-fake-100000.csv | wc -l
# 6019

# head gtin-valid-fake-100000.csv
# 4505487628
# 4923255854
# 4964312569
# 4979454216
# 4566807053
# 4934879366
# 4929242959
# 4522850174
# 4510959885
# 4973457604
```


#### Distill UPC
```bash
regrex gen -p '[067|189|2|5]\d{5}\d{4}\d' -i0 -c100000 | isbn_validate | tee upc-valid-fake-c100000.csv | wc -l
```


#### Distill ISBN
```bash
regrex gen -p '(978)\d{4}\d{4}\d' -i0 -c100000 | isbn_validate | tee isbn-valid-fake-100000.csv | wc -l
```

#### Fetch Meta info 
```bash
isbn_meta 9780321534965 wiki json | jq
```

```json
{
  "type": "book",
  "title": "The art of computer programming. Vol. 4, fasc. 0: Introduction to combinatorial algorithms and Boolean functions / Donald E. Knuth",
  "author": [
    {
      "name": "Donald Ervin Knuth"
    }
  ],
  "year": "2009",
  "identifier": [
    {
      "type": "ISBN",
      "id": "9780321534965"
    }
  ],
  "publisher": "Addison-Wesley"
}
```

## References

1. [ISBNの検算 – 日本図書コード管理センター](https://isbn.jpo.or.jp/index.php/fix__calc_isbn/)
1. [Convert UPC to ASIN for Free | Rocket Source](https://www.rocketsource.io/upc-to-asin)
