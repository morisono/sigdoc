`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -nodes`


```
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:
```

```
組み込まれる情報の入力を求められます
証明書リクエストに追加します。
これから入力しようとしているのは、識別名または DN と呼ばれるものです。
かなりの数のフィールドがありますが、いくつかのフィールドを空白のままにすることもできます
一部のフィールドにはデフォルト値があります。
「.」を入力した場合、フィールドは空白のままになります。
-----
国名 (2 文字コード) [AU]:
州名または県名 (フルネーム) [Some-State]:
地域名 (市など) []:
組織名 (例: 会社) [Internet Widgits Pty Ltd]:
組織単位名 (セクションなど) []:
共通名 (サーバーの FQDN またはあなたの名前など) []:
電子メールアドレス []：
```