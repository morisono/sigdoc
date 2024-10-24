# Gradio Discord の連携

1. Get token from https://huggingface.co/settings/tokens
1. Write code like https://huggingface.co/spaces/freddyaboulton/echo-chatbot-gradio-discord-bot/blob/main/app.py
1. `pipreqs . --force --savepath=requirements.txt`
1. `gradio deploy --title $title --app-file app.py,requirements.txt`
1. `gradio deploy-discord --src $user/$title` or `gradio deploy-discord --src $user/$title --discord-bot-token $token`
1. add secrets at repo settings
1. add bot to discord server

```python
import gradio_client as grc
grc.Client("ysharma/Explore_llamav2_with_TGI").deploy_discord(to_id="llama2-70b-discord-bot")
```

- ハグフェイスのスペースは展開されたセッションを 48 時間で切れる為、一日中目覚め続けるようにプランをアップグレードします。

- https://www.gradio.app/guides/creating-a-discord-bot-from-a-gradio-app
- https://huggingface.co/docs/hub/webhooks
- https://huggingface.co/gradio-discord-bots
- https://github.com/lovvskillz/python-discord-webhook
- https://huggingface.co/spaces/abidlabs/gradio-discord-bot-server/tree/main
- https://huggingface.co/docs/hub/spaces-gpus#using-gpu-spaces
