ご指摘ありがとうございます。より柔軟で競合を避ける設定にし、IPアドレスを自動取得するように改善します。

```batch
@echo off
setlocal enabledelayedexpansion

REM ランダムな非ウェルノウンポートを生成（10000-65535の範囲）
set /a port=%RANDOM% * 55535 / 32768 + 10000

REM 内部IPアドレスの自動取得
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| find "IPv4 Address"') do (
    set internal_ip=%%a
    set internal_ip=!internal_ip:~1!
    goto :break
)
:break

REM グローバルIPアドレスの自動取得（外部サービスを使用）
for /f %%a in ('powershell -Command "(Invoke-WebRequest -Uri 'http://ifconfig.me/ip').Content"') do set global_ip=%%a

echo Internal IP: !internal_ip!
echo Global IP: !global_ip!
echo Selected Port: !port!

REM PowerShellの実行ポリシーを設定
PowerShell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"

REM ファイアウォールルールの追加
netsh advfirewall firewall add rule name="Open Port !port!" protocol=TCP dir=in localport=!port! action=allow

REM ポートフォワーディングの設定
netsh interface portproxy add v4tov4 listenport=!port! listenaddress=0.0.0.0 connectport=!port! connectaddress=!internal_ip!

echo Configuration completed.
echo Please ensure your router is configured to forward port !port! to !internal_ip!
echo You can access your service from the internet using: http://!global_ip!:!port!

```

この改訂版スクリプトの特徴：

1. ポート番号をランダムに生成：
   - 10000から65535の範囲でランダムなポートを選択し、競合の可能性を低減します。

2. 内部IPアドレスの自動取得：
   - `ipconfig` コマンドを使用して、現在のマシンの内部IPアドレスを自動的に取得します。

3. グローバルIPアドレスの自動取得：
   - 外部サービス（ifconfig.me）を使用して、現在のグローバルIPアドレスを取得します。
   - 注意：この方法はインターネット接続が必要で、外部サービスに依存します。

4. 遅延環境変数展開の使用：
   - `setlocal enabledelayedexpansion` と `!変数名!` を使用して、変数の値を正しく展開します。

検証方法：

1. スクリプト実行後、表示される情報を確認します。
2. ポートフォワーディングの設定を確認：
   ```
   netsh interface portproxy show all
   ```
3. ファイアウォールルールの確認：
   ```
   netsh advfirewall firewall show rule name="Open Port <表示されたポート番号>"
   ```
4. ルーターの設定：表示されたポート番号を内部IPアドレスに転送するよう設定します。
5. 外部からのアクセステスト：別のネットワークから `http://<グローバルIP>:<ポート番号>` にアクセスします。

注意点：
- グローバルIPの取得にはインターネット接続が必要です。
- ルーターの設定は手動で行う必要があります。
- セキュリティリスクを考慮し、必要な場合のみこの設定を使用してください。
- 可能であれば、より安全な方法（VPNなど）でのアクセス提供を検討してください。