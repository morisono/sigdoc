# HF Spacesのみを公開する方法 

以下の手順を参照してください。

1. ソースコードを非公開にするためには、公開スペースからプライベートスペースをロードします。
```py
import os
import gradio as gr

read_key = os.environ.get('HF_TOKEN', None)

with gr.Blocks() as demo:
    gr.load("uname/repo", hf_token=read_key, src="spaces")

demo.queue(concurrency_count=10, max_size=20)
demo.launch()
```

1. 特定のファイルだけを非公開にするためには、プライベートデータセット/モデルを作成し、huggingface_hubクライアントを使用してSpace設定経由でhubトークンを使用してデータセット/モデルをロードします。

例：
  - GitHub Workflow でEmail自動返信して、新規登録手続きを行う。
  - Gradioで認証画面をpublic に保存して公開する。
  - Streamlit でドキュメントをprivate に保存する。

Ref.
- https://huggingface.co/docs/hub/security-tokens
- https://discuss.huggingface.co/t/embedding-spaces-with-auth-for-public-models-counter-intuitive/32868
- https://discuss.huggingface.co/t/accessing-data-in-a-private-space-from-a-public-space/49741

