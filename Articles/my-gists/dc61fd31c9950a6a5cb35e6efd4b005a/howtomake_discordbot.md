
# Discordスラッシュコマンドに応答するボットの作成手順

ディスコードボットを作成して、応答する機能を実装するには、
プログラミングの知識とディスコードAPIへのアクセスが必要です。
以下に、手順の一般的な概要を示します：
以下は、Discordスラッシュコマンドに応答するボットを作成する手順の概要です。


## 1. 環境の設定

- ボットのプログラミング言語を選択します。Python（discord.pyライブラリを使用）やJavaScript（discord.jsライブラリを使用）などが一般的です。
- 選んだ言語のパッケージマネージャー（Pythonの場合はpip、JavaScriptの場合はnpmなど）を使用して、必要なライブラリをインストールします。


```bash
python3 -m pip install -U discord.py

# Windowsの場合
py -3 -m pip install -U discord.py

# Linux環境の場合
apt install libffi-dev libnacl-dev python3-dev
```

## 2. Discord Botの作成

Discordのウェブサイトにログインしてください。
Applicationページに移動し、「New Application」ボタンをクリックして新しいアプリケーションを作成します。
アプリケーションの名前を決め、「Create」をクリックします。
「Bot」タブに移動して、必要に応じてPublic Botにチェックを入れます。
トークンをコピーして保存しておきます。このトークンはあなたのボットの識別と認証に使用されます。他人と共有しないように注意してください。

https://discord.com/developers/applications


## 3. Botのコーディング

- 選んだプログラミング言語とライブラリを使用して、ボットの基本的な構造を設定します。
- Discord APIのスラッシュコマンドイベントに対する応答を実装します。


```python
import discord
from discord.ext import commands

intents = discord.Intents.default()  # 必要に応じてインテントをカスタマイズ
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def explain(ctx, topic):
    # ここでトピックに関する説明を取得または生成し、日本語に翻訳する処理を実装
    explanation = get_explanation_in_japanese(topic)
    await ctx.send(explanation)

bot.run('YOUR_BOT_TOKEN')

```

## 4.  Botを招待する

「Bot」項目の「Add Bot」ボタンをクリックして、botを作成します。
その際、Privileged Gateway Intents>SERVER MEMBERS INTENT, MESSAGE CONTENT INTENTをオンにしてください。



Botを招待するためのURLを作成するために、Applicationページから「OAuth2 > URL Generator」タブに移動します。
「scopes」の下にある「bot」チェックボックスを選択します。
「Bot Permissions」からボットが必要な権限を選択します。
生成されたURへアクセスして、ボットを追加したいサーバーを選択します。サーバー管理権限が必要です。

https://discordapp.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=0


https://discordpy.readthedocs.io/ja/latest/discord.html#


---
REFs:
https://blog.bridgey.dev/2023/01/29/discord-py/

https://github.com/kkrypt0nn/Python-Discord-Bot-Template

