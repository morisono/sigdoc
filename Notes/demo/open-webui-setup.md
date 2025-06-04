---

title: Open Web UI setup
name: open-webui-setup
description: 
status: pending
categories: ai
tags: 
  - #ai

lang: en
private: true
weight: 1
image: 
video: 
id: 8da302
uid: 04d8822a-8f32-497e-bd27-9d2951786423
link: https://username.github.io/repo/posts/2024/08/23/0/1/open-web-u-i-setup-
path: Notes/pending/open-webui-setup.md
slug: open-webui-setup
date: 2024-08-23T10:14:01
created_at: 1724375641
updated_at: 1724375641

---

# open-webui-setup


## Abstract


## Objectives

### Reason to run LLM locally

- **Cost Efficiency**: When you're using large language models from providers like OpenAI's GPT-4, Google Gemini, etc., there are costs involved. While prototyping or developing an MVP might not incur substantial costs, you will eventually need to put a credit card on file for continued use.
- **Security**: 
For enterprises or organizations dealing with private or sensitive documents, running an LLM locally can be a game-changer. It ensures that your data doesn't have to leave your secure environment, making it perfect for tasks involving confidential information.
- **Offline access**: Local LLMs can operate without an internet connection, which is beneficial in areas with poor connectivity or in situations where internet access is restricted.
- **Lower latency**: Local models can provide faster response times since there's no need to send requests to and receive responses from a remote server.
- **Customization and** fine-tuning: Local deployment allows for easier customization and fine-tuning of the model to specific use cases or domains.
- **Regulatory compliance**: For industries with strict data regulations, local LLMs can help ensure compliance by keeping data within controlled environments.

## Methodologies

- [Calculate GPU memory capacity](https://www.substratus.ai/blog/calculating-gpu-memory-for-llm)
- [Setup GPU dricer (CUDA)](https://developer.nvidia.com/cuda-downloads)
- Setup Docker
- Setup WSL
- Download LLM

---

- `.wslconfig`に以下のパラメタを追加する

   ```bash
   [wsl2]
   ..
   networkingMode=mirrored # WSL2側のLAN設定をミラーする
   ```
   ― `code (wslpath "$(wslvar USERPROFILE)\.wslconfig")`
   - [Advanced settings configuration in WSL](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#example-wslconfig-file)
   - [Can't connect to docker container running inside WSL2 · Issue #4983 · microsoft/WSL](https://github.com/microsoft/WSL/issues/4983)
- Setup Ollama

```bash
set model llama3.1
# Run one shot
ollama run $model "刀の効率的な研ぎ方を教えて"

# Run from API HTTP Req 
curl -X POST http://localhost:11434/api/generate -d "{
    \"model\": \"$model\",
    \"prompt\": \"Here is a story about llamas eating grass\"
   }"

# Start interaction
ollama run $model 
```

- Setup Open Web UI

```bash
# Config

# Install with GPUs
docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-web
ui --restart always ghcr.io/open-webui/open-webui:cuda

# Run GUI
docker run -d -p 3000:3000 openwebui/ollama
```

バンドルインストールも可能です。

```bash


```

#### IPEX-LLM: Intel CPU における高速化
- [Local LLM Setup with IPEX-LLM on Intel GPU | Open WebUI](https://**docs**.openwebui.com/tutorial/ipex_llm/)


#### TTS



#### 検索エンジンの統合

- `.env`
  
```bash
WEBUI_URL=https://localhost:3000/?models=<model_id>&q=%s

```

```
webui your search query
```

#### Uninstalling Open WebUI

```
# Remove all Containers, Images, Volues
```

### GGUF のカスタムモデルの読み込み

LM Studioで導入したモデルを使う場合、変換が必要です。


```bash
# Search and set model 
set model_dir '/mnt/f/.cache/lm-studio/models'
cd $model_dir

set model_path ( fd -t f --exec basename {} .gguf | fzf )

set model (basename $model_path)

# Create model index dir
set index_path ~/.ollama/user_custom
mkdir -p $index_path

# Write user_custom config file

echo "FROM $model_path" > $index_path/$model

# ,jhjCreate Ollama model from gguf
ollama create $model -f $model_path
```
- [GitHub - ollama/ollama: Get up and running with Llama 3.1, Mistral, Gemma 2, and other large language models.](https://github.com/ollama/ollama?tab=readme-ov-file#customize-a-prompt)


## Additional 設定

- Scan Documents
```bash
# Set docs dir
set DOCS_DIR /data/docs # default
```

- Enable Web search

- TTS/STT

- Set task model


## References

1. 
1. 
1. 

