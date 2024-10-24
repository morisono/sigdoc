# Proton Client Usage

python setup.py installでモジュールをインストールすると、通常はグローバルなPython環境にモジュールがインストールされます。これにより、そのモジュールはプロジェクトルート外でも使用可能になります。

具体的には、システム全体で共有されるPythonのsite-packagesディレクトリにモジュールがインストールされます。このディレクトリは通常、Pythonの実行環境ごとに異なりますが、一般的にはシステム全体で利用可能な場所になります。

例えば、Linuxの場合、/usr/lib/python3.10/site-packagesなどがそのようなディレクトリです。このため、他のプロジェクトやスクリプトからもそのモジュールを利用できます。

ただし、一部のプロジェクトでは仮想環境や仮想環境マネージャ（virtualenv、condaなど）を使用してプロジェクトごとに独立したPython環境を構築することがあります。この場合、プロジェクトごとに仮想環境を作成し、その中にモジュールをインストールすることが一般的です。これにより、プロジェクトごとに異なるバージョンのモジュールを使用できるため、依存関係の衝突を避けることができます。

開発中は、pip install -e .を実行して開発モードでプロジェクトをインストールすることが一般的です。これにより、プロジェクトが変更されるたびに即座に変更が反映されます。

https://github.com/ProtonMail/proton-python-client?tab=readme-ov-file#setup

```sh
pip install -r requirements.txt
python setup.py install
pip install -e .
pip show proton-client
```

導入の際はトップレベルのパッケージ名を使います
```
from proton.api import Session, ProtonError
```