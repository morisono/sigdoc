# Gradio-Lite について

主に次の手順で、実行ファイルを作成します。

1. `app.py` などで書いて動作確認
1. `<head>` タグで Gradio-Lite に関連した JS と CSS をインポート
1. `<body>` 内部の `<gradio-lite>` のタグの中に Gradio で実装
1. `<gradio-requirements>` の中に依存関係
1. `<gradio-file>` で分離

### Gradio-liteとFastAPIを統合してファイルパス問題を解決する方法

Gradio-liteを使用してソフトウェアを作成する際、処理後のファイルパスに関する問題に直面することがあります。特に、`os.getcwd()`を使用して現在のディレクトリを設定しても、ファイルパスが存在しないと言われてしまう場合があります。この記事では、GradioアプリケーションをFastAPI内にマウントすることで、この問題を解決する方法を紹介します。

#### 問題の背景

Gradio-liteでは、処理後のファイルパスが以下のように設定されることがあります。

```
file:///D:/home/pyodide/XcjLxsoo/file=/tmp/gradio/401789a4725504a82befd2cd5fa600ad93b56337/2024-06-26T17-57-16.zip
```

しかし、実際にはファイルが存在しないというエラーが発生することがあります。これは、Gradio-liteがローカルURLを立ち上げないため、launch()内で指定するルートパス`root_path`と許可パス`allowed_paths`の嵌合が変わってしまうことに起因します。

#### 解決方法：GradioアプリケーションのFastAPIへのマウント

GradioアプリケーションをFastAPI内にマウントすることで、この問題を解決できます。以下の手順に従って、設定を行ってください。

##### 1. 必要なパッケージのインストール

まず、FastAPI、Uvicorn、Gradioをインストールします。

```bash
pip install fastapi uvicorn gradio
```

##### 2. コードの作成

以下のコードを使用して、GradioアプリケーションをFastAPI内にマウントします。

```python
from fastapi import FastAPI
import gradio as gr
import uvicorn

app = FastAPI()
@app.get("/api")
def read_main():
    return {"message": "This is your main app"}
io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path="/gradio")

uvicorn.run(app, host="127.0.0.1", port='/')
```

##### 3. アプリケーションの実行

上記のコードを実行して、FastAPIアプリケーションを起動します。

```bash
poetry run uvicorn run:app --reload --app-dir src/app
```

##### 4. Gradioアプリケーションにアクセス

ブラウザで以下のURLにアクセスして、Gradioアプリケーションが正しくマウントされていることを確認します。

```
http://localhost:8000/
```

#### 解説

- `gr.mount_gradio_app(app, io, path=CUSTOM_PATH)`を使用して、GradioアプリケーションをFastAPIアプリケーションにマウントします。これにより、GradioのUIがFastAPIのエンドポイントで提供されます。
- `uvicorn.run(app, host="127.0.0.1", port=8000)`でFastAPIアプリケーションを起動し、ローカルホストでアクセスできるようにします。

これにより、Gradio-liteで発生していたパスの問題を解決でき、ファイルの処理後のパスが正しく設定されます。また、GradioのインターフェースをFastAPIアプリケーションに統合することで、より柔軟なアプリケーション開発が可能になります。

### 参考文献

- [Mounting Gradio within another FastAPI app](https://www.gradio.app/guides/sharing-your-app#mounting-within-another-fast-api-app)
- [GitHub Issue: Gradio Path Problems](https://github.com/gradio-app/gradio/issues/4352)

この方法を試して、Gradio-liteとFastAPIの統合によるパス問題の解決に役立ててください。