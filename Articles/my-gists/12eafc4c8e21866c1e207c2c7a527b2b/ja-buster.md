[dirsearch](https://github.com/maurosoria/dirsearch) 
[ffuf](https://github.com/ffuf/ffuf)
wfuzz
gobuster
urlbuster
dirbuster
[dirhunt](https://github.com/Nekmo/dirhunt)
cloakquest3r
theintruder
[feroxbuster](https://github.com/epi052/feroxbuster)
[waybackurls](https://github.com/tomnomnom/waybackurls)
Nuclei 
git clone https://github.com/cipher387/juicyinfo-nuclei-templates
/home/user/codes/github.com/0xKayala/NucleiFuzzer
https://github.com/PortSwigger/burp-smart-buster
```
dirsearch  -e php,html,js -u http://abehiroshi.la.coocan.jp -t 20 --exclude-sizes 1B,243KB --max-recursion-depth 3 --recursion-status 200-399 --subdirs /,admin/,folder/ --max-recursion-depth 3 --recursion-status 200-399 -o target.json
```

```sh
gobuster dns -d abehiroshi.la.coocan.jp -t 50 -w wordlist2.txt
gobuster dir -u http://abehiroshi.la.coocan.jp -w wordlist2.txt -x .php,.html > gobusterresults.txt
sed -i 's/2K/abehiroshi.la.coocan.jp/g' gobusterresults.txt
sed 's/(.*//' gobusterresults.txt >gobusterresults_clean.txt
sed 's/^.\{3\}//' gobusterresults_clean.txt > gobusterresults_clean_final.txt

```

```
dirhunt http://abehiroshi.la.coocan.jp
```

```
echo http://abehiroshi.la.coocan.jp | waybackurls
```

```
feroxbuster -u http://abehiroshi.la.coocan.jp -x pdf -x js,html -x php txt json,docx
```

```
echo 'abehiroshi.la.coocan.jp' > urls.txt
nuclei -t juicyinfo-nuclei-templates/juicy_info/pdf.yaml -l urls.txt
nuclei -t juicyinfo-nuclei-templates/juicy_info/email.yaml -l urls.txt

| xargs -a files_urls.txt -I{} curl -# -O {}
```

```
pip install MetaDetective
sudo apt install libimage-exiftool-perl
MetaDetective -d /workspace/company_information_gathering_automation/
python3 src/MetaDetective/MetaDetective.py --scraping --scan --url https://example.com/
```

```
gem install wayback_machine_downloader
wayback_machine_downloader http://sector035.nl
nuclei -u /workspace/company_information_gathering_automation/websites  -t juicyinfo-nuclei-templates/juicy_info/url.yaml

```

Awesome Wordlists	https://github.com/gmelodie/awesome-wordlists
Backup files wordlist	https://github.com/xajkep/wordlists/blob/master/discovery/backup_files_only.txt
Backup files with path wordlist	https://github.com/xajkep/wordlists/blob/master/discovery/backup_files_with_path.txt
Xajkep wordlists	https://github.com/xajkep/wordlists
Kkrypt0nn wordlists	https://github.com/kkrypt0nn/wordlists
https://github.com/Ademking/repolist