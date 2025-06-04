---
title: Setting Up WSL
name: setting-up-wsl.md
description: Setting Up WSL
type: tutorial
categories: tech
topics: tech
tags: 
  - #note

id: 2f3823
uid: d91d80a9-c18d-4c2d-8190-38c44aad145e
date: 2024-09-18T20:06:16
created_at: 1726657576
updated_at: 1726657576
path: \6da1f06a9bbee97a1ce9ffe8447bc104\setting-up-wsl.md
slug: setting_up_wsl
url: https://username.github.io/repo/posts/2024/09/18/0/1/setting-up-wsl
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
---

# WSLの設定

<div class='top' align='center'>
  <img src='top.png' alt='alt' height='200px'>
</div>
<div class="toc"></div>
<div style="page-break-after: always;"></div>

## Abstract

WSL2を設定およびカスタマイズするための設定ファイルやコマンドについて説明します。

## Introduction

WSL2（Windows Subsystem for Linux 2）は、Windows 10およびWindows 11で利用可能なLinux環境の仮想化プラットフォームです。Powershellを用いてインストールします。

## WSL2の導入

```powershell
wsl --install -d Ubuntu-24.04
wsl --status
```
username/passwordを控えてください。

## Windows Terminal.app の設定

- Distro名を確認する。
![alt text](3baf-00017.png)

- プロファイルとして、起動コマンドを設定する。
![alt text](5340-00018.png)

- スタートアップのデフォルトに設定する。
![alt text](8ed5-00019.png)

## WSL2の設定

### .wslconfig

`.wslconfig`ファイルを作成することで、WSL2の動作をカスタマイズできます。以下は`.wslconfig`ファイルの例です。

```ini
[wsl2]
memory=8GB
swap=0
processors=2
networkingMode=mirrored
```

このファイルでは、WSL2仮想マシンのメモリ、スワップ、プロセッサの設定を調整できます。ファイルを作成または編集するには、次のPowerShellコマンドを使用します。
```powershell
code %USERPROFILE%/.wslconfig
```

### /etc/wsl.conf 

Linuxディストリビューション内でのWSL2の動作をカスタマイズするために、/etc/wsl.confファイルを使用できます。以下は一般的な設定例です。
```
[boot]
systemd=true

# [automount]
# default=true

# [network]
# generateHosts = false

[interop]
appendWindowsPath = false
```

このファイルでは、systemdの有効化やWindowsの環境変数へのパスの自動追加など、WSL2の動作に関する設定を調整できます。ファイルを作成または編集するには、次のコマンドを使用します。
```sh
sudo nano /etc/wsl.conf
```

### WSL2の再起動

WSL2の設定を変更した場合、変更を適用するためにWSL2を再起動する必要があります。次のPowerShellコマンドを使用してWSL2をシャットダウンできます。


```powershell
wsl --shutdown
```

以上がWSL2の設定およびカスタマイズに関する基本的な情報です。詳細な情報については、Microsoftの公式ドキュメントを参照してください。


## References

1. [WSL での詳細設定の構成](https://learn.microsoft.com/ja-jp/windows/wsl/wsl-config)
