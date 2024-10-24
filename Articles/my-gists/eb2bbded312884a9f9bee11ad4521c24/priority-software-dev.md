# ソフトウェア開発における作業優先順

工程
要求分析
1. 分析
1. アーキテクチャ設計
1. 詳細設計
1. 実装
1. テスト

成果物
1. ユースケースモデル
1. イベントフロー
1. 画面遷移図
1. 概念モデル
1. 分析モデル
1. アーキテクチャ設計書
1. 設計モデル
1. ソースコード テスト仕様書、テストコード

UML
ユースケース図
1. アクティビティ図
1. クラス図、オブジェクト図、コミュニケーション図
1. パッケージ図、クラス図、シーケンス図
1. クラス図、シーケンス図


<table><thead><tr><th>工程</th><th>主な成果物</th><th>UMLモデル図</th></tr></thead><tbody><tr><td>要求分析</td><td>ユースケースモデル<br>イベントフロー<br>画面遷移図</td><td>ユースケース図<br>アクティビティ図<br>なし</td></tr><tr><td>分析</td><td>概念モデル<br>分析モデル</td><td>クラス図、オブジェクト図<br>コミュニケーション図</td></tr><tr><td>アーキテクチャ設計</td><td>アーキテクチャ設計書</td><td>パーッケージ図、クラス図<br>シーケンス図</td></tr><tr><td>詳細設計</td><td>設計モデル</td><td>クラス図、シーケンス図</td></tr><tr><td>実装</td><td>ソースコード</td><td>なし</td></tr><tr><td>テスト</td><td>テスト仕様書、テストコード</td><td>なし</td></tr></tbody></table>


```mermaid
gantt
    title ソフトウェア開発工程（2週間スケジュール）
    dateFormat  YYYY-MM-DD
    section 工程
    要求分析           :active, des1, 2024-06-01, 2d
    アーキテクチャ設計 : des2, after des1, 2d
    詳細設計           : des3, after des2, 2d
    実装               : des4, after des3, 4d
    テスト             : des5, after des4, 3d
    ドキュメンテーション : des6, after des5, 1d
    
    section 成果物
    ユースケースモデル  :milestone, m1, 2024-06-03, 0d
    イベントフロー      : des7, after des1, 1d
    画面遷移図          : des8, after des1, 1d
    概念モデル          : des9, after des2, 2d
    分析モデル          : des10, after des2, 2d
    アーキテクチャ設計書 : des11, after des2, 2d
    設計モデル          : des12, after des3, 2d
    ソースコード        : des13, after des4, 4d
    テスト仕様書、テストコード : des14, after des4, 4d

    section UML
    ユースケース図      : des15, after m1, 1d
    アクティビティ図    : des16, after des2, 2d
    クラス図、オブジェクト図、コミュニケーション図 : des17, after des3, 2d
    パッケージ図、クラス図、シーケンス図          : des18, after des3, 2d
    クラス図、シーケンス図                       : des19, after des4, 4d
```

RD:委任 UI:委任 SS-IT:請負
準委任推奨