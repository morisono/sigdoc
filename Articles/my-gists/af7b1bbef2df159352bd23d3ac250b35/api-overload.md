APIリクエストを複数のエンドポイントに対して行う場合、共通のロジックを抽象化し、コードの凝集度を高めることは非常に重要です。これにより、コードの重複を減らし、保守性を向上させることができます。以下に、APIリクエストを共通化するための戦略として、継承モデルと設計パターンを活用した実装例を示します。

### 1. ベースクラスの作成

まず、共通のAPIリクエストロジックを含むベースクラスを作成します。

```python
import requests
from abc import ABC, abstractmethod

class BaseAPIClient(ABC):
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def request(self, method, endpoint, params=None, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method,
            url,
            headers=self.headers,
            params=params,
            data=data,
            json=json
        )
        response.raise_for_status()  # エラーがあれば例外を発生させる
        return response.json()

    @abstractmethod
    def specific_request(self, *args, **kwargs):
        pass
```

### 2. 継承クラスの作成

次に、特定のAPIに対するクライアントクラスを作成し、共通のロジックを継承します。

```python
class UserAPIClient(BaseAPIClient):
    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)

    def get_user(self, user_id):
        return self.request("GET", f"/users/{user_id}")

    def create_user(self, user_data):
        return self.request("POST", "/users", json=user_data)

    def update_user(self, user_id, user_data):
        return self.request("PUT", f"/users/{user_id}", json=user_data)

    def specific_request(self, *args, **kwargs):
        # 実装は任意
        pass

class ProductAPIClient(BaseAPIClient):
    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)

    def get_product(self, product_id):
        return self.request("GET", f"/products/{product_id}")

    def create_product(self, product_data):
        return self.request("POST", "/products", json=product_data)

    def update_product(self, product_id, product_data):
        return self.request("PUT", f"/products/{product_id}", json=product_data)

    def specific_request(self, *args, **kwargs):
        # 実装は任意
        pass
```

### 3. クライアントの利用

これで、異なるAPIに対して同様の方法でリクエストを行うことができ、コードの再利用性と保守性が向上します。

```python
if __name__ == "__main__":
    user_client = UserAPIClient(base_url="https://api.example.com", headers={"Authorization": "Bearer token"})
    product_client = ProductAPIClient(base_url="https://api.example.com", headers={"Authorization": "Bearer token"})

    # ユーザーを取得
    user = user_client.get_user(user_id=123)
    print(user)

    # 商品を取得
    product = product_client.get_product(product_id=456)
    print(product)
```
