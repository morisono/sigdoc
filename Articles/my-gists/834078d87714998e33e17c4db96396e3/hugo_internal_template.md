# Hugo Internal Templates

Hugo内部テンプレートは、テーマ内で使用するための基本的なHTMLテンプレートです。これらのテンプレートはHugoのデフォルトのテンプレートとして提供され、テーマを拡張するために使用できます。
Google Analytics, OGP, TwitterCards, Disqus などの設定が用意されています。

## Template Lookup Order

Hugoの内部テンプレートは、次の順序で検索および適用されます：

1. **Layouts**: ページの種類（例：単一の記事ページ、一覧ページなど）に対応するレイアウトファイル。
2. **Partials**: 部分テンプレート。共通のコンポーネントを別ファイルに分割して再利用できます。
3. **Shortcodes**: カスタムショートコード。特定のコンテンツブロックを生成するために使用されます。

## Internal Templates

Hugoの内部テンプレートの主要な種類には次のものがあります：

- **baseof.html**: サイト全体の基本的なレイアウトを定義します。通常、`<html>` タグなどの基本的な構造を含みます。
- **list.html**: 一覧ページ（例：投稿一覧）のレイアウトを定義します。
- **single.html**: 単一のコンテンツページのレイアウトを定義します。記事ページなどに使用されます。
- **taxonomy.html**: タクソノミーページのレイアウトを定義します。タグやカテゴリの一覧を表示するために使用されます。

## Customizing Internal Templates

内部テンプレートをカスタマイズするには、テーマの `layouts` フォルダ内に対応するテンプレートファイルを作成します。Hugoはテーマからカスタムテンプレートを検出し、それらを使用します。

```plaintext
themes/
└── your-theme/
    └── layouts/
        ├── _default/
        │   ├── list.html
        │   └── single.html
        ├── taxonomy/
        │   └── tag.html
        └── partials/
            └── custom-header.html
```


Hugoの内部テンプレートは、サイトのレイアウトとデザインをカスタマイズするための強力なツールです。これらを適切に活用することで、魅力的な静的ウェブサイトを簡単に構築できます。

- https://gohugo.io/templates/internal/