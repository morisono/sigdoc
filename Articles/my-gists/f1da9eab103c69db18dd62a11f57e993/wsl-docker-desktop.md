# Docker による容量肥大化

「No space left on device」のエラーは、通常、ディスクスペースが不足していることを示しています。この問題は、Dockerのボリューム、イメージの削除、Dockerのクリーンアップ、またはデバイス上の他のスペースの解放など、いくつかの方法で解決できます。また、ログの管理も重要で、ディスク上のログを管理することで解決できる場合もあります。


単純な容量不足の場合、WSL全体のデータ保存先ドライブを移動することも選択肢です。

```
# 確認
wsl -l -v

# エクスポート
wsl --export Ubuntu-<version> ubuntu.tar 

# 削除: 名前競合を避けたい場合、このタイミングで削除する必要があるが、リスクヘッジのため後に回してもよい。
wsl --shutdown
wsl --unregister Ubuntu-<version>

# インポート
mkdir -p D:\\wsl\ubuntu-<version> | cd 
wsl --import Ubuntu-<version> . ubuntu.tar --version 2

wsl --set-default Ubuntu-<version>
wsl # 初回起動時、待機時間が2分ほどかかる
```

- User settings: regedit:
- DefaultUid 1000: `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\Ubuntu-xxxx`


```


以下に対応手順を示します：

## 解決策1. `vhdx` を最適化する
```powershell
# 確認
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
echo "%APPDATA%\Local Settings\Docker\wsl\data\ext4.vhdx"
ls "%APPDATA%\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState"
diskpart

# Linuxディストリビューションに関連付けられているext4.vhdxファイルへのディレクトリパスを指定します
Select vdisk file="C:\Users\<USERNAME>\Appdata\Local Settings\Docker\wsl\data\ext4.vhdx"
Select vdisk file="${env:APPDATA}\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalSta
te\ext4.vhdx"

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

- Windows 10 Pro
```powershell
# WSLを停止
wsl --shutdown

# 仮想ディスクイメージファイルが存在するディレクトリに移動
cd C:\Users\admin\AppData\Local\Docker\wsl\data

# 最適化
Optimize-VHD -Path .\ext4.vhdx
```

- Windows 10 Home
```powershell
# WSLを停止
wsl --shutdown

# diskpartを起動
diskpart

# 仮想ディスクイメージファイルを指定
select vdisk file="C:\\Users\\<USERNAME>\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\LocalState\\ext4.vhdx"

# 読み取り限定でアタッチしないと最適化できない
attach vdisk readonly

# 最適化
compact vdisk

# 終了
detach vdisk
exit

```

## 解決策2. WSL2 バックエンドを作り直す

  
Docker Desktop の設定で `User the WSL 2 based engine` のチェックを外し、 `Apply & Restart` する:

チェックを外すと、Docker は WSL2 を使わなくなるものの、WSL に登録されたディストリビューションは残ったままとなる:

```
> wsl --list --verbose
  NAME                   STATE           VERSION
* Ubuntu                 Stopped         2
  docker-desktop-data    Stopped         2
  docker-desktop         Stopped         2
```
ディストリビューションを削除すれば、ディスクも消える:
```
> wsl --unregister docker-desktop-data
Unregistering...
> wsl --unregister docker-desktop
Unregistering...
> wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Running         2
```
その後、再度 Docker Desktop の設定より、チェックを入れて適用すれば、ディストリビューションが再作成される。ただし、**Docker 上の全てが吹き飛ぶ**。

## dockerアンインストールでの注意点

- dockerをアンインストールすると、コンテナのファイル `C:\Users\your-account\AppData\Local\Docker\wsl`( `%USERPROFILE%\AppData\Local\Docker` ) の中のフォルダのファイルを消してしまうので、必要ならばバックアップしておく。`data\ext4.vhdx` では 10GBくらいは普通にありえる。

- https://github.com/microsoft/WSL/issues/4699
- https://docs.microsoft.com/ja-jp/powershell/module/hyper-v/Optimize-VHD?view=win10-ps
- https://github.com/mikemaccana/compact-wsl2-disk
- https://learn.microsoft.com/ja-jp/windows/wsl/tutorials/wsl-containers
- https://docs.docker.jp/desktop/windows/wsl.html
- https://superuser.com/questions/1561190/how-to-reclaim-the-space-used-by-wsl2s-ext4-vhdx
- https://superuser.com/questions/1606213/how-do-i-get-back-unused-disk-space-from-ubuntu-on-wsl2
- https://superuser.com/questions/1805114/reclaim-space-of-pruned-images-docker-wsl
- https://stackoverflow.com/questions/70946140/docker-desktop-wsl-ext4-vhdx-too-large