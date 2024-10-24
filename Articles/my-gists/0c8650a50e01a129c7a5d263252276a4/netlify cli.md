# Netlify CLI

```sh
# Install
npm install netlify-cli -g
netlify login
netlify --telemetry-disable

# Setup
netlify init

# Build Test
netlify build --dry
netlify build --context deploy-preview

# Deploy manually
netlify deploy --dir=_site --functions=functions
netlify deploy --prod

# Linking
netlify link
```

https://docs.netlify.com/cli/get-started/?_gl=1%2axi05is%2a_gcl_au%2aMjE0NzMxNjgyNy4xNjk0ODI5ODM1