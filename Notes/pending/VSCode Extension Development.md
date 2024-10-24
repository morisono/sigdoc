---
title: VSCode Extension Development
allDay: true
date: 2024-07-08
completed:
---
# VSCode Extension Development


昨今の脆弱性を持ちうるAttack Surfaceとして、特筆して以下の領域が挙げられます。

- webshell 
- webproxy
- vscode-extension


これらのうち、利用率の高いVSCode Extensionの開発経験を通して、セキュリティ技術を学びましょう。

## Getting started

```
mkdir my-vscode-extension
cd my-vscode-extension
```

```
npm install -g yo generator-code
```

```
yo code
```

```
npx create-react-app bee --template typescript
cd bee
```

```
npm i -D tailwindcss postcss
npx tailwindcss init
```



## Plan[Imgur upload error]()


## Ref.


- [Building a VS Code Extension to Fetch and Display Content from an API - DEV Community](https://dev.to/shriya_5/building-a-vs-code-extension-to-fetch-and-display-content-from-an-api-31f1)
- https://code.visualstudio.com/api/get-started/your-first-extension
- [generator-code - npm](https://www.npmjs.com/package/generator-code)
- https://github.com/microsoft/vscode-docs/blob/main/api/index.md
- https://snyk.io/blog/modern-vs-code-extension-development-basics/
- 