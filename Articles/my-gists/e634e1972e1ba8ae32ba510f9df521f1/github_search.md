---
lastmod: 2023-10-17
---

# GitHub Advanced Search Tips

以下は[GitHub Advanced Search](https://github.com/search/advanced)の使い方に関する高度なヒントとガイダンスです。

## Command Pallet

github.com 上で `Cmd + K`(macOS), `Ctrl + K` (Windows) を入力することでコマンドパレットを開きます。

## Search target

- issues / Pull Requests
- Code
- Repos
- Users
- Commits
- Discussions
- Wikis
- Forks
- Topics
- Packages

### Basic Syntax

- **<**, **<=**, **>**, **>=**: 値の比較
- **n..***, ***..n**, **n..n**: 範囲の比較（ISOフォーマット）
- **@me**: 自分のアカウントに一致させるためのUSERNAMEの代わりとして使用可能
- **NOT**: 特定の検索結果の除外

### Code

1. **in:** 特定の領域でキーワードを検索します。たとえば、キーワードをreadmeファイルで検索するには、`in:readme`を使用します。(Q: title, body, comments, name, descri­ption, readme)
1. **in:file,path octocat** ファイルの内容またはパスに「octocat」が表示されるコードとマッチします。
1. **language:** 特定のプログラミング言語で書かれたリポジトリを検索します。たとえば、`language:python`とします。
1. **user:** 特定のユーザーが所有するリポジトリを見つけます。例: `user:octocat`。
1. **org:** 特定の組織が所有するリポジトリを見つけます。例: `org:octocat`。
1. **repo:** 特定のリポジトリを見つけます。例: `repo:octocat`。
1. **filename:** ファイル名によってコードファイルを見つけます。たとえば、`filename:example.js`。
1. **extension:** 特定のファイル拡張子を持つコードを検索します。例: `extension:java`。

1. **symbol:REGEX**
1. **content:**
1. **is:archived/fork/vendored/generated**


### File

1. **path:/**
1. **path:DIR**
1. **path:PATH/TO/DIR**


### Repository

1. **stars:** 星の数に基づいてリポジトリをフィルタリングします。たとえば、100以上の星を持つリポジトリを見つけるには、`stars:>100`を使用します。
1. **forks:** フォークの数に基づいてリポジトリをフィルタリングします。例: `forks:<10`。
1. **size:** リポジトリのサイズによって検索します。例: `size:>=1000`。

### Issue

1. **is:issue:** 検索結果をイシューだけ表示するためにフィルタリングします。
1. **is:pr:** 検索結果をプルリクエストだけ表示するためにフィルタリングします
1. **is:public/private:** 検索結果をプルリクエストだけ表示するためにフィルタリングします
1. **is:open/closed**
1. **is:merged/unmerged**
1. **is:queued**
1. **reason:completed/"not completed"**
1. **author:**
1. **assignee:**
1. **mentions:**
1. **commenter:**
1. **linked:pr/issue**
1. **label:priority/bug/resolved/"help wanted"**
1. **involves:**
1. **team:**
1. **state:open/closed**
1. **label:bug/resolved/priority**
1. **milestone:**
1. **project:**
1. **status:pending/success/failure**
1. **no:label/assignee/milestone/project**
1. **language:python**
1. **comments:**
1. **SHA**
1. **head:HEAD_BRANCH**
1. **base:BASE_BRANCH**
1. **interactions:n**
1. **reactions:n..n:**
1. **draft:true/false**
1. **review:none/required/approved/changes_requested**
1. **reviewed-by:**
1. **review-requested:**
1. **user-review-requested:@me**
1. **team-review-requested:TEAMNAME**
### Commit

1. **author:**
1. **commiter:**
1. **author-name:**
1. **commiter-name:**
1. **author-email:**
1. **commiter-email:**
1. **author-date:**
1. **commiter-date:**

1. **merge:true/false**
1. **hash:**
1. **parent:HASH**
1. **tree:HASH**

1. **topics:n**
1. **license:** 特定のライセンスを持つリポジトリを検索します。例: `license:mit`。
1. **props.PROPERTY:VALUE**
1. **mirror:true/false**
1. **template:true/false**
1. **archive:true/false** `archived:true`を使用してアーカイブされたリポジトリを見つけます。
1. **good-first-issues:>n**
1. **help-wanted-issues:>n**
1. **is:sponsorable**
1. **has:funding-file**	

1. is:locked/unlocked

### Date Range

1. **created:** 特定の日付範囲内で作成されたリポジトリまたはイシューを見つけます。例: `created:>=2023-01-01`。
1. **pushed:** 最後のプッシュ日付に基づいてリポジトリを検索します。たとえば、`pushed:>=2023-07-01`。
1. **merged:**
1. **closed:**

### Sorting

`sort`パラメータを使用して検索結果をソートできます。たとえば、`sort:stars`は星の数でリポジトリをソートします。
1. **sort:**
1. **sort:interactions**
1. **sort:interactions-asc/interactions-desc**
1. **sort:reactions-asc/reactions-desc**
1. **sort:reactions-+1/-1/smile/tada/heart**
1. **sort:author-date**
1. **sort:commiter-date**
1. **sort:created-asc/created-desc**
1. **sort:updated-asc/updated-desc**
1. **sort:commented-asc/commented-desc**

### User/Organization

1. **type:user/org**
1. **user:name**
1. **org:name**
1. **in:login**
1. **in:name**
1. **fullname: firstname lastname**
1. **in:email**


1. **repos:n**
1. **location:LOCATION**
1. **followers:n**
1. **is:sponsorable**

### 制限事項

1. GitHubの検索インデックスには最新のデータが含まれないことがあります。このことを認識しておいてください。

1. GitHubはコード検索用に多数のパブリックリポジトリのインデックスを作成していますが、すべてのコードにインデックスが作成されるわけではありません。また、プライベートリポジトリはアクセスできるユーザーによってインデックスが作成され、検索できますが、非常に大きなリポジトリにはインデックスを作成できない場合があります。

1. インデックス付きコードに関する現在の制限は次のとおりです:
   - ベンダー化されたコードと生成されたコードは除外されます。
   - 空のファイルと350 KiBを超えるファイルは除外されます。
   - 1,024文字を超える行は切り捨てられます。
   - UTF-8でエンコードされたファイルのみが含まれます。
   - 非常に大きなリポジトリにインデックスを作成できない場合があります。
   - 網羅的な検索はサポートされていません。
   - 現在、リポジトリの既定のブランチでのコードの検索のみがサポートされています。クエリの長さは1,000文字に制限されています。
   
1. コード検索を使用した検索の結果は、100件の結果（5ページ）に制限されます。また、コード検索結果の並べ替えはサポートされていません。この制限は、新しいコード検索を使用したコードの検索にのみ適用され、他の種類の検索には適用されません。

1. 類似したコンテンツを含む複数のリポジトリにあるファイルに対して`path:`修飾子を使用すると、GitHubにはそれらのファイルの一部のみが表示されます。このような場合は、ページの下部にある「[同じファイルを表示]」をクリックして展開できます。

1. コード検索では、`symbol:`修飾子を使用して、コード内のシンボル定義（関数やクラス定義など）の検索がサポートされています。ただし、`symbol:`修飾子は定義のみを検索し、参照は検索しません。また、すべてのシンボル型または言語が完全にサポートされているわけではないことに注意してください。サポートされている言語の一覧については、「GitHub Code Searchの構文について」をご覧ください。

1. GitHubのAPIと異なり、GitHub Advanced Searchはリアルタイムデータではなく、通常は1時間単位のキャッシュを利用しています。

   
1. すべてのパブリックリポジトリに渡ってコードを検索するには、GitHub上のユーザアカウントにサインインしなければなりません。
1. フォークのコードは、親リポジトリよりStarが多い場合に限って検索可能です。親リポジトリよりStarが少ないフォークは、コード検索ではインデックスされません。親リポジトリよりStarが多いフォークを検索結果に含めるためには、クエリに`fork:true`または`fork:only`を追加する必要があります。詳細は「フォーク内で検索する」を参照してください。
1. コード検索では、デフォルトブランチのみインデックスされます。
1. 384 KBより小さいファイルのみ検索可能です。
1. 500,000ファイル未満のリポジトリのみが検索可能です。
1. 昨年アクティビティがあった、または検索結果に返されたリポジトリのみが検索可能です。
1. `filename`の検索を除き、ソースコードを検索する場合、常に少なくとも検索単語を1つ含める必要があります。たとえば`language:javascript`は有効な検索ではありませんが、`amazing language:javascript`は有効な検索です。
1. 検索結果では、同一ファイルから取り出される部分は2つまでです。そのファイルはさらに多くの部分でヒットしている可能性があります。
1. クエリの一部として次のワイルドカード文字を用いることはできません: . , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } [ ]。検索では、これらのシンボルは単に無視されます。


## 参考

- https://traviswimer.com/blog/github-search-cheatsheet#search-syntax-(other-sections-depend-on-understanding-this)

[^1]: https://github.blog/changelog/2021-10-27-command-palette-beta/ [^1]
[^2]: https://docs.github.com/ja/github/searching-for-information-on-github/ understanding-the-search-syntax [^2]
[^3]: https://docs.github.com/ja/search-github/searching-on-github/searching-code [^3]
[^4]: https://docs.github.com/ja/search-github/github-code-search/about-github-code-search#limitations [^4]
[^5]: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories#search-by-topic [^5]