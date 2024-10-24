# WSL 2 Tips

## Vscode on WSL2

初回実行
```
cd /mnt/c
code .
```

または、次のようにWindows側のVisual Studio Codeのシンボリックリンクを作成して使う。
```
sudo ln -s '/mnt/c/Users/<user name>/AppData/Local/Programs/Microsoft VS Code/bin/code' /usr/local/bin/code
ln -s "/mnt/c/Program Files/Docker/Docker/resources/bin/docker-credential-desktop.exe"
ln -s "/mnt/c/Program Files/Mozilla Firefox/firefox.exe"
```
  
## 動作が遅くなったと感じたときは

拡張機能の実行時間を確認してみましょう。

> Tip: Once installed, you can use the Developer: Show Running Extensions command to see whether VS Code is running the extension locally or remotely. [^2]



[^1]: https://learn.microsoft.com/ja-jp/windows/wsl/tutorials/wsl-vscode [^1]

[^2]: https://code.visualstudio.com/api/advanced-topics/remote-extensions#installing-a-development-version-of-your-extension
