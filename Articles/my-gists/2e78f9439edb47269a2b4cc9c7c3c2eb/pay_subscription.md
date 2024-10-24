# 決済代行による支払い画面の作成

決済代行を使用して、サブスクリプション支払い画面を作成する方法について説明します。以下のサービスからサブスクリプション支払い画面を作成する手順を取得できます。

## Stripe

Stripeを使用してサブスクリプション支払い画面を作成するには、次の手順に従います。

1. Stripeの[ドキュメンテーション](https://stripe.com/docs/billing/subscriptions/build-subscriptions?ui=embedded-form#set-up-server)を参照します。
2. サーバーサイドで必要な設定とAPI呼び出しを実装します。
3. フロントエンドでStripeのUIコンポーネントを組み込んでサブスクリプション支払い画面を表示します。

以下はStripeによるサブスクリプション支払い画面を作成するためのコードブロックの一部です。

```py
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_09l3shTSTKHYCzzZZsiLl2vA"

stripe.checkout.Session.create(
  mode="subscription",
  line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}],
  ui_mode="embedded",
  return_url="https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
)
```


## PayPal

PayPalも多くのオンライン支払いオプションを提供しています。PayPalサブスクリプション支払い画面の作成方法については、[PayPalのヘルプページ](https://www.paypal.com/jp/cshelp/article/paypal%E3%82%B5%E3%83%96%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E4%BD%9C%E6%88%90%E3%81%8A%E3%82%88%E3%81%B3%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95) をご覧ください。

## Square

Squareは小売業者向けの決済ソリューションを提供しています。Squareでサブスクリプションビジネスを始める方法については、[Squareの公式ウェブサイト](https://squareup.com/jp/ja/townsquare/starting-subscription-business) を参照してください。

## PayPay

PayPayは日本の決済サービスで、継続的な支払いをサポートしています。PayPayでの継続的な支払いの設定方法については、[PayPayの公式ドキュメンテーション](https://www.paypay.ne.jp/opa/doc/jp/v1.0/continuous_payments) をご確認ください。

これらのサービスを使用して、支払い画面を作成し、顧客にサブスクリプションや継続的な支払いオプションを提供できます。各サービスの公式ドキュメンテーションを参照して、具体的な手順やコード例を確認してください。
