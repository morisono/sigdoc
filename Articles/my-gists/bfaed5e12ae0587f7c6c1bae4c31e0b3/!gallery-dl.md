![](https://example.com/gallery-dl-logo.png)

# gallery-dl: ウェブ上の画像ギャラリーをダウンロードするためのツール

`gallery-dl`は、Python製のコマンドラインツールで、ウェブ上の画像ギャラリーやアルバムをダウンロードするための強力なツールです。この記事では、`gallery-dl`の基本的な使い方と便利な機能について説明します。

## インストール

`gallery-dl`をインストールするには、Pythonのパッケージマネージャである`pip`を使用します。

```
pip install gallery-dl
```

## 使い方

gallery-dlを使用してギャラリーをダウンロードするには、以下のようにコマンドを実行します。
```
gallery-dl $url

#-dオプションを使用して、ダウンロード先のディレクトリを指定できます。
gallery-dl -d /path/to/save/directory $url

# --rangeオプションを使用して、ダウンロードする画像の範囲を指定できます。
gallery-dl --range 1-10 $url

# --filterオプションを使用して、特定の条件に合致する画像のみをダウンロードできます。
gallery-dl --filter "width>1920" $url

# (.+\/)([^/\r\n]+)
gallery-dl $1$2 --write-metadata -o skip=true\ngallery-dl $1$2/media --write-metadata -o skip=true\ngallery-dl $1search?q=from:$2 --write-metadata -o skip=true -o "directory=[""twitter"",""{$2}""]"

gallery-dl $1$2 --write-metadata -o skip=true\ngallery-dl $1$2/media --write-metadata -o skip=true\ngallery-dl $1search?q=from:$2 --write-metadata -o skip=true -o "directory=[\"twitter\",\"{$2}\"]"
```


## 設定 [^2]

設定ファイルは `%APPDATA%\gallery-dl\config.json `(Windows),  `/etc/gallery-dl.conf`(Linux) に保存されます。このファイルを編集することで、gallery-dlの動作をカスタマイズできます。

`/etc/gallery-dl.conf`
```json
{
    "extractor": {
        "cookies": ["<your browser (firefox, chromium, etc>"],
        "twitter": {
            "users": "https://twitter.com/{legacy[screen_name]}",
            "text-tweets": true,
            "quoted": true,
            "retweets": true,
            "logout": true,
            "replies": true,
            "filename": "twitter_{author[name]}_{tweet_id}_{num}.{extension}",
            "directory": {
                "quote_id != 0": ["twitter", "{quote_by}", "quote-retweets"],
                "retweet_id != 0": ["twitter", "{user[name]}", "retweets"],
                "": ["twitter", "{user[name}"]
            },
            "postprocessors": [
                {"name": "metadata", "event": "post", "filename": "twitter_{author[name]}_{tweet_id}_main.json"}
            ]
        }
    }
}
```

上記の設定は、gallery-dlを使用してTwitterからメディアをダウンロードするためのサンプル設定です。設定ファイルの詳細については、gallery-dlの公式ドキュメント[^1]を参照してください。

この設定を使用する前に、クッキーと詳細な設定を適切に設定することが重要です。また、環境やニーズに合わせて設定をカスタマイズすることもできます。

[^1]: https://github.com/mikf/gallery-dl
[^2]: https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst
[^3]: https://www.reddit.com/r/DataHoarder/comments/yy8o9w/for_everyone_using_gallerydl_to_backup_twitter/ [^3]