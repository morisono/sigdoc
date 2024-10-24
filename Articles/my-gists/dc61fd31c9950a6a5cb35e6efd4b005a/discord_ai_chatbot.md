# Discord AI Chatbot

参考[^1]

1. Git クローン リポジトリ  
    ```
    git clone https://github.com/mishalhossin/Discord-AI-Chatbot
    ```
    
1. ボットを実行する  
    ```
    cd Discord-AI-Chatbot
    python3 main.py
    ```

1.  ボットを招待する  
コンソールに表示された招待URLを使用する

    ```bash
    > python3 main.py
    Looks like the environment variables exists...
    Discord Token environment variable is valid
    2023-06-16 01:33:03 INFO     discord.client logging in using static token
    2023-06-16 01:33:04 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: 010f408865df03025026fd84bc19b602).
    1_gpt4free#0099 aka 1_gpt4free has connected to Discord!
    Invite link: https://discord.com/oauth2/authorize?client_id=1118405797869781063&scope=bot+applications.commands&permissions=0
    ```
1. Tokenの取得, Intentの有効化  
    https://discord.com/developers/applications
    - [x] PRESENCE INTENT
    - [x] SERVER MEMBERS INTENT
    - [x] MESSAGE CONTENT INTENT
    
1.  チャットコマンド
    ```
     /help: 他のすべてのコマンドを取得します。⚙️
     /pfp [image_url]: ボットの実際のプロフィール写真を変更します。🖼️
     /imagine: を使用して画像を生成しますImaginepy 🖼️
     /changeusr [new_username]: ボットのユーザー名を変更します。📛
     /ping: ボットから「ポン」応答を取得します。🏓
     /toggleactive: アクティブなチャンネルを切り替えます。🔀
     /toggledm: チャット用の DM を切り替えます。💬
     /clear：メッセージ履歴を消去します。🗑️
     /gif: ネコ、ワイフ、夫、キツネ、またはその他のアクションのランダムな画像または GIF を表示します。🐱
    ```

[^1]: https://github.com/mishalhossin/Discord-AI-Chatbot

