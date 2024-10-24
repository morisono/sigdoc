# 動画配信サイトの放送の自動要約と共有

## 概要
近年、動画配信サイトの利用が急増しており、様々なコンテンツが数多く生まれています。これに伴い、新着放送の効率的かつ迅速な収集・整理・共有が求められています。本論文では、動画配信サイトの新着放送一覧ページをスクレイピングし、指定ユーザーの放送開始を検知した場合、自動まとめ機能に引き渡し、まとめ内容を自動でツイートする統合システムについて述べます。

## システム構成

本システムは、AmazonのFargateを利用し、計算リソースを柔軟に管理します。また、音声テキスト変換にはOpenAIのwhisper-1、要約にはgpt-4を使用します。さらに、X-Twitter APIを利用して自動ツイートを実現し、Amazon ECSとS3を組み合わせてデータの永続的な保存とアクセスを確保します。動画の自動録画はJsonlとts形式で行い、サムネイルキャプチャにはMediaPipeを用いたフィルター実装を行い、半目率を改善しました。

### スクレイピングと検知アルゴリズム

動画配信サイトの新着放送一覧ページをスクレイピングすることで、新しい放送が開始されたかどうかを検知します。この際、特定ユーザーの放送を対象とし、検知されたらまとめ機能に引き渡します。これにより、リアルタイムでの新着情報の取得が可能となります。

### 画像処理とキャプチャ

- サムネイルキャプチャにはMediaPipeを用い、指定した目の範囲を抽出するアルゴリズムを実装します。
```python
eye_indices = {
    "left_eye": [33, 133, 159, 145],
    "right_eye": [362, 263, 386, 374],
}
```
これにより、放送の特徴的な部分を視覚的に捉え、まとめに活用します。

- また、MediaPipeによるフィルター実装により、不適切な内容(半目,汚物など)を検知します。
- 特定の観点で画像を採点し、スコア上位の画像をサムネイルに使用。
```
#指示
☆画像には4枚の写真が含まれています。(左上1,右上2,左下3,右下ム、
とします)
☆以下の「条件」に合致する写真の番号を教えてください。
☆回答には、余計な説明は含める必要はありません。

#条件
☆目が半分閉じているもの

#解答例
1,4

#解答
```

### 音声テキスト変換と要約
- STT変換にはOpenAIのwhisper-1を使用します。要約にはgpt-4Vを利用し、まとめの内容を簡潔に表現します。
- 要約機能はFargateを使用してサーバーレスで実装され、スケーラビリティを確保
- GPT-4 Turbo で入力トークンが増えたのでコメントも投入して解析対象にした
- 暴力的なコメント等があると API が拒否するので事前に moderation API にかけることにした
- 原因不明の放送接続切れ対策で ffmpeg のバージョンを上げるために Docker イメージを更新した (効果不明)
- 明らかな NG コメントは moderation かける前に事前にはじく
- audio を whisper に投げる前に無音部分を検知・取り除く
- transcript の明らかな hallucination は取り除いてから summary 作成に進む
```
Instruction:
* I want you to act as a breaking news tweet.
* The input text is a part of a transcription of a live stream currently on the air.
* Summarize the live stream in a live coverage-ish manner.
* Be sure to refer the live program info below.
* Be sure to follow the constraints below.

LiveProgramlnformation:
* Title: {title}
* Streamer Name: {streamer}

Constraints:
* Must be written in Japanese.
* Must be written in bullet points.
* 3 bullet points at maximum.
* Prefer to use a proper streamer name rather than a common noun tike "Efä%" .
* Don't use any title of honor for person tike " & 'i g */-u", 'i < h," , and so on.
* Must follow the format of the output text template.
* For literary style, refer to the below sample.
* The content of the live program should be inferred from the text fragments, because the machine transcription is inacc
* Summarize only those points that are clearly identifiable as factual. Don't write that the live has ended, since this is a live program in progress.

Common Transcription Inaccuracies:
* Missing words
* Incorrect translations
* Out-of-context information

OutputText
. <Sentence#l,
. <Sentence#2,
. <Sentence#3,

Template:
Most important information in the summarization,
2nd important one,
3rd important one,

# Literary Style Sample:
* {streamer}は___しているようだ。
* {streamer}は___について話しているようだ。
* {streamer}は___について___と主張している。
* {streamer}日く、___は___ということらしい。
* ___という話題が出て{streamer}は___ということを言っている。
* 放送は___な雰囲気で行われているようだ。
* 放送中に___という出来事があったようだ。
* ___というコメントが多く出ている。

lnputText:

{text}

OUtputText:

```


```
#指示:
入力文はライブ配信の書き起こしです。
これを読んで、配信の様子がわかるよう実況風に要約してください。
以下の制約を必ず守ってください。
日本語70-80文字>
日本語70-80文字>
日本語70-80文字>
日本語70-80文字>
日本語70-80文字>
{text}

#入力文:
*出力文テンプレートのフォーマットに従うこと
☆日本語で書くこと

#制約:

#出力文テンプレート:

#出力文:
・く配信の要約文#5′
・く配信の要約文#4′
・く配信の要約文#5′
・く配信の要約文#2′
・く配信の要約文#1′
```

### 自動録画と永続的な保存 (Optional)
動画の自動録画はJsonlとts形式で行い、Amazon ECSを介して永続的な保存を実現します。これにより、将来的にまとめられた情報にアクセスする際にも、動画データを利用できます。

### SNS自動投稿
- まとめたコンテンツはTwitter APIを使用して自動でツイートされる。
- ShadowBan対策に、URLをh抜きにする