# Memo to generate store templates.

- decode then install pdfs from url list.csv

- create dir

cat /home/user/codes/tmp/list.csv | xargs -I {} sh -c 'url=$(echo {} | sed "s/%\([0-9a-fA-F][0-9a-fA-F]\)/\\\\\x\1/g"); sub_dir=$(dirname "$url" | sed "s|https://[^/]*/||g"); mkdir -p "$sub_dir"; wget -P "$sub_dir" "$url"'


- create montage

montage -resize 400xx600 -background black -fill white -pointsize 30 -label '%t' (find . -name '*.png') -geometry +0+5 -tile 6x4 -border 10x10 -bordercolor black montage.png


- make readme, thumbnails, etc.
then create zip to 'bdist',
then upload to mega with pass-phrase. # WIP

```sh
set type tools,combos,configs

set base_dir files
set base_dir categories/rat/{clipper,stealers,cryters,miner}

set sub_dir Accounts Combos Configs Gaming Streaming Social Money Cryptocurrency VPN Keys+Codes Giftcards Tools Source Codes Bases Databases Services Clouds Proxies OpenBullet RDP+Server Scama+Letter Credit Cards+Banks SMTP+Shell+CP+WP EBooks+Methods IDs+Passports Cheats Jobs Others "Custom Order"

set tags rdp otp bot root-kit exploit-kit c2 clipper stealer cryter sniffer miner malware ddos setools uncategorized psd-template rat raidar phishing anonym panel other

mkdir -p "$base_dir"/{$sub_dir}/__TMP__/{img,src,pkg,cmd}; and touch "$base_dir"/{$sub_dir}/__TMP__/readme.txt;

❯ find categories -type d | xargs -i sh -c \
'[ -z "$(find "{}" -mindepth 1 -type d)" ] &&
echo "\
---
category: {}
title:
tag: [\"$tags\"]
lastmod:
license:
link: $base_url/{}
---
" > {}/readme.txt'

mkdir -p bdist/

find . -type d | xargs -i sh -c 'sub_dir=$(echo {} | sed "s|./||g"); base_dir=$(echo {} | sed "s|/[^/]*$||g"); cd "$base_dir"; zip -r ../bdist/{}.zip "$sub_dir"'
```