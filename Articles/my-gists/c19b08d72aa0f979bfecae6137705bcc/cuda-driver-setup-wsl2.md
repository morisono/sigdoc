---
<div class="frontmatter"><ul>
title: Setup GPU Drivers on Wsl2
name: GPUDriversSetupWsl2
description: GPU Drivers Setup Wsl2
type: quick_start
categories: tech
topics: tech
tags: 
  - #note

id: 567ddd
uid: 417cf5ed-1ec9-49a6-a776-dbd91a7ea61c
date: 2024-08-26T17:58:34
created_at: 1724662714
updated_at: 1724662714
path: Articles/my-gists/c19b08d72aa0f979bfecae6137705bcc/gpu-drivers-setup-wsl2.md
slug: gpu_drivers_setup_wsl2
url: https://username.github.io/repo/posts/2024/08/26/0/1/gpu-drivers-setup-wsl2
redirect_from: 
  - 

lang: en
author: undefined
private: true
weight: 1
toc: false
draft: true
status: 
keywords: 
changelog: 
versions: 
</ul></div>
---


# Setup NVIDIA GPU Drivers on WSL2

<div class='toc'>

- [Setup NVIDIA GPU Drivers on WSL2](#setup-nvidia-gpu-drivers-on-wsl2)
  - [Abstract](#abstract)
  - [Introduction](#introduction)
  - [Methodologies](#methodologies)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
      - [Uninstall old driver / toolkit](#uninstall-old-driver--toolkit)
      - [Installing NVIDIA Drivers](#installing-nvidia-drivers)
      - [Installing CUDA Toolkit](#installing-cuda-toolkit)
      - [Installing the NVIDIA Container Toolkit](#installing-the-nvidia-container-toolkit)
      - [Configure Docker](#configure-docker)
      - [Restart daemon](#restart-daemon)
    - [Installing cuDNN (Optional)](#installing-cudnn-optional)
  - [References](#references)


</div>

## Abstract

WSL2におけるNVIDIA GPU Driversのインストールについて


## Introduction

WSL2下でGPU パワーを使用する計算を行う場合、ドライバ ソフトウェアの導入が必要となる。
例えば、`Open-WebUI`のようなソフトウェア場合、CLI-Baseで導入したいため、必然的にプロジェクトルートもLinux側になる。
一方で、NVIDIA Driverは、仮想環境に置く必要はないため、インストーラーでWindows側にインストールする。

<div style="page-break-after: always;"></div>

## Methodologies

### Prerequisites

- Installer type : `runfile(local)` # recommended

### Steps

- 環境変数類の確認をおこないます。

```bash
➜ nvidia-smi
Mon Aug 26 18:07:28 2024
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 510.73.08    Driver Version: 516.40       CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:3B:00.0  On |                  N/A |
|  0%   47C    P8    12W / 200W |   1259MiB /  8192MiB |     14%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A        27      G   /Xwayland                       N/A      |
|    0   N/A  N/A        98      G   /Xwayland                       N/A      |
+-----------------------------------------------------------------------------+

➜ cat /etc/docker/daemon.json
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "args": [],
            "path": "nvidia-container-runtime"
        }
    }
}⏎

➜ cat /etc/*-release # Check OS distr
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04 LTS"
..

➜ lscpu # Check OS Arch
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
..

# ➜ sudo lshw -C system # Check HW info
```
- WSL2のバージョンを確認します。

```powershell
# wsl cat /proc/version  # Specify the WSL ver.
```

#### Uninstall old driver / toolkit

過去に導入している場合、古いドライバーを削除します。

```bash
# To uninstall cuda ( adjust X.Y to your env )
sudo /usr/local/cuda-X.Y/bin/cuda-uninstaller 
# To uninstall nvidia
sudo /usr/bin/nvidia-uninstall

# If you install via package manager
sudo apt --purge remove <package_name> 

## For CUDA 11.3 and earlier
sudo apt-get --purge remove "*nvidia*"
sudo apt-get --purge remove "*cublas*" "cuda*" "nsight*" 

# --- 

# To remove CUDA Toolkit:
sudo apt-get --purge remove "*cuda*" "*cublas*" "*cufft*" "*cufile*" "*curand*" "*cusolver*" "*cusparse*" "*gds-tools*" "*npp*" "*nvjpeg*" "nsight*" "*nvvm*"

# To remove NVIDIA Drivers:
sudo apt-get --purge remove "*nvidia*" "libxnvctrl*"

# If you've install via source files
sudo rm -rf /usr/local/cuda*

# If you cleanup totally
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt-get autoremove && sudo apt-get autoclean
sudo apt autoremove
```

- [18. Removing CUDA Toolkit and Driver](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#removing-cuda-toolkit-and-driver)

#### Installing NVIDIA Drivers 

NVIDIA Driverの`Manual Driver Search`から、使用する端末の適切なドライバを検索する。

- [Download The Latest Official NVIDIA Drivers](https://www.nvidia.com/en-us/drivers/)

取得した実行ファイルを実行して、インストールを完了する。

#### Installing CUDA Toolkit

CUDAは、NVIDIAによって作成された並列コンピューティングプラットフォームとアプリケーション・プログラミング・インターフェース（API）モデルの名前です。CUDAツールキットをインストールすることでTensorFlowにGPU加速が可能になります。

```bash
# sudo apt update
# sudo apt upgrade -y
# sudo apt install cuda-toolkit
# sudo apt install nvidia-gds
# sudo reboot

# Install Driver
wget https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda_12.6.0_560.28.03_linux.run

# Install CUDA Driver
sudo sh cuda_12.6.0_560.28.03_linux.run
sudo sh cuda_12.6.0_560.28.03_linux.run --silent --driver

## Add filepath
cat /etc/ld.so.conf.d/cuda-12-6.conf
sudo echo -e "\n/usr/local/cuda-12.6/lib64\n" > /etc/ld.so.conf.d/cuda-12-6.conf

## Or set PATH  ( e.g. add to ~/.config/fish/config.fish )
set -gx CUDA_HOME /usr/local/cuda-12.6/bin
set -gx PATH $PATH:$CUDA_HOME/bin
set -gx LD_LIBRARY_PATH /usr/local/cuda-12.6/lib64

# Check PATH 
echo $PATH | tr ' ' '\n' | grep cuda
echo $LD_LIBRARY_PATH | tr ' ' '\n' | grep cuda
```

うまくいかないときは、`deb (network)` インストールを試しましょう。
```bash
cat /var/log/cuda-installer.log

wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6

sudo apt-get install -y nvidia-open
```

スクリプトを実行後、数分後、次のような案内が表示される。
それぞれ適切な値を入力する。

```bash
┌──────────────────────────────────────────────────────────────────────────────┐
│  End User License Agreement                                                  │
│  --------------------------                                                  │
│                                                                              │
│  NVIDIA Software License Agreement and CUDA Supplement to                    │
│  Software License Agreement.                                                 │
│                                                                              │
│  The CUDA Toolkit End User License Agreement applies to the                  │
│  NVIDIA CUDA Toolkit, the NVIDIA CUDA Samples, the NVIDIA                    │
│  Display Driver, NVIDIA Nsight tools (Visual Studio Edition),                │
│  and the associated documentation on CUDA APIs, programming                  │
│  model and development tools. If you do not agree with the                   │
│  terms and conditions of the license agreement, then do not                  │
│  download or use the software.                                               │
│                                                                              │
│  Last updated: January 12, 2024.                                             │
│                                                                              │
│                                                                              │
│  Preface                                                                     │
│  -------                                                                     │
│                                                                              │
│──────────────────────────────────────────────────────────────────────────────│
│ Do you accept the above EULA? (accept/decline/quit):                         │
│ accept                                                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

導入するソフトウェアの選択

```bash
┌──────────────────────────────────────────────────────────────────────────────┐
│ CUDA Installer                                                               │
│ + [X] CUDA Toolkit 12.6                                                      │
│   [X] CUDA Demo Suite 12.6                                                   │
│   [X] CUDA Documentation 12.6                                                │
│ - [ ] Kernel Objects                                                         │
│      [ ] nvidia-fs                                                           │
│   Options                                                                    │
│   Install                                                                    │
│                                                                              │
~
│ Up/Down: Move | Left/Right: Expand | 'Enter': Select | 'A': Advanced options │
└──────────────────────────────────────────────────────────────────────────────┘
```

シンボリックリンクがある場合の表示

```bash
┌──────────────────────────────────────────────────────────────────────────────┐
│ A symlink already exists at /usr/local/cuda. Update to this installation?    │
│ Yes                                                                          │
│ No                                                                           │
│                                                                              │
~
│ Up/Down: Move | 'Enter': Select                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

Toolkitがある場合の表示

```bash
┌──────────────────────────────────────────────────────────────────────────────┐
│ Existing installation of CUDA Toolkit 12.6 found:                            │
│ Upgrade all                                                                  │
│ Choose components to upgrade                                                 │
│ No, abort installation                                                       │
│                                                                              │
~
│ Up/Down: Move | 'Enter': Select                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

数分要するので、待機する。

完了後の表示

```bash
┌──────────────────────────────────────────────────────────────────────────────┐
│ Existing installation of CUDA Toolkit 12.6 found:                            │
│ Upgrade all                                                                  │
│ Choose components to upgrade                                                 │
│ No, abort installation                                                       │
│                                                                              │
~
│ Up/Down: Move | 'Enter': Select                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

失敗した場合等の表示 (詳細はトラブルシューティングガイドを参照)

```bash
===========
= Summary =
===========

Driver:   Not Selected
Toolkit:  Installed in /usr/local/cuda-12.6/

Please make sure that
 -   PATH includes /usr/local/cuda-12.6/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-12.6/lib64, or, add /usr/local/cuda-12.6/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-12.6/bin
***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 560.00 is required for CUDA 12.6 functionality to work.
To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
    sudo <CudaInstaller>.run --silent --driver

Logfile is /var/log/cuda-installer.log
```


#### Installing the NVIDIA Container Toolkit

Dockerを使う場合、コンテナツールキットを導入します。

```bash
➜ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### Configure Docker

```bash
➜ sudo nvidia-ctk runtime configure --runtime=docker
```

#### Restart daemon

```bash
➜ sudo systemctl restart docker
```

### Installing cuDNN (Optional)

Tensorflowなどのフレームワークを使う場合、CuDNNを入れる必要があります。

- https://developer.nvidia.com/rdp/form/cudnn-download-survey

```bash
# adjust X.Y to your env
tar xzvf cudnn-**.tgz 
cp -a cuda/lib64/* /home/hogehoge/cuda-X.Y/lib64/
cp -a cuda/include/* /home/hogehoge/cuda-X.Y/include/
```

## References

1. [CUDA on WSL](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl)
1. [CUDA Toolkit 12.1 Downloads](https://developer.nvidia.com/cuda-downloads)
1. [GPU in Windows Subsystem for Linux (WSL)](https://developer.nvidia.com/cuda/wsl)
1. [Upgrading to the NVIDIA Container Runtime for Docker :: DGX Systems Documentation](https://docs.nvidia.com/dgx/nvidia-container-runtime-upgrade/)
1. [CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#handle-conflicting-installation-methods)
1. [How to remove cuda completely from ubuntu?](https://stackoverflow.com/questions/56431461/how-to-remove-cuda-completely-from-ubuntu)
1. [CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#wsl)
1. [How to remove cuda completely from ubuntu?](https://stackoverflow.com/questions/56431461/how-to-remove-cuda-completely-from-ubuntu)