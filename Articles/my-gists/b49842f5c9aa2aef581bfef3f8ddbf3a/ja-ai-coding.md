# AI Coding の手引き

## Auto completion の設定

- GitHub Copilot


## Auto commit message の設定

```sh
npm install -g opencommit
oco hook set
oco config set OCO_OPENAI_API_KEY=$OPENAI_API_KEY
oco config set OCO_DESCRIPTION=true
# oco config set OCO_LANGUAGE=en
# oco config set OCO_EMOJI=false
# config set OCO_MODEL=gpt-4 # gpt-3.5-turbo-16k (default), gpt-3.5-turbo-0613, gpt-3.5-turbo

git config --global core.editor true

git add .
opencommit
```
- https://github.com/di-sukharev/opencommit
- https://platform.openai.com/account/api-keys


## Auto code review

- CodeRabbit