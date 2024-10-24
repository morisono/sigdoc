# Docker による容量肥大化

「No space left on device」のエラーは、通常、ディスクスペースが不足していることを示しています。この問題は、Dockerのボリューム、イメージの削除、Dockerのクリーンアップ、またはデバイス上の他のスペースの解放など、いくつかの方法で解決できます。また、ログの管理も重要で、ディスク上のログを管理することで解決できる場合もあります。

WSL2のUbuntuは、デフォルトではWindowsのC:ドライブに存在する仮想ディスク内に存在します。したがって、WindowsのC:ドライブの空き容量が不足している可能性があります。

以下に対応手順を示します：

```powershell
# 
(Get-ChildItem "C:\" -recurse -force | Select-Object Fullname,Length | Sort-Object Length -descending )[0..29] 2>$null
cd ${env:APPDATA}\Local Settings\Docker\wsl\data


# すべてのWSLインスタンスを終了します
wsl -l -v
wsl --shutdown
wsl --shutdown docker-desktop

# Docker Desktopのアンインストール
wsl --unregister docker-desktop
wsl --unregister docker-desktop-data

# Docker Desktopの再インストール
# Docker Desktopをダウンロードしてインストールします

- Windows standard 
# 管理者特権でWindowsコマンドプロンプトを開き、diskpartコマンドインタープリターを開きます
diskpart

# Linuxディストリビューションに関連付けられているext4.vhdxファイルへのディレクトリパスを指定します
Select vdisk file="<pathToVHD>"
Select vdisk file="${env:APPDATA}\Local Settings\Docker\wsl\data\ext4.vhdx"
# この仮想ディスクに関連付けられている詳細を表示します
detail vdisk

# このLinuxディストリビューションに割り当てる新しい最大サイズの値を入力します
expand vdisk maximum=<sizeInMegaBytes>

attach vdisk readonly
compact vdisk
detach vdisk

- HyperV
# 
Optimize-VHD -Path .\ext4.vhdx -Mode Full
Optimize-VHD -Path "$Env:LOCALAPPDATA\Docker\wsl\data\ext4.vhdx" -Mode Full
Optimize-VHD -Path "$Env:LOCALAPPDATA\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\ext4.vhdx" -Mode Full


Get-ChildItem -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss

```

```
wsl --shutdown
diskpart
select vdisk file="C:\\Users\\ユーザー名\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit

```