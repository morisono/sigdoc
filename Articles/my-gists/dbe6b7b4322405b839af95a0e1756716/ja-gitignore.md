# gitignore


~/.config/git/ignore: 

バージョン管理され、クローンを通じて他のリポジトリに配布する必要があるパターン（つまり、すべての開発者が無視したいファイル）は、.gitignoreファイルに入れるべきです1。

.git/info/exclude: 

特定のリポジトリに特有であり、他の関連するリポジトリと共有する必要がないパターン（例えば、リポジトリ内に存在するが、一人のユーザーのワークフローに特化した補助ファイル）は、$GIT_DIR/info/excludeファイルに入れるべきです1。

core.excludesFileで指定されたファイル: 

ユーザーがすべての状況でGitに無視させたいパターン（例えば、ユーザーの選択したエディタによって生成されるバックアップや一時ファイル）は、通常、ユーザーの~/.gitconfigで指定されたcore.excludesFileによって指定されたファイルに入れます1。そのデフォルト値は$XDG_CONFIG_HOME/git/ignoreです。もし$XDG_CONFIG_HOMEが設定されていないか空であれば、代わりに$HOME/.config/git/ignoreが使用されます1。

```sh
# ディレクトリとファイルを作成
mkdir -p (dirname $gitignore); and touch $gitignore

# .gitignoreテンプレートをダウンロード
set gitignore ~/.config/git/ignore
set urls \
https://raw.githubusercontent.com/github/gitignore/main/Global/Windows.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/Global/macOS.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/Global/VisualStudioCode.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/C%2B%2B.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/Go.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/Lua.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore \
https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore \


# 設定を追記
# Ignore Identifiers
*.Identifiers
```

https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files

https://github.com/github/gitignore

https://toptal.com/developers/gitignore/