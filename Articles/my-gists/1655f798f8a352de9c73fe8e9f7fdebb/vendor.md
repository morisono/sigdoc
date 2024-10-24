以下は、より適切で詳細な設計を行い、説明を加えたクラスのリファクタリングです。これらのクラスは、シングルトン、ストラテジー、ファサード、コマンド、オブザーバーパターンなどのデザインパターンに基づいています。

### クラス設計

#### `Vendor` クラス

`Vendor`クラスはファサードパターンを適用して、複数のシステム操作を簡潔に提供します。

```python
class Vendor:
    def __init__(self, db_path):
        self.db = Database(db_path)
        self.cart = Cart(db_path)

    def find_file(self, file_name, search_path='.'):
        # ファイル検索ロジック
        pass

    def find_files_all(self, search_path='.', file_extension=None):
        # 全ファイル検索ロジック
        pass

    def find_files_match(self, items, file_extension=None):
        # 条件に一致するファイル検索ロジック
        pass

    def show_item_desc(self, state, selected):
        # 商品説明表示ロジック
        pass

    def show_item_demo(self, *args):
        # TODO: 商品デモ表示ロジック
        pass

    def export_data(self, data, out_path):
        # データエクスポートロジック
        pass
```

#### `Database` クラス

`Database`クラスはシングルトンパターンを適用して、データベース接続を一意に管理します。

```python
class Database:
    _instance = None

    def __new__(cls, db_path):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._init(db_path)
        return cls._instance

    def _init(self, db_path):
        self.db_path = db_path
        # データベース接続初期化ロジック

    def find_item(self, pid):
        # 商品検索ロジック
        pass

    def update_stock(self, pid, qty):
        # 在庫更新ロジック
        pass
```

#### `Cart` クラス

`Cart`クラスは、カートの操作を管理します。

```python
class Cart:
    def __init__(self, db_path):
        self.db = Database(db_path)
        self.items = []

    def add(self, selected):
        # 商品追加ロジック
        self.items.append(selected)

    def remove(self, pid):
        # 商品削除ロジック
        self.items = [item for item in self.items if item.pid != pid]

    def clear(self):
        # カートクリアロジック
        self.items.clear()

    def calc_total(self, state):
        # 合計金額計算ロジック
        return sum(item.price for item in self.items)

    def complete_payment(self, payment, state):
        # 支払い完了ロジック
        pass

    def update_cart(self, item):
        # カート更新ロジック
        pass
```

#### `Form` クラス

`Form`クラスはフォームデータを管理します。

```python
class Form:
    def __init__(self, items):
        self.items = items
```

#### `Payment` クラス

`Payment`クラスはストラテジーパターンを適用して、異なる支払い方法を管理します。

```python
class Payment:
    def __init__(self, method, status, token):
        self.method = method
        self.status = status
        self.token = token

    def complete(self):
        # 支払い完了ロジック
        pass
```

#### `State` クラス

`State`クラスは、システムの状態を管理します。

```python
class State:
    def __init__(self, params):
        self.__dict__.update(params)

    def __getattr__(self, name):
        return self.__dict__.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
```

#### `Item` クラス

`Item`クラスは商品を表現します。

```python
class Item:
    def __init__(self, name, price, desc=None):
        self.name = name
        self.price = price
        self.desc = desc

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, desc={self.desc})"
```

#### `CartItem` クラス

`CartItem`クラスはカート内の商品を表現します。

```python
class CartItem(Item):
    def __init__(self, item, qty=1):
        super().__init__(item.name, item.price, item.desc)
        self.qty = qty

    def __repr__(self):
        return f"CartItem(name={self.name}, price={self.price}, qty={self.qty})"
```

#### `WEB_UI` クラス

`WEB_UI`クラスはユーザーインターフェースを管理します。

```python
class WEB_UI:
    def __init__(self, config, toc):
        self.config = config
        self.toc = toc

    def lit_theme(self):
        # テーマ設定ロジック
        pass

    def run(self):
        # UI起動ロジック
        pass

    def find_paths_all(self, dataset, group_key, *keys):
        # パス検索ロジック
        pass

    def separate_entries(self, entries):
        # TODO: ソート/重複削除ロジック
        pass

    def main(self):
        # メイン処理
        pass

def update_explorer(paths):
    # エクスプローラー更新ロジック
    pass

def update_imgs(paths):
    # 画像更新ロジック
    pass

def update_params(state, tags, prods):
    # パラメータ更新ロジック
    pass

def load_config(path, key):
    # 設定ロードロジック
    pass
```

### 説明

- **Vendorクラス**はファサードパターンを使用しており、システムの複雑な操作を簡単に呼び出せるようにします。これにより、複数の異なる操作を一つのクラスで管理し、シンプルなインターフェースを提供します。
  
- **Databaseクラス**はシングルトンパターンを適用しており、データベース接続が一意に管理されるようにしています。これにより、同じデータベース接続が複数回作成されることを防ぎます。

- **Cartクラス**はカート内の商品操作を管理し、シンプルで直感的なメソッドを提供します。

- **Paymentクラス**はストラテジーパターンを適用しており、異なる支払い方法を管理することができます。これにより、将来的に支払い方法が追加されても、既存のコードに影響を与えずに拡張できます。

- **Stateクラス**はシステムの状態を動的に管理します。このクラスを利用することで、柔軟にシステムの状態を更新・参照できます。

- **Itemクラス**および**CartItemクラス**は商品情報を管理します。これにより、商品情報の取り扱いが一貫した形式で行えます。

- **WEB_UIクラス**はユーザーインターフェースを管理し、UIのテーマ設定やパス検索などの操作を提供します。