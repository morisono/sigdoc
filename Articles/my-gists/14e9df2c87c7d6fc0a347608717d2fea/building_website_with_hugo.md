# Hugo Website Creation Summary

#### Quickstart

https://gohugo.io/getting-started/quick-start/

Initialize your repo as a module (replace <username> and <projectname>):

`hugo mod init github.com/<username>/<projectname>`

Download the documented config file from reference template, e.g. via curl:

`curl https://raw.githubusercontent.com/<username>/<projectname>/master/exampleSite/config.yaml -O`

#### Upgrade

`hugo mod get -u`

#### Configuration and Usage

`hugo new gallery/my-item.md`

## Detail

1. Create a New Hugo Site

  ```
hugo new site mywebsite
cd mywebsite
```

1. Choose a Theme

```
git init
git submodule add https://github.com/<your><theme> themes/<theme>
```
  
1. Configure Your Site

```  
nano config.toml
baseURL = "http://example.com/" Your website's base URL
title = "My Hugo Website"       Your website's title
theme = "<theme>"                Your selected theme (e.g., "<theme>")
```

1. Add Content

```
mkdir -p content/posts
hugo new content posts/00001-first-post.md
```
```
---
title: "My First Post"
date: 2022-11-20T09:03:20-08:00
draft: true
---

# Hi there 👋🏻 This is my first post.
```
  
1. Start the Server

```
hugo server -D
```

1. Publish Your Site
  
```
hugo
```