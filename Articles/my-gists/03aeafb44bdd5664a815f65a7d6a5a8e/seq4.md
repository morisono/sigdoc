

```mermaid
participant User
participant Firewall
participant FastAPI
participant AuthenticateUser
participant UserRepository
participant EncryptionService
participant CartRepository
participant ManageCart
participant Cart
participant FormRepository
participant ManageForm

User->FastAPI: ユーザがログインリクエストを送信
FastAPI->Firewall: IPアドレスチェック
Firewall->FastAPI: IPアドレス許可済み
FastAPI->AuthenticateUser: ユーザ認証
AuthenticateUser->UserRepository: ユーザ情報検索
UserRepository-->AuthenticateUser: ユーザ情報
AuthenticateUser->EncryptionService: パスワード復号化
EncryptionService-->AuthenticateUser: 復号化済みパスワード
AuthenticateUser-->FastAPI: 認証結果
FastAPI-->User: 認証成功/失敗のレスポンス

User->FastAPI: 商品をカートに追加リクエストを送信
FastAPI->Firewall: IPアドレスチェック
Firewall->FastAPI: IPアドレス許可済み
FastAPI->ManageCart: カートに商品追加リクエスト
ManageCart->CartRepository: カート情報検索
CartRepository-->ManageCart: カート情報
ManageCart->Cart: カート更新
Cart-->ManageCart: 更新後のカート情報
ManageCart-->FastAPI: 更新後のカート情報
FastAPI-->User: カート更新結果のレスポンス

User->FastAPI: カートをクリアリクエストを送信
FastAPI->Firewall: IPアドレスチェック
Firewall->FastAPI: IPアドレス許可済み
FastAPI->ManageCart: カートクリアリクエスト
ManageCart->CartRepository: カート情報検索
CartRepository-->ManageCart: カート情報
ManageCart->Cart: カートクリア
Cart-->ManageCart: 更新後のカート情報
ManageCart-->FastAPI: 更新後のカート情報
FastAPI-->User: カート更新結果のレスポンス

User->FastAPI: フォーム送信リクエストを送信
FastAPI->Firewall: IPアドレスチェック
Firewall->FastAPI: IPアドレス許可済み
FastAPI->ManageForm: フォーム送信リクエスト
ManageForm->FormRepository: フォームデータ保存
FormRepository-->ManageForm: フォームデータ保存完了
ManageForm-->FastAPI: フォーム送信結果のレスポンス
FastAPI-->User: フォーム送信結果のレスポンス
```