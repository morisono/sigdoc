# Install Rust on Ubuntu in WSL2

システム パッケージを更新します。

Linux ディストリビューション内でターミナルを開きます。
次のコマンドを実行して、パッケージ リストを更新し、既存のパッケージをアップグレードします。
```
sudo apt update && sudo apt upgrade
```

Rustをインストールします。

ターミナルで次のコマンドを実行して Rust をダウンロードしてインストールします。
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
このコマンドは、Rustup インストーラー スクリプトをダウンロードして実行します。
インストール中に、続行するように求められます。「1」を押してから Enter を押し、デフォルトのインストールを続行します。

Rust を設定します。
インストールが完了すると、Rustup は必要な環境変数をシェル構成ファイルに追加します。
ターミナルを閉じて再度開き、変更を適用します。
Rust が正しくインストールされていることを確認するには、次のコマンドを実行します。
```
rustc --version
```

環境変数を設定します
```
# bash
export PATH="$HOME/.cargo/bin:$PATH" >> ~/.bashrc


# fish shell
echo 'set -gx PATH "$HOME/.cargo/bin:$PATH"' >> ~/.config/fish/config.fish
```

