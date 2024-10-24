オニオンアーキテクチャの実装サンプルコードを以下のステップに従って生成します。

### Step 1: ドメイン層のエンティティを定義

```python
# core/entities/user.py

class User:
    def __init__(self, user_id: str, username: str, hashed_password: str):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
```

### Step 2: ユースケース層のインターフェースを定義

```python
# core/use_cases/authenticate_user.py

from abc import ABC, abstractmethod
from core.entities.user import User

class AuthenticateUserUseCase(ABC):
    @abstractmethod
    async def execute(self, username: str, password: str) -> User:
        pass
```

### Step 3: ユースケース層の具象実装を作成

```python
# application/use_cases/authenticate_user_impl.py

from core.use_cases.authenticate_user import AuthenticateUserUseCase
from core.interfaces.repositories import UserRepository
from core.entities.user import User

class AuthenticateUserUseCaseImpl(AuthenticateUserUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, username: str, password: str) -> User:
        user = await self.user_repository.find_by_username(username)
        if user and user.hashed_password == hash_password(password):
            return user
        return None
```

### Step 4: インフラストラクチャ層のリポジトリインターフェースを定義

```python
# core/interfaces/repositories.py

from abc import ABC, abstractmethod
from core.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    async def find_by_username(self, username: str) -> User:
        pass
```

### Step 5: インフラストラクチャ層のリポジトリ具象実装を作成

```python
# infrastructure/repositories/user_repository_impl.py

from core.interfaces.repositories import UserRepository
from core.entities.user import User

class UserRepositoryImpl(UserRepository):
    async def find_by_username(self, username: str) -> User:
        # データベースからユーザーを検索するロジック
        pass
```

### Step 6: プレゼンテーション層のルーティングを定義

```python
# presentation/controllers/auth_controller.py

from fastapi import APIRouter, Depends
from core.use_cases.authenticate_user_impl import AuthenticateUserUseCaseImpl
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    user_repository = UserRepositoryImpl()
    authenticate_user_use_case = AuthenticateUserUseCaseImpl(user_repository)
    user = await authenticate_user_use_case.execute(username, password)
    if user:
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
```

### Step 7: ルーターをアプリケーションに追加

```python
# src/app/main.py

from fastapi import FastAPI
from presentation.controllers.auth_controller import router as auth_router

app = FastAPI()

app.include_router(auth_router)
```

これで、オニオンアーキテクチャの一部である各レイヤーが適切なファイル名で実装されました。各層は疎結合であり、それぞれが特定の役割を果たしています。