# 可視化ツール

- [7. Supported Network File Formats — Cytoscape User Manual 3.10.2 documentation](https://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html)
- [Datasets](https://github.com/gephi/gephi/wiki/Datasets)


### Preprocess
- jq
- jqpg
- https://github.com/MiSawa/xq
- https://nocodefunctions.com/networkconverter/network_format_converter.html
- https://gephi.org/plugins/#/plugin/jsonexporter-plugin
- https://networkx.org/documentation/stable/reference/readwrite/graphml.html#module-networkx.readwrite.graphml

#### Desktop
- https://cytoscape.org/
- https://orangedatamining.com/
- https://graphia.app/
- https://www.vosviewer.com/
- https://gephi.org/
- https://github.com/socnetv/app

#### Shareware
- https://www.graphext.com/
- https://www.graphistry.com/
- https://kumu.io/register

#### Web
- https://gephi.org/gephi-lite/
- https://cosmograph.app/run/
- https://jacomyma.github.io/gephisto/
- https://vistorian.github.io/vistorian/#/wizard


### Edge Bundling

> 多くの3D-CADがハーネスや配管の経路をモデリングするための機能や、始終点位置から経路を自動生成する機能を備えるようになっている（一覧表）。
_from [ハーネス設計ツール | Nikkei XTech](https://xtech.nikkei.com/dm/article/COLUMN/20130424/278611/)_

これらのソフトウェアとデータは専用のフォーマットが使用されている。
ハイエンドのCADツール等では、小規模なデータに対する束線化が行われている。

テキストベースで束線化を行うメリットとして、ハイ・スケーラビリティのソフトウェアがある、応用が効く、等がある。
- https://deepai.org/publication/edge-path-bundling-a-less-ambiguous-edge-bundling-approach
- https://medium.com/@tatsurokawamoto/hierarchical-edge-bundling-explained-1-2-ea4ea45c5861
JSONをノード・リンクに抽象化する必要がある。


### See also

| 機能 | Superset | Redash | Grafana | RATH | PyGwalker | Metabase | Tableau | Power BI | Google Data Studio |
|---|---|---|---|---|---|---|---|---|---|
| ビルド | Python | Python | Go | Python | Python | Java | Windows, macOS, Linux | Microsoft | Google |
| データソース | SQL, NoSQL, クラウドストレージ | SQL, NoSQL, クラウドストレージ | インデックス, タイムシリーズDB, クラウドストレージ | SQL, NoSQL, クラウドストレージ | SQL, NoSQL, クラウドストレージ | SQL, NoSQL, クラウドストレージ | SQL, NoSQL, クラウドストレージ | Google Workspace | Google Workspace |
| ダッシュボード | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 | ドラッグアンドドロップで作成 |
| レポート | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 | クエリ結果をレポートとして出力 |
| アラート | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 | クエリ結果に基づいてアラートを送信 |
| コラボレーション | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 | 複数人でダッシュボードやレポートを共有 |
| 価格 | オープンソース | オープンソース | オープンソース | オープンソース | オープンソース | 無料 | 有料 | 有料 | 無料 |


Supersetは、最も多くの機能と柔軟性を備えたダッシュボードツールです。SQL、NoSQL、クラウドストレージなど、幅広いデータソースに対応しています。また、ドラッグアンドドロップでダッシュボードを作成したり、レポートを作成したりすることができます。さらに、アラートやコラボレーションなどの機能も充実しています。ただし、Supersetは他のツールよりも複雑で、学習曲線が急です。

Redashは、Supersetよりも使いやすく、手頃な価格のダッシュボードツールです。SQL、NoSQL、クラウドストレージなど、Supersetと同じデータソースに対応しています。また、ドラッグアンドドロップでダッシュボードを作成したり、レポートを作成したりすることもできます。さらに、アラートやコラボレーションなどの機能も備えています。ただし、RedashはSupersetほど多くの機能を備えていません。

Grafanaは、インデックス、タイムシリーズDB、クラウドストレージなど、時系列データの**可視化**に特化したダッシュボードツールです。ドラッグアンドドロップでダッシュボードを作成したり、レポートを作成したりすることができます。さらに、アラートやコラボレーションなどの機能も備えています。ただし、GrafanaはSupersetやRedashほど多くの機能を備えていません。

RATHは、Pythonで構築されたオープンソースのダッシュボードツールです。SQL、NoSQL、クラウドストレージなど、幅広いデータソースに対応しています。また、ドラッグアンドドロップでダッシュボードを作成したり、レポートを作成したりすることもできます。さらに、アラートやコラボレーションなどの機能も備えています。ただし、RATHは他のツールほど多くのユーザーベースを持っていません。

多くの機能を備えたダッシュボードツールが必要な場合は、Superset、Tableau、Power BIが最適です。使いやすく、手頃な価格のダッシュボードツールが必要な場合は、Redash、Metabase、Google Data Studioが最適です。時系列データの可視化に特化したダッシュボードツールが必要な場合は、Grafanaが最適です。Pythonで構築されたオープンソースのダッシュボードツールが必要な場合は、PyGwalkerが最適です。Pythonで構築されたオープンソースのダッシュボードツールが必要な場合は、RATHが最適です。

Feature	Superset	Redash	Grafana	RATH
Visualization types	30+	10	20+	-
Data sources	30+	20+	10	-
User management	Yes	Yes	Yes	-
Dashboard sharing	Yes	Yes	Yes	-
Embedding	Yes	Yes	Yes	-
Alerting	No	Yes	Yes	-
SQL querying	Yes	Yes	No	Yes
Customization	High	Medium	High	High