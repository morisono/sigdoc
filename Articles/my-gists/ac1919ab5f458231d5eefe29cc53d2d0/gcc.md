# gcc on WSL2 のインストール方法

WSL2 (Windows Subsystem for Linux 2) 上で GCC（GNU Compiler Collection）をインストールするために、GNU アセンブラ (as) と binutils パッケージの最新バージョンを設定する必要があります。特に、GCC 11 で使用される `--gdwarf-5` フラグのサポートを確保する必要があります。

まず、`as` が `--gdwarf-5` フラグをサポートするかどうかを確認します。以下のコマンドを使用して確認できます：

```bash
as --help | grep gdwarf
```

もし `--gdwarf-5` がサポートされていない場合、以下の手順で設定を行います：

```bash
brew install binutils
brew link binutils --force
```

これにより、`as` が `--gdwarf-5` フラグをサポートするように設定され、GCC 11 のデバッグが可能になります。

以上の手順に従うことで、WSL2 環境において GCC 11 を正しく設定し、デバッグに問題が発生しないようにすることができます。詳細な情報やトラブルシューティングに関しては、[Stack Overflow](https://stackoverflow.com/questions/74000991/gcc-11-is-not-debugging-it-shows-as-unrecognized-option-gdwarf-5) のスレッドを参考にしてください。
