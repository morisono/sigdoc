# ハードウェア要件

このプロジェクトにはArduinoボードと10kオームのポテンショメータが必要です。

<div align="center" style="width: 500px; height: 400px; box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);">
  <img width="300" alt="Z45eHnqLlz" src="https://user-images.githubusercontent.com/111455900/270384663-28a9639f-4de3-4d23-8a0b-ae09332ea394.png">
  <p>Arduino Uno Rev 4 Minima ABX00080</p>
  https://jp.rs-online.com/web/p/arduino/2662936?gb=b
  <br>
</div>

- Circuit: ポテンショメータの3つのワイヤーをボードに接続します。外側のピンの一方は接地に、もう一方は5ボルトに接続され、中央のピンはアナログピンA0に接続されます。
- Code: コード部分では、セットアップ関数でボードとコンピュータ間のシリアル通信を開始し、メインループでポテンシ- ョメータからの抵抗値を読み取ります。値は0から1023の範囲で、シリアルモニタウィンドウに表示されます。
- Learn more: さらに基本的なチュートリアルやArduinoプログラミング言語の詳細なコレクションを探索することができます。

## 確認

- 問題の定義: アナログダイヤルの読み取りが必要な場合があります。例えば、化学反応における温度や圧力の計測などです。
- 解決策: オブジェクト検出技術を使用して、アナログ圧力計などのダイヤルの針の先端と基部を検出します。
- 実装手順: 画像のアップロードと注釈付け、ダイヤル機能の検出モデルのトレーニング、ダイヤルの読み取りスクリプトの作成などが含まれます。
- 結論: この記事では、ダイヤルの中心と針の先端を認識するコンピュータビジョンモデルを構築し、トレーニングしました。ダイヤルの角度とPSI（圧力）の相関を特定し、コンピュータビジョンでダイヤル値を読み取るための情報とコードを提供しています。
- アナログとデジタルの統合: この技術は、古いアナログシステムと新しいデジタル技術を統合する際にどのように役立つでしょうか？
- 産業への応用: この技術は、どのような産業や分野で特に有用となると考えられますか？
- セキュリティと信頼性: アナログデータをデジタルに変換するプロセスにおいて、セキュリティや信頼性の問題はどのように考慮されるべきでしょうか？

```
/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1);  // delay in between reads for stability
}
```


## Comfirmed product List

以下は、Amazonで入手可能な一般的なアナログゲージメーターのリストです。

- AC Voltmeter Ammeter 80-260V 100A KT-D135
    - LCDディスプレイのデジタルボルトアンペアメーター
    - 価格: $15.90

- BTMETER BT-770K Auto Ranging Automotive Multimeter
    - Dwell角度、パルス幅、タッチ、温度、デューティサイクル、電圧、電流、抵抗テスト用
    - 価格: $66.99

- Baomain 65C5 Analogue Panel Meter Volt Voltage Gauge
    - アナログボルトメーター、DC 0-15 V
    - 価格: $10.79

- Baomain DH-670 DC 0-50A Analog Amp Panel Meter
    - アナログアンペアパネルメーター、75mVシャント付き
    - 価格: $11.29

- Beslands 6 Pc Telescoping Gage Set
    - 5/16" - 6"範囲、T-ボアホールゲージ
    - 価格: $20.25-$46.80

- LEPEVNEY Analog Dial Panel Meter Voltmeter Gauge SO-45
    - DC 0-30Vラウンド電流測定アンペアメーター
    - 価格: $9.99

- AWELTEC Digital Tire Pressure Gauge 150 PSI
    - 車、トラック、バイク、自転車用
    - 価格: $7.99

- CGELE DC Multifunction Battery Monitor Meter with Shunt
    - 0-200V、0-500A、LCDディスプレイのデジタル電流マルチメーター
    - 価格: $35.99


このリストは、暫定的な要件のみを示しており、他にも多くの互換品が存在します。
