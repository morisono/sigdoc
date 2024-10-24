# pytest: Pythonのテスティングフレームワーク

pytestは、Pythonのテスティングフレームワークの一つで、Pythonプロジェクトのユニットテスト、結合テスト、機能テストを簡単に実行できる強力なツールです。pytestは、多くの拡張機能やプラグインを提供しており、柔軟性が高く、カスタマイズが容易です。

## インストール

pytestをインストールするには、pipを使用します。以下のコマンドを実行してインストールできます。

```bash
pip install pytest
```

## 基本的な使用法

ターミナルで以下のコマンドを実行して、テストを実行します。
```
pytest -v
```

テストが成功すると、合格したテストケースの数と結果が表示されます。

```
============================= test session starts =============================
platform darwin -- Python 3.x.x, pytest-6.x.x, pluggy-0.x.x
...
collected 2 items

test_sample.py::test_addition PASSED                                [ 50%]
test_sample.py::test_subtraction PASSED                             [100%]

============================= 2 passed in 0.xxs ==============================
```


## テストケース

テストケースをPythonの関数として書き、test_で始まる関数名を持たせます。例えば：

```python
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 1 == 2

pytest test_module.py
```


## アサーション

pytestでは、アサーションを使用してテスト結果を確認します。アサーションが真であれば、テストは合格となります。偽の場合はエラーとして報告されます。


```python
# アサーションを使用したテスト
def test_multiplication():
    result = 2 * 3
    assert result == 6, "2 * 3 should be 6"
```

## フィクスチャ

pytestはフィクスチャをサポートしており、テストケース間で共通のセットアップやクリーンアップを実行できます。フィクスチャを定義するには、@pytest.fixtureデコレータを使用します。

```python
import pytest

# フィクスチャの定義
@pytest.fixture
def setup_and_teardown_example():
    # セットアップ
    print("Setup")
    
    # テスト実行
    yield
    
    # クリーンアップ
    print("Teardown")

# テストケースでフィクスチャを使用
def test_with_fixture(setup_and_teardown_example):
    print("Test logic here")
```

- https://docs.pytest.org/en/latest/

[Sansan 新卒向け資料](https://buildersbox.corp-sansan.com/entry/2023/10/25/110000#%E3%83%86%E3%82%B9%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)