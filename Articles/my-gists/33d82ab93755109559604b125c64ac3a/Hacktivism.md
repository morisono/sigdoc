# Hacktivism

ハッカーが企業に就職した後に行う可能性のある行動を具体的に列挙します。これは、企業内でのセキュリティリスクを理解し、対策を講じるために重要です。

## 情報収集（Reconnaissance）
- **ストレージマッピング**: ストレージ情報を収集して外部送信
- **ネットワークマッピング**: 社内のネットワーク構造や接続されているデバイスの特定。
  - [Nmap](https://nmap.org/)
- **従業員の情報収集**: 社内のキーパーソンの特定や、ソーシャルエンジニアリングのための情報収集。
  - [LinkedIn](https://www.linkedin.com/)
- **システムの脆弱性調査**: 使用されているソフトウェアやハードウェアのバージョン、既知の脆弱性の確認。
  - [Shodan](https://www.shodan.io/)

## アクセス権の取得と拡大（Privilege Escalation）
- **パスワードクラッキング**: パスワードの解読やハッシュ化されたパスワードの解析。
  - [John the Ripper](https://www.openwall.com/john/)
- **フィッシング攻撃**: 社内メールを利用したフィッシング攻撃による認証情報の取得。
  - [Gophish](https://getgophish.com/)
- **エクスプロイト利用**: ソフトウェアやネットワーク機器の脆弱性を利用して特権を獲得。
  - [Metasploit](https://www.metasploit.com/)

## 継続的アクセスの維持（Maintaining Access）
- **バックドアの設置**: 将来的なアクセスのためのバックドアやリモートアクセスツールの設置。
  - [Netcat](http://nc110.sourceforge.net/)
- **ルートキットの使用**: 侵入の痕跡を隠すためのルートキットのインストール。
  - [Rootkit Hunter](http://rkhunter.sourceforge.net/)
- **アカウント作成**: 不正アカウントを作成し、発見されにくい形で特権を維持。

## 社内データの盗難および利用（Data Exfiltration and Utilization）
- **データの窃盗**: 顧客情報、知的財産、財務データなどの機密情報のコピー。
  - [Wireshark](https://www.wireshark.org/)
- **スニッフィング**: ネットワークトラフィックを傍受し、送信されるデータを収集。
  - [tcpdump](https://www.tcpdump.org/)
- **クラウドストレージの利用**: クラウドサービスを使ってデータを外部に転送。

## 攻撃の準備および実行（Preparing and Executing Attacks）
- **マルウェアの展開**: 社内ネットワークにマルウェアを仕込み、他のシステムに感染させる。
- **ランサムウェア攻撃**: ファイルを暗号化し、復号のための身代金を要求。
  - [Hidden Tear](https://github.com/goliate/hidden-tear)
- **DDoS攻撃**: 分散型サービス妨害攻撃を計画し、社内システムのダウンを狙う。
  - [LOIC](https://github.com/NewEraCracker/LOIC)

## 内部者の協力（Collaboration with Insiders）
- **共犯者の勧誘**: 社内の不満を持つ従業員を勧誘し、協力を得る。
  - [Wickr](https://wickr.com/)
- **情報交換**: 共犯者との情報交換や、内部情報の共有。
  - [ProtonMail](https://proton.me/mail)

## 証拠の隠蔽および操作（Evidence Tampering and Manipulation）
- **ログの改ざん**: システムログを操作し、侵入の痕跡を消す。
  - [Log Cleaner](https://github.com/ccesar1989/logCleaner)
- **監視の回避**: セキュリティ監視システムを無効化または回避。
  - [AntiSpy](https://www.anti-spy.info/)

## エスカレーションおよび破壊活動（Escalation and Destructive Actions）
- **データ破壊**: 重要なデータの削除や破壊。
  - [DBAN](https://dban.org/)
- **システムの妨害**: 重要なシステムやインフラストラクチャの停止。
  - [C4](https://github.com/0xC4/C4)
- **内部告発**: 企業の機密情報を外部に漏洩し、社会的なダメージを与える。
  - [SecureDrop](https://securedrop.org/)

## 退職後の活動（Post-Employment Activities）
- **残存アクセスの利用**: 退職後も残されたバックドアやアカウントを利用してアクセス。
  - [SSH](https://www.openssh.com/)
- **内部情報の売却**: 得た情報を競合企業や闇市場に売却。
  - [Dark Web](https://darkweb.ws/)
- **報復攻撃**: 不満が残る場合の報復目的の攻撃。
  - [Kali Linux](https://www.kali.org/)

