
# Backup

- [3-2-1 Backup](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/)
- [Home | World Backup Day — March 31st](https://www.worldbackupday.com/en/)


- ### Copy/paste your repositories
**Pros**

- “Easy”
- Preserves vendored dependencies.

**Cons**

- You will regret very fast taking this decision.

### # Zip the repository

**Pros**:

- Allows you keep (or not) vendored dependencies.
- Offline

**Cons**:

- You need to include/exclude files one by one.
- Barely better than copy-pasting.

```bash
zip -r -9 backup.zip path/to/repo
```

- 
-  ### [git bundle](https://git-scm.com/docs/git-bundle)

```bash
# You can also use --all instead of a branch for bundling  
# all branches  
$ git bundle create path/to/file.bundle branch_name# Verify the content of the bundle.  
$ git bundle verify file.bundle# Add the bundle as origin for a new repository.  
$ git init backup-repo  
$ cd backup-repo  
$ git remote add origin path/to/file.bundle  
$ git pull origin master
```
**Pros**:

- Preserves git commit history.
- Allows updating the bundle to pull changes.
- Offline.

**Cons**:

- Requires creating a new repository to see the contents.
- You can easily mess it up when you try to pull changes from the bundle.

- ### [git archive](https://git-scm.com/docs/git-archive)
```bash
git archive --output=backup.zip HEAD
```
**Pros**:

- Easy handle: it is just a zip.
- Offline

**Cons**:

- It does not preserve the git commit history.

### 同時に複数のオリジンにリポジトリをプッシュする

```
git remote set-url --add --push origin git://original/repo.git  
git remote set-url --add --push origin git://another/repo.git
```

- [リポジトリのバックアップ - GitHub Docs](https://docs.github.com/ja/repositories/archiving-a-github-repository/backing-up-a-repository)

バンドルを使用する代わりにローカルのリモート リポジトリを使用する
```
git remote add backup file://path/to/usb/repo.git
```



### REf
- [How to back up your Git repositories | by threkk | Medium](https://threkk.medium.com/how-to-back-up-your-git-repositories-1298a4487a31)