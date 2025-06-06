# Pineスクリプトでのシンプルなインジケータ作成チュートリアル

## ステップ1: Pineスクリプトのバージョンを宣言する
まず最初に、使用するPineスクリプトのバージョンを宣言します。最新バージョンのPineスクリプトを使用することをお勧めします。

```pinescript
//@version=4
```

ステップ2: インジケータの設定を定義する
次に、インジケータの基本設定を定義します。これには、インジケータのタイトルやオーバーレイの設定などが含まれます。
```
study(title="My Simple MA Indicator", shorttitle="MSMAI", overlay=true)
```

ステップ3: パラメータを定義する
次に、移動平均線の期間を定義します。これはユーザーがインジケータの設定で変更できるようにするためのものです。
```
length = input(14, title="Length")
```

ステップ4: 計算を行う
次に、移動平均線を計算します。この例では、終値の単純移動平均を計算します。
```
sma = sma(close, length)
```

ステップ5: 結果をプロットする
最後に、計算した移動平均線をチャートにプロットします。
```
plot(sma, title="SMA", color=color.red)
```

以上で、シンプルな移動平均線インジケータの作成が完了しました。このスクリプトをTradingViewのPineエディタに貼り付けて保存すると、チャート上に移動平均線が表示されます。