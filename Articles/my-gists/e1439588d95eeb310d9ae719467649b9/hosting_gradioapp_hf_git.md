# HF Spacesでのホスティング

GradioアプリをHugging Face Spacesにデプロイするための3つの方法があります。

1. ターミナルから: アプリのディレクトリでgradio deployを実行します。CLIが基本的なメタデータを収集し、アプリを起動します。スペースを更新するには、このコマンドを再実行するか、Github Actionsオプションを有効にして、git pushでSpacesを自動更新します。
1. ブラウザから: Gradioモデルと関連ファイルが含まれるフォルダをここにドラッグ＆ドロップします。
1. GitリポジトリとSpacesの連携: SpacesがGradioアプリをGitリポジトリからプルします。

以下に3. による手順を示します。

```sh
python -m pip install huggingface_hub
huggingface-cli login
git config --global credential.helper store
```

```sh
 # If your needs to deal large file
brew install git-lfs
git lfs track "fonts/*.ttf"
git lfs install
huggingface-cli lfs-enable-largefiles .

# (1.) complete auth may be needed, interaction will start. 
gradio deploy --app-file <app.py> #  files/folder inside current directory will be sent recursively.　
git clone https://huggingface.co/spaces/<your_id>/<your_repo> # Then clone repo to get readme/requirements generated automatically.

# check and edit dependencies and readme, etc.
pipreqs . --force --savepath=requirements.txt 
gradio deploy

---

# then send to remote server
git init

git add .
git add .gitattributes

git commit -m 'first commit'
git push origin main

# to include as git branch/ update hf.co : 
git remote add space https://huggingface.co/spaces/<your_name>/<your_repo>
git push space main
```

[^1]: https://huggingface.co/docs/hub/repositories-getting-started [^1]
[^2]: https://www.gradio.app/guides/sharing-your-app [^2]
[^3]: https://huggingface.co/settings/tokens [^3]