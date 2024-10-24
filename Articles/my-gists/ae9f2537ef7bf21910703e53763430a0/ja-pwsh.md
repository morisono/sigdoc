Powershellから外部へ送信した情報が送信元にどのように記録されるかは、状況によって異なります。一般的には以下のような場所に記録される可能性があります。

1. **ファイアウォール**: 送信元のネットワークに設定されているファイアウォールは、外部への通信を監視し、ログを残すことがあります。送信元からの外部への通信がファイアウォールを通過する際に、そのログが残されることがあります。
   - 製品例: Cisco ASA、Palo Alto Networks Firewall、Fortinet FortiGate、Check Point Firewall、SonicWall、Juniper Networks SRX Series

2. **プロキシサーバ**: 企業や組織内でネットワークトラフィックを監視するためにプロキシサーバが使用されている場合、Powershellからの外部への通信もそのプロキシサーバを経由します。プロキシサーバは通信内容をログとして残すことがあります。

3. **IDS/IPS**: ネットワーク内での異常なトラフィックや悪意のある活動を検知するためにIDSやIPSが設置されている場合、Powershellからの外部への通信も監視対象となります。異常が検知されると、そのイベントがログとして残されることがあります。
   - 製品例: Snort、Suricata、Cisco Firepower、IBM Security QRadar、Trend Micro Deep Discovery Inspector、McAfee Network Security Platform


4. **SIEM (セキュリティ情報およびイベント管理)**: セキュリティ情報とイベント管理システムは、複数のデバイスやアプリケーションからのネットワーク上で発生したイベントやログを収集し、統合して分析します。Powershellからの外部への通信に関する情報も、このようなシステムによってセキュリティインシデントとして収集される可能性があります。
   - 製品例: Splunk Enterprise Security、IBM QRadar、LogRhythm

5. **組織のセキュリティポリシーによる監査**: 多くの組織は、セキュリティポリシーに準拠するためにセキュリティイベントの監査を実施します。Powershellからの外部への送信がポリシーに違反する場合、それに関する監査ログが残り、セキュリティチームによってレビューされます。
   - 製品例: IBM QRadar、SolarWinds Security Event Manager、Splunk Enterprise Security、LogRhythm、ArcSight、RSA Security Analytics、RSA NetWitness

6. **ログ**: システムログやセキュリティイベントログは、組織のログ管理システムによって収集、保存、分析されます。Powershellからの外部への送信は、適切なログに記録されます。これには、送信元IPアドレス、送信先URL、実行された操作などが含まれます。
   - 製品例: Splunk、ELK Stack（Elasticsearch、Logstash、Kibana）、Microsoft Azure Sentinel、AlienVault USM（Unified Security Management）、Graylog

7. **クラウドプラットフォームの監査ログ**: 多くのクラウドプラットフォームは、ユーザーアクションやAPI呼び出しに関する監査ログを提供しています。Powershellを使用して外部への送信がクラウドプラットフォームで行われた場合、これらのプラットフォームの監査ログに記録されることがあります。
   - 製品例: AWS CloudTrail、Microsoft Azure Monitor、Azure Activity Log、Azure Security Center、Google Cloud Audit Logs、Google Cloud Security Command Center

7. **エンドポイントセキュリティソリューション**: エンドポイントセキュリティソリューションは、デバイス（エンドポイント）でのセキュリティを強化し、不正な活動を検知して防御します。Powershellからの外部への送信が不審な活動として検知されると、これらのソリューションはアラートを生成し、適切なログに記録します。
   - 製品例: Symantec Endpoint Protection、CrowdStrike Falcon、McAfee Endpoint Security

8. **ネットワーク監視ソリューション**: ネットワーク監視ソリューションは、ネットワークトラフィックやデバイスのパフォーマンスを監視し、異常なアクティビティを検知します。Powershellからの外部への送信がネットワーク上で行われた場合、これらのソリューションはトラフィックを監視し、不審な活動として識別することがあります。
   - 製品例: Wireshark、SolarWinds Network Performance Monitor、Nagios、Zabbix、PRTG Network Monitor


以上のようなセキュリティインフラストラクチャが適切に設定されている場合、Powershellからの外部への通信はこれらのシステムによって監視され、ログとして残ることがあります。