# 業務情報を埋め込むために例外をキャッチ＆スロー

```py
# RuntimeExceptionに業務情報を詰めて、それをスローします。
# スタックトレースに例外情報が含まれるため、エラーが発生した箇所を追跡できます。
# 行数以外にもIDやキーのような情報を含めることをお勧めします。
# メソッドやクラスが分かれている場合、必要な業務情報を取り出せる場所が限られるため、
# 例外を入れ子にし、メッセージを埋め込んで親にエスカレーションさせる必要があります。
# RuntimeExceptionに限らず、適切な既存例外やSystemException、BusinessExceptionのような独自例外を使用することも検討してください。

names = ["Nanoha.Takamachi", "Vivio.Takamachi", "Fate"]
upper_names = []
lower_names = []

try:
    for name in names:
        upper_names.append(name.split(".")[1].upper())
except Exception as ex:
    raise RuntimeError(f"upper_names.size={len(upper_names)}", ex)
finally:
    print("System.exit(1)")

try:
    for name in names:
        lower_names.append(name.split(".")[1].lower())
except Exception as ex:
    raise RuntimeError(f"lower_names.size={len(lower_names)}", ex)
finally:
    print("System.exit(1)")
```

## データをスキップするために例外をキャッチ

```py
# バッチの中には数十分から数時間かかるジョブもあります。
# データ読み込み時に不正なデータ行がある場合、ある程度内容が分かっており、
# かつ個別修復が業務影響がないものに関してはその行をスキップすることがあります。
# この場合、意図的に例外を捨てる挙動を採用しますが、
# スキップさせたくない場合以外には行わないように注意してください。

def parse(line):
    # ダミーのparseメソッド。実際の処理に置き換えてください。
    pass

with open("pom.xml", "r", encoding="utf-8") as file:
    proc_count = 0
    skip_count = 0
    for line in file:
        try:
            parse(line)
            proc_count += 1
        except UnicodeDecodeError as ex:
            skip_count += 1
            print(f"WARN: Skip: line={line}")
    print(f"End Job, proc={proc_count}, skip={skip_count}")

# 重要なのはExceptionなどの大本のクラスではなく、できるだけ限定された例外を指定することです。
# いつもの問題と思ってスキップしていたら別の問題だったというケースもありますので、注意が必要です。
# また、処理した数とスキップした数をログに出力すると良いです。
# JavaではRuntimeExceptionを継承していないExceptionは検査例外なので、catchかthrowをしないとコンパイルエラーになります。
# まずは、シンプルに原則的にメソッドには`throws Exception`をつけることが一般的です。
# 次がRuntimeExceptionやUncheckedIOExceptionでラッピングする方法です。
```