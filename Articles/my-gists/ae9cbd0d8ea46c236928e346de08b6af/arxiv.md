# arXiv 利用ガイドライン

arXiv（アーカイブ）は、学術論文の無料オープンアクセスリポジトリであり、研究者や学術コミュニティにとって貴重な情報源です。arXivを効果的に利用するためのガイドラインを以下に示します。

## arXivの特徴

arXivは、多くの学術分野にわたる論文を収録しており、その特徴は次のとおりです：

1. **無料オープンアクセス**: arXivは無料で利用できるオープンアクセスのプラットフォームです。誰でもアクセスでき、論文を閲覧できます。

2. **多様な分野**: arXivには物理学、数学、コンピュータサイエンス、生命科学など、さまざまな学術分野の論文が収録されています。

3. **プレプリントサーバー**: arXivはプレプリント（査読前の論文）を提供し、研究成果を迅速に共有できるプラットフォームとしても知られています。

## arXivの利用ガイド

arXivを効果的に利用する際には、以下のポイントに注意してください。

1. **論文検索**: arXivのウェブサイトやAPIを使用して、必要な論文を検索しましょう。ウェブサイトではキーワード、著者、分野などを使った高度な検索が可能です。

2. **論文閲覧**: 論文を閲覧する際には、著作権や利用規約に従ってください。一般的に、arXivの論文は無料で利用できますが、一部例外があります。

3. **論文の引用**: arXivの論文を引用する際には、適切な引用スタイルと著者情報を使用し、正確な情報を提供しましょう。

4. **APIの利用**: arXivはAPIを提供しており、研究プロジェクトやアプリケーションで利用できます。APIを使用する場合は、[arXiv APIガイドライン](https://info.arxiv.org/help/api/) を遵守してください[^1].

5. **査読プロセス**: arXivは査読を受けていない論文も提供しています。査読済みの論文を探す場合は、別途学術ジャーナルなどを検討しましょう。

## APIを使用した例

以下のは、Pythonライブラリを使用してTop 20の論文記事のPDFを取得するPythonコードの例です：

```python
# arxiv.pyを使用したTop 20 論文記事のPDFを取得する例
import arxiv

# 検索クエリを定義
query = arxiv.query(query="machine learning",  # query='ti:<keyword>' [/ 'au', 'abs', 'cat', 'all' ]
            id_list=[],
            max_results=None,
            start = 0,
            sort_by="relevance", # [/ 'lastUpdatedDate', 'submittedDate' ]
            sort_order="descending",
            prune=True,
            iterative=False,
            max_results=20) 
            
# 検索結果からPDFリンクを取得
for result in query:
    pdf_link = result.get("pdf_url")
    print(pdf_link)
    
    arxiv.download((l[0], 'outputs/', lambda x: x.get('id').split('/')[-1])
    time.sleep(10)
```
 - `submittedDate:[YYYYMMDDHHMMSS TO YYYYMMDDHHMMSS]` などと指定可能

arXivの利用に関する詳細情報は、[arXivの公式ウェブサイト](https://arxiv.org/) および [arXiv APIユーザーマニュアル](https://info.arxiv.org/help/api/user-manual.html) を参照してください[^1][^2].

arXivは学術研究に貢献する重要なツールであり、正確な情報の提供と適切な利用が求められます。これらのガイドラインを守りながら、研究や学習にarXivを活用しましょう。

### 付録

- PDF to HTML: https://www.arxiv-vanity.com/

[^1]: 参考: arXivの公式ウェブサイト
[^2]: API情報は arXiv APIユーザーマニュアル をご参照ください。
