import os

def create_dir_structure(base_dir):
    # ディレクトリのリスト
    dirs = [
        "src",  # プロジェクトのソースコードのルートディレクトリ
        "src/domain",  # ドメイン層のディレクトリ
        "src/domain/entities",  # エンティティクラスを格納するディレクトリ
        "src/domain/services",  # ドメインサービスを格納するディレクトリ
        "src/domain/value_objects",  # 値オブジェクトを格納するディレクトリ
        "src/domain/repositories",  # リポジトリインターフェースを格納するディレクトリ
        "src/application",  # アプリケーション層のディレクトリ
        "src/application/use_cases",  # ユースケースを実装するディレクトリ
        "src/application/dtos",  # データ転送オブジェクト（DTO）を格納するディレクトリ
        "src/infrastructure",  # インフラストラクチャ層のディレクトリ
        "src/infrastructure/database",  # データベース接続やモデルを格納するディレクトリ
        "src/infrastructure/email",  # メール送信ロジックを格納するディレクトリ
        "src/infrastructure/logging",  # ロギング関連の実装を格納するディレクトリ
        "src/infrastructure/file_storage",  # ファイルストレージ関連の実装を格納するディレクトリ
        "src/presentation",  # プレゼンテーション層のディレクトリ
        "src/presentation/controllers",  # プレゼンテーション層のコントローラを格納するディレクトリ
        "src/presentation/views",  # プレゼンテーション層のビューを格納するディレクトリ
        "src/presentation/templates",  # テンプレートファイルを格納するディレクトリ
        "src/presentation/static",  # 静的ファイルを格納するディレクトリ
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
        "src/domain/__init__.py",  # domainディレクトリをPythonパッケージとして扱うためのファイル
        "src/domain/entities/user.py",  # ユーザーエンティティを定義するファイル
        "src/application/__init__.py",  # applicationディレクトリをPythonパッケージとして扱うためのファイル
        "src/application/use_cases/authenticate_user.py",  # ユーザー認証ユースケースを実装するファイル
        "src/infrastructure/__init__.py",  # infrastructureディレクトリをPythonパッケージとして扱うためのファイル
        "src/infrastructure/database/models.py",  # データベースモデルを定義するファイル
        "src/infrastructure/email/email_service.py",  # メール送信サービスを実装するファイル
        "src/presentation/__init__.py",  # presentationディレクトリをPythonパッケージとして扱うためのファイル
        "src/presentation/templates/.keep",  # テンプレートディレクトリをバージョン管理するためのプレースホルダーファイル
        "src/presentation/static/.keep",  # 静的ファイルディレクトリをバージョン管理するためのプレースホルダーファイル
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
base_directory = "vending_machine_system_onion"

# ディレクトリとファイルの構造を作成
create_dir_structure(base_directory)
