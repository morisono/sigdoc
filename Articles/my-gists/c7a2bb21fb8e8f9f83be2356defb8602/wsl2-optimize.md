---
title: Optimizing WSL
name: OptimizingWSL
description: Optimizing WSL
type: tutorial
categories: tech
topics: tech
tags: 
  - #article

id: 3a8516
uid: ab2dfc6f-1a23-4c76-8692-3543939318ee
date: 2024-09-18T20:22:18
created_at: 1726658538
updated_at: 1726658538
path: C:\Users\gemjin\Documents\Obsidian\ Vault\ 2\Articles\my-gists\c7a2bb21fb8e8f9f83be2356defb8602\optimizing-wsl.md
slug: optimizing_wsl
url: https://username.github.io/repo/posts/2024/09/18/0/1/optimizing-wsl
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

# Wsl2 Optimize

<div class='top' align='center'>
  <img src='top.png' alt='alt' height='200px'>
</div>
<div class="toc"></div>
<div style="page-break-after: always;"></div>


## Abstract

WSLのストレージ設定を最適化するための手順を説明します。

## Introduction

WSLのデータは一つの仮想ファイルにまとめて保存されています。そのため、データ容量に関するトラブルが生じます。問題発生防止のため、使用状況を確認し、制約を設けるようにしておきましょう。

### Steps

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

## References

1. [How to manage WSL disk space](https://learn.microsoft.com/en-us/windows/wsl/disk-space)
