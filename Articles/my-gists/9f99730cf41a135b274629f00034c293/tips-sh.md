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


-  bulk download Zenn dev or Qiita.com
```bash
#!/usr/bin/env fish

# Function to handle script termination gracefully
function on_exit
	echo "Exiting script..."
	# Perform any cleanup if necessary
end

# Trap signals for graceful exit
trap on_exit INT TERM

# Base URL
set base_url "https://zenn.dev"
# set base_url "https://qiita.com/"

# Step 1: Parse HTML and extract URLs
echo "Parsing HTML and extracting URLs..."
if not cat elem.html | pup -p json{} | jq -r '.. | .href? | select(. != null)' > url-list.txt
	echo "Error: Failed to extract URLs from HTML"
	exit 1
end
echo "URLs extracted successfully."

# Step 2: Download content from URLs
echo "Downloading content from URLs..."
cat url-list.txt | uniq | grep '/articles/' | head -n 5 | while read -l url
	set output (echo "$url" | awk -F'/' '{print $2"/"$4".html"}')
	echo "Processing $url -> $output"
	mkdir -p (dirname $output)

	# Use curl instead of monolith for a simpler example
	if not curl -s "$base_url$url" -o $output
		   echo "Error: Failed to download $base_url$url"
		   continue
	    end
	echo "Downloaded $base_url$url successfully."
end

# Step 3: Create list.json from elem.html
echo "Creating list.json..."
if not cat elem.html | pup -p json{} | jq -r '[
	.. | objects
	| select(.class? == "CommonPostItemRow_mainLink__RiTOf" and .href)
	| {
	    href: .href,
	    title: (.children[]? | select(.class? == "CommonPostItemRow_title__C_QvL").text // empty),
	    date: (.children[]? | select(.class? == "CommonPostItemRow_metaContainer__Kn2zI") | .children[]? | select(.class? == "CommonPostItemRow_meta__PVsvB").text // empty)
	}
 ]' > list.json
	echo "Error: Failed to create list.json"
	exit 1
end
echo "list.json created successfully."

# Qiita trends: Selector
# #HomeTrendPage-react-component-ddeeb7ff-b5e0-4b09-94b8-0ef3003df11e > div > main > div.style-1p44k52 > article:nth-child(1) > a


# Step 4: Group by href and create retrieve.json
echo "Grouping by href and creating retrieve.json..."
if not cat list.json | jq -r 'group_by(.href) | map({href: .[0].href, title: .[0].title, date: .[0].date, likes: .[1].date})' > retrieve.json
	echo "Error: Failed to create retrieve.json"
	exit 1
end
echo "retrieve.json created successfully."

# Step 5: Create index.md from retrieve.json
echo "Creating index.md..."
if not cat retrieve.json | tr '\n\n' '\n' | tr '[' '\[' | tr ']' '\]' | jq -r '.[] | "1. [\(.title)](.\(.href).html) \(.date) ♡ \(.likes)\n"' | sed 's/\/articles//g' > index.md
	echo "Error: Failed to create index.md"
	exit 1
end
echo "index.md created successfully."

echo "Script completed successfully."

```