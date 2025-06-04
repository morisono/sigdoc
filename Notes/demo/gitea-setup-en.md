---
<div class=
><ul>
title: Gitea Setup En
name: GiteaSetupEn
description: Gitea Setup En
type: overview
categories: tech
topics: tech
tags: 
  - #note

id: e308b2
uid: dd2c066e-877d-4f50-acb6-73aa8c32345a
date: 2024-09-01T21:41:21
created_at: 1725194481
updated_at: 1725194481
path: Notes/pending/gitea-setup-en.md
slug: gitea_setup_en
url: https://username.github.io/repo/posts/2024/09/01/0/1/gitea-setup-en
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

# Gitea Setup En

<div class='top' align='center'>
  <img src='top.png' alt='alt' height='200px'>
</div>
<div class="toc"></div>
<div style="page-break-after: always;"></div>

# Complete Guide: Hosting Gitea Server & DevSecOps on WSL2

## Abstract

This guide provides a comprehensive, step-by-step walkthrough for hosting a Gitea server on Windows Subsystem for Linux 2 (WSL2), and implementing DevSecOps practices. The guide covers the installation, configuration, and management of Gitea, including SSL certificate integration, database permissions, upgrade strategies, and backup procedures.

## Introduction

Gitea is a lightweight, self-hosted Git service that offers collaborative development and version control similar to GitHub. Hosting Gitea on WSL2 allows you to leverage a Linux environment on a Windows machine, combining the advantages of both systems. This guide will also incorporate DevSecOps practices, ensuring that security is integrated into every phase of the development lifecycle.

## Methodologies

### Prerequisites

1. **Windows 10/11 with WSL2 enabled**
   - Install WSL2 and set up a Linux distribution (e.g., Ubuntu).
2. **Basic understanding of Linux command-line interface (CLI)**
   - Familiarity with tools like `curl`, `nano`, `vim`, `systemctl`.
3. **Installation of Docker (optional)**
   - Useful for containerizing your Gitea installation.
4. **Administrative privileges**
   - Ensure you have the necessary permissions to install and configure software on your system.

### Steps

#### 1. Set Up WSL2 Environment

1. Install WSL2:
   ```bash
   wsl --install
   ```
2. Update and upgrade your Linux distribution:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
3. Install necessary tools:
   ```bash
   sudo apt install -y git curl nano wget
   ```

#### 2. Install Gitea

1. Download and install Gitea:
   ```bash
   wget -O gitea https://dl.gitea.io/gitea/1.20/gitea-1.20-linux-amd64
   chmod +x gitea
   sudo mv gitea /usr/local/bin/
   ```
2. Create Gitea directories:
   ```bash
   sudo mkdir -p /var/lib/gitea/{custom,data,log}
   sudo chown -R $(whoami): /var/lib/gitea/
   sudo chmod -R 750 /var/lib/gitea/
   ```

#### 3. Configure Gitea

1. Create the Gitea configuration file:
   ```bash
   sudo nano /etc/gitea/app.ini
   ```
2. Example configuration:
   ```bash
   [database]
   DB_TYPE  = sqlite3
   PATH     = /var/lib/gitea/data/gitea.db

   [server]
   DOMAIN           = localhost
   HTTP_PORT        = 3000
   ROOT_URL         = http://localhost:3000/
   DISABLE_SSH      = false
   START_SSH_SERVER = true
   SSH_PORT         = 22
   LFS_START_SERVER = true
   LFS_CONTENT_PATH = /var/lib/gitea/data/lfs
   ```

3. Start Gitea as a service:
   ```bash
   sudo systemctl start gitea
   sudo systemctl enable gitea
   ```

### Config Files

#### a) Gitea Configuration File: `/etc/gitea/app.ini`
```bash
[database]
DB_TYPE  = sqlite3
PATH     = /var/lib/gitea/data/gitea.db

[server]
DOMAIN           = localhost
HTTP_PORT        = 3000
ROOT_URL         = http://localhost:3000/
DISABLE_SSH      = false
START_SSH_SERVER = true
SSH_PORT         = 22
LFS_START_SERVER = true
LFS_CONTENT_PATH = /var/lib/gitea/data/lfs
```

#### b) Gitea Service File: `/etc/systemd/system/gitea.service`
```bash
[Unit]
Description=Gitea (Git with a cup of tea)
After=network.target

[Service]
User=git
Group=git
WorkingDirectory=/var/lib/gitea/
ExecStart=/usr/local/bin/gitea web
Restart=always
Environment=USER=git HOME=/var/lib/gitea GITEA_WORK_DIR=/var/lib/gitea

[Install]
WantedBy=multi-user.target
```

### SSL Certificates

1. Install `certbot` for SSL:
   ```bash
   sudo apt install certbot
   ```
2. Obtain an SSL certificate:
   ```bash
   sudo certbot certonly --standalone -d yourdomain.com
   ```
3. Configure Gitea to use SSL:
   ```bash
   [server]
   PROTOCOL     = https
   CERT_FILE    = /etc/letsencrypt/live/yourdomain.com/fullchain.pem
   KEY_FILE     = /etc/letsencrypt/live/yourdomain.com/privkey.pem
   ```

### Database Permissions

1. Set up MySQL or PostgreSQL:
   ```bash
   sudo apt install mysql-server
   ```
2. Create a Gitea database:
   ```bash
   mysql -u root -p
   CREATE DATABASE gitea;
   CREATE USER 'gitea'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON gitea.* TO 'gitea'@'localhost';
   FLUSH PRIVILEGES;
   ```

### Upgrades

1. Backup your Gitea instance:
   ```bash
   tar -czvf gitea-backup-$(date +%F).tar.gz /var/lib/gitea
   ```
2. Download and replace the Gitea binary:
   ```bash
   wget -O gitea https://dl.gitea.io/gitea/latest/gitea-1.20-linux-amd64
   chmod +x gitea
   sudo mv gitea /usr/local/bin/
   sudo systemctl restart gitea
   ```

### Backups

1. Automate backups using a cron job:
   ```bash
   crontab -e
   ```
2. Add the following line to backup daily:
   ```bash
   0 2 * * * tar -czvf /var/backups/gitea-$(date +\%F).tar.gz /var/lib/gitea
   ```

## References

- [WSL Gitea Setup](https://raspberry-valley.azurewebsites.net/wsl-gitea/)
- [Installing Gitea on Ubuntu](https://linuxize.com/post/how-to-install-gitea-on-ubuntu-20-04/)
- [Gitea on WSL2](https://zenn.dev/hiro345/articles/n100_01_20240110)
- [Gitea Configuration and Setup](https://blog.lycolia.info/0156)
