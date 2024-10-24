# Python Collection > View

Pythonにもポインタに近い概念が存在します。
 
## PythonのViewとは
PythonのViewオブジェクトは、辞書のキー、値、またはキーと値のペアへの動的な参照を提供します。辞書の内容が変更されると、その変更を反映します。

## C言語のポインタとの類似性
C言語のポインタとPythonのViewオブジェクトは、データ構造の特定の部分への参照を提供する点で類似しています。ポインタはメモリ上の特定のアドレスを指し示し、Viewオブジェクトは辞書の特定の部分を指し示します。

## 使い方と利点
Viewオブジェクトは、`keys()`, `values()`, `items()`などのメソッドで取得できます。メモリ効率が良く、元のデータ構造と一貫性を保つことができます。

[^1]: Python公式ドキュメント : [https://docs.python.org/3/library/stdtypes.html#dict-views](https://docs.python.org/3/library/stdtypes.html#dict-views)[^1]
