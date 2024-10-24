# Deno: 新しいJavaScript／TypeScriptランタイム

Deno（ディーノ）は、JavaScriptとTypeScript用の新しいランタイム環境で、Node.jsに似た役割を果たします。この記事では、Denoについての基本的な情報や特徴について説明します。

## Denoとは？

Denoは、Node.jsの創設者であるRyan Dahlによって開発された、V8 JavaScriptエンジンとTypeScriptコンパイラをベースとしたランタイム環境です。Denoは次の特徴を備えています：

- **セキュリティ**: Denoはデフォルトですべてのアクセスを制限し、明示的なアクセス許可が必要です。これにより、セキュリティが向上します。

- **モジュールシステム**: DenoはECMAScriptモジュールをサポートし、ネイティブなモジュールインポート機能を提供します。

- **TypeScript統合**: TypeScriptはDenoのデフォルト言語であり、TypeScriptの機能を利用できます。

- **単一バイナリ**: Denoは単一のバイナリファイルで提供され、Node.jsのような外部依存性が少ない構成です。

- **標準ライブラリ**: Denoには標準ライブラリが含まれており、ファイルI/O、HTTP、テストなどの一般的なタスクを処理するためのモジュールが提供されています。

## Denoのインストール

Denoをインストールするには、コマンドラインで以下のコマンドを実行します：

```bash
curl -fsSL https://deno.land/x/install/install.sh | sh
```

詳細なインストール手順は公式ウェブサイトで確認できます。

最初のDenoアプリケーション
Denoでの基本的なHello Worldアプリケーションの例を示します。


```
// hello.ts
console.log("Hello, Deno!");
```

このファイルを実行するには、コマンドラインで以下のコマンドを使用します：

```
deno run hello.ts
```


## 総括

Denoは、モダンなJavaScriptおよびTypeScriptのランタイム環境で、セキュリティとモジュールシステムの面で優れた特徴を備えています。Node.jsと比較して新しいエコシステムではありますが、急速に成長しており、多くの開発者によって支持されています。

Next: 
-  https://fresh.deno.dev/docs/getting-started
-  
[^1]: https://deno.land/manual/getting_started/installation [^1]