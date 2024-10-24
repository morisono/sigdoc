# Netlify Build hook

## Build Hook URLをGitHubのシークレットに設定する

ここではビルド先を秘匿するため、Actions workflowとHookを設定します。

1. `Build & Deploy > Build hooks` から取得したurlを GitHub.secret に `NETLIFY_BUILD_HOOK_URL`として登録する。

1. Actions workflow を構成する。

```
name: Trigger Netlify Build
on:
  workflow_dispatch:
  schedule:
    # Run at 0815 daily
    - cron: '15 8 * * *'
jobs:
  build:
    name: Request Netlify Webhook
    runs-on: ubuntu-latest
    steps:
      - name: Curl request
        run: curl -X POST -d {} ${{ secrets.NETLIFY_BUILD_HOOK_URL }}
```