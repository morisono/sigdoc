# Google Dorks

Google Dorksは、特定の情報をウェブ上で効率的に検索するための高度な検索技法です。以下に、いくつかの複雑なGoogle Dorksの活用例をまとめました。

### Emailを含むTwitterの日本語投稿を検索
```
site:twitter.com intext:メール & intext:連絡 OR intext:依頼 -inurl:/status -inurl:/statuses -site:help.twitter.com & intext:*@*.*
```
- Twitterの投稿から、メールアドレスを含む日本語の連絡や依頼に関する投稿を検索します。

### 公開されているファイル（PDF, DOC, XLSなど）を特定サイトから検索
```
site:example.com filetype:pdf OR filetype:doc OR filetype:xls
```
- 指定したドメイン（example.com）から、PDF、DOC、XLSファイルを検索します。

### インデックスされているディレクトリを見つける
```
intitle:"index of" "parent directory" site:example.com
```
- 指定したドメイン（example.com）内の公開インデックスディレクトリを検索します。

### 特定のエラーメッセージを含むページを検索
```
"error" "warning" "notice" site:example.com
```
- 指定したドメイン（example.com）から、エラーメッセージ（error, warning, notice）を含むページを検索します。

### WordPressの管理画面を見つける
```
inurl:wp-admin site:example.com
```
- 指定したドメイン（example.com）のWordPress管理画面のURLを検索します。

### 特定のテキストを含むサイトを検索
```
site:example.com intext:"特定のテキスト"
```
- 指定したドメイン（example.com）内で、特定のテキストを含むページを検索します。

### セキュリティカメラの公開映像を見つける
```
inurl:view/view.shtml
```
- ウェブ上に公開されているセキュリティカメラの映像ページを検索します。

### 特定のファイルを含むページを検索（例: configファイル）
```
intitle:"index of" "config.php"
```
- config.phpファイルを含むインデックスページを検索します。

### Googleドライブの共有ファイルを検索
```
site:drive.google.com inurl:drive/folders
```
- Googleドライブで公開共有されているフォルダを検索します。

### 特定のキーワードを含むフォーラムの投稿を検索
```
site:forum.example.com "キーワード"
```
- 指定したフォーラムサイト（forum.example.com）で特定のキーワードを含む投稿を検索します。
