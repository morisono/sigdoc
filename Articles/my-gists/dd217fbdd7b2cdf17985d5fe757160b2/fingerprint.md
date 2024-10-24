# フィンガープリント

## 1. フィンガープリントとは
フィンガープリントは、指紋（を採る）、拇印という意味の英単語で、IT分野では人物や端末などの識別や同定、真正性の確認に用いられる短いデータ列などを指すことが多い[^1^][2][^2^][3]。

## 2. フィンガープリントの種類
フィンガープリントは、実は何かひとつの固有の情報のことではなく複数の情報の総称です。大きく分けると3種類あります[^3^][1]。
- そのデバイスで利用しているソフトウェアに関する情報
    - 例：ユーザーエージェント（利用OS、ブラウザのバージョンなどが分かる情報群のこと）／ブラウザ設定言語など
- そのデバイスのスペックに関する情報
    - 例：CPUの情報、スピーカーやマイクの数、スクリーンサイズなど
- ネットワークに関連する情報
    - 例：IPアドレス、リファラー（直前に見ていたページのURL）など

## 3. フィンガープリントの利用
フィンガープリント自体は昔から存在していたものですが、その活用用途が「Cookieの代替方法」として着目されてきたことで、ブラウザ側はCookie同様、フィンガープリントへの対策も強化しつつあります[^3^][1]。

## 4. フィンガープリントの弱点
フィンガープリントは「時と場合によって精度が落ちることもある」ことが弱点だと言えます[^3^][1]。

- request
```json
{
  "getUserAgent": true,
  "getScreenResolution": true
}
```

- response
```json
{
  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
  "screenResolution": "1920x1080"
}
```

- imprement
```
var userAgent = navigator.userAgent;

var screenResolution = window.screen.width + "x" + window.screen.height;

console.log("User Agent: " + userAgent);
console.log("Screen Resolution: " + screenResolution);
```