通常、クラスのインスタンスメソッドが async（コルーチン）関数である場合、そのメソッドを直接実行すると、コルーチンオブジェクトが返されますが、実行はされません。代わりに、コルーチンを実行するには await を使用するか、asyncio モジュールの run 関数を介して実行する必要があります。

以下は、クラスのインスタンスメソッドを直接実行する例です：

```py
class PdfProcessor:

    def __init__(self, params):
        self.params = params

    async def gen(self):
        # ここにコルーチンの処理を記述

# インスタンスの作成
pdf_processor = PdfProcessor(params)

# 直接実行するとコルーチンオブジェクトが返される
coro_object = pdf_processor.gen()

# コルーチンを実行するにはawaitを使用するか、asyncio.runを介して実行する
result = await coro_object
```