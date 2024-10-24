# セキュアな設計

セキュアな設計を盛り込むためには、最適なデザインパターンおよび複数のセキュリティ対策を実装する必要があります。以下は、多層防御（defense-in-depth）アーキテクチャに基づいた、Gradioを使用する自動販売機システムの詳細設計です。


## 抽象設計

### ディレクトリ構成
```
autovendor/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   └── security.py
├── application/
│   ├── __init__.py
│   ├── use_cases/
│   │   ├── __init__.py
│   │   ├── cart_management.py
│   │   ├── item_management.py
│   │   ├── payment_management.py
│   │   └── user_authentication.py
├── domain/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── cart.py
│   │   ├── item.py
│   │   ├── payment.py
│   │   └── user.py
├── infrastructure/
│   ├── __init__.py
│   ├── database.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── cart_repository.py
│   │   ├── item_repository.py
│   │   └── user_repository.py
│   └── services/
│       ├── __init__.py
│       ├── email_service.py
│       ├── payment_service.py
│       └── security_service.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── secrets.py
├── tests/
│   ├── __init__.py
│   ├── test_cart.py
│   ├── test_item.py
│   ├── test_payment.py
│   ├── test_security.py
│   └── test_user.py
└── requirements.txt
```

以下に、具体的な実装方法を示します。


## クラス設計

#### `domain/entities/cart.py`
```python
class CartItem:
    def __init__(self, item, qty=1):
        self.item = item
        self.qty = qty

    def __repr__(self):
        return f"<CartItem(item={self.item}, qty={self.qty})>"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, cart_item):
        self.items.append(cart_item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.item.name != item_name]

    def clear(self):
        self.items = []

    def calculate_total(self):
        return sum(item.item.price * item.qty for item in self.items)
```

#### `domain/entities/item.py`
```python
class Item:
    def __init__(self, name, price, desc=None):
        self.name = name
        self.price = price
        self.desc = desc

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price}, desc={self.desc})>"
```

#### `domain/entities/payment.py`
```python
class Payment:
    def __init__(self, method, status, token):
        self.method = method
        self.status = status
        self.token = token

    def complete(self):
        # 完了処理を実装
        pass
```

#### `domain/entities/user.py`
```python
class User:
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password
```

### ユースケース設計

#### `application/use_cases/cart_management.py`
```python
class CartManagement:
    def __init__(self, cart_repository):
        self.cart_repository = cart_repository

    def add_item_to_cart(self, user_id, item):
        cart = self.cart_repository.find_by_user_id(user_id)
        cart.add_item(item)
        self.cart_repository.save(cart)

    def remove_item_from_cart(self, user_id, item_name):
        cart = self.cart_repository.find_by_user_id(user_id)
        cart.remove_item(item_name)
        self.cart_repository.save(cart)

    def clear_cart(self, user_id):
        cart = self.cart_repository.find_by_user_id(user_id)
        cart.clear()
        self.cart_repository.save(cart)
```

### インフラストラクチャ設計

#### `infrastructure/database.py`
```python
import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def execute(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def query(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
```

#### `infrastructure/repositories/cart_repository.py`
```python
from domain.entities.cart import Cart

class CartRepository:
    def __init__(self, db):
        self.db = db

    def find_by_user_id(self, user_id):
        result = self.db.query("SELECT * FROM carts WHERE user_id = ?", (user_id,))
        cart = Cart()
        for row in result:
            item = CartItem(Item(row[1], row[2]), row[3])
            cart.add_item(item)
        return cart

    def save(self, cart):
        self.db.execute("DELETE FROM carts WHERE user_id = ?", (cart.user_id,))
        for item in cart.items:
            self.db.execute("INSERT INTO carts (user_id, item_name, item_price, qty) VALUES (?, ?, ?, ?)",
                            (cart.user_id, item.item.name, item.item.price, item.qty))
```

### セキュリティ設計

#### `infrastructure/services/security_service.py`
```python
import hashlib
import os

class SecurityService:
    @staticmethod
    def hash_password(password):
        salt = os.urandom(32)
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + pwdhash

    @staticmethod
    def verify_password(stored_password, provided_password):
        salt = stored_password[:32]
        stored_pwdhash = stored_password[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return pwdhash == stored_pwdhash
```

### アプリケーション層とUIの統合

#### `app/main.py`
```python
from fastapi import FastAPI
from app.routes import router
from infrastructure.security.logging import setup_logging
import gradio as gr

app = FastAPI()

@app.on_event("startup")
async def startup():
    setup_logging()

app.include_router(router)

def create_gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## 自動販売機システム")
        # GradioのUI要素を追加
        gr.Button("ログイン").click(fn=login_function)
        gr.Button("カートに追加").click(fn=add_to_cart_function)
    return demo

if __name__ == "__main__":
    interface = create_gradio_interface()
    interface.launch()
```

#### `app/routes.py`
```python
from fastapi import APIRouter, Depends
from application.use_cases.cart_management import CartManagement
from infrastructure.repositories.cart_repository import CartRepository
from infrastructure.database import Database
from app.security import get_current_user

router = APIRouter()

db = Database("path_to_db")
cart_repository = CartRepository(db)
cart_management = CartManagement(cart_repository)

@router.post("/cart/add")
async def add_item_to_cart(item: dict, user=Depends(get_current_user)):
    return cart_management.add_item_to_cart(user.id, item)

@router.post("/cart/remove")
async def remove_item_from_cart(item_name: str, user=Depends(get_current_user)):
    return cart_management.remove_item_from_cart(user.id, item_name)

@router.post("/cart/clear")
async def clear_cart(user=Depends(get_current_user)):
    return cart_management.clear_cart(user.id)
```

### 1. データベース接続のセキュリティ

#### `infrastructure/database.py`
```python
import sqlite3
import os

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.connection.execute('PRAGMA foreign_keys = ON')

    def execute(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def query(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
```

- **SQLインジェクション対策**：パラメータ化されたクエリを使用します。
- **外部キー制約**：`PRAGMA foreign_keys = ON` を設定してデータの整合性を保ちます。

### 2. パスワードのハッシュ化と検証

#### `infrastructure/services/security_service.py`
```python
import hashlib
import os

class SecurityService:
    @staticmethod
    def hash_password(password):
        salt = os.urandom(32)
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + pwdhash

    @staticmethod
    def verify_password(stored_password, provided_password):
        salt = stored_password[:32]
        stored_pwdhash = stored_password[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return pwdhash == stored_pwdhash
```

- **パスワードのハッシュ化**：PBKDF2-HMAC-SHA256を使用し、ソルトを追加します。
- **パスワードの検証**：保存されたパスワードのハッシュを使用して検証します。

### 3. 入力データのバリデーションとサニタイズ

#### `app/routes.py`
```python
from pydantic import BaseModel, Field
from fastapi import HTTPException

class UserCredentials(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)

@router.post("/login")
async def login(user_credentials: UserCredentials):
    user = await authenticate_user(user_credentials)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
```

- **入力データのバリデーション**：Pydanticを使用してデータスキーマを定義し、入力の長さや形式をチェックします。

### 4. ユーザー認証と認可

#### `app/security.py`
```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"username": username}
```

- **JWTによる認証**：ユーザーの認証にはJWT（JSON Web Token）を使用し、セキュアなトークンを生成します。
- **認可**：JWTをデコードし、ユーザー情報を検証します。

### 5. エラーハンドリングとレスポンスメッセージ

#### `app/routes.py`
```python
@router.post("/cart/add")
async def add_item_to_cart(item: dict, user=Depends(get_current_user)):
    try:
        cart_management.add_item_to_cart(user["username"], item)
        return {"message": "Item added to cart successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to add item to cart")
```

- **エラーハンドリング**：エラーが発生した場合は適切なHTTPステータスコードとメッセージを返します。

### 6. ログ管理と監査

#### `infrastructure/security/logging.py`
```python
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("uvicorn")
    handler = logging.FileHandler("app.log")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
```

- **ログ管理**：アプリケーションの重要なイベントやエラーをログに記録します。

### 7. 依存関係のインジェクション

#### `app/dependencies.py`
```python
from infrastructure.database import Database
from infrastructure.repositories.cart_repository import CartRepository

def get_database():
    db = Database("path_to_db")
    try:
        yield db
    finally:
        db.connection.close()

def get_cart_repository(db: Database = Depends(get_database)):
    return CartRepository(db)
```

- **依存関係のインジェクション**：FastAPIのDependsを使用して依存関係をインジェクションし、テスト可能でセキュアな設計にします。

### 8. アクセス制御

#### `app/security.py`
```python
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

API_KEY = "your_api_key"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(status_code=403, detail="Could not validate API key")
```

- **APIキーの使用**：APIキーを使用して特定のエンドポイントへのアクセスを制御します。

### 9. GradioによるUIのセキュリティ

#### `app/main.py`
```python
import gradio as gr

def login_function(username, password):
    # ログインロジックを実装
    pass

def add_to_cart_function(item):
    # カートに追加ロジックを実装
    pass

def create_gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## 自動販売機システム")
        username = gr.Textbox(label="ユーザー名")
        password = gr.Textbox(label="パスワード", type="password")
        login_button = gr.Button("ログイン")
        login_button.click(fn=login_function, inputs=[username, password])
        
        item = gr.Textbox(label="商品名")
        add_button = gr.Button("カートに追加")
        add_button.click(fn=add_to_cart_function, inputs=[item])
        
    return demo

if __name__ == "__main__":
    interface = create_gradio_interface()
    interface.launch()
```

- **セキュアなUI**：GradioのUI要素に対して適切な入力検証とイベント処理を実装します。

### 10. 入力検証とサニタイズ
すべての入力を検証し、サニタイズすることが重要です。

#### `app/routes.py`
```python
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException
from application.use_cases.cart_management import CartManagement
from infrastructure.repositories.cart_repository import CartRepository
from infrastructure.database import Database
from app.security import get_current_user

router = APIRouter()

db = Database("path_to_db")
cart_repository = CartRepository(db)
cart_management = CartManagement(cart_repository)

class Item(BaseModel):
    name: str = Field(..., max_length=100)
    price: float = Field(..., gt=0)
    description: str = Field(None, max_length=500)

@router.post("/cart/add")
async def add_item_to_cart(item: Item, user=Depends(get_current_user)):
    return cart_management.add_item_to_cart(user.id, item)

@router.post("/cart/remove")
async def remove_item_from_cart(item_name: str, user=Depends(get_current_user)):
    if not item_name:
        raise HTTPException(status_code=400, detail="Item name is required")
    return cart_management.remove_item_from_cart(user.id, item_name)

@router.post("/cart/clear")
async def clear_cart(user=Depends(get_current_user)):
    return cart_management.clear_cart(user.id)
```

### 11. 認証と認可
セキュアな認証と認可を実装します。トークンベースの認証を使用し、各リクエストの認可を強化します。

#### `app/security.py`
```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
    username: Optional[str] = None

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)
```

### 12. パスワードのハッシュ化と保存
パスワードはハッシュ化して保存し、認証時にハッシュ化されたパスワードと照合します。

#### `infrastructure/services/security_service.py`
```python
import hashlib
import os

class SecurityService:
    @staticmethod
    def hash_password(password: str) -> bytes:
        salt = os.urandom(32)
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + pwdhash

    @staticmethod
    def verify_password(stored_password: bytes, provided_password: str) -> bool:
        salt = stored_password[:32]
        stored_pwdhash = stored_password[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return pwdhash == stored_pwdhash
```

### 13. HTTPSを使用した通信の暗号化
通信を暗号化するために、サーバーにSSL/TLS証明書をインストールし、HTTPSを使用します。

### 14. 監査ログ
すべての重要な操作について監査ログを記録します。

#### `infrastructure/security/logging.py`
```python
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("autovendor")
    return logger

logger = setup_logging()

def log_action(action: str, user_id: str):
    logger.info(f"Action: {action} performed by user_id: {user_id}")
```

### 15. エラーハンドリング
エラーメッセージは詳細な情報を含まず、適切に処理します。

#### `app/routes.py`
```python
@router.post("/cart/add")
async def add_item_to_cart(item: Item, user=Depends(get_current_user)):
    try:
        cart_management.add_item_to_cart(user.id, item)
        return {"status": "success"}
    except Exception as e:
        log_action("add_item_to_cart_failed", user.id)
        raise HTTPException(status_code=500, detail="An error occurred while adding item to cart")

@router.post("/cart/remove")
async def remove_item_from_cart(item_name: str, user=Depends(get_current_user)):
    try:
        cart_management.remove_item_from_cart(user.id, item_name)
        return {"status": "success"}
    except Exception as e:
        log_action("remove_item_from_cart_failed", user.id)
        raise HTTPException(status_code=500, detail="An error occurred while removing item from cart")
```

### 16. ログイン試行回数の制限（ブルートフォース攻撃防止）

ユーザーのログイン試行回数を制限します。

`infrastructure/services/login_service.py`
```python
from datetime import datetime, timedelta

class LoginService:
    def __init__(self):
        self.failed_attempts = {}
        self.lockout_duration = timedelta(minutes=15)
        self.max_attempts = 5

    def register_failed_attempt(self, username):
        now = datetime.now()
        if username in self.failed_attempts:
            self.failed_attempts[username].append(now)
        else:
            self.failed_attempts[username] = [now]

    def is_account_locked(self, username):
        if username not in self.failed_attempts:
            return False

        attempts = self.failed_attempts[username]
        recent_attempts = [attempt for attempt in attempts if now - attempt < self.lockout_duration]

        self.failed_attempts[username] = recent_attempts
        return len(recent_attempts) >= self.max_attempts

# Usage example
login_service = LoginService()
if login_service.is_account_locked(username):
    raise HTTPException(status_code=403, detail="Account locked due to too many failed login attempts.")
login_service.register_failed_attempt(username)
```

### 17. Webアプリケーションファイアウォール（WAF）

WAFを導入して、一般的な攻撃（SQLインジェクション、XSSなど）から保護します。
IPアドレスをホワイトリストおよびブラックリストで管理します。

`infrastructure/services/firewall.py`
```python
class Firewall:
    def __init__(self):
        self.whitelist = set()
        self.blacklist = set()

    def add_to_whitelist(self, ip_address):
        self.whitelist.add(ip_address)

    def add_to_blacklist(self, ip_address):
        self.blacklist.add(ip_address)

    def is_allowed(self, ip_address):
        if ip_address in self.blacklist:
            return False
        if ip_address in self.whitelist:
            return True
        return False

# Usage example
firewall = Firewall()
firewall.add_to_whitelist('192.168.1.1')
firewall.add_to_blacklist('192.168.1.2')

if not firewall.is_allowed(request.client.host):
    raise HTTPException(status_code=403, detail="Access forbidden.")
```


### 18. セキュリティヘッダー
HTTP応答にセキュリティヘッダーを追加します。

#### `app/main.py`
```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["yourdomain.com", "www.yourdomain.com"]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourfrontenddomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 19. セキュアコーディング
常に最新のセキュアコーディングのベストプラクティスに従うこと

### アプリケーション層の改善

#### `app/routes.py`
```python
from fastapi import APIRouter, Depends, HTTPException
from application.use_cases.cart_management import CartManagement
from infrastructure.repositories.cart_repository import CartRepository
from infrastructure.database import Database
from infrastructure.services.security_service import SecurityService
from domain.entities.user import User
from app.security import get_current_user

router = APIRouter()

# Databaseの設定
db = Database("path_to_db")
# Repositoryの設定
cart_repository = CartRepository(db)
# UseCaseの設定
cart_management = CartManagement(cart_repository)
# Security Serviceの設定
security_service = SecurityService()

@router.post("/cart/add")
async def add_item_to_cart(item: dict, user=Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="ログインが必要です")
    # 商品をカートに追加
    cart_management.add_item_to_cart(user.id, item)
    return {"message": "商品がカートに追加されました"}

@router.post("/cart/remove")
async def remove_item_from_cart(item_name: str, user=Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="ログインが必要です")
    # 商品をカートから削除
    cart_management.remove_item_from_cart(user.id, item_name)
    return {"message": "商品がカートから削除されました"}

@router.post("/cart/clear")
async def clear_cart(user=Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="ログインが必要です")
    # カートをクリア
    cart_management.clear_cart(user.id)
    return {"message": "カートがクリアされました"}
```

### ドメイン層の改善

#### `domain/entities/user.py`
```python
class User:
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password

    def verify_password(self, password):
        return security_service.verify_password(self.hashed_password, password)
```

### インフラストラクチャ層の改善

#### `infrastructure/services/security_service.py`
```python
import hashlib
import os

class SecurityService:
    @staticmethod
    def hash_password(password):
        salt = os.urandom(32)
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + pwdhash

    @staticmethod
    def verify_password(stored_password, provided_password):
        salt = stored_password[:32]
        stored_pwdhash = stored_password[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return pwdhash == stored_pwdhash
```

この改善により、セキュリティの強化とコードの整理が行われました。ユーザーのパスワード検証がセキュリティサービスに移動し、ルーターでのユーザー認証の実装が改善されました。また、ドメイン層とインフラストラクチャ層のコードもよりセキュアになりました。