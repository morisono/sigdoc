# 仕様書

セキュアでパフォーマンス最適化されたSPA（Single Page Application）自動販売機の設計を、オニオンアーキテクチャに基づいて詳細に説明し、適切なディレクトリ配置も行います。以下に、ステップバイステップで設計の改善を行います。

### オニオンアーキテクチャの概要
オニオンアーキテクチャでは、システムは複数のレイヤーに分割されます。これにより、関心の分離が行われ、システムの変更が容易になります。以下のレイヤーを定義します：
1. **ドメイン層**：ビジネスロジックとルールを含む
2. **アプリケーション層**：ユースケースやサービスを含む
3. **インフラストラクチャ層**：データベース、外部API、メールサーバーなど
4. **プレゼンテーション層**：UIやAPIエンドポイントを含む

### 改善されたクラス設計

#### ドメイン層

```python
# domain/models.py
class Item:
    def __init__(self, name: str, price: float, desc: str = None):
        self.name = name
        self.price = price
        self.desc = desc

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, desc={self.desc})"


class CartItem(Item):
    def __init__(self, item: Item, qty: int = 1):
        super().__init__(item.name, item.price, item.desc)
        self.qty = qty

    def __repr__(self):
        return f"CartItem(name={self.name}, price={self.price}, qty={self.qty})"

# domain/services.py
class Payment:
    def __init__(self, method: str, status: str, token: str):
        self.method = method
        self.status = status
        self.token = token

    def complete(self):
        self.status = "completed"

# domain/entities.py
class State:
    def __init__(self, params: dict):
        self.__dict__.update(params)

    def __getattr__(self, name):
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
```

#### アプリケーション層

```python
# application/use_cases.py
class CartService:
    def __init__(self, cart_repository, payment_service):
        self.cart_repository = cart_repository
        self.payment_service = payment_service

    def add_item(self, user_id: str, item: Item, qty: int):
        cart = self.cart_repository.find_by_user_id(user_id)
        cart.add(CartItem(item, qty))
        self.cart_repository.save(cart)

    def remove_item(self, user_id: str, item_id: str):
        cart = self.cart_repository.find_by_user_id(user_id)
        cart.remove(item_id)
        self.cart_repository.save(cart)

    def complete_payment(self, user_id: str, payment_info):
        cart = self.cart_repository.find_by_user_id(user_id)
        total = cart.calc_total()
        payment = self.payment_service.process_payment(payment_info, total)
        if payment.status == "completed":
            cart.clear()
            self.cart_repository.save(cart)

# application/services.py
class AuthenticationService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str):
        user = self.user_repository.find_by_username(username)
        if user and user.check_password(password):
            return user
        raise Exception("Authentication failed")
```

#### インフラストラクチャ層

```python
# infrastructure/db.py
import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def execute(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.fetchall()

# infrastructure/repositories.py
class UserRepositoryImpl:
    def __init__(self, database):
        self.database = database

    def find_by_username(self, username: str):
        result = self.database.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        )
        if result:
            return User(result[0])  # Assuming a User class exists

class CartRepositoryImpl:
    def __init__(self, database):
        self.database = database

    def find_by_user_id(self, user_id: str):
        result = self.database.execute(
            "SELECT * FROM carts WHERE user_id = ?", (user_id,)
        )
        if result:
            return Cart(result[0])  # Assuming a Cart class exists

    def save(self, cart):
        # Convert cart object to database record and save
        pass

# infrastructure/email.py
import smtplib
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, to, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.smtp_user
        msg['To'] = to

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.smtp_user, [to], msg.as_string())
```

#### プレゼンテーション層

```python
# presentation/routes.py
from fastapi import APIRouter, Depends
from application.use_cases import CartService, AuthenticationService
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/login")
async def login(user_credentials: dict):
    auth_service = AuthenticationService()
    user = auth_service.authenticate(user_credentials['username'], user_credentials['password'])
    return user

@router.post("/cart")
async def add_item_to_cart(item: dict, user=Depends(get_current_user)):
    cart_service = CartService()
    cart_service.add_item(user.id, item['item'], item['qty'])
    return {"message": "Item added to cart"}

@router.post("/cart/remove")
async def remove_item_from_cart(item_id: str, user=Depends(get_current_user)):
    cart_service = CartService()
    cart_service.remove_item(user.id, item_id)
    return {"message": "Item removed from cart"}

@router.post("/form")
async def submit_form(form_data: dict):
    form_repository = FormRepositoryImpl()
    form_repository.save_form_data(form_data)
    return {"message": "Form submitted successfully"}
```

### ディレクトリ構成

```
project_root/
├── app/
│   ├── __init__.py
│   ├── dependencies.py
│   ├── main.py
│   └── routes.py
├── domain/
│   ├── __init__.py
│   ├── entities.py
│   ├── models.py
│   └── services.py
├── application/
│   ├── __init__.py
│   ├── use_cases.py
│   └── services.py
├── infrastructure/
│   ├── __init__.py
│   ├── db.py
│   ├── repositories.py
│   └── email.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_cart.py
│   └── test_form.py
└── requirements.txt
```

### セキュリティ要件とパフォーマンス最適化の考慮
1. **セキュリティ要件**
    - パスワードのハッシュ化と復号化には強力なアルゴリズムを使用。
    - ユーザー認証にはJWTトークンを使用し、セッション管理を行う。
    - ファイアウォールでIPフィルタリングを実施。
    - 入力データのバリデーションとサニタイズを行う。

2. **パフォーマンス最適化**
    - 非同期通信を使用して、データベースアクセスや外部API呼び出しの待ち時間を短縮。
    - キャッシュを利用して頻繁にアクセスされるデータを高速化。
    - データベースクエリを最適化し、必要なインデックスを追加。
    - コンテンツ配信ネットワーク（CDN）を使用して、静的リソースの提供を高速化。

この設計により、セキュリティを確保しつつ、パフォーマンスを最大化した自動販売機システムを実現できます。