# Git コンフリクトへの一般的な対処

リモートの main ブランチから変更を取得し、ローカルの main ブランチにマージしようとします。
Gitコンフリクトは、複数のブランチで同じファイルの同じ部分を編集し、それをマージしようとしたときに発生します。この状況では、Gitはどの変更を優先するかを自動的に決定できません。その結果、コンフリクトが発生し、手動で解決する必要があります。

```
❯ git pull origin main
From https://github.com/***/***

 * branch            main       -> FETCH_HEAD
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint: 
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

このエラーメッセージは、ローカルのmainブランチとリモートのmainブランチが異なるコミットで進行しており、Gitがどのようにそれらを調整するかを指定していないことを示しています。この状態では、Gitはどの操作を実行すべきかを判断できないため、指示を与える必要があります。

**コンフリクトの解決**

Gitコンフリクトを解決するには、競合しているファイルを手動で編集し、競合を解消する必要があります。競合が発生したファイルは、次のような形式でマークされます：
```
<<<<<<< HEAD
// ここにローカルの変更が表示されます
=======
// ここにリモートの変更が表示されます
>>>>>>> branch-name
```
このマークアップを使用して、どちらの変更を保持するか、または両方の変更を組み合わせる方法を選択します。競合を解決したら、ファイルを保存します。


**コンフリクトのマークを削除**

競合が解決したら、ファイルからコンフリクトのマークアップ（<<<<<<< HEAD、=======、>>>>>>> branch-name）を削除します。


**コンフリクトをコミット・プッシュ**

```
git commit -m "Merge conflict resolved"
git push origin main
```

これで、コンフリクトが解決し、リモートブランチとローカルブランチが同期されます。

---

その他、指示を与える方法として、以下の3つの選択肢があります：

**マージ**する

リモートブランチから取得した変更をローカルブランチにマージします。これは競合が発生しない場合に使用できます。以下のコマンドを実行します：

```bash
git pull origin main --no-rebase
```

エディタが開きます。確認後、`:qa`で完了します。

**リベース**する

リモートブランチから取得した変更をローカルブランチの最新コミットの上にリベースします。これは、クリーンな履歴を維持するために使用できます。以下のコマンドを実行します：

```bash
git pull origin main --rebase
```


**ファストフォワードのみを許可**する

このオプションを選択すると、リモートブランチの変更が現在のローカルブランチにファストフォワードできる場合のみ変更が取得されます。競合が発生した場合、このオプションは変更を拒否します。以下のコマンドを実行します：

```bash
git pull origin main --ff-only
```

どのオプションを選択するかは、プロジェクトのワークフローと共同作業の方法に応じて異なります。一般的には、競合が発生しない場合はリベースオプションを使用し、競合が予想される場合はマージオプションを使用することが多いです。

選択したオプションを実行して、コミットを調整し、その後に再度 git push を実行してください。