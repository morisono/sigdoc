# Auto Deploy to Vercel workflow

vercel.json:

```json
{
  "git": {
    "deploymentEnabled": false
  }
}
```

```yaml
name: Vercel Preview Deployment
env:
  VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
  VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
on:
  pull_request:
    types: [opened, synchronize]
    branches:
      - main
jobs:
  deploy_preview:
    runs-on: ubuntu-latest
    steps:
      - name: Create Deployment
        id: create_deployment
        uses: octokit/request-action@v2.x
        with:
          route: POST /repos/{owner}/{repo}/deployments
          owner: ${{ github.repository_owner }}
          repo: ${{ github.event.repository.name }}
          ref: ${{ github.head_ref }}
          environment: preview
          required_contexts: '[]'
          auto_merge: false
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Checkout Code
        uses: actions/checkout@v2
        with:
          ref: ${{ github.head_ref }}
      - name: Install Vercel CLI
        run: npm install --global vercel@latest
      - name: Deploy Project to Vercel
        id: deployment_to_vercel
        run: | 
          set +e
          preview_url=$(vercel deploy --token=${{ secrets.VERCEL_TOKEN }})
          echo "deploy_exit_code=$?" >> $GITHUB_OUTPUT
          set -e
          echo "preview_url=${preview_url}" >> $GITHUB_OUTPUT
      - name: Update Deployment Status
        uses: octokit/request-action@v2.x
        with:
          route: POST /repos/{owner}/{repo}/deployments/{deployment_id}/statuses
          owner: ${{ github.repository_owner }}
          repo: ${{ github.event.repository.name }}
          deployment_id: ${{ fromJson(steps.create_deployment.outputs.data).id }}
          state: ${{ steps.deployment_to_vercel.outputs.deploy_exit_code == 0 && 'success' || 'failure' }}
          environment_url: ${{ steps.deployment_to_vercel.outputs.preview_url }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Promote Error
        run: exit ${{ steps.deployment_to_vercel.outputs.deploy_exit_code }}

```