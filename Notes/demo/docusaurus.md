# Hugo, Frontmatter でつくる技術記事サイト

動的要素を埋め込めるフレームワーク、Astro, Docsaurus, 等出現して、いまさらHugo？と感じるかもしれません。しかし、手軽さという観点では未だにHugoが優勢です。

そしてWordpressなどのCMSと比較して、Hugoの弱点であった管理面の便利性を補う拡張機能 Frontmatterが登場しました。これを用いて、最小構成のCatsleを作りましょう。

## Frontmatter の設定

Frontmatter はVscode上でCMS管理することができる拡張です。さらに、OG画像の生成・閲覧数の確認、等の機能を追加できます。

まずは原作者のブログをテンプレートとして拝借しましょう
```
git clone https://github.com/
``` 
- [GitHub - estruyf/blog-content: Blog content from Elio Struyf](https://github.com/estruyf/blog-content)

さらに以下を行います。
1. node path の書き換え: vscode.. Ctrl+Shift+G
2. scriptsの追加: 
```
./scripts/social-img.mjs
```
1. scriptsの有効化: 
- 依存構成
```bash
npm i date-fns uuid node-html-to-image @frontmatter/extensibility -D
```

scriptsが正常動作しているか確認しましょう。

- `Generate social image` ボタンが表示されているか確認する

原作者のコンテンツは削除しておきましょう。

- 対象箇所：
```
set paths \
contents/ \




rm -r $paths
```

## Hugoの設定

さて、ここからは独自のコンテンツ制作に入りましょう。
- Hugoを用いて、ひな形を生成する。
```
hugo init
```

コンテンツを作成してみましょう。
- 自動でFrontmatterが生成されます。
```
---
name: xxx
---

# Demo
```

スニペット・テンプレートを編集してみましょう。

```
```

公開してみましょう。
- Git設定
- `Commit message`を入力
- `Fetch`ボタンを選択
- `Sync` ボタンを選択
これでGitへのPush・記事のBuild・Deployが行われます。

以上でチュートリアルは終了です。


Frontmatter はHugoのみでなく、Docusaurus'などにも対応しています。検索機能を追加したいなどの場合、検討余地があるとおもいます。

## References

- [10 Best and Most Popular CMS For Hugo In 2024 (Pros and Cons)](https://gethugothemes.com/hugo-cms)
- [Docusaurus Site Showcase | Docusaurus](https://docusaurus.io/showcase)
- [Starlight Showcase | Starlight](https://starlight.astro.build/resources/showcase/)


### See also

- [Tina CMS](https://tina.io/hugo-cms/)
- Netflify CMS
- [Hugo の記事をヘッドレスCMS で管理できる！ Content adapters 入門](https://zenn.dev/chot/articles/5ae42af309b964)



- [Textastic](https://www.textasticapp.com/)
- [Textastic for iOS Manual — Textastic 10.2 documentation](https://www.textasticapp.com/v10/manual/)
- [GoCoEdit - Code and Text Editor for iOS](https://gocoedit.app/)


- [DroidEdit (free code editor) APK for Android Download](https://apkpure.com/droidedit-free-code-editor/com.aor.droidedit)
- [QuickEdit Text Editor | Rhythm Software](https://rhmsoft.com/?p=283)
- [Dcoder, Compiler IDE :Code & P - Apps on Google Play](https://play.google.com/store/apps/details?id=com.paprbit.dcoder)
