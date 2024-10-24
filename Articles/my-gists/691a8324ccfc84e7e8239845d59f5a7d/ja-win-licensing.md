# Windwows Licensing

```cmd
# コマンドプロンプトを開いて、ライセンスの詳細な情報を表示
slmgr.vbs /dlv

# Activate
slmgr.vbs /ato
```

```powershell
# PowerShellを開いて、ライセンスが有効な製品の名前を表示
(Get-CimInstance -Query "SELECT * FROM SoftwareLicensingProduct WHERE LicenseStatus='1'").Name
```

```yaml
Software licensing service version: 10.02621.3007
Name: Windows(R), Professional edition
Description: Windows(R) Operating System, RETAIL channel
Activation ID: @@@@@@@@-@@@@@@@@-@@@@-@@@@@@@@@@@@
Application ID: @@@@@@@-@@@@@@@@-@@@@-@@@@@@@@@@@@
Extended PID: *****-*****-**-*****-***-****-*****.****-*******
Product Key Channel: Retail
Installation ID: *************************************************************
use License URL: https://activation-v2.sls.microsoft.com/SLActivateProduct/SLActivateProduct.asmx?configextension=Retail
Validation URL: https://validation-v2.sls.microsoft.com/SLWGA/slwga.asmx
Partial Product Key: @@@@@
License Status: Licensed
Remaining Windows rearm count: 1001
Remaining SKIJ rearm count: 1001
Trusted time: 2/3/2024 AM
```

- 