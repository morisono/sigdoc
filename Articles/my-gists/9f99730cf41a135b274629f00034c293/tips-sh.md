- Find 
```sh
# /img ディレクトリーに存在するファイルを24時間以内に変更されたものを検索し、絶対パスで /tmp ディレクトリーに出力します。
fd --glob -H './img/*' \ --changed-within '1 day' --absolute-path /tmp | xargs -I {} echo {}

# 10MB以上のもの
fd --glob -H './img/*' --size >10M --absolute-path /tmp | xargs -I {} echo {}

# 2022年1月1日に変更されたものを検索
--mtime '2022-01-01' 
```



- request get multiprocessing
```sh
cat urlList.txt | parallel -j 4 wget {} -O image-{#}.png --secure-protocol=SSLv3 --no-check-certificate --verbose --debug
```

- powershell stopwatch
```powershell
$watch = New-Object System.Diagnostics.Stopwatch; 
$watch.Start(); 
foreach ($item in $computers) { test-connection $item; }; 
echo "Elapsed time:" $watch.Elapsed.TotalSeconds;
```

- 
```sh
 set items (find tmp -name "*.txt")
  set pass (openssl rand -base64 32)
  set time 1w
  echo $pass
  for i in $items
            ffsend upload $i --archive --copy -v -p $pass --shorten --qrcode -y -q
  end            
```

- 
```sh
cat list.txt | while read l; monolith -s "$l" > (basename $l | cut -d. -f1)/(basename $l); end
```


- 
```sh
cat list.csv | xargs -n 1 -i httpx --follow-redirects --download {}
```


- 
```sh
twurl -X GET "/1.1/favorites/list.json?count=200" | jq -r '.[] | .id_str' | while read id; twurl -v -X POST "/1.1/favo
rites/destroy.json?id={id}"; end
```


- parse partial HTML elem from web
```sh
powershell.exe -command get-clipboard > elem.html
cat elem.html  | pup 'span' json{} | jq
```
