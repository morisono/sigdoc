オニオンアーキテクチャに従った自動販売機の実装サンプルコードを作成します。まずは、下位レイヤーから上位レイヤーに向かって実装していきます。

### 1. エンティティ (Domain)
- エンティティを定義
#### `domain/entities/user.py`

```python
class User:
    def __init__(self, user_id: str, username: str, hashed_password: str):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
```

#### `domain/entities/cart.py`

```python
class Cart:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.items = []

    def add_item(self, item: dict):
        self.items.append(item)

    def remove_item(self, item_id: str):
        self.items = [item for item in self.items if item['id'] != item_id]

    def clear(self):
        self.items = []

    def get_items(self):
        return self.items
```

### 2. ユースケース (Application)

#### `application/use_cases/authenticate_user.py`
- ユースケース層のインターフェースを定義
```python
from domain.repositories import UserRepository

class AuthenticateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_credentials: dict):
        username = user_credentials.get('username')
        password = user_credentials.get('password')
        user = self.user_repository.find_by_username(username)
        if user and user.hashed_password == hash(password):
            return user
        return None
```

#### `application/use_cases/manage_cart.py`
- ユースケース層の具象実装を作成
```python
from domain.repositories import CartRepository

class ManageCart:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    async def add_item_to_cart(self, user_id: str, item: dict):
        cart = self.cart_repository.find_by_user_id(user_id)
        if cart:
            cart.add_item(item)
        else:
            cart = Cart(user_id)
            cart.add_item(item)
        self.cart_repository.save(cart)
        return cart

    async def remove_item_from_cart(self, user_id: str, item_id: str):
        cart = self.cart_repository.find_by_user_id(user_id)
        if cart:
            cart.remove_item(item_id)
            self.cart_repository.save(cart)
        return cart

    async def clear_cart(self, user_id: str):
        cart = self.cart_repository.find_by_user_id(user_id)
        if cart:
            cart.clear()
            self.cart_repository.save(cart)
        return cart
```

### 3. インフラストラクチャ (Infrastructure)

#### `infrastructure/repositories/user_repository_impl.py`
- インフラストラクチャ層のリポジトリインターフェースを定義
```python
from domain.repositories import UserRepository
from domain.entities.user import User

class UserRepositoryImpl(UserRepository):
    def __init__(self):
        # データベース接続などの初期化処理
        pass

    def find_by_username(self, username: str) -> User:
        # データベースからユーザーを取得するロジック
        pass
```

#### `infrastructure/repositories/cart_repository_impl.py`
- インフラストラクチャ層のリポジトリ具象実装を作成
```python
from domain.repositories import CartRepository
from domain.entities.cart import Cart

class CartRepositoryImpl(CartRepository):
    def __init__(self):
        # データベース接続などの初期化処理
        pass

    def find_by_user_id(self, user_id: str) -> Cart:
        # データベースからユーザーのカートを取得するロジック
        pass

    def save(self, cart: Cart):
        # カートをデータベースに保存するロジック
        pass
```

### 4. プレゼンテーション (Presentation)

#### `presentation/controllers/auth_controller.py`
- プレゼンテーション層のルーティングを定義
```python
from fastapi import APIRouter, Depends
from application.use_cases.authenticate_user import AuthenticateUser
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter()
authenticate_user_use_case = AuthenticateUser(UserRepositoryImpl())

@router.post("/login")
async def login(user_credentials: dict):
    return await authenticate_user_use_case.execute(user_credentials)
```

#### `presentation/controllers/cart_controller.py`

```python
from fastapi import APIRouter, Depends
from application.use_cases.manage_cart import ManageCart
from infrastructure.repositories.cart_repository_impl import CartRepositoryImpl

router = APIRouter()
manage_cart_use_case = ManageCart(CartRepositoryImpl())

@router.post("/cart/add")
async def add_to_cart(user_id: str, item: dict):
    return await manage_cart_use_case.add_item_to_cart(user_id, item)

@router.post("/cart/remove")
async def remove_from_cart(user_id: str, item_id: str):
    return await manage_cart_use_case.remove_item_from_cart(user_id, item_id)

@router.post("/cart/clear")
async def clear_cart(user_id: str):
    return await manage_cart_use_case.clear_cart(user_id)
```

### 5. アプリケーション

- ルーターをアプリケーションに追加
#### `application/main.py`
```python
from fastapi import FastAPI
from presentation.controllers.auth_controller import router as auth_router

app = FastAPI()

app.include_router(auth_router)
```

このように、オニオンアーキテクチャではビジネスロジックが中心に配置され、外側に向かってインフラストラクチャやプレゼンテーション層が配置されます。各レイヤーは他のレイヤーに依存しないようになっており、疎結合で柔軟性が高いシステムを構築することができます。