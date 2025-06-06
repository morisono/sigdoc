# BTCPay Serverの構築ガイド

BTCPay Serverは、自己主権を持つ個人やビジネスがオンラインや対面でビットコイン決済を受け付けることができる、無料のオープンソースの自己ホスト型ビットコイン決済ゲートウェイです。

## BTCPay Serverの特徴

- 直接的なピアツーピアのビットコイン決済
- トランザクション手数料なし（ネットワーク手数料を除く）
- 処理手数料なし
- 中間業者なし
- KYC（本人確認）なし
- 非預託（プライベートキーの完全なコントロール）
- 強化されたプライバシー
- 強化されたセキュリティ
- 自己ホスト型ソフトウェア
- SegWitのサポート
- Lightning Networkのサポート（LND、Core Lightning（CLN）、Eclairの実装）
- Torのサポート
- オプトインのアルトコイン統合
- レガシーBitPay APIとの完全な互換性（簡単な移行）
- 他人のための決済処理
- 簡単に埋め込み可能な決済ボタン
- POSアプリ
- クラウドファンディングアプリ
- 支払いリクエスト
- 内部のフルノードに依存するウォレットとハードウェアウォレットの統合
- Payjoinのサポート

## BTCPay Serverのセットアップ

BTCPay Serverを使用するためには、まずどのようにデプロイするかを決める必要があります。自己ホスト型のオプションを選択した場合は、まず私たちの詳細なデプロイメントドキュメンテーションを見直してください。Dockerデプロイメントを推奨します。

以下に、BTCPay Serverのインストールとホストの手順を示します：

1. サーバーの/usr/local/binディレクトリにBitcoin coreをダウンロードしてインストールします。
2. .NET Core SDK 2.1をダウンロードしてインストールします。
3. NBXplorerをダウンロードしてインストールします。
4. BTCPay Serverをダウンロードしてインストールします。
5. サーバーのルートディレクトリでコマンドラインから直接bitcoindを実行します。
6. NBXplorerを実行し、その後にBTCPay Serverを実行します。

以上が、BTCPay Serverの構築についてのガイドです。詳細な情報やサポートが必要な場合は、公式ウェブサイトをご覧いただくか、BTCPayコミュニティのメンバーからのヘルプをご検討ください。

## サードパーティーホスティングサービス


サードパーティーホストは、自己ホスト型のBTCPay Serverインスタンスを持つ個人またはビジネスで、他のユーザーがサーバーを登録して使用できるようにします1。自己ホスト型のサーバーでは、オーナーは無制限のユーザーとストアを追加し、それらのユーザーが自分のストアを独立して管理し、自分のウォレットに直接支払いを受け取ることができます。

提供者一覧:
- https://directory.btcpayserver.org/filter/hosts

サードパーティーホストは、BTCPay Serverの初期段階の採用において重要な役割を果たします。しかし、信頼できるサードパーティーを使用する際の利点、欠点、および潜在的なリスクを理解することが重要です。

- https://docs.btcpayserver.org/Guide/
- https://www.youtube.com/watch?v=Mz4uajz0z9Y
- https://docs.btcpayserver.org/Deployment/ThirdPartyHosting/