
### TOR settings

- Enable HTTPS-Only Mode
- Cryptocurrency safety
- Disable JAVASCRIPT
   - https://chromewebstore.google.com/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm
- Don't open documents downloaded through Tor while online
- Use bridges and/or find company

### Torrc example
- ExcludeNodes {jp},{us},{gb},{ca},{au},{nz},127.0.0.1
- ExcludeExitNodes {jp},{us},{gb},{ca},{au},{nz},{dk},{fr},{nl},{no},{de},{be},{it},{es},{se},{at},{cz},{gr},{hu},{is},{lu},{pl},{pt},{kr},{ch},{tr},127.0.0.1
- StrictNodes 1
   - StrictNodesを1にすると必ず設定を守り、0にするとたまに破りjます。
- UseEntryGuards 0

```
 {Japan},{United States},{United Kingdom},{Canada},{Australia},{New Zealand},{Denmark},{France},{Netherlands},{Norway},{Germany},{Belgium},{Italy},{Spain},{Sweden},{Austria},{Czech Republic},{Greece},{Hungary},{Iceland},{Luxembourg},{Poland},{Portugal},{South Korea},{Switzerland},{Turkey}
```
### Bridge settings
- [Bridges](https://bridges.torproject.org/options/)
- [Bridges docs](https://www.torproject.org/docs/bridges)

```
obfs4
Makes your Tor traffic look like random data. May not work in heavily censored regions.

Snowflake
Routes your connection through Snowflake proxies to make it look like you’re placing a video call, for example.

meek-azure
Makes it look like you’re connected to a Microsoft website, instead of using Tor. May work in heavily censored regions, but is usually very slow.
```
- 1. why tor have 2 bridges
- manually add
```sh
# Step one: open Terminal.

# Step two: type in:
sudo nano /etc/tor/torrc
sudo apt install obfs4proxy
# Whinix:sudo nano /usr/local/etc/torrc.d/50_user.conf

# Step three: Paste in the following text at the bottom:
UseBridges 1
ClientTransportPlugin obfs3,obfs4 exec /usr/bin/obfs4proxy

# Step four: Paste your bridge lines below that. They may look something like this:
bridge obfs4 192.235.207.85:42086 0EEB10BF4B4FAF56D46E cert=oue8sYYw5wi4n3mf2WDOg iat-mode=0

# Step five: Ensuring that there is not a # before DisableNetwork 0, save the file with Ctrl+X, then Y, and then press enter.

# Step six: Reload Tor. Enter this command in Terminal:
sudo service tor@default reload

# Check Tor's daemon status. sudo service tor@default status
# It should include a message saying:
# Active: active (running) since ...

# In case of issues, try the following debugging steps.

# Check Tor's config.
sudo -u debian-tor tor --verify-config

# The output should be similar to the following.
# Sep 17 17:40:41.416 [notice] Read configuration file "/etc/tor/torrc".
# Configuration was valid

```

- [creatorrc](https://github.com/hephaest0s/creatorrc)

- [Hidden wiki](http://ieeppzy7cz254nz2iz7omykshnlap5ktjq3r7ujfpxagygaobpxfdbqd.onion/)

```sh
# Install nyx: utility of tor
# https://nyx.torproject.org/

sudo pip install nyx
# brew install nyx
# sudo apt install nyx
nyx --config ~/.nyx/nyxrc
```
### Browser settings

- Disable javascript: `brave://settings/content/javascript`

- Tor circuit

- Torrent

   - uTorrent
   - [qBittorrent v4.4.1](https://www.fosshub.com/qBittorrent.html?dwl=qbittorrent_4.6.5_x64_setup.exe)	https://www.qbittorrent.org/
   - Deluge	https://deluge-torrent.org/
   - Tixati	https://www.tixati.com/
   - BiglyBT	https://www.biglybt.com/
   - Vuze	https://www.vuze.com/
  - Transmission v4.0

## What's Tor2web


## References
### misc

- https://community.torproject.org/onion-services/setup/
- https://medium.com/axon-technologies/hosting-anonymous-website-on-tor-network-3a82394d7a01
- https://opensource.com/article/19/8/how-create-vanity-tor-onion-address


- https://check.torproject.org/
- https://github.com/topics/tor
- https://github.com/torpyorg/torpy
- https://github.com/StreisandEffect/streisand
- https://github.com/webfp/tor-browser-selenium
- https://github.com/MikeMeliz/TorCrawl.py
- https://github.com/torproject/stem
- https://dev.to/sigmapie8/how-to-use-requests-with-tor-1m95
- https://otariglonti.medium.com/scraping-websites-with-tor-and-selenium-and-python-part-1-c38bc803e379
- https://zenn.dev/harurow/articles/7b845931350cb8
- https://github.com/xaviha/kalitorify
- https://github.com/cedrickchee/awesome-wireguard
- https://www.reddit.com/r/VPN/
- https://www.torlock.com/

### Tor over VPN or VPN over Tor?
- [Should You Use Tor Over VPN or VPN Over Tor?](https://www.howtogeek.com/845840/should-you-use-tor-over-vpn-or-vpn-over-tor/)

## Tor Alternative

### I2P

### Freenet

### Shadowsocks

### Orbot
- https://orbot.app/en/
- https://github.com/guardianproject/orbot

### Snowflake Tor

### Lokinet
### Zeronet
- Tor対応版TorrentであるZeroNet
- トレントはポート開放しないと落とせても公開は出来ないが、ZeroNetは巨大ファイルの細分化、ハッシュ計算、Torのサーバー公開の機能を使った公開
- 表層ユーザーが落とした瞬間、もしそのユーザーがポート開放できるユーザーだったらそこを媒介してクリアネットへ拡散
- トレントは表層トラッカーに繋ぐと、IP:ポートの一覧を取得できる
- ZeroNetはonionトラッカーに繋ぎ、***.onion:ポートの一覧を取得できる
- ZeroNet使うと身バレするって言う人いるけど --tor-onlyオプション見えてないんかな
- デカいファイル配布するなら表層トレントかZeroNetかi2p torrentに
- 1ファイルならレンジリクエストで24分割 匿名性は無視
- magnet:?xt=urn
- https://cdn3.filehaus.su/files
- 64個立ち上げたTorにロードバランサ組み合わせたシステムでトレントやったら250Mbps
- curlで--proxy socket5h://127.0.0.1:9150 

- [Veracryptで暗号化した外付けHDDに入れ](https://www.veracrypt.fr/en/Security%20Requirements%20and%20Precautions.html)

- v*rayで接続ごとにcircuitをrandomize 255

- torrentで放流するよかIPFSに上げたほうが匿名性と長期保存のためにはええ

- rarで配布する人間なんてNTFS ADSにマルウェア仕込みたい人間ぐらいだし

- URLとハッシュ値対応してるからIPFSでいいんだけど、先にSHA-3でのハッシュ値リスト誰か作ってくんねえかな

- torrentってプロキシにtorかませることできるクライアントあるでしょ

- http://yutou4.com

- https://www.sendspace.com

- rendezvousセッション

- mdbファイルはどうやって見ればええんや Microsoft Access　id付で落ちてるよ

- aria2ってheaderのContent Sizeからファイルサイズ確認及びresumeしてくれたっけ

- CVE-2024-6387
- CVE-2017-16541

- http://hctxrvjzfpvmzh2jllqhgvvkoepxb4kfzdjm6h7egcwlumggtktiftid.onion/userstats-bridge-country.html?start=2024-04-07&end=2024-07-06&country=jp

- oshi.atはすぐ消されるから使えないな

- 漏洩している電話番号に匿名化したIP電話で脅迫
- canvas blocker
- 魚拓はhttps://archive.md推奨(reCAPTCHAさえ突破できればTor経由でもアクセスできる)

pastebinの代わりはhttps://privatebin.info/directoryから選べるけど削除要請に応じるかは分からない
http://uploaddd5rychb5mzvpycwr4c6pomy6ptr3gqbluivnig2jokirmf6qd.onion/ などにtxtファイルでアップロードするのもあり

- HSDirの浸透が遅くてちょっとノードが死ぬだけですぐ経路がなくなる

- sudo killall -HUP tor

- archive.mdがアクセスできなくなってるけど、archive.phに変えればアクセスできるみたい
- tbbはfirefoxだから about:debugging#/runtime/this-firefox から拡張使ったらええねん fetchで繋がったらURLリストから browser.downloads.download({url:url, saveAs: false, filename: URLに基づいて決める})でDL
browser.downloads.onChanged.addListener
でstateが`in_progress`でなくなったら(`complete`なら成功)removeListenerして次
https://rentry.org/ServerResponseChecker

```sh
mkdir -p ./mirror/dwango/sangrok ; tar --strip-components=2 -xf ./sangrok*.tar.xz -C ./mirror/dwango/sangrok
cd ./mirror
torsocks wget --retry-connrefused --tries=inf --waitretry=1 -N -m -nH -np -c http://ro4...onion/dwango/sangrok/
```
- https://manpages.debian.org/experimental/tor/tor.1.en.html#DENIAL_OF_SERVICE_MITIGATION_OPTIONS

- https://paste.centos.org/
- http://uploaddd5rychb5mzvpycwr4c6pomy6ptr3gqbluivnig2jokirmf6qd.onion/
- http://5ety7tpkim5me6eszuwcje7bmy25pbtrjtue7zkqqgziljwqy3rrikqd.onion/
- https://lelantos.feralhosting.com/kadokawa/kado/20240709/

- https://csvfileview.en.lo4d.com/windows

- wgetはWindows版だと、どうやっても文字化けが直らないので、lftpを使っている。mirrorコマンド一発で楽
- 
-  よいツールある？PikaZipで24Hで割れない PassFab for ZIP 8.2.5.3 がトレントで転がってる
GUIで数字大小英字記号桁数を設定できるから誰でも参加できる

- オフィスはCSVをShift-JISで自動的に開いてくれないときあるから

- [Veracryptを安全に使うために必要な設定](https://www.veracrypt.fr/en/Security%20Requirements%20and%20Precautions.html)

- CRC32がB0176195になるcsvを作れたら、pkcrackで暗号化を解除できる。
- 暗号化zipは平文がわかるファイルが一つでもあると解読できるって知られてるので。
https://doz13189.hatenablog.com/entry/2017/07/09/131657


```
find . -type f -cmin -1440 -exec stat -c%s {} + | awk '{s+=$1} END {printf "%f GB/day\n", s/1e9}'
```

- 言い出しっぺとして、ファイルサイズ付きのsha256sumを計算してるけど、結構時間がかかりそう。
```
find . -type f -print0 | sort -z | while IFS= read -r -d '' file; do size=$(stat -c%s "$file"); checksum=$(sha256sum "$file" | awk '{ print $1 }'); echo "$checksum $size $file"; done
```
- DL済みのファイルを黒服のmtimeとファイルサイズで比較するスクリプト

- Privoxy 

- https://ensaimada.xyz/43044/#2

- PassGAN
- https://www.4everproxy.com/
```
[116](http://5b7lrclibipnhlrh6gubuvn5yojfmtchthvi2onxaqtc34vje53tldid.onion/black2/2ovji68w/#116)NO NAME2023-08-03 Thu 20:36:09

TorProjectってなんでデフォルトの検索エンジンにDuckDuckgo採用しているんやろうか Startpageの方がデフォルトでTorのexitIPブロックしているサイトにもアクセスできるしするべきだと思うんやが、Googleベースだから検索結果も勝っているようにも思えるし

[195](http://5b7lrclibipnhlrh6gubuvn5yojfmtchthvi2onxaqtc34vje53tldid.onion/black2/2ovji68w/#195)NO NAME2023-08-28 Mon 19:14:17

わかる人教えてほしいんだけど([**https**://www.astrill.com/ja/dns-leak-test](https://www.astrill.com/ja/dns-leak-test))みたいなDNSリークのチェックができるサイトはなんでDNSリクエストのIPが分かるの？ DNSリークってISPのDNSに生IPでアクセスしてしまうことによって起きるのだからアクセス先サーバーに生IPが漏れる理由が分からないんだが


①PCで某ノーログVPNを起動しダブルVPN(海外の2箇所経由)で接続
②Linux仮想マシン(NAT接続)起動して、仮想マシン上のMullvadブラウザでVPN経由WEB接続になってることを確認
③仮想マシン上のTorブラウザを起動してダークウェブに接続
EX1：飽きたらスナップショット戻しで仮想マシンを初期化し再構築する
EX2：年1回or半年に1回、ファイル抹消ソフトでPC上のイベントログ/仮想化ソフトのログ/空き領域を抹消する
```

```
[54](http://5b7lrclibipnhlrh6gubuvn5yojfmtchthvi2onxaqtc34vje53tldid.onion/black2/1so5ag1j/#54)NO NAME2024-04-06 Sat 16:10:00

難読化にはpyarmorを使用してパッキングにはupxバイナリ生成にはpyinstallerを使用しました。 検知率が一番低かったのは難読化した.pyを実行ファイルに変換したものでした。 パッキングすると逆に検知率が上がってしまった。(それでもWindowsDefenderとかには引っかからなくて海外のマニアックなAV以外検知されなかったけど)

>>55
UPXを使ってもUPXが悪用され過ぎてすぐにAVに解凍される。そもそも、UPXは大きいPEファイルのサイズを小さくするためにするツールなので悪用するためのものではないね。
なんならupx -d [PEファイル名]で解凍できるよ。
```
### SSD Erase
- SecureErase

### Venv
- libvirt
- https://github.com/LightRider5/lnvpn
- https://lnvpn.net/phone-numbers


[Anonymous Port Scanning: Nmap + Tor + ProxyChains - ShellHacks](https://www.shellhacks.com/anonymous-port-scanning-nmap-tor-proxychains/)
## Anonymous Port Scanning Through Tor

```bash
proxychains nmap -sT -PN -n -sV -p 80,443,21,22 217.xx.xx.xx
proxychains nmap -sT -PN -n -sV -p 21 217.xx.xx.xx
```

|     |                                                     |
| --- | --------------------------------------------------- |
| -sT | full TCP connection scan                            |
| -PN | do not perform host discovery                       |
| -n  | never perform DNS resolution (to prevent DNS leaks) |
| -sV | determine service version/info                      |
| -p  | ports to scan                                       |
## Nmap Through Tor: Get Round Blocked Endpoints
- /etc/proxychains.conf
```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks4  127.0.0.1 9050
socks4 115.71.237.212 1080
```
## Lists of Free Public Proxy Servers
```
tor-resolve google.com
```

### Setting up Tor VPN on Kali Linux
- Configure Tor
- `sudo service tor start`
- Users can verify their Tor connection by visiting check.torproject.org in a web browser
- `sudo systemctl start tor.service`

```  
socks-proxy localhost 9050  
socks-proxy-retry  
```
- `sudo systemctl restart [vpn-service-name]`

- [Install TOR on Kali Linux Tutorial](https://www.hackingloops.com/install-tor-on-kali-linux-tutorial/)
- [how to install tor vpn in kali linux | by Isaachcpfer | Medium](https://medium.com/@isaachcpfer/how-to-install-tor-vpn-in-kali-linux-589e6f967827)
### 前例

大阪地検特捜部主任検事証拠改ざん事件
パソコン遠隔操作事件の誤認逮捕
PlayStation Network個人情報流出事件
桜田義孝サイバーセキュリティ担当大臣「USBが何かよくわかりません」
2024年KADOKAWA・ニコニコ動画へのサイバー攻撃

- [GitHub - Ned84/OnionSwitch: Easily switch the Tor-Exit-Node Destination Country in your Tor-Browser.](https://github.com/Ned84/OnionSwitch)

- black
```
684NO NAME2024-07-31 Wed 05:23:01
・aria2
・tor多重起動
・HAProxy
・定期的にレイテンシ測定してSIGHUP
これ組み合わせて黒服鯖から常時100Mbpsでダウンロードできてる
今回の件で色々勉強になったわ


```