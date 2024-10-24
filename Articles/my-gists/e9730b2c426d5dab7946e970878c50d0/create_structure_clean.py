import os

def create_dir_structure(base_dir):
    # ディレクトリのリスト
    dirs = [
        "src",  # プロジェクトのソースコードのルートディレクトリ
        "src/app",  # アプリケーション層のディレクトリ
        "src/app/controllers",  # コントローラを格納するディレクトリ（ルートハンドラ）
        "src/app/gateways",  # 外部サービスやインフラとのインターフェースを提供するゲートウェイ
        "src/app/presenters",  # プレゼンテーションロジックを担当するディレクトリ
        "src/app/views",  # ビュー（テンプレートや静的ファイル）を格納するディレクトリ
        "src/core",  # ビジネスロジックやユースケースのためのディレクトリ
        "src/core/entities",  # エンティティクラスを格納するディレクトリ
        "src/core/use_cases",  # ユースケースを実装するディレクトリ
        "src/core/interfaces",  # インターフェースを定義するディレクトリ
        "src/infrastructure",  # インフラストラクチャ層のディレクトリ
        "src/infrastructure/database",  # データベース接続やモデルを格納するディレクトリ
        "src/infrastructure/email",  # メール送信ロジックを格納するディレクトリ
        "src/infrastructure/logging",  # ロギング関連の実装を格納するディレクトリ
        "src/infrastructure/file_storage",  # ファイルストレージ関連の実装を格納するディレクトリ
        "tests",  # テストコードを格納するディレクトリ
        "tests/unit",  # ユニットテストを格納するディレクトリ
        "tests/integration",  # 統合テストを格納するディレクトリ
        "tests/e2e",  # エンドツーエンドテストを格納するディレクトリ
    ]

    # ファイルのリスト
    files = [
        "src/__init__.py",  # srcディレクトリをPythonパッケージとして扱うためのファイル
        "src/main.py",  # アプリケーションのエントリポイント
        "src/config.py",  # アプリケーションの設定を管理するファイル
        "src/app/__init__.py",  # appディレクトリをPythonパッケージとして扱うためのファイル
        "src/app/controllers/__init__.py",  # controllersディレクトリをPythonパッケージとして扱うためのファイル
        "src/app/controllers/auth_controller.py",  # 認証に関するコントローラを実装するファイル
        "src/app/gateways/__init__.py",  # gatewaysディレクトリをPythonパッケージとして扱うためのファイル
        "src/app/presenters/__init__.py",  # presentersディレクトリをPythonパッケージとして扱うためのファイル
        "src/app/views/__init__.py",  # viewsディレクトリをPythonパッケージとして扱うためのファイル
        "src/core/__init__.py",  # coreディレクトリをPythonパッケージとして扱うためのファイル
        "src/core/entities/__init__.py",  # entitiesディレクトリをPythonパッケージとして扱うためのファイル
        "src/core/entities/user.py",  # ユーザーエンティティを定義するファイル
        "src/core/use_cases/__init__.py",  # use_casesディレクトリをPythonパッケージとして扱うためのファイル
        "src/core/use_cases/authenticate_user.py",  # ユーザー認証ユースケースを実装するファイル
        "src/core/interfaces/__init__.py",  # interfacesディレクトリをPythonパッケージとして扱うためのファイル
        "src/infrastructure/__init__.py",  # infrastructureディレクトリをPythonパッケージとして扱うためのファイル
        "src/infrastructure/database/__init__.py",  # databaseディレクトリをPythonパッケージとして扱うためのファイル
        "src/infrastructure/database/models.py",  # データベースモデルを定義するファイル
        "src/infrastructure/email/__init__.py",  # emailディレクトリをPythonパッケージとして扱うためのファイル
        "src/infrastructure/email/email_service.py",  # メール送信サービスを実装するファイル
        "src/infrastructure/logging/__init__.py",  # loggingディレクトリをPythonパッケージとして扱うためのファイル
        "src/infrastructure/file_storage/__init__.py",  # file_storageディレクトリをPythonパッケージとして扱うためのファイル
        "tests/__init__.py",  # testsディレクトリをPythonパッケージとして扱うためのファイル
    ]

    # ディレクトリを作成
    for dir in dirs:
        os.makedirs(os.path.join(base_dir, dir), exist_ok=True)

    # 空のファイルを作成
    for file in files:
        file_path = os.path.join(base_dir, file)
        open(file_path, 'a').close()

# ベースディレクトリの名前
base_directory = "vending_machine_system_clean"

# ディレクトリとファイルの構造を作成
create_dir_structure(base_directory)