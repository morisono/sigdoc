# コンテンツ作成ガイド - Terminal Recording

この記事では、以下の内容について説明します。

- asciinema/aggとffmpegを使ったターミナル画面の録画

## asciinema

asciinemaは、ターミナルのセッションを記録し、再生するためのオープンソースのソフトウェアです。以下に、asciinemaのインストールと使用方法を示します。

1. asciinemaをインストールします。
```sh
brew install asciinema
```

2. asciinemaを使用して、ターミナルセッションを記録します。
```sh
# Start recording
asciinema rec # Ctrl + D to exit
```

## agg

`asciinema/agg`は、asciinemaターミナルレコーダーによって生成されたasciicast v2ファイルからアニメーションGIFファイルを生成するためのコマンドラインツールです。以下に、`asciinema/agg`のインストールと使用方法を示します。

```bash
# Install agg
cargo install --git https://github.com/asciinema/agg

# Generate GIF
agg demo.cast demo.gif
```

## ffmpeg
ffmpegは、動画や音声を記録・変換・再生するためのフリーソフトウェアで、ターミナルから操作をすることができます。以下に、ffmpegを使って変換する方法を示します。

```sh
# Install ffmpeg
brew install ffmpeg

# Convert gif to mp4
ffmpeg -i demo.gif -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" demo.mp4

```

このコマンドは、`demo.gif`を`demo.mp4`に変換します。


https://github.com/asciinema

https://github.com/asciinema/agg