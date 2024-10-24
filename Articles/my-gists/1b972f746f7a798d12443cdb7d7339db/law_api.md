# 法令API

- [ ] 3 種類のAPI(/条文内容/更新法令)の利用方法を理解する

  - 法令名
  
    `https://elaws.e-gov.go.jp/api/{Version}/lawlists/{法令種別} `

    - 法令取得
      `https://elaws.e-gov.go.jp/api/{Version}/lawdata/{法令番号}又は{法令 ID}`

  - 条文内容
  
    `https://elaws.e-gov.go.jp/api/{Version}/articles;lawNum={法令番号};article={条};paragraph={項};appdxTable={別表}`
     
    例:
    ```py
    params = {
      'Version': 1,
      'lawNum': '平成十五年法律第五十七号',
      # 'lawId': '415AC0000000057',
      'article': '第十一条',
      'paragraph': '',
      'appdxTable': '',
    }
    ```

  - 更新法令
  
    `https://elaws.e-gov.go.jp/api/{Version}/updatelawlists/{年月日}`
    
- https://elaws.e-gov.go.jp/apitop/#
- https://elaws.e-gov.go.jp/file/houreiapi_shiyosyo.pdf