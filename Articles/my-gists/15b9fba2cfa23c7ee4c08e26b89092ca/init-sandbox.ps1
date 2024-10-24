# 仮想マシンの作成
New-VM -Name "DarkWebVM" -MemoryStartupBytes 2GB -NewVHDPath "C:\DarkWebVM\DarkWeb.vhdx" -NewVHDSizeBytes 20GB -SwitchName "Virtual Switch"

# 仮想マシンの起動
Start-VM -Name "DarkWebVM"

# Torブラウザのダウンロードとインストール
Invoke-WebRequest -Uri "https://www.torproject.org/dist/torbrowser/11.0.1/torbrowser-install-win64-11.0.1_en-US.exe" -OutFile "$env:TEMP\torbrowser-install.exe"
Start-Process -FilePath "$env:TEMP\torbrowser-install.exe" -ArgumentList "/S" -Wait

# セキュリティ設定の構成
# 例: Windowsファイアウォールの設定
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
