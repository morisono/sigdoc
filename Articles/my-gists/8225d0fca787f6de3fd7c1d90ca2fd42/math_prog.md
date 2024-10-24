# 支払額最小化(最適化問題)

最も支払額が少なくなる支払通貨・購入回数・組み合わせのパターンを次のyaml形式で教えて。

pay: # 購入回: 複数回に分けてもよい
  - cart: # 商品組み合わせ
  - currency: # 支払通貨
  - count: # 購入回数
  - cost: # 小計
pay:
pay:
...
total-cost: # 総計

以下はAliexpressセールの買い物です。

rate_USD-JPY: 151.30 # 為替レート
cart: 
  - iCopy-XS: # 商品名
    - price: $313.30 # 支払額
  - Proxmark3:
    - price: ¥5400
  - ChameleonUltra Devkit:
    - price: ¥8186
  - ChameleonUltra:
    - price: $74.94
  - Lock-pick:
    - price: $2.92
    - shipping: $1.99 # 送料
  - DIYFIX Store:
    - price: $3.27

coupon:
- currency: USD # 通貨
  - code: None
    - discount: 4 # 割引額
    - min: 20 # 条件購入額
    - max: 16 # 最大割引額
  - code: '11SALE8'
    - discount: 8
    - min: 50 
  - code: '11SALE15'
    - discount: 40
    - min: 100
  - code: '11SALE30'
    - discount: 30
    - min: 200
  - code: '11SALE50'
    - discount: 40
    - min: 250
  - code: '11SALE100'
    - discount: 100
    - min: 500
    
- currency: JPY
  - code: None
    - discount: 500
    - step: 2500
    - max: 2000
  - coupon: '11SALE8'
    - discount: 500
    - min: 2500
  - coupon: '11SALE15'
    - discount: 1000
    - min: 100
  - coupon: '11SALE30'
    - discount: 1500
    - min: 7500
  - coupon: '11SALE50'
    - discount: 2000
    - min: 10000
  - coupon: '11SALE100'
    - discount: 15000
    - min: 79000

