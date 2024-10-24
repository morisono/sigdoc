# Python テストとデバッグについて (Testing and Debugging)

## 一般的な流れ

1. **Read log**:
   プログラムが正常に実行されているかどうかを確認するために、ログファイルを検査します。ログには実行時の情報やエラーメッセージが記録されており、問題の特定に役立ちます。

2. **Reproduce**:
   問題が再現可能であることを確認します。問題を再現できれば、デバッグ作業を行うためのスタート地点となります。

3. **Check**:
   問題を特定するために、以下の方法を使用します。
   - `print()` ステートメントを追加して、実行時の変数やステップごとの値を表示します。
   - デバッガを使用して、コードの特定のステップで実行を一時停止し、変数の値を調査します。
   - スタックトレースを確認し、どの関数が問題を引き起こしているかを特定します。
   - ステップ実行や次のステップへの移動など、デバッガの機能を活用して問題を追跡します。

4. **Inspect Functions**:
   問題の特定が難しい場合、特定の関数内で問題が発生しているかどうかを確認します。関数内の変数やデータの状態を注意深く調査します。

5. **Documentation**:
   問題を特定し解決したら、コードに適切なコメントやドキュメンテーションを追加します。将来のデバッグや他の開発者とのコラボレーションを支援するために、コードの理解を容易にします。


## 例外処理 (Exception)

  例外処理は、プログラムがエラーに遭遇した場合に制御を継続するための方法です。以下の方法で例外処理を行います：

- **try-catch-except**: 例外処理を行うために、`try`, `catch`, `except`構文を使用します。コードブロック内で例外が発生する可能性がある部分を`try`ブロックで囲み、例外が発生した場合の処理を`catch`または`except`ブロックで定義します。

- [contextlib](https://docs.python.org/ja/3/library/contextlib.html)

- [tenacity](https://github.com/jd/tenacity)
```
import random
from tenacity import retry

@retry
def foo():
    print(1 / random.randint(0, 1))

def main():
    foo()
```
tenacityライブラリを使用することで、関数foo()内の例外をキャッチし、リトライすることができます。このライブラリは、プログラムの頑健性を向上させるのに役立ちます。

## ロギング (Logging)

プログラム開発において、デバッグや問題の追跡、パフォーマンス監視などのために、ログを記録することは非常に重要です。ログはアプリケーションの動作を記録し、問題解決や運用管理に役立ちます。Pythonには標準の`logging`モジュールが組み込まれており、ログの処理をサポートしていますが、より効果的なロギングを実現するために、サードパーティのライブラリも利用できます。

- [**loguru**](https://readthedocs.org/projects/loguru/downloads/pdf/stable/):
  - LoguruはPythonのロギングライブラリで、使いやすさと柔軟性に焦点を当てています。詳細なドキュメンテーションは[こちら](https://readthedocs.org/projects/loguru/downloads/pdf/stable/)から入手できます。

## デバッグ (Debugging)

プログラムのデバッグは、バグの特定やコードの問題解決に欠かせないプロセスです。Pythonでは、さまざまなデバッガが利用でき、コードの実行を追跡および解析するのに役立ちます。以下に、主要なPythonデバッガの概要と機能を紹介します。

### pdb

[pdb](https://docs.python.org/library/pdb.html)はPythonの標準デバッガです。主要なコマンドには次のものが含まれます：
- `h`：ヘルプ情報の表示
- `p`：変数の値の表示
- `up`：親のスタックフレームに移動
- `pp`：変数のPretty Print
- `n`：次の行に進む
- `s`：ステップ実行
- `c`：現在のコンテキストでの実行継続
- `unt`：指定行まで実行をスキップ

### python-devtools

[python-devtools](https://github.com/samuelcolvin/python-devtools)は、デバッグ、ログ、テスト、プロファイリング、ベンチマーキングなど、多くのツールを提供するライブラリです。Python開発の多くの側面において役立ちます。

### ipython

[ipython](https://pypi.org/project/ipython/)は、対話型Pythonシェルの強化版であり、デバッガ機能も提供しています。主要なコマンドには次のものが含まれます：
- `n`：次の行に進む
- `s`：ステップ実行
- `c`：現在のコンテキストでの実行継続
- `l`：ソースコードの表示
- `p`：変数の値の表示
- `q`：デバッガの終了

### python3-trepan

[python3-trepan](https://pypi.org/project/trepan3k/#command-completion)は、多くのデバッグ機能を提供し、例えば以下のコマンドをサポートしています：
- `b`：ブレークポイントの設定
- `c`：実行の継続
- `disable`：ブレークポイントの無効化
- `display`：変数の表示
- `down`：スタックフレームの移動
- `enable`：ブレークポイントの有効化
- `finish`：現在の関数の終了
- `ignore`：ブレークポイントの無視設定
- `info`：デバッグ情報の表示
- `jump`：指定行へのジャンプ
- `restart`：プログラムの再起動
- `return`：関数の即時終了
- `run`：プログラムの実行
- `step`：ステップ実行

### pdp++

[pdp++](https://github.com/pdbpp/pdbpp)は、対話型デバッグに特化したPythonデバッガです。主要な機能には以下が含まれます：
- `sticky`：ブレークポイントの設定と保持
- `w`：ステップ実行と同時にウォッチリストの変数を表示
- `args`：関数の引数とデフォルト引数の表示
- `interact`：対話モードの開始
- `longlist`：ソースコードの拡張表示
- `jump`：指定行へのジャンプ
- `enable`：ブレークポイントの有効化
- `disable`：ブレークポイントの無効化
- `debug`：デバッグ情報の表示

### ipdb

[ipdb](https://github.com/gotcha/ipdb)は、対話型デバッグを提供するPythonデバッガです。主要なコマンドには次のものが含まれます：
- `n`：次の行に進む
- `s`：ステップ実行
- `w`：カレントスタックフレーム内での変数の表示
- `b`：ブレークポイントの設定
- `c`：実行の継続
- `a`：スタックフレーム間の移動
- `r`：リターン

### madbg

[madbg](https://github.com/kmaork/madbg)はPython用のデバッガで、詳細なデバッグとトレース機能を提供します。

これらのデバッガツールは、Pythonプログラムのデバッグ作業を支援し、問題の特定と修正を効果的に行うのに役立ちます。プロジェクトの要件や好みに合わせて選択し、バグの特定と解決に活用してください。

## スタックトレース（Stack Trace）

プログラムの実行中にエラーや例外が発生すると、スタックトレースが生成されます。スタックトレースは、エラーが発生した箇所からバックトレースして関数呼び出しの履歴を示す重要な情報です。Pythonでは、`traceback`モジュールを使用してスタックトレースを取得および表示することができます。

### [traceback](http://docs.python.org/library/traceback.html)
```
import sys
import traceback

try:
    eval('a')
except NameError:
    traceback.print_exc(file=sys.stdout)
```
このコード例では、eval('a')の評価中にNameErrorが発生した場合に、traceback.print_exc()を使用してスタックトレースを標準出力に表示します。

スタックトレースには、エラーの種類、エラーメッセージ、エラーが発生したファイル名、行番号、関数呼び出しの履歴などが含まれます。スタックトレースは問題の特定とデバッグに不可欠な情報を提供し、エラーがどこで発生したのかを理解するのに役立ちます。

Pythonのスタックトレースは、問題解決に役立つ情報を提供する重要なツールであり、エラーが発生した場合に迅速な対応を可能にします。

## プロファイリング（Profiling）

プロファイリングは、プログラムの実行時間やリソース使用率を測定し、どの部分が最も時間を消費しているかを特定するための技術です。Pythonでは、さまざまなプロファイリングツールが利用でき、コードのパフォーマンスチューニングに役立ちます。

- [cProfile](https://docs.python.jp/3/library/profile.html)

- [line_profile](https://github.com/rkern/line_profiler)


## インスペクト（Inspect）

Pythonの`inspect`モジュールは、実行中のプログラムやコードを検査し、情報を取得するための強力なツールです。`inspect`モジュールを使用することで、クラスや関数のメタデータ、引数、ソースコードなどを取得し、動的なプログラムの解析やデバッグに役立ちます。

### [inspect](https://docs.python.org/ja/3/library/inspect.html)　

[inspect](https://docs.python.org/ja/3/library/inspect.html)はPythonの標準ライブラリに含まれており、以下のような機能を提供します：

- **関数やクラスの情報取得**: `inspect`モジュールを使用して、関数やクラスのメタデータ、ドキュメンテーション文字列、ソースコードを取得できます。

- **フレーム情報の取得**: 現在の実行フレームやコールスタックを調べ、スタックトレース情報を取得できます。

- **引数情報の取得**: 関数やメソッドの引数情報やデフォルト値を取得できます。これは特にデコレータやメタプログラミングに役立ちます。

- **ソースコードの取得**: ソースコードを文字列として取得し、動的なコード生成やエラーメッセージの表示に使用できます。

### typing-inspect

[typing-inspect](https://github.com/ilevkivskyi/typing_inspect)は、型アノテーションや型ヒントの解析に特化したサードパーティのライブラリです。以下は、typing-inspectを使用して型アノテーションを解析する簡単な例です：

```python
from typing_inspect import get_type_hints

def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

type_hints = get_type_hints(greet)
print(type_hints)
```

この例では、typing_inspectからget_type_hints関数を使用して、greet関数の型アノテーションを解析し、型ヒントを取得しています。

inspectモジュールとtyping-inspectライブラリは、プログラムの解析、デバッグ、メタプログラミング、型情報の取得など、Pythonコードの検査に役立つ強力なツールです。特にコードの動的な操作や型アノテーションの解析において、これらのツールを活用できます。


## 構文木（Syntax Tree）

構文木は、プログラムのソースコードを解析し、その構造を階層的に表現するデータ構造です。Pythonでは、ソースコードを構文木として表現するための組み込みモジュールである`ast`（Abstract Syntax Tree）が提供されています。`ast`モジュールを使用すると、Pythonコードの構文解析と操作が可能になり、コード解析ツールや自動化スクリプトの作成に役立ちます。

### ast
[ast](https://docs.python.org/ja/3/library/ast.html)はPythonの標準ライブラリに含まれており、以下のような機能を提供します：

- **ソースコードの解析**: `ast`モジュールを使用して、Pythonのソースコードを構文木に変換できます。これにより、プログラムの構造を視覚的に理解できます。

- **ノードのトラバース**: 構文木のノードをトラバースして、ソースコード内の要素を操作できます。これはコードリファクタリングや自動コード生成に役立ちます。

- **カスタムコード解析**: `ast`モジュールを使用して、独自のコード解析ツールを開発できます。コードの特定の部分を抽出したり、変更したりすることができます。

以下は、`ast`を使用して簡単な構文木を生成する例です：

```python
import ast

source_code = """
def add(a, b):
    return a + b
"""

# ソースコードを構文木に変換
tree = ast.parse(source_code)

# 構文木を表示
ast.dump(tree)
```

## バイトコード（Bytecodes）

バイトコードは、Pythonプログラムが実行される際に使用される中間表現の一種です。Pythonのソースコードは、通常、バイトコードにコンパイルされ、Pythonインタープリタによって実行されます。バイトコードは、Pythonコードを実行可能な機械語に変換するための効率的な方法を提供し、プラットフォームに依存しない実行を可能にします。

### dis

[dis](https://docs.python.org/ja/3/library/dis.html)はPythonの標準ライブラリに含まれており、バイトコードを分析し、ディスアセンブルするためのツールを提供します。`dis`モジュールを使用すると、Pythonコードのバイトコード表現を確認し、コードがどのように実行されるかを理解することができます。

以下は、`dis`モジュールを使用してPythonコードのバイトコードをディスアセンブルする例です：

```python
import dis

def example_function(x, y):
    result = x + y
    return result

# 関数をディスアセンブルしてバイトコードを表示
dis.dis(example_function)
```
この例では、dis.dis()関数を使用してexample_functionのバイトコードを表示しています。ディスアセンブルされたバイトコードは、Pythonインタープリタによって実行される命令のシーケンスを示します。

バイトコードを理解することは、Pythonのパフォーマンスの最適化、コードの解析、デバッグ、セキュリティ評価などの用途に役立ちます。disモジュールを活用して、Pythonコードのバイトコードを詳細に調査し、その動作を理解しましょう。

## コード解析器（Linter）

Linterは、ソースコードを静的に解析して、コーディング規約や潜在的な問題を検出するツールです。PythonのLinterは、コードの品質向上、エラーの予防、一貫性の維持などのために広く使用されています。ここでは、Pythonにおける主要なLinterツールである`pylint`と`flake8`について説明します。

### pylint

[pylint](https://pylint.pycqa.org/)は、Pythonコードの品質評価を行うための非常に強力なLinterです。以下は、`pylint`の基本的な使用例です：

```bash
pylint your_python_file.py
```
pylintは、コードスタイルの遵守、不正確な変数の使用、未使用の変数、コードの一貫性などを評価し、スコアを付けてレポートを生成します。pylintの設定ファイルを使用してカスタマイズすることも可能です。

### flake8

flake8は、Pythonコードの検証とコードスタイルの確認を行うLinterツールです。以下は、flake8の基本的な使用例です：

```bash
flake8 your_python_file.py
```
flake8は、PEP 8スタイルガイドに基づいてコードスタイルの確認を行い、コード内の不正確なパターンや問題を検出します。また、カスタムプラグインを追加してflake8の機能を拡張することもできます。

どちらのLinterも、コードの品質向上とエラーの早期検出に役立ち、プロジェクトの一貫性を維持するのに貢献します。プロジェクトに合わせて適切なLinterを選択し、コードの品質管理に活用しましょう。


## デコレータ（Decorator）

デコレータは、Pythonの関数やメソッドに対する追加の振る舞いや機能を提供するための特別な関数です。デコレータは、関数を修飾して、コードの再利用性や拡張性を向上させるのに役立ちます。以下は、デコレータの基本的な概念を理解するための例です。

`import functools`

(timer, cache, log, retry, authorize, memoizeimport functools)

```python
import functools

# デコレータ関数
def lazy_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"計算中: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"計算終了: {func.__name__}")
        return result
    return wrapper

# デコレータを使用して関数を修飾
@lazy_decorator
def expensive_calculation(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

@lazy_decorator
def slow_function():
    import time
    time.sleep(2)

if __name__ == "__main__":
    result1 = expensive_calculation(1000000)
    result2 = slow_function()
```
この例では、lazy_decoratorというデコレータ関数を定義し、それを@記号を使って関数 expensive_calculation と slow_function に適用しています。デコレータ lazy_decorator は、関数を呼び出す前後にログメッセージを表示する機能を提供します。

デコレータを使用することで、複数の関数で共通の振る舞いを追加したり、コードの再利用性を向上させたりできます。デコレータは、特にログ出力、認証、キャッシュ、パフォーマンス計測、エラーハンドリングなどの場面で役立ちます。デコレータはPythonの強力な機能の一つであり、柔軟性と拡張性を提供します。



## Ref.

- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Python pdb Documentation](https://docs.python.org/3/library/pdb.html)
- [Analyzing Python Stack Traces](https://realpython.com/python-traceback/)
- [Python Debugging Best Practices](https://realpython.com/tutorials/best-practices/)

