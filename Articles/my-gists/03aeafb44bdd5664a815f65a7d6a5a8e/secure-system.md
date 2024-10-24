# セキュアなシステム設計

セキュアなシステムを設計するためには、多層防御（Defense in Depth）戦略を採用することが重要です。以下に、セキュアな「要塞」システムを構築するための構成を示します。これには、ネットワークセキュリティ、アプリケーションセキュリティ、データベースセキュリティ、監視・ログ、エンドポイントセキュリティなど、各レイヤーでのセキュリティ対策が含まれます。

## 主なセキュリティ対策

#### 1. ネットワークセキュリティの強化
- **ゼロトラストモデル:** ネットワークの内部と外部を問わず、すべてのリソースに対して厳密な認証とアクセス制御を実施。
- **侵入防止システム (IPS):** ファイアウォールと連携して、ネットワーク内の悪意のあるアクティビティを検出して防止。
- **DNSセキュリティ:** DNSクエリの監視とフィルタリングを行い、悪意のあるドメインへのアクセスを防ぐ。
- **ネットワーク分離とセグメンテーション**: **DMZ (非武装地帯) セグメント:** 外部からのアクセスを受ける公開サービスを配置。内部ネットワークとのアクセスを制限。
- **内部ネットワーク:** 非公開の内部サービスやデータベースサーバーを配置。アクセスはDMZや特定のVPN接続からのみ許可。
- **管理ネットワーク:** 管理用のアクセスを別のセグメントに分離。管理者のみアクセス可能。
- **ファイアウォール**: 外部ネットワークと内部ネットワークの間にファイアウォールを配置し、必要最小限のポートのみを開放。アプリケーション層ファイアウォール (WAF) を導入して、アプリケーションレベルの攻撃を防止。
- **VPN (仮想プライベートネットワーク)**: リモートアクセスはVPN経由で行い、強力な認証と暗号化を使用。

#### 2. アプリケーションセキュリティの強化
- **認証と認可**: 多要素認証 (MFA) を使用し、ユーザーの本人確認を強化。ロールベースアクセス制御 (RBAC) を実装し、ユーザーのアクセス権限を厳密に管理。
- **入力検証**: すべてのユーザー入力を厳密に検証し、SQLインジェクションやクロスサイトスクリプティング（XSS）などの攻撃を防止。
- **セキュアコーディング:** OWASPトップ10の脅威を防ぐためのセキュアコーディングプラクティスを導入。
- **セキュリティパッチ**: アプリケーションや依存ライブラリのセキュリティパッチを定期的に適用。
- **コードレビューとセキュリティテスト:** 静的解析、動的解析、ペネトレーションテストを実施。
- **セッション管理:** セッションタイムアウト、セッション固定攻撃防止、セッションIDの安全な管理。

#### 3. データベースセキュリティの強化
- **データベース監査:** すべてのデータベース操作を監査し、ログに記録。
- **データマスキング:** テスト環境や開発環境で使用するデータのマスキング。
- **動的データ暗号化:** アプリケーションレベルでの動的データ暗号化の導入。

#### 4. 監視とログの強化
- **侵入検知システム (IDS):** ネットワークおよびホストベースの侵入検知システムを導入。
- **リアルタイムアラート:** 重大なセキュリティイベントに対するリアルタイムアラートを設定。
- **インシデント対応**: セキュリティインシデント対応計画 (IRP) を策定し、インシデント発生時の対応手順を明確にする。
- **監査ログ**: データベースの操作を監査し、不正アクセスや異常な操作を記録。
- **ログの保管:** 監査目的でログを安全な場所に保管し、規制に準拠。
- **セキュリティ情報およびイベント管理 (SIEM)**: SIEMシステムを導入し、リアルタイムのセキュリティ監視、異常検知、ログの集中管理を実施。
- **アクセス制御**: 最小権限の原則 (Principle of Least Privilege) を適用し、ユーザーやアプリケーションのデータベースアクセスを必要最小限に制限。

#### 5. エンドポイントセキュリティの強化
- **パッチ管理:** すべてのエンドポイントで最新のセキュリティパッチを適用。
- **デバイス制御:** 未承認のデバイスがネットワークに接続するのを防止。
- **モバイルデバイス管理 (MDM):** モバイルデバイスのセキュリティを管理。
- **エンドポイント検出と対応 (EDR)**: エンドポイントにEDRソリューションを導入し、マルウェアや攻撃の検出と対応を自動化。
- **アンチウイルスとマルウェア対策**: アンチウイルスソフトウェアを全てのエンドポイントにインストールし、定期的にスキャンを実施。

#### 6. バックアップとリカバリの強化
- **オフサイトバックアップ:** 物理的に異なる場所にバックアップを保管。
- **バックアップの暗号化:** バックアップデータも暗号化して保存。定期的なリストアテストを行う。
- **定期的なDRテスト:** ディザスタリカバリの計画を定期的にテストし、復旧時間目標 (RTO) と復旧時点目標 (RPO) を確認。

#### 7. セキュリティ教育と訓練の強化
- **フィッシングシミュレーション:** 定期的にフィッシングテストを実施し、従業員の対応を評価。
- **セキュリティワークショップ:** 専門家を招いてセキュリティに関するワークショップを開催。
- **継続的な教育:** セキュリティに関する継続的な教育プログラムを実施。


### ディレクトリ構成

以下は、具体的なディレクトリ構成と各層のコード例です。

```
my_secure_system/
├── app/
│   ├── routes.py
│   ├── dependencies.py
│   ├── main.py
├── application/
│   ├── use_cases/
│   │   ├── authenticate_user.py
│   │   ├── manage_cart.py
│   │   ├── manage_form.py
├── domain/
│   ├── entities/
│   │   ├── user.py
│   │   ├── cart.py
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── cart_repository.py
│   │   ├── form_repository.py
├── infrastructure/
│   ├── repositories/
│   │   ├── user_repository_impl.py
│   │   ├── cart_repository_impl.py
│   │   ├── form_repository_impl.py
│   ├── security/
│   │   ├── encryption.py
│   │   ├── logging.py
│   │   ├── firewall.py
├── config/
│   ├── settings.py
│   ├── secrets.py
└── tests/
    ├── test_auth.py
    ├── test_cart.py
    ├── test_form.py
```

### ドメイン層

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

#### `domain/repositories/user_repository.py`
```python
from abc import ABC, abstractmethod
from domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def find_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User):
        pass
```

#### `domain/repositories/cart_repository.py`
```python
from abc import ABC, abstractmethod
from domain.entities.cart import Cart

class CartRepository(ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> Cart:
        pass

    @abstractmethod
    def save(self, cart: Cart):
        pass
```

#### `domain/repositories/form_repository.py`
```python
from abc import ABC, abstractmethod

class FormRepository(ABC):
    @abstractmethod
    def save_form_data(self, form_data: dict):
        pass
```

### アプリケーション層

#### `application/use_cases/authenticate_user.py`
```python
from domain.repositories.user_repository import UserRepository

class AuthenticateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_credentials: dict):
        username = user_credentials.get('username')
        password = user_credentials.get('password')
        user = self.user_repository.find_by_username(username)
        if user and user.hashed_password == password:
            return user
        return None
```

#### `application/use_cases/manage_cart.py`
```python
from domain.repositories.cart_repository import CartRepository
from domain.entities.cart import Cart

class ManageCart:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    async def add_item_to_cart(self, user_id: str, item: dict):
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
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

#### `application/use_cases/manage_form.py`
```python
from domain.repositories.form_repository import FormRepository

class ManageForm:
    def __init__(self, form_repository: FormRepository):
        self.form_repository = form_repository

    async def submit_form(self, form_data: dict):
        self.form_repository.save_form_data(form_data)
        return {"message": "Form submitted successfully"}
```

### インフラストラクチャ層

#### `infrastructure/repositories/user_repository_impl.py`
```python
from domain.repositories.user_repository import UserRepository
from domain.entities.user import User

class UserRepositoryImpl(UserRepository):
    def __init__(self):
        self.users = {}  # In-memory storage for simplicity

    def find_by_username(self, username: str) -> User:
        return self.users.get(username)

    def save(self, user: User):
        self.users[user.username] = user
```

#### `infrastructure/repositories/cart_repository_impl.py`
```python
from domain.repositories.cart_repository import CartRepository
from domain.entities.cart import Cart

class CartRepositoryImpl(CartRepository):
    def __init__(self):
        self.carts = {}  # In-memory storage for simplicity

    def find_by_user_id(self, user_id: str) -> Cart:
        return self.carts.get(user_id)

    def save(self, cart: Cart):
        self.carts[cart.user_id] = cart
```

#### `infrastructure/repositories/form_repository_impl.py`
```python
from domain.repositories.form_repository import FormRepository

class FormRepositoryImpl(FormRepository):
    def __init__(self):
        self.forms = []  # In-memory storage for simplicity

    def save_form_data(self, form_data: dict):
        self.forms.append(form_data)
```

#### `infrastructure/security/encryption.py`
```python
from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self, key: str):
        self.cipher = Fernet(key)

    def encrypt(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)

    def decrypt(self, encrypted_data: bytes) -> bytes:
        return self.cipher.decrypt(encrypted_data)
```

#### `infrastructure/security/logging.py`
```python
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("system.log"),
                                  logging.StreamHandler()])

def log_security_event(event: str):
    logger = logging.getLogger('security')
    logger.info(event)
```

#### `infrastructure/security/firewall.py`
```python
import ipaddress

class Firewall:
    def __init__(self):
        self.allowed_ips = set()

    def allow_ip(self, ip: str):
        self.allowed_ips.add(ipaddress.ip_network(ip))

    def is_ip_allowed(self, ip: str) -> bool:
        ip_addr = ipaddress.ip_address(ip)
        return any(ip_addr in network for network in self.allowed_ips)
```

### プレゼンテーション層

#### `app/dependencies.py`
```python
from infrastructure.security.encryption import EncryptionService
from infrastructure.security.firewall import Firewall

encryption_service = EncryptionService(key='your-secret-key-here')
firewall = Firewall()

def get_encryption_service():
    return encryption_service

def get_firewall():
    return firewall
```

#### `app/routes.py`
```python
from fastapi import APIRouter, Depends, HTTPException
from application.use_cases.authenticate_user import AuthenticateUser
from application.use_cases.manage_cart import ManageCart
from application.use_cases.manage_form import ManageForm
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from infrastructure.repositories.cart_repository_impl import CartRepositoryImpl
from infrastructure.repositories.form_repository_impl import FormRepositoryImpl
from app.dependencies import get_encryption_service, get_firewall

router = APIRouter()
authenticate_user_use_case = AuthenticateUser(UserRepositoryImpl())
manage_cart_use_case = ManageCart(CartRepositoryImpl())
manage_form_use_case = ManageForm(FormRepositoryImpl())

@router.post("/login")
async def login(user_credentials: dict, encryption_service=Depends(get_encryption_service)):
    encrypted_password = encryption_service.encrypt(user_credentials['password'].encode())
    user_credentials['password'] = encrypted_password.decode()
    user = await authenticate_user_use_case.execute(user_credentials)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@router.post("/cart/add")
async def add_to_cart(user_id: str, item: dict):
    return await manage_cart_use_case.add_item_to_cart(user_id, item)

@router.post("/cart/remove")
async def remove_from_cart(user_id: str,

 item_id: str):
    return await manage_cart_use_case.remove_item_from_cart(user_id, item_id)

@router.post("/cart/clear")
async def clear_cart(user_id: str):
    return await manage_cart_use_case.clear_cart(user_id)

@router.post("/form")
async def submit_form(form_data: dict):
    return await manage_form_use_case.submit_form(form_data)
```

#### `app/main.py`
```python
from fastapi import FastAPI
from app.routes import router
from infrastructure.security.logging import setup_logging

app = FastAPI()

@app.on_event("startup")
async def startup():
    setup_logging()

app.include_router(router)
```

### 設定ファイル

#### `config/settings.py`
```python
import os

class Settings:
    DB_USER = os.getenv("DB_USER", "your_db_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "your_db_password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "your_db_name")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

settings = Settings()
```

#### `config/secrets.py`
```python
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
```

### テスト

#### `tests/test_auth.py`
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def user_data():
    return {"username": "test_user", "password": "test_password"}

def test_login(user_data):
    response = client.post("/login", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}
```

#### `tests/test_cart.py`
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def cart_data():
    return {"user_id": "test_user", "item": {"id": "item1", "name": "test_item"}}

def test_add_to_cart(cart_data):
    response = client.post("/cart/add", json=cart_data)
    assert response.status_code == 200

def test_remove_from_cart(cart_data):
    response = client.post("/cart/add", json=cart_data)
    assert response.status_code == 200
    response = client.post("/cart/remove", json={"user_id": "test_user", "item_id": "item1"})
    assert response.status_code == 200

def test_clear_cart(cart_data):
    response = client.post("/cart/add", json=cart_data)
    assert response.status_code == 200
    response = client.post("/cart/clear", json={"user_id": "test_user"})
    assert response.status_code == 200
```

#### `tests/test_form.py`
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def form_data():
    return {"field1": "value1", "field2": "value2"}

def test_submit_form(form_data):
    response = client.post("/form", json=form_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Form submitted successfully"}
```

以上がセキュアな自動販売機システムの完全なスクリプトです。この構成は、オニオンアーキテクチャの原則に従い、各層が独立しており、依存関係を注入してテスト可能な設計となっています。また、セキュリティ対策を各層で実施し、全体的なセキュリティを強化しています。