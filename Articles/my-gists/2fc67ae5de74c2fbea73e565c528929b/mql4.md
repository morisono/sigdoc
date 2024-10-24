# MQLでのシンプルなインジケータ作成チュートリアル

## ステップ1: インジケータの設定を定義する
まず最初に、インジケータの基本設定を定義します。これには、インジケータのタイトルやオーバーレイの設定などが含まれます。

```mql
#property indicator_chart_window
#property indicator_buffers 1
#property indicator_color1 Blue
```

ステップ2: グローバル変数を定義する
次に、移動平均線の期間を定義します。これはユーザーがインジケータの設定で変更できるようにするためのものです。
```
int length = 14;
double ma[];
```

ステップ3: 初期化関数を定義する
次に、初期化関数を定義します。この関数では、インジケータバッファの設定を行います。
```
int init() {
   SetIndexBuffer(0, ma);
   SetIndexStyle(0, DRAW_LINE);
   return(0);
}
```

ステップ4: 計算を行う
次に、移動平均線を計算します。この例では、終値の単純移動平均を計算します。
```
int start() {
   int counted_bars = IndicatorCounted();
   int i, limit;
   if(counted_bars > 0) limit = Bars - counted_bars;
   else limit = Bars - length;
   for(i = 0; i < limit; i++) {
      ma[i] = iMA(NULL, 0, length, 0, MODE_SMA, PRICE_CLOSE, i);
   }
   return(0);
}
```

以上で、シンプルな移動平均線インジケータの作成が完了しました。このスクリプトをMetaTraderのエディタに貼り付けて保存すると、チャート上に移動平均線が表示されます。