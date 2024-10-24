# プロジェクトの組織運用 に関する知識

1. Netlify Free plan では public repo のみ連携可能。
  ゆえにソースコードが公開情報となるが、積極的に検索されたくない場合、
  GitHubリポジトリにサイト名等特定につながる情報が含まれないようにしておくとよい。

  ```
  example-banana.com: org_name/banana -> org_name/proj_fruit_001
  ```

1. First commit のgit user を個人と紐づけたくない場合、以下のように一時的な名称でコミットする。

```
git config --global --unset credential.helper
git config --global --unset user.name
git config --global --unset user.email

git config --global user.name 'admin'
```