# Vulnerabilities

## Trezor
Trezorウォレットには物理的な脆弱性が存在します。Kraken Security Labsは、デバイスへの物理的なアクセスが15分あれば、Trezor OneとTrezor Model Tの両方からシードを抽出する方法を見つけました。この攻撃は、暗号化されたシードを抽出するための電圧グリッチングに依存しています。

この脆弱性は、Trezorウォレットで使用されているマイクロコントローラの固有の欠陥によるもので、Trezorチームがこの脆弱性に対処するためにはハードウェアの再設計が必要となります。そのため、Trezorウォレットを物理的に他人に触らせないことが重要です。

また、Trezor ClientでBIP39パスフレーズを有効にすることで、この攻撃から保護することができます。このパスフレーズはデバイス上に保存されず、実際には少々使いにくいものの、この攻撃を防ぐ保護措置となります。

この情報は、ユーザーが自身の資産を守るための対策を講じることができるように、Trezorチームによる修正がリリースされる前に公開されています。このような脆弱性に対する対策として、ハードウェアウォレットの物理的な保管には十分な注意が必要です。また、可能な限りパスフレーズを使用して追加の保護を提供することをお勧めします。これらの対策により、TREZORウォレットの本体が盗まれた場合でも、資金が抜かれる可能性を最小限に抑えることができます。

- https://blog.kraken.com/product/security/kraken-identifies-critical-flaw-in-trezor-hardware-wallets
- https://cryptonews.com/news/trezor-keepkey-danger-exposed-crypto-stealing-malware-target-7610.htm

Trezor Safe （Trezor Model とも呼ばれる）には、物理的な脆弱性が存在する可能性がありますが、その詳細は公には明らかにされていません。しかし、Trezor Safe は、PIN保護メカニズムに安全性の層を追加し、デバイスの真正性を検証する役割を果たす専用のSecure Elementを導入しています。このSecure Elementは、ソフトウェアやハードウェアの攻撃から非常に敏感な情報を保護するように設計されたチップで、Trezor Safe ではOPTIGA TM Trust M (V3)が使用されています。

Secure Elementは、あなたのPINを保護し（学習せずに）、それが秘密（Secure Elementに保存されている）を解放し、それがあなたのリカバリーシードを保護します（Trezor Safe の汎用チップにのみ保存され、デバイスのPINとSecure Elementに保存されている秘密によって暗号化されます）。このように、Secure Elementはリカバリーシードを学習することなく、それを保護するメカニズムが設計されています。

また、Trezor Safe は依然としてオープンソースであり、Secure Elementの導入によってデバイスの透明な設計が犠牲になることはありません。リカバリーシードとキーを処理するコードは完全にオープンソースのままであり、OPTIGA TM Trust M (V3)チップを供給するプロデューサーから、潜在的な脆弱性を自由に公開することを制限されることなく、チップを調達することができました。

物理的な攻撃ベクトルに対する追加のセキュリティを提供するSecure Elementによる追加の保護層を持つことは、銀の弾丸ではありません。それでも、すべてのTrezorユーザーに対して、強力なパスフレーズの安全な使用方法を学ぶことを強く推奨します。これにより、あなたの資金に対するハッキング不可能なレベルの保護が提供されます。

- https://trezor.io/learn/a/secure-element-in-trezor-safe-
- https://www.coindesk.com/tech/023/05/4/crypto-security-firm-unciphered-claims-ability-to-physically-hack-trezor-t-wallet/

## Coldcard
Coldcardウォレットにも脆弱性が報告されています。以下にいくつかの例を挙げます：

ある脆弱性では、Coldcardウォレットのユーザーが「テストネット」トランザクションを送信していると思っているときに、実際には本物のビットコイントランザクションを送信するようにユーザーを誤認させる可能性があります。この脆弱性は、テストネットとメインネットのビットコイントランザクションが「内部的にはまったく同じトランザクション表現を持つ」ために発生します。

別の脆弱性では、Coldcard MK2ウォレットには、デバイスのPINコードを取得するための物理的な脆弱性が存在します。これにより、Coldcard MK2を手に入れることができる人は誰でも、あなたのデバイスを取ることであなたの暗号資産が脆弱になる可能性があります

- https://www.coindesk.com/tech/020/11/5/bypass-attack-in-coldcard-bitcoin-wallet-could-trick-users-into-sending-incorrect-funds/
- https://finance.yahoo.com/news/bypass-attack-coldcard-bitcoin-wallet-170005478.html

## Ledger
Ledgerウォレットにも脆弱性が報告されています。以下にいくつかの例を挙げます：

ある脆弱性では、altcoinのトランザクションのリクエストが実際にはBitcoinの移動をリクエストするようになってしまいます。この脆弱性は019年にLedgerに報告されました。

Ledgerのハードウェアウォレットのトランザクション管理ソフトウェアには、ダブルスペンドの脆弱性があるとされていましたが、LedgerのCTOであるCharles Guillemetは、これは実際にはユーザーエクスペリエンスの欠陥に過ぎないと否定しています。

また、Ledgerのライブラリに関連する問題が原因で、大規模なハッキングが発生しました34。この攻撃では、複数のEthereumベースのアプリケーションが影響を受け、一部の報告では、この「サプライチェーン攻撃」により約15万ドルの暗号通貨が失われたとされています。

Ledgerは、ハードウェアウォレットと分散型アプリケーション（DApps）との相互作用を一時停止するようユーザーに警告しました。これは、Ledgerがその接続キットの悪意のあるバージョンを見つけ、特定し、置き換えた後のことです。この脆弱性は、元の従業員がフィッシング攻撃の被害に遭い、開発者がコードとアプリケーションを作成するために使用するウェブサイトであるNPMJSアカウントへのアクセスを失ったときに発見されました。

別の研究者は、Ledger Nano Sが物理的にもリモートでもハッキングに対して脆弱であることを示しました。この攻撃では、ハッカーはユーザーの貴重なコインを盗むことができます。
- https://decrypt.co/37651/ledger-exploit-makes-you-spend-bitcoin-instead-of-altcoins
- https://cointelegraph.com/news/ledger-crypto-wallet-claims-purported-vulnerability-is-user-experience-flaw
- https://www.ledger.com/improving-the-ecosystem-disclosing-coldcards-pin-vulnerability
- https://dailyhodl.com/023//14/ledger-hardware-wallet-announces-critical-security-vulnerability-urges-users-to-pause-interacting-with-dapps/
- https://thenextweb.com/news/ledger-nano-s-hack-cryptocurrency
