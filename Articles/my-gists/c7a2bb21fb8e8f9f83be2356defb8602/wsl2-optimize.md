# WSL2 Storage


- インスタンス格納ファイル`ext4.vhdx`の存在を確認する
```cmd
OS=CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc
%USERPROFILE%\Appdata\Local\Packages\$OS\LocalState
```

- `optimize-vhd`で最適化

- docker
```sh
docker container prune
docker volume prune
docker system prune
docker image prune
docker builder prune
```

- ディスク容量を変更する

```powershell
wsl --shutdown
diskpart

DISKPART> select vdisk file="C:\Users\myname\AppData\…\ext4.vhdx"

DiskPartにより、仮想ディスクファイルが選択されました。

DISKPART>expand vdisk maximum=480000 # = 480 GB


DISKPART> attach vdisk readonly

  100%完了しました

DiskPartにより、仮想ディスクファイルがアタッチされました。

DISKPART> compact vdisk

  100%完了しました <- サイズが大きいと結構時間かかる。私は20分はかからなかったくらい。

DiskPartにより、仮想ディスクファイルは正常に圧縮されました。

DISKPART> detach vdisk

DiskPartにより、仮想ディスクファイルがデタッチされました。


DISKPART> exit
```

- WSL2 設定
```sh
sudo resize2fs /dev/sdc 480000M
```