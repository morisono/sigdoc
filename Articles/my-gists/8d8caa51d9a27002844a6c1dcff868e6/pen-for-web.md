```sh
set URL <URL>

nc -v $URL 80
openssl s_client -connect domain.com:443

nikto -h $URL
whatweb -a 4 $URL
webtech -u <URL>
webanalyze -host $URL -crawl 2
wapiti -u $URL
W3af
nmap -p80 --script http-waf-detect $URL
zaproxy #You can use an API
nuclei -ut && nuclei -target $URL

# https://github.com/ignis-sec/puff (client side vulns fuzzer)
node puff.js -w ./wordlist-examples/xss.txt -u "http://www.xssgame.com/f/m4KKGHi2rVUN/?query=FUZZ"
```