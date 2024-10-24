# 並列処理
ThreadPoolExecutor と httpx.AsyncClient は、異なるアプローチを取る非同期処理の手法です。以下に、それぞれの特徴と違いを説明します。

## ThreadPoolExecutor:

concurrent.futures.ThreadPoolExecutor は、スレッドベースの非同期処理を提供します。
スレッドプールを使用して同時に複数のタスクを実行できます。
I/O バウンドな操作（ファイルの読み書き、ネットワーク通信など）を効果的に非同期に処理する場合に適しています。
CPU バウンドな操作（計算が主要な操作）には適していません。これは、Python の GIL（Global Interpreter Lock）により、同時に複数のスレッドで Python コードが実行されることが防がれるためです。
例えば、concurrent.futures.ThreadPoolExecutor を使用して非同期なファイルの読み書きを行う場合、以下のようになります：

```
import concurrent.futures

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_read = executor.submit(read_file, 'input.txt')
    future_write = executor.submit(write_file, 'output.txt', future_read.result())
    # 他の処理...

    result = future_write.result()
    print(result)
```

## httpx.AsyncClient:

httpx.AsyncClient は httpx ライブラリに含まれる非同期な HTTP クライアントです。
async/await を使用して非同期なコードを記述します。
非同期な I/O バウンドな操作（HTTP リクエスト、データベースクエリなど）に適しています。
httpx は非同期な HTTP リクエストをサポートしており、コルーチン内で同時に多くの非同期なリクエストを発行できます。
例えば、httpx.AsyncClient を使用して非同期な HTTP リクエストを行う場合、以下のようになります：


```py
import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def main():
    url = 'https://example.com'
    content = await fetch(url)
    print(content)

asyncio.run(main())
```