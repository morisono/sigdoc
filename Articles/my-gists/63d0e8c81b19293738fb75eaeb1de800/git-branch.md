# ブランチ操作

```sh
git branch -v # 新しいブランチの作成
git checkout -b features # 新規ブランチの作成と切り替え

git branch -a # 一覧の表示
git branch -d branch-to-delete # 削除
```
- 新規ブランチ作成後のプッシュ

```sh
git push -u origin HEAD:refs/heads/pubs
```

[Creating and deleting branches within your repository](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository)
