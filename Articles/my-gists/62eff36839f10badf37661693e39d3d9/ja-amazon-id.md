# Tracking ID, Associate ID

AmazonのトラッキングIDやアソシエイトIDを検索するため, Amazon自体が提供している機能を利用することで、一部の情報を取得することが可能です。

- **Amazonアソシエイトセントラル**⁴: ここでは、すでに取得済みのトラッキングIDの一覧を見ることができます。新しいトラッキングIDを追加するには「トラッキングIDを追加」ボタンをクリックします⁴。

- **Amazonの配送状況追跡**¹⁵: Amazonで商品を注文すると発送時に「トラッキングID」と呼ばれる問い合わせ番号が付与され、配送業者のページでより詳しい配送状況を確認できるほか、Amazonや配送業者への問い合わせなどにも利用できます¹。

これらの機能を利用することで、AmazonのトラッキングIDやアソシエイトIDに関する一部の情報を取得することが可能です。ただし、これらの機能はIDの管理や配送状況の追跡に限定されており、特定のURLからIDを抽出するという具体的な機能は提供されていないようです。

そのため、特定のURLからAmazonのトラッキングIDやアソシエイトIDを抽出するためには、Pythonなどのプログラミング言語を使用して自分でコードを書く必要があります。これに関して何か他にご質問がありましたら、お気軽にお知らせください。😊

Source: Conversation with Bing, 5/6/2024
- (1) アソシエイト・セントラル. https://affiliate.amazon.co.jp/help/node/topic/GJDYPQZK6E37RLPU.
- (2) Amazon「トラッキングID」とは？ 配送の追跡や問い合わせ、再 .... https://appllio.com/amazon-tracking-id.
- (3) AmazonのトラッキングIDから配送状況を追跡・確認する方法 .... https://mag.app-liv.jp/archive/142215/.
- (4) AmazonアソシエイトのトラッキングIDとは？トラッキングIDを追加 .... https://sigezo.xsrv.jp/amazon-tracking.
- (5) 知っておきたい！AmazonアソシエイトのトラッキングIDの使い方 .... https://agousa.com/amazon-tracking-id/.

```
from urllib.parse import urlparse, parse_qs

def find_ids_in_url(url):
    # URLを解析します
    parsed_url = urlparse(url)
    
    # クエリパラメータを抽出します
    params = parse_qs(parsed_url.query)
    
    # トラッキングIDとアソシエイトIDを探します
    tracking_id = params.get('tracking_id', [None])[0]
    associate_id = params.get('associate_id', [None])[0]
    
    return tracking_id, associate_id

# テスト用のURL
url = "https://www.amazon.co.jp/dp/B08F7W5K8G?tracking_id=12345&associate_id=67890"

# IDを検索します
tracking_id, associate_id = find_ids_in_url(url)

print(f"Tracking ID: {tracking_id}")
print(f"Associate ID: {associate_id}")
```