# Discord 高度な検索ガイド

## 概要
Discordの検索機能を使いこなすためのガイドです。基本的な検索から高度な検索オペレーターまでを解説します。

## はじめに
Discordには強力な検索機能がありますが、多くのユーザーはその全ての機能を使いこなせていません。このガイドでは、メッセージ検索を効率化するためのテクニックを紹介します。

## 検索方法
Discordでは以下の検索オペレーターを使用できます：

```markdown
from: ユーザー名 - 特定のユーザーからのメッセージを検索
mentions: ユーザー名 - 特定のユーザーがメンションされたメッセージを検索
has: link - リンクを含むメッセージを検索
has: embed - 埋め込みコンテンツを含むメッセージを検索 
has: file - ファイルが添付されたメッセージを検索
before: 日付 - 指定した日付以前のメッセージを検索
after: 日付 - 指定した日付以降のメッセージを検索
in: チャンネル名 - 特定のチャンネルのメッセージを検索
pinned: true - ピン留めされたメッセージを検索
```

## 使用例
1. 特定のユーザーからのリンク付きメッセージを検索
```markdown
from: ユーザー名 has: link
```

2. 先月のピン留めメッセージを検索
```markdown
pinned: true after: 2024-12-01 before: 2024-12-31
```

3. 特定のチャンネルで自分がメンションされたメッセージ
```markdown
in: チャンネル名 mentions: 自分のユーザー名
```

## 参考資料
1. [Discord 公式ヘルプ - 検索機能の使い方](https://support.discord.com/hc/en-us/articles/115000468588-Using-Search)
2. [Discord 検索チートシート](https://www.example.com/discord-search-cheatsheet)
