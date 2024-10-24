# 2Captchaを使用したreCAPTCHAの解決方法

この記事では、2Captchaの日本語版ウェブサイトを使用してウェブサイト上のCAPTCHAを解決する方法を詳しく説明します。

## 準備

- **2Captcha API KEY**: 2CaptchaのAPIキーを取得します。
- **reCAPTCHA Target URL**: 解決したいreCAPTCHAが設置されているウェブサイトのURLを用意します。
- **reCAPTCHAのgoogle_site_key**: reCAPTCHAのdata-sitekeyを取得します。これはDeveloper Toolsを使用してウェブサイトから取得できます。


## アカウントの作成

1. 2Captchaの公式ウェブサイト（[https://2captcha.com/ja/](https://2captcha.com/ja/)） にアクセスし、アカウントを作成します。

2. アカウント作成後、ログインし、ダッシュボードにアクセスします。

## 支払いと完了

2CaptchaはCAPTCHAの解決に先んじて、最低 $3/1000 アクセスの課金を請求します。

## APIキーの取得

ダッシュボードで、APIキーを取得します。これは2Captchaをプログラムから使用する際に必要です。

## APIの使用

2Captcha APIを使用してreCAPTCHAを解決するには、以下の手順を実行します。

  ### Pythonスクリプトの作成

  以下のPythonスクリプトを使用して、reCAPTCHAを解決し、トークンを取得します。

  ```python
  import json
  import time    
  import getpass
  import requests
  from selenium import webdriver
  from selenium.webdriver.support.ui import Select

  # 2Captcha API KEY
  service_key = 'Your2CaptchaAPIKey'
  # reCAPTCHAのgoogle_site_key
  google_site_key = 'YourGoogleSiteKey'
  # reCAPTCHAが設置しているURL
  pageurl = 'YourTargetURL'

  # Selenium WebDriverの初期化
  driver = webdriver.Chrome()

  # reCAPTCHAのiframe内のtextareaタグを表示する
  driver.get(pageurl)
  driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

  # 2CaptchaにreCAPTCHAを送信
  url = f"http://2captcha.com/in.php?key={service_key}&method=userrecaptcha&googlekey={google_site_key}&pageurl={pageurl}"
  resp = requests.get(url)
  if resp.text[0:2] != 'OK':
      quit(f'Service error. Error code:resp.text')
  captcha_id = resp.text[3:]

  # 2Captchaからトークンを取得
  fetch_url = f"http://2captcha.com/res.php?key={service_key}&action=get&id={captcha_id}"

  for i in range(1, 10):
      time.sleep(5)
      resp = requests.get(fetch_url)
      if resp.text[0:2] == 'OK':
          break
  print('Google response token: ', resp.text[3:])

  # reCAPTCHAフォームにトークンを入力
  driver.find_element_by_id('g-recaptcha-response').send_keys(resp.text[3:])
  ```
このスクリプトは、2Captchaを使用してreCAPTCHAを解決し、取得したトークンをウェブサイトのreCAPTCHAフォームに入力します。

以上の手順に従うことで、2Captchaを使用してウェブサイト上のCAPTCHAを効果的に解決できます。必要に応じて、2Captchaのドキュメンテーションを参照して、APIの詳細やオプションを理解してください。

[2Captcha 日本語版ウェブサイト](https://2captcha.com/ja/)