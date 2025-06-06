# Carl-botのReaction-Roleの設定

Carl-botを使用してDiscordサーバーでReaction-Roleを設定する手順を説明します。Reaction-Roleは、ユーザーがメッセージにリアクションを追加することで役職を自動的に付与または削除できる機能です。

1. **Carl-botの招待**:
   - Carl-botをDiscordサーバーに招待します。これには適切な権限が必要です。[Carl-botの公式ウェブサイト](https://carl.gg/)から招待リンクを取得できます。

1. **Discordサーバーでrolesチャンネルを作成**:
   - リアクションで役職を設定するメッセージを送信するためのチャンネルを作成します。通常、これは「rules」または「roles」などの名前のテキストチャンネルです。

1. **メッセージを送信**:
   - Reaction-Roleを設定するためのメッセージを選んで、チャンネルに送信します。これは通常、ルールや説明を含むメッセージです。

1. **Reaction-Roleを設定**:
   - メッセージを送信したら、Carl-botの設定コマンドを使用してReaction-Roleを設定します。一般的なコマンドは次のとおりです:
   ```bash
   !rr create <message_id> <emoji> <role_name> 
   ```
   - `<message_id>`: Reaction-Roleを設定したいメッセージのID
   - `<emoji>`: ユーザーがリアクションを追加するための絵文字（例: :thumbsup:）
   - `<role_name>`: 付与または削除する役職の名前

    このコマンドを実行すると、Carl-botがリアクションロールの設定ウィザードを開始します。
  
1. サーバーのメンバーは、リアクションをクリックすることでロールを取得できます。

     - リアクションを追加:
     ユーザーがリアクションを追加すると、指定した役職が付与されます。
     - リアクションを削除:
     ユーザーがリアクションを削除すると、指定した役職が削除されます。

1. **役職を設定**: Carl-botの指示に従って、リアクションロールの詳細を設定します。これにはリアクションをつけたい絵文字、関連づけるロール、そして説明が含まれます。


これで、Carl-botを使用してリアクションロールを設定しました。メンバーは簡単に特定のロールを取得できるようになり、サーバーの運営やコミュニケーションを円滑に進めるのに役立ちます。

注意: Carl-botのコマンドプレフィックス（`!`など）はサーバーごとに異なる場合があります。Carl-botの使用方法に関する詳細な情報は、公式ドキュメントやサーバー内のヘルプコマンドを参照してください。
