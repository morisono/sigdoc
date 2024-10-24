# Netlify Settings

## Site configuration

1. Navigate to your Netlify dashboard.

1. Select the site you want to configure.

## Domain settigns

1. **add payment method**
To add a payment method for your site, go to the "Billing & Usage" section in your Netlify dashboard and follow the prompts to add your payment information.

1. **register custom domain**
To register a custom domain for your site, go to the "Domain settings" section in your Netlify dashboard and click the "Add custom domain" button. Follow the steps to register and configure your custom domain.

1. **dns verification**
For DNS verification of your custom domain, click on the custom domain you've added in the "Domain settings" section. Follow the instructions provided to complete the DNS verification process.

## Form Setup

1. **Create the Form**: Design the necessary form elements and embed them on your web page.

1. **Testing and Debugging**: Test the form and identify and fix any errors.

1. **Activation**: Enable the form from the Netlify site management dashboard. Navigate to `Forms > Enable form detection`.

Please note that after enabling form detection, you may need to redeploy your site for the changes to take effect.

## Deploy

1. In your Netlify dashboard, go to the "Deploys" section.

1. Set up your preferred deployment method, such as connecting to a Git repository or manual drag-and-drop deployment.
Domain settings

1. Having a netlify.toml file ready allows you to pre-configure various settings, making it very convenient.

## `netlify.toml`

You can configure your site's build and deployment settings in the netlify.toml file. Here's an example netlify.toml file:


```toml
[build]
  publish = "public"
  command = "hugo --gc --minify  --source exampleSite --themesDir ../../ -t repo --cleanDestinationDir --baseURL $HUGO_BASE_URL"

[context.production.environment]
  HUGO_VERSION = "0.118.2"
  HUGO_ENV = "production"
  HUGO_ENABLEGITINFO = "true"
  HUGO_BASE_URL = "https://awesome-identity.netlify.com"

[context.deploy-preview]
command = "hugo --gc --minify --buildFuture --source exampleSite --themesDir ../../ -t repo --baseURL $DEPLOY_PRIME_URL"

[context.deploy-preview.environment]
  HUGO_VERSION = "0.118.2"

[context.branch-deploy]
command = "hugo --gc --minify --source exampleSite --themesDir ../../ -t repo --baseURL $DEPLOY_PRIME_URL"

[context.branch-deploy.environment]
HUGO_VERSION = "0.118.2"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 301
```

Make sure to customize the netlify.toml file to match your specific project and Hugo settings. This configuration file controls how Netlify builds and deploys your site.

[^1]: https://docs.netlify.com/configure-builds/overview/　[^1]
[^1]: https://docs.netlify.com/configure-builds/file-based-configuration/[^1]
[^1]: https://docs.netlify.com/site-deploys/create-deploys[^1]
[^1]: https://docs.netlify.com/forms/setup/　[^1]
[^1]: https://www.netlify.com/integrations/very-good-security/[^1]
