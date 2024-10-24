---
title: "Netlify CMSとWowchemyを使ったウェブサイトの構築"
date: 2023-09-03
categories:
  - 技術
tags:
  - Netlify CMS
  - Wowchemy
---

# Netlify CMSとWowchemyを使用したウェブサイトの構築

このガイドでは、Netlify CMSとWowchemyを使用してプロフェッショナルなウェブサイトを構築する手順について説明します。

1. **Wowchemyのセットアップ**

  Wowchemyは、Hugoテーマを提供するツールです。まず、Wowchemyをセットアップします。

  1. Hugoのインストール:

  ```shell
  brew install hugo
  ```

  1. Wowchemyテーマのインストール:

    1. WowchemyのGitHubリポジトリからテーマをクローンします

    ```  
    git clone https://github.com/wowchemy/starter-academic.git my-academic-website
    cd my-academic-website
    ```

    1. Wowchemyテーマをサブモジュールとして追加します
    
    ```
    git submodule update --init --recursive
    ```

  1. ウェブサイトのカスタマイズ:

  Wowchemyテーマのカスタマイズを行い、コンテンツを追加します。Wowchemyのドキュメンテーションを参照してください。  [from Here](https://wowchemy.com/docs/)

1. **Netlify CMSのセットアップ**

Netlify CMSは、ウェブサイトのコンテンツを管理するためのユーザーフレンドリーなインターフェースを提供します。

  1. **Netlifyアカウントの作成**:

  Netlifyでアカウントを作成します。

  1. **ウェブサイトをデプロイ**:

  Wowchemyで作成したウェブサイトをGitHubリポジトリにプッシュし、Netlifyにデプロイします。Netlifyは自動的にビルドしてウェブサイトをホスティングします。

  1. **Netlify CMSの設定**:

  Netlifyのダッシュボードから、"Settings > Identity"セクションに移動し、認証を有効にします。OAuthプロバイダーを設定して、GitHubなどのアカウントでログインできるようにします。 [from here](https://v1.netlifycms.org/docs/)

  1. **Netlify CMSの設定ファイル**:

  リポジトリにconfig.ymlという名前のNetlify CMSの設定ファイルを作成します。これにはコンテンツの設定やコレクションの定義が含まれます。Netlify CMSのドキュメンテーションを参照してください。


1. **コンテンツの管理**

Netlify CMSを使用して、ウェブサイトのコンテンツを管理できます。Markdownファイルや画像などのコンテンツを追加、編集、削除できます。

ウェブサイトのコンテンツの変更は、GitHubリポジトリにコミットされ、Netlifyに自動的にデプロイされます。

以上で、Netlify CMSとWowchemyを使用したウェブサイトの構築手順が完了しました。ウェブサイトのデザインやコンテンツのカスタマイズは、Wowchemyのドキュメンテーションを参考にして行ってください。