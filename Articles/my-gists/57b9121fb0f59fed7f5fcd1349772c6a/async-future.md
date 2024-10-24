# 非同期処理

asyncは通常、非同期処理を行うためのキーワードです。非同期処理では、処理が完了するのを待たずに次の処理を進めることができます。一方で、Future（またはPromiseなど、プログラミング言語やフレームワークによって異なる場合があります）は、非同期処理の結果を表すためのオブジェクトや概念です。

言い換えると、一般的には、async関数は非同期的な処理を行いますが、それがFutureを返すとは限りません。非同期処理が完了するまで待つことなく、他の処理を進めるために使用されるasyncキーワードと、非同期処理の結果を表すFutureオブジェクトが分離されていると考えることができます。

## async：不確定な未来状態

例えば、Pythonのasyncioモジュールでは、asyncキーワードを使用して非同期関数を定義しますが、その関数が返すものは通常はFutureではなく、await式を使用して待機できる何らかの非同期オブジェクトです。非同期関数がawaitを含まない場合、その関数は同期的に実行される可能性があります。

以下は、Pythonの非同期関数の簡単な例です：

```py
import asyncio

async def example_async_function():
    print("Start async function")
    await asyncio.sleep(2)
    print("Async function completed")

# 非同期関数を呼び出す
asyncio.run(example_async_function())
```

この例では、example_async_functionは非同期的に実行されますが、Futureを直接返しているわけではありません。代わりに、await asyncio.sleep(2)のように非同期処理を含んでおり、その結果を表すオブジェクトを返します。

## Promised / Future：確定された未来

しかし、すべての`async`関数が直接`Future`オブジェクトを返すわけではありません。そのため、一般的なパターンとして、一旦空の`Future`を割り当て、後で非同期処理が完了したときにその結果を取得することがあります。

まず、非同期処理が発生する前に、結果を格納するための空の`Future`オブジェクトを割り当てます。

```python
import asyncio

async def example_async_function():
    # 空のFutureを割り当て
    result_future = asyncio.Future()

    print("Start async function")

    # 非同期処理の発生（例：非同期でデータを取得）
    # ここで非同期処理の結果をresultに代入

    result = await get_async_data()

    # 空のFutureに結果を設定
    result_future.set_result(result)

    print("Async function completed")

# 別の非同期関数でデータを取得する例
async def get_async_data():
    await asyncio.sleep(2)
    return "Async data"
```

この例では、example_async_function内で非同期処理が発生する前に、asyncio.Future()を使用してresult_futureという空のFutureオブジェクトを割り当てています。

## 非同期処理が完了したら結果を設定
非同期処理が完了したら、その結果を割り当てた空のFutureに設定します。上記の例では、get_async_data関数で非同期にデータを取得し、その結果をresult_future.set_result(result)でresult_futureに設定しています。

このようにして、example_async_functionを呼び出した際に、非同期処理の結果を待たずに次の処理を進めることができます。非同期処理の結果を取得する必要がある場合は、後でresult_futureを使用して取得することができます。

以上が、非同期処理とFutureの取り扱いに関する一般的なパターンです。