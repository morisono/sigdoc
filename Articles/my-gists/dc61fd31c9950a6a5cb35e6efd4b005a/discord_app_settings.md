# Discord アプリの設定

以下にそれぞれの概要を説明します。

## General

```
Interactions Endpoint URL:
Discordは、Botを使用する代わりにGateway上でHTTP POSTを介してインタラクションを受け取るためのInteractions Endpointを設定するオプションを提供しています。これは、あなたのアプリケーションがユーザーと対話するためのポイントを提供します。たとえば、ユーザーがコマンドを送信したときや特定のアクションを取ったときにサーバーと通信します。

Linked Roles Verification URL:
これはDiscordの役割リンク設定の一部としてアプリケーションを必須にするために構成できる検証URLです。これにより、特定のサーバー役割に関連付けられたユーザーがアプリケーションを使用する前に、その役割が確認されます。これは、ある役割を持つユーザーだけが特定のアクションを実行できるようにするための一つの方法です。

Terms of Service URL:
これはアプリケーションの利用規約へのリンクです。Discordアプリケーションの開発者は、利用規約に同意することがアプリケーションの使用の条件となるようにすることができます。このURLはユーザーに提供され、ユーザーがそのアプリケーションのルール、制約、および利用条件を理解できるようにします。

Privacy Policy URL:
これはアプリケーションのプライバシーポリシーへのリンクです。開発者はこれを設定して、ユーザーデータの収集、使用、共有に関するアプリケーションのポリシーを説明します。これは、ユーザーデータの保護とプライバシーを確保するために重要な情報です。
```

## OAuth2

Default Authorization Linkは、他のDiscordユーザーがあなたのアプリケーションを直接自分のサーバーに追加することができるリンクです。このリンクは、あなたのアプリケーションが必要とする特定のスコープと権限を持つように設定されます。

Custom URLについては、これは一般的に、デフォルトの認証リンクに代わるオプションとして使用されます。このURLは、アプリケーションがDiscordユーザーに対して特別な認証フローやユーザーエクスペリエンスを提供したい場合に利用します。例えば、特定のアプリケーションで必要な追加情報を収集するための特別なログインページや、アプリケーションの特定の部分へのアクセスを提供するリンクなどがここで設定できます。

ただし、Custom URLを使用する場合は、それがDiscordの規定に適合し、ユーザーのプライバシーとセキュリティを尊重するものであることが必要です。Custom URLを使用する前に、アプリケーションが適切な認証フローを経てユーザーデータを収集し、ユーザーの許可を得ていることを確認する必要があります。

一般的にDiscord botを作成するときには、認証スコープとして "bot" を選択します。これは、あなたのアプリケーションがBotとして動作し、サーバーに参加し、必要な権限に基づいてアクションを実行することを意味します。



このスコープを選択すると、ユーザーがBotを自分のサーバーに追加するための認証リンクが生成されます。このリンクを使用すると、ユーザーはあなたのBotを自分のサーバーに招待することができます。

ただし、どの権限がBotに必要かは、Botが何をする必要があるかによります。例えば、メッセージを送信したり、メッセージを読んだりするための権限が必要な場合もありますし、他の特定のアクションを実行するためには他の権限が必要な場合もあります。権限は、あなたのアプリケーションが必要とする具体的な機能に基づいて選択するべきです。

`applications.commands` はDiscord APIの特定のスコープです。このスコープは、あなたのアプリケーションがSlash Commands（スラッシュコマンド）を作成し使用するための権限を与えます。

Slash Commands（スラッシュコマンド）はDiscordで提供される新しいタイプのコマンドで、ユーザーがコマンド名を直接チャットに入力することで実行できます。これらのコマンドはボットとの対話をより直感的にし、より自然なユーザーエクスペリエンスを提供します。例えば、/play というコマンドを使って音楽を再生することができます。

## OAuth2 URL Generator

URLジェネレータは以下の情報を提供するために使用されます：

```
Client ID: これはあなたのアプリケーションの一意の識別子です。
Redirect URI: これは認証後にユーザーをリダイレクトするURLです。
Scope: これらはあなたのアプリケーションがユーザーから要求する権限です。これらはスペースで区切られ、例えば 'bot' や 'applications.commands' などのスコープを含むことができます。
Permissions: これらはあなたのアプリケーションが要求する特定のDiscord権限です。これらは整数値で指定され、それぞれが特定の権限を表します。
```


```
GENERAL PERMISSIONS
- Administrator: このパーミッションはすべての他のパーミッションをオーバーライドします。これを持つボットは、サーバー上のすべてのアクションを実行することが許可されています。
- View Audit Log: このパーミッションはボットが監査ログを閲覧することを可能にします。これはサーバーの変更履歴を追跡するためのものです。
- 

TEXT PERMISSIONS
- Send Messages: このパーミッションはボットがテキストチャンネルにメッセージを送信することを許可します。
- Read Message History: このパーミッションはボットがチャンネルのメッセージ履歴を閲覧することを許可します。
- 

VOICE PERMISSIONS
- Connect: このパーミッションはボットが音声チャンネルに接続することを許可します。
- Speak: このパーミッションはボットが音声チャンネルで話すことを許可します。
- Mute Members: このパーミッションはボットが他のメンバーをミュートすることを許可します。
- 

```

OAuth2スコープは、ユーザーに特定のアクションを要求するために使用されます。スコープは、どの種類の情報にアプリケーションがアクセスでき、ユーザーがアプリケーションで何ができるかを指定します。

`bot`スコープを有効にしましょう。

```
bot: このスコープは、アプリケーションがボットとして動作し、特定のサーバーに参加することを許可します。

connections: このスコープは、アプリケーションがユーザーの接続を表示することを許可します。これはユーザーがDiscordにリンクした他のサービス（例えば、SpotifyやReddit）のことを指します。

email: このスコープは、アプリケーションがユーザーの電子メールアドレスにアクセスすることを許可します。

identify: このスコープは、アプリケーションがユーザーの基本情報（ユーザー名、画像、Discord ID等）にアクセスすることを許可します。

guilds: このスコープは、アプリケーションがユーザーが所属するサーバー一覧を取得することを許可します。

guilds.join: このスコープは、アプリケーションがユーザーの代わりにサーバーに参加することを許可します。

messages.read: このスコープは、アプリケーションがユーザーの代わりにメッセージを読むことを許可します。

rpc: このスコープは、アプリケーションがDiscordのRich Presence機能を利用することを許可します。

rpc.api: このスコープは、アプリケーションがDiscordのRPC APIを利用することを許可します。

rpc.notifications.read: このスコープは、アプリケーションがDiscord上の通知を読むことを許可します。

webhook.incoming: このスコープは、アプリケーションがWebhook経由でメッセージを送信することを許可します。

applications.builds.upload: このスコープは、アプリケーションがゲームビルドをアップロードすることを許可します。

applications.builds.read: このスコープは、アプリケーションがゲームビルドを読むことを許可します。

applications.store.update: このスコープは、アプリケーションがストアアプリのデータを更新することを許可します。

applications.entitlements: このスコープは、アプリケーションがユーザーのエンタイトルメント（購入したアイテムやサービス）を読むことを許可します。

relationships.read: このスコープは、アプリケーションがユーザーのフレンドリストを読むことを許可します。

activities.read: このスコープは、アプリケーションがユーザーのアクティビティ（現在プレイしているゲームなど）を読むことを許可します。

activities.write: このスコープは、アプリケーションがユーザーのアクティビティを書き込むことを許可します。

applications.commands: このスコープは、アプリケーションがスラッシュコマンドを使用することを許可します。
```

## Bot

Botセクションには、あなたのボットがどのように機能するか、そしてどのように他のDiscordユーザーと相互作用するかを制御するいくつかの重要な設定があります。あなたが指定したそれぞれのセクションについて説明します。

```
Authorization Flow:

Public Bot: この設定は、ボットがパブリック（誰でも追加できる）か、あるいはプライベート（あなた自身しか追加できない）かを制御します。これは、あなたがボットを一般のDiscordユーザーに公開するか、あるいは限定的な使用に留めるかを決めるための設定です。

Privileged Gateway Intentの3項目を有効にしましょう。

Requires OAuth2 Code Grant: この設定は、ボットがサーバーに参加する前に、アプリケーションがトークンを取得する必要がある完全なOAuth2フローが必要かどうかを制御します。これは、アプリケーションが複数のスコープを必要とする場合に役立ちます。

Privileged Gateway Intents:

Presence Intent: ボットがPresence Updateイベントを受け取るために必要です。これによりボットはユーザーがオンラインか、AFKか、またはどのゲームをプレイしているかなどの情報を取得できます。ボットが100以上のサーバーに参加すると、このインテントは検証と承認が必要になります。

Server Members Intent: ボットがGUILD_MEMBERS下のイベントを受け取るために必要です。これによりボットはサーバーのメンバーに関する情報を取得できます。ボットが100以上のサーバーに参加すると、このインテントは検証と承認が必要になります。

Message Content Intent: ボットがメッセージ内のコンテンツを受け取るために必要です。これによりボットはメッセージのテキスト内容などを取得できます。ボットが100以上のサーバーに参加すると、このインテントは検証と承認が必要になります。
```

## Rich Presence 

DiscordのRich Presence Art Assetsは、DiscordのRich Presence機能を強化するための視覚的な要素です。Rich Presenceは、ユーザーが現在何をしているのか、どのアプリケーションやゲームを使用しているのかをDiscord上で表示する機能です。これにより、他のユーザーはあなたが何をしているかを一目で理解することができます。

Rich Presence Art Assetsは、この表示をカスタマイズするための画像やアイコンを指します。これには、特定のアクティビティやステータス、ゲームキャラクター、レベルなどを表す画像が含まれます。これらのアセットは、あなたのアプリケーションやゲームのユーザー体験を強化し、より視覚的に表現するのに役立ちます。

これらのアセットをアップロードするには、Discord Developer Portal内のアプリケーションページに移動し、左側のナビゲーションメニューから "Rich Presence" > "Art Assets" を選択します。そして、アートアセットをアップロードして、それぞれに名前を付けることができます。これらの名前は後でプログラムで参照され、特定の状況に応じて表示されます。

## App Testers

Discordアプリの"App Testers"セクションは、あなたのアプリケーションやボットのテストフェーズに参加するユーザーを管理するための場所です。

App Testersは、あなたのアプリケーションをテストし、フィードバックを提供し、問題を報告するために特別に指定されたユーザーです。これには、機能のテスト、バグの発見、パフォーマンスのチェック、ユーザーエクスペリエンスの評価などが含まれます。これらのテスターは、アプリケーションの改善と品質保証に非常に重要な役割を果たします。

あなたはこのセクションでテスターを追加したり、削除したり、管理したりすることができます。Discord Developer Portalにログインし、あなたのアプリケーションを選択し、左側のナビゲーションパネルで"App Testers"を選択します。そして、新しいテスターを追加するためには、そのユーザーのDiscordのユーザー名とタグを入力します。




