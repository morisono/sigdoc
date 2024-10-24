了解しました。有効な設定やBotの参考リンクを追加して説明します。

## 対策に有効な設定

### ユーザー権限の適正化 (roles)
- 新規メンバーには最小限の権限しか与えない
- 運営チームには必要十分な権限を設定する
- [Roleの管理ガイド](https://support.discord.com/hc/en-us/articles/214836687-Role-Management-101)

### メッセージ監視とフィルタリング
- 不適切な単語をブロックするフィルタを設定
- [メッセージコンテンツのスキャンBotの例: Dyno](https://dyno.gg/)

### 招待リンク発行の制限 (invite)
- 新規リンク発行には一定の権限が必要
- 不審な大量招待には制限をかける
- [招待設定ガイド](https://support.discord.com/hc/en-us/articles/213043767-Inviting-Members)  

### 2段階認証の導入 (2FA)
- Discordアカウントに2段階認証を設定
- 乗っ取りリスクを大幅に下げられる
- [2FA設定ガイド](https://support.discord.com/hc/en-us/articles/219576828-Setting-up-Two-Factor-Authentication)

### メッセージ履歴の保持期間延長
- デフォルトは1週間だが、期間を延長できる
- 過去のログから荒らし状況を追跡し易くなる

### 公認botのみの許可 (bots)
- 信頼できるbotのみを許可するWhitelistモード
- 不審なbotの招待を防げる
- [Botの招待ガイド](https://support.discord.com/hc/en-us/articles/204025198-Authorized-Bot-Setup)

## 有効なBotの例

- **Dyno** - メッセージ監視、フィルタリング、自動化
- **Tatsumaki** - スパム対策、メンバー承認制に有効  
- **Gaius** - 高度なロギングとメッセージ削除履歴の管理
- **Red** - カスタマイズ可能な多機能ボット、モデレーション機能が充実

荒らし対策は、設定の最適化と信頼できるBotの連携で、より強固なものになります。サーバーの健全性維持に役立ててください。