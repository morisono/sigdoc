# ソフトウェア設計・アーキテクチャ

次の例、自動販売機システムの設計は、以下の設計思想とディレクトリ構成が最適です。このシステムでは、認証、カートシステム、フォーム入力、ファイル保存、Email自動返信、アクセスログの管理を行います。

## 設計思想

### SOLID原則

SOLIDは、ロバート・C・マーチン（Uncle Bob）が提唱した5つの設計原則の頭文字を取ったものです。これらの原則は、ソフトウェア設計における柔軟性、保守性、拡張性を向上させるためのコードを書く際の具体的な指針です。

1. **単一責任の原則 (Single Responsibility Principle, SRP)**:
 1つのクラスは1つの責任のみを持つべきであり、クラスが変更される理由は1つだけであるべきです。これにより、クラスがシンプルで保守しやすくなります。

2. **オープン・クローズドの原則 (Open-Closed Principle, OCP)**:
 ソフトウェアのエンティティ（クラス、モジュール、関数など）は、拡張に対して開かれており、修正に対して閉じているべきです。新しい機能を追加する場合は、既存のコードを変更するのではなく、拡張することで行います。

3. **リスコフの置換原則 (Liskov Substitution Principle, LSP)**:
 サブタイプ（派生クラスやインタフェースの実装クラス）は、その親タイプ（基底クラスやインタフェース）の代替物として振る舞うことができなければなりません。つまり、サブタイプは親タイプと互換性があり、同じように振る舞うべきです。

4. **インタフェース分離の原則 (Interface Segregation Principle, ISP)**:
 クライアントは、自分が使わないメソッドに依存すべきではありません。インタフェースは、クライアントが必要とする機能にのみ依存するように設計されるべきです。インタフェースは、クライアントに必要な機能だけを提供するべきです。

5. **依存関係逆転の原則 (Dependency Inversion Principle, DIP)**:
 高レベルのモジュールは、低レベルのモジュールに依存すべきではなく、両方は抽象に依存するべきです。また、具体的な実装ではなく、抽象に依存すべきです。これにより、システムの柔軟性が向上し、変更に対する耐性が向上します。


### オニオンアーキテクチャ

オニオンアーキテクチャ (Onion Architecture)は、ジェフリー・パーマーが提案したアーキテクチャスタイルで、クリーンアーキテクチャと非常に似ていますが、依存関係を「内側から外側に向かって」の一方向に限定する点が特徴です。

1. **中心にドメイン**: エンティティとドメインサービス(ビジネスロジック)が中心に位置する。外部に依存しません。
2. **依存性の方向**: 内側から外側への依存性。インターフェースが内側、実装が外側。
3. **レイヤー構造**: ドメイン、アプリケーション、インフラストラクチャ、プレゼンテーションのレイヤーが存在。

オニオンアーキテクチャは、SOLID原則をよく満たした設計であるといえます。

## 他の候補

### クリーンアーキテクチャ

クリーンアーキテクチャ(Clean Architecture)は、ロバート・C・マーチン（Uncle Bob）によって提唱されたアーキテクチャスタイルです。

1. **依存性のルール**: 外側のレイヤーは内側のレイヤーに依存してもよいが、逆は不可。
2. **エンティティ(Entities):**: ビジネスルールやドメインオブジェクトを表現します。システムの中心的な部分であり、他のレイヤーに依存しません。
3. **ユースケース(Use Cases)**: アプリケーション固有のビジネスルールを含みます。エンティティを使用して、特定のユースケースを実現します。
4. **インターフェース・アダプタース (Interface Adapters)**: コントローラー、プレゼンター、ゲートウェイなど、外部とのインターフェースを担います。データをユースケースやエンティティが理解できる形式に変換します。
5. **フレームワークとドライバー (Frameworks & Drivers)**: Webフレームワーク、データベース、外部サービスなどのインフラストラクチャに依存する部分です。システムの外周に位置し、他のレイヤーから依存されますが、他のレイヤーには依存しません。

クリーンアーキテクチャは、保守性が高く、テストしやすいコードを実現します。

### レイヤードアーキテクチャ（N層アーキテクチャ）:
   - 伝統的な方法であり、プレゼンテーション層、ビジネスロジック層、データアクセス層に分かれます。
   - 簡単に理解できるが、レイヤー間の依存関係が強くなることがある。

### ヘキサゴナルアーキテクチャ (Hexagonal Architecture)
- またの名をポート＆アダプターアーキテクチャ。
- アプリケーションのコアロジックを外部から隔離し、コアに対する入出力をポートとして定義し、アダプターがそれを実装する。
- 入力アダプター：ユーザーインターフェースやAPIエンドポイント。
- 出力アダプター：データベースや外部サービスとの接続。
- コアロジックが外部依存から独立。テストが容易で、柔軟性が高い。
- 初期学習コストがある。設計の複雑さが増すことがある。
- 中規模から大規模なエンタープライズシステムなどに適する。

### サーバーレスアーキテクチャ (Serverless Architecture)
- 開発者はサーバー管理を意識せずにコードを実行できる。FaaS (Function as a Service) プラットフォームを使用して、小さな関数をデプロイする。
- サーバー管理の手間が省ける。自動スケーリングと支払いが実行回数に基づくため、コスト効率が高い。
- レスポンス時間が不安定になる場合がある。ベンダーロックインのリスクがある。
- イベント駆動型アプリケーションやバックエンドサービスなどに適する。

### イベント駆動アーキテクチャ (Event-Driven Architecture)
- 各アクションやイベント（ユーザーログイン、アイテム追加）などのシステムの状態変更をイベントとして発行し、他のコンポーネントがそれにリアクティブに反応する。メッセージングキューやイベントストリームを使用。
- 高度なスケーラビリティと柔軟性が求められる場合に有効。システムの柔軟性が向上し、リアクティブな処理が可能。
疎結合な設計が実現できる。
- イベントの順序や重複処理の管理が難しい。イベントの可視化やトラッキングが複雑。
- リアルタイムデータ処理や大規模分散システムなどに適する。

### マイクロサービスアーキテクチャ
- 各機能（認証、カート、メール送信など）を独立したサービスとして実装し、それぞれが独立してデプロイおよびスケールできる。
- サービス間の通信はHTTP/RESTやメッセージングキューを使用する。
- 独立したデプロイとスケーリングが可能。各サービスが小さいため、理解しやすく保守しやすい。技術スタックの多様性が許容される。
- サービス間の通信が複雑になる可能性がある。トランザクション管理が難しい。
- 大規模なエンタープライズシステムやクラウドネイティブアプリケーションなどに適する。

### CQRS（Command Query Responsibility Segregation）

- コマンド（書き込み）とクエリ（読み取り）を分離するアーキテクチャ。自動販売機システムにおいて、書き込み操作（カートへのアイテム追加、フォーム入力の保存など）と読み取り操作（カート内容の表示、フォームデータの表示など）を分けて実装することができます。
- イベントソーシング: システムの状態をイベントのシーケンスとして保存する。
- 書き込みと読み取りのスケーラビリティが向上。過去の状態を再構築可能で、監査やデバッグに有用。
- 実装が複雑。一貫性の管理が難しい。
- 金融システムや監査が重要なシステムなどに適する。

## 結論

クリーンアーキテクチャとオニオンアーキテクチャはどちらも上記の自動販売機システムに適しています。特にクリーンアーキテクチャは、依存性の方向や層の分離が明確で、保守性と拡張性が高いため推奨されます。他の候補としてマイクロサービスアーキテクチャやCQRSも考慮できますが、システムの規模や要求に応じて選択することが重要です。


## サンプルコード

以下に、サンプルコードの一部を実装します。


#### `core/entities/user.py`

```python
class User:
    def __init__(self, user_id: str, username: str, hashed_password: str):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
```

#### `core/use_cases/authenticate_user.py`

```python
from core.interfaces.repositories import UserRepository

class AuthenticateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username: str, password: str):
        user = self.user_repository.find_by_username(username)
        if user and user.hashed_password == hash_password(password):
            return user
        return None
```

#### `app/controllers/auth_controller.py`

```python
from fastapi import APIRouter, Depends
from core.use_cases.authenticate_user import AuthenticateUser
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    user_repository = UserRepositoryImpl()
    authenticate_user_use_case = AuthenticateUser(user_repository)
    user = authenticate_user_use_case.execute(username, password)
    if user:
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
```

#### `app/main.py`

```python
from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_db()
    load_web_ui()
    load_api()
    # 他の初期化処理

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_connection()
    # 他のシャットダウン処理

app.include_router(router)
```

#### `app/routes.py`

```python
from fastapi import APIRouter, Depends
from application.use_cases import authenticate_user, add_to_cart, save_form_data
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/login")
async def login(user_credentials: dict):
    return await authenticate_user(user_credentials)

@router.post("/cart")
async def add_item_to_cart(item: dict, user=Depends(get_current_user)):
    return await add_to_cart(user, item)

@router.post("/form")
async def submit_form(form_data: dict):
    return await save_form_data(form_data)
```

#### `infrastructure/database/models.py`

```python
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

# 他のモデル定義

def init_db():
    Base.metadata.create_all(bind=engine)
```

#### `application/use_cases.py`

```python
from domain.repositories import UserRepository, CartRepository
from domain.entities import User, Cart

async def authenticate_user(credentials: dict) -> User:
    # 認証ロジック
    pass

async def add_to_cart(user: User, item: dict) -> Cart:
    # カートにアイテムを追加するロジック
    pass

async def save_form_data(form_data: dict):
    # フォームデータを保存するロジック
    pass
```

#### `infrastructure/email/email_service.py`

```python
import smtplib
from email.mime.text import MIMEText

def send_email(to: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "noreply@example.com"
    msg["To"] = to

    with smtplib.SMTP("localhost") as server:
        server.sendmail("noreply@example.com", [to], msg.as_string())
```

## ディレクトリ構成・適用

### クリーンアーキテクチャ

- `python create_structure_clean.py`

### オニオンアーキテクチャ

- `python create_structure_onion.py`

## ディレクトリ構成(縮小版）

### クリーンアーキテクチャ

```
vending_machine_system/
│
├── core/
│   ├── entities/
│   ├── usecases/
│   ├── repositories/
│   └── __init__.py
│
├── interface_adapters/
│   ├── controllers/
│   ├── gateways/
│   ├── presenters/
│   └── __init__.py
│
├── frameworks_and_drivers/
│   ├── database/
│   ├── web/
│   ├── email/
│   ├── logging/
│   └── __init__.py
│
└── app/
    ├── __init__.py
    ├── main.py
    ├── config.py
    ├── routes.py
    ├── dependencies.py
    └── errors.py
```

### オニオンアーキテクチャ

```
vending_machine_system/
│
├── domain/
│   ├── entities/
│   ├── services/
│   └── __init__.py
│
├── application/
│   ├── use_cases/
│   ├── dto/
│   └── __init__.py
│
├── infrastructure/
│   ├── database/
│   ├── email/
│   ├── logging/
│   └── __init__.py
│
├── interface/
│   ├── controllers/
│   ├── views/
│   └── __init__.py
│
└── app/
    ├── __init__.py
    ├── main.py
    ├── config.py
    ├── routes.py
    ├── dependencies.py
    └── errors.py
```

### 結論

クリーンアーキテクチャまたはオニオンアーキテクチャは、要件に適しており、特にビジネスロジックの分離とテスタビリティを向上させるために有効です。どちらのアーキテクチャも、他の候補（マイクロサービスアーキテクチャ、ヘキサゴナルアーキテクチャ、Event-Driven Architecture）と比べて、モノリシックなアプローチながら柔軟で保守性の高いシステムを構築するのに適しています。

どちらのアーキテクチャを選ぶかは、チームの経験やプロジェクトの特定のニーズに依存しますが、上記のディレクトリ構成例に基づいて、クリーンアーキテクチャまたはオニオンアーキテクチャを採用するのが良いでしょう。