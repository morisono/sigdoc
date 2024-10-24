# find, fd

Why these are not same result ? 

```
for sub_dir in $sub_dirs; printf "%s ->\n%s\n" $sub_dir (fd --full-path -t f -e png "./$base_dir/$sub_dir"); end
```

このコマンドは、各サブディレクトリ名の後に、そのサブディレクトリ内で見つかったすべての.pngファイルのリストを表示します。 xargsコマンドはファイルパスを1つの文字列に連結し、それを表示します。

```
for sub_dir in $sub_dirs; printf "%s: \n%s\n" $sub_dir (find "./$base_dir/$sub_dir" -type f -name "*.png"); end
```

このコマンドは、各サブディレクトリ名の後に、指定されたすべてのサブディレクトリで見つかったすべての.pngファイルパスを表示します。 xargsコマンドはすべてのファイルパスを1つの文字列に連結し、それを表示します。

主な違いは、ファイルパスがどのようにフォーマットされ、表示されるかです。
