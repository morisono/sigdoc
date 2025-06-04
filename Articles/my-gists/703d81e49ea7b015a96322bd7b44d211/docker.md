# Dockerのセットアップ

### はじめに

Dockerは、アプリケーションの開発、テスト、およびデプロイを効率化するためのコンテナ化プラットフォームです。コンテナは、アプリケーションとその依存関係を隔離し、異なる環境でも一貫した実行を保証します。この記事では、Dockerの主要コンポーネントである**コンテナ (Container)**、**イメージ (Image)**、**ボリューム (Volume)**について解説し、Windows、macOS、Linuxそれぞれのセットアップ方法を体系的に説明します。

### コンテナ

Dockerコンテナは、軽量で独立した実行環境を提供します。コンテナは、ホストマシンのカーネルを共有し、仮想マシンよりも効率的にリソースを使用します。

- コンテナは、実行中のアプリケーションやプロセスを隔離するために使用される。
- コンテナは、指定した**イメージ**を基にして起動される。
- コンテナは、リソースの利用を制限するための機能（CPU、メモリ、I/Oなど）を提供する。

#### コンテナの基本操作

Dockerの基本操作は、次のコマンドで行います。

```bash
docker run -d --name my_container my_image
```

- **`docker run`**: 新しいコンテナを起動する。
- **`-d`**: バックグラウンドでコンテナを実行するオプション。
- **`--name`**: コンテナの名前を指定する。
- **`my_image`**: 使用するDockerイメージ。

### イメージ

Dockerイメージは、コンテナの実行環境を定義する不変のテンプレートです。各イメージは、アプリケーション、ライブラリ、設定ファイルなどを含んでおり、コンテナを生成するために使用されます。

- イメージは、ベースイメージ（たとえば**Ubuntu**）の上にアプリケーションを積み重ねる形で作成される。
- イメージは、軽量であり、多くのイメージを一つのホスト上で同時に扱うことが可能である。
- イメージは、**Docker Hub**や**プライベートリポジトリ**から取得できる。

#### イメージの操作

イメージの操作には、次のようなコマンドを使います。

```bash
docker pull ubuntu
docker build -t my_custom_image .
```

- **`docker pull`**: リポジトリからイメージをダウンロードする。
- **`docker build`**: Dockerfileを基に新しいイメージを作成する。
- **`-t`**: 新しいイメージにタグを付ける。

### ボリューム

Dockerボリュームは、コンテナ間でデータを共有したり、永続化するために使用されます。ボリュームを使うことで、ホストマシン上に保存されたデータをコンテナが利用できるようにします。

- ボリュームは、ホストシステムのファイルシステム上に保存され、コンテナが停止してもデータが保持される。
- ボリュームは、複数のコンテナ間でデータを共有できる。
- ボリュームは、コンテナのライフサイクルとは独立して管理される。

#### ボリュームの操作

ボリュームを作成および使用するための基本コマンドは以下の通りです。

```bash
docker volume create my_volume
docker run -d -v my_volume:/data my_image
```

- **`docker volume create`**: 新しいボリュームを作成する。
- **`-v`**: コンテナとホスト間でボリュームをマウントする。

### Windowsでのセットアップ

WindowsでDockerをセットアップするには、**Docker Desktop (Windows)** をインストールします。

1. Docker公式サイトから**Docker Desktop**をダウンロードします。
2. インストーラーを起動し、指示に従ってインストールを完了します。
3. インストール後、Docker Desktopを起動し、設定から**WSL 2 Backend**を有効にします。

### macOSでのセットアップ

macOSでも、**Docker Desktop (macOS)** を利用して簡単にDockerをセットアップできます。

1. Docker公式サイトから**Docker Desktop**をダウンロードします。
2. ダウンロードした.dmgファイルを開き、指示に従ってインストールします。
3. インストールが完了したら、Docker Desktopを起動します。

### Linuxでのセットアップ

Linuxでは、Docker Engineを直接インストールします。以下の手順は、**Ubuntu**を例にしています。

1. パッケージ情報を更新します。

   ```bash
   sudo apt-get update
   ```

2. 依存パッケージをインストールします。

   ```bash
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```

3. Dockerの公式GPGキーを追加します。

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```

4. Dockerのリポジトリを追加し、Dockerをインストールします。

   ```bash
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   sudo apt-get update
   sudo apt-get install docker-ce
   ```

5. Dockerサービスを起動します。

   ```bash
   sudo systemctl start docker
   ```

## Docker Desktop

Docker Desktop のインストールに含まれるのは、 Docker Engine 、 Docker CLI クライアント、 Docker Compose 、 Notary 、 Kubernetes 、Credential Helper です。

### Docker Engine

Docker Engineは、Dockerコンテナをビルド、実行、管理するための中核となるコンポーネントです。コンテナの作成、起動、停止、削除などの操作を可能にし、仮想化技術を使用してアプリケーションを独立した環境にパッケージ化します。

### Docker CLI クライアント

Docker CLIクライアントは、コマンドラインを通じてDocker Engineと対話するためのツールです。コンテナのビルド、イメージの管理、ネットワークの設定など、様々な操作を行うことができます。シンプルで強力なコマンドセットを提供し、開発者が簡単にDockerを操作できるようになっています。

### Docker Compose

Docker Composeは、複数のコンテナを組み合わせてアプリケーションを構築および管理するためのツールです。YAMLファイルを使用して複数のサービス、ネットワーク、ボリュームなどを定義し、一括で起動や停止を行うことができます。複雑なアプリケーション環境の構築を簡素化し、環境の再現性を向上させます。

### Notary

Notaryは、Dockerイメージの署名と検証を行うセキュリティツールです。コンテナイメージの信頼性を向上させ、改ざんされていないことを確認するために使用されます。Dockerイメージに署名を追加することで、信頼性の高いデプロイメントが可能となります。

### Kubernetes

Kubernetesは、Dockerコンテナを自動的にデプロイ、スケーリング、管理するためのオーケストレーションツールです。コンテナクラスタを効果的に管理し、アプリケーションの高可用性やスケーラビリティを確保します。Dockerと組み合わせて使用され、大規模な分散システムの構築を容易にします。

### Credential Helper

Credential Helperは、Dockerクライアントがリモートレジストリに対して認証情報を管理するための仕組みです。ユーザーが認証情報を手動で入力することなく、Dockerが自動的に認証を行えるようになります。セキュアなイメージのプルやプッシュを容易にし、運用の簡略化を図ります。

### Docker Extension Essentials

**Ref.**: 
- [..](https://hub.docker.com/extensions/tailscale/docker-extension)


### Usage

```bash
 git clone https://github.com/<repo-name>/<name-of-your-extension>
 make build-extension
 docker extension install <repo-name>/<name-of-your-extension>
 docker extension ls
 docker pull <Docker-Hub-username>/<image-name>
 docker extension install <Docker-Hub-username>/<image-name>
```
**Ref.**: 
- [A Curated List of Docker Extensions - DEV Community](https://dev.to/docker/a-curated-list-of-docker-desktop-extensions-10k5)

### まとめ

Dockerは、コンテナ化技術を活用して開発とデプロイメントの効率を向上させるツール群を提供しています。Docker Engine、CLI、Compose、Notary、Kubernetes、Credential Helperなどの要素を理解し、組み合わせて使用することで、開発者や運用担当者は柔軟で効果的なコンテナ環境を構築できます。
