オニオンアーキテクチャに基づいて、自動販売機システムの実装サンプルコードを生成します。まずはドメイン層から始めます。

### 1. ドメイン層

#### `domain/entities/user.py`

```python
class User:
    def __init__(self, user_id: str, username: str, hashed_password: str):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
```

#### `domain/entities/item.py`

```python
class Item:
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price
```

### 2. サービス層

#### `application/use_cases/authenticate_user.py`

```python
from domain.repositories import UserRepository

class AuthenticateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username)
        if user and user.hashed_password == hash_password(password):
            return True
        return False
```

#### `application/use_cases/add_to_cart.py`

```python
from domain.repositories import CartRepository

class AddToCart:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    async def execute(self, user_id: str, item_id: str) -> bool:
        # カートにアイテムを追加するロジック
        pass
```

#### `application/use_cases/save_form_data.py`

```python
class SaveFormData:
    def __init__(self, form_repository: FormRepository):
        self.form_repository = form_repository

    async def execute(self, form_data: dict) -> bool:
        # フォームデータを保存するロジック
        pass
```

### 3. インフラ層

#### `infrastructure/repositories/user_repository.py`

```python
from domain.repositories import UserRepository
from domain.entities import User

class UserRepositoryImpl(UserRepository):
    def find_by_username(self, username: str) -> User:
        # ユーザーをデータベースから取得するロジック
        pass
```

#### `infrastructure/repositories/cart_repository.py`

```python
from domain.repositories import CartRepository
from domain.entities import Cart

class CartRepositoryImpl(CartRepository):
    def add_item(self, user_id: str, item_id: str) -> None:
        # カートにアイテムを追加するロジック
        pass
```

#### `infrastructure/repositories/form_repository.py`

```python
from domain.repositories import FormRepository

class FormRepositoryImpl(FormRepository):
    def save(self, form_data: dict) -> None:
        # フォームデータをデータベースに保存するロジック
        pass
```

これで各層ごとに適切なファイルが生成されました。次に、これらのコンポーネントを組み合わせてアプリケーションを構築するインフラ層の実装を行います。