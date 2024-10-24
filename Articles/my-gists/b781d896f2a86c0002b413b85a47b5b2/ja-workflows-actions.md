# Reusing Workflows と Composite Actions

## [Reusing Workflows](https://docs.github.com/ja/actions/using-workflows/reusing-workflows)

Reusing Workflowsは、同じまたは類似のワークフローを異なるリポジトリで再利用できる仕組みです。これにより、標準化されたビルド、テスト、デプロイの手順を一元管理し、プロジェクト間でコンシステントな CI/CD プロセスを確立できます。
例えば、共通のライブラリやフレームワークを使用している場合、その特定のワークフローをReusable Workflowとして定義し、異なるプロジェクトで再利用できます。

```yaml
# .github/workflows/reusing-workflow.yml

name: Reusable Workflow

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Build and Test
        run: |
          npm install
          npm test
```

## [Composite Actions](https://docs.github.com/ja/actions/creating-actions/creating-a-composite-action)
Composite Actionsは、複数のステップやジョブを1つの論理的なアクションにまとめ、再利用可能な形で提供できる仕組みです。これにより、独自のアクションを定義して、異なるワークフローで容易に再利用できます。

```
# .github/actions/my-composite-action.yml

name: 'My Composite Action'

description: 'Custom composite action for common tasks.'

runs:
  using: 'composite'
  steps:
    - name: Setup
      run: echo 'Setting up the environment'

    - name: Execute Task 1
      run: echo 'Executing Task 1'

    - name: Execute Task 2
      run: echo 'Executing Task 2'
```

そして、Reusing WorkflowsでこのComposite Actionを利用する例：

```
# .github/workflows/composite-action-example.yml

name: Composite Action Example

on:
  pull_request:
    branches:
      - main

jobs:
  use-composite-action:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Use Composite Action
        uses: ./path/to/my-composite-action
```