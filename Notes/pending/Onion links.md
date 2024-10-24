# Onion links


### Getting start onionshare-cli
```sh
dpkg --print-architecture # Check arch
lsb_release -c # Check OS version
cat /etc/debian_version 

sudo apt install apt-transport-https

nano /etc/apt/sources.list.d/tor.list
# Add kegs
deb     [arch=amd64 signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org focal main
deb-src [arch=amd64 signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org focal main

# Add sigs
wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | sudo tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null

sudo apt update
sudo apt install tor deb.torproject.org-keyring


# OnionShare installation
# Detail: https://docs.onionshare.org/2.6.2/en/install.html#linux

pip3 install --user onionshare-cli

# sudo apt update
# sudo apt install snapd
# sudo snap install onionshare

# Or manually install
# wget https://onionshare.org/dist/2.6.2/onionshare_2.6.2_amd64.snap
# wget https://onionshare.org/dist/2.6.2/onionshare_2.6.2_amd64.snap.asc
# snap install --dangerous onionshare_VERSION_amd64.snap
```
- https://support.torproject.org/apt/#tor-deb-repo
- https://snapcraft.io/onionshare

## Onion sites

### Alternatives

- [Nitter](http://qwikxx2erhx6qrymued6ox2qkf2yeogjwypqvzoif4fqkljixasr6oid.onion/)

- [Reddit](https://github.com/01Kevin01/OnionLinksV3/?tab=readme-ov-file#Find-Your-Onion)

- [Proton mail](https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/)

- [Facebook](https://www.facebookcorewwwi.onion/)

- [Twitter](https://twitter3e4tixl4xyajtrzo62zg5vztmjuricljdp2c5kshju4avyoid.onion/)

- [Ahmia](http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/)

- [4chang](http://bhm5koavobq353j54qichcvzr6uhtri6x4bjjy4xkybgvxkzuslzcqid.onion/a/)

- [Duckduckgo](https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/)

- [Brave](https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/)

- [True tube 54](http://trutube54vqa3baer2kc7aggfc5qstxkgcmzm4qxxzfaxdsihu3znzid.onion/)

- [Archive.Today](http://archiveiya74codqgiixo33q62qlrqtkgmcitqx5u2oeqnmn5bpcbiyd.onion/)


### Search engine

- [Find Your Onion](http://fyonionq6mktpre6ustimnlqxbl5g757khnbgpyxt46lxx7umcy6ptid.onion/)

- [TorTorGO](http://tortorgohr62yxcizqpcpvwxupivwepkzl24cwkt4nnnkflvg7qraayd.onion/)

- [0xacab](https://0xacab.org/explore)


### Data sharing

- [AnonnLeaks Fileshare](http://lu4aakwcq2b5dgqufc464fireyxvjb7o2rcwmojtjwuxlmwcyi345gyd.onion/)

- [Zerobin](http://zerobinftagjpeeebbvyzjcqyjpmjvynj5qlexwyxe7l3vqejxnqv5qd.onion/)

- [Remove metadata](http://liqr2cbsjzxmpw6savgh274tuzl34x6cd56h7m7ceatnrokveffm66ad.onion/)

- File sharing

- [oshi.at](http://5ety7tpkim5me6eszuwcje7bmy25pbtrjtue7zkqqgziljwqy3rrikqd.onion/)

- [0.0g.gg (Clearweb)](https://0.0g.gg/)


### Messsaging

- [0ute3r Space](https://reycdxyc24gf7jrnwutzdn3smmweizedy7uojsa7ols6sflwu25ijoyd.onion/)

- [SuprBay: The PirateBay Forum](http://suprbaydvdcaynfo4dgdzgxb4zuso7rftlil5yg5kqjefnw4wq4ulcad.onion/)

- [remoteIP](http://bru56n3gn4gqbkgs4gf2b6i2lgz4emw67kzneamfvinbm3qf4fza7vad.onion/)

### Hosting

- [Image Hosting](http://uoxqi4lrfqztugili7zzgygibs4xstehf5hohtkpyqcoyryweypzkwid.onion/)

- [Ablative.hosting](https://hzwjmjimhr7bdmfv2doll4upibt5ojjmpo3pbp5ctwcg37n3hyk7qzid.onion/)

### Money

- [HiddenMixer](http://hiddenxdcq2fzwygfaf64uaohhts2sup4fpjplrxd3u5hrf45txumjyd.onion/)

- [First Trust Escrow Inc.](http://escrowaxbxjpez5n5zrgmytyqeqfag2w3pchadtjyfvzek57ww3ixvyd.onion/)

### MISC

- [OnionLinks](http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/)

- [Hacked databases store](http://hackeoyrzjy3ob4cdr2q56bgp7cpatruphcxvgbfsiw6zeqcc36e4ryd.onion/)


- [TorScamList](http://5n4qdkw2wavc55peppyrelmb2rgsx7ohcb2tkxhub2gyfurxulfyd3id.onion/)

- [OnionLinks](http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/)

- [.onion links directory](http://bbng47x4sdy3fralpblqcvgmzmlljah72vys6ip2wtzu6wnorggartyd.onion/)

- [SimplyTranslate](http://xxtbwyb5z5bdvy2f6l2yquu5qilgkjeewno4qfknvb3lkg3nmoklitid.onion/?text=&sl=auto&tl=ja)


### JP

```
Onionちゃんねる、ダークちゃんねる+、0chiaki、OZOZ管理人、BLACK板、淡路島、LibreJP、筑波のけしからん登、LAChan、匿名シリーズ、俺メモ、たいやき、珊瑚、今井、まーくん、ときえのき、テク子、小豆チャット、JPちゃんねるv3、陰翳シリーズ、ActiveTK、カタツムリ okojo、bibis 昆布くん

```
- [Onion ch](http://xiwayy2kn32bo3ko.onion/)

- [hachTech](http://ihnvxmcb2xfddsxr6fhllpjebxu5bjtaav7ol7nbkxqmxjiotalksqid.onion/)

- [KIRASEN/KARASEN/BLACK](http://5b7lrclibipnhlrh6gubuvn5yojfmtchthvi2onxaqtc34vje53tldid.onion/black2/)

- [dark ch](http://6tjycbfa36qhybydqerfqizot32krpk4hnbi6rzwabhmgkghch6mwvqd.onion/phpBB3/)

- [tokumei chat](http://igrafe5xheloghlc.onion/)

- [ozoz](http://aeva5sl6vv7woqqscgnp5ytgq7thigaqv3bmt6cci3zrpzrigzgbu4yd.onion/)

- [taiyaki](http://secysonfrxo2qmpzz7zox65gp65zyiys327mrdst4jdtfqo3a4lm3vqd.onion/) 
### REF

- https://nextstepbiblestudy.net/index.php/2019/12/09/pseudepigraphy-and-pseudonymity/

- https://beincrypto.com/learn/anonymity-vs-pseudonymity/

- https://github.com/Polycarbohydrate/awesome-tor#tails

- https://support.torproject.org/faq/staying-anonymous/

- https://cybersynchs.com/tor-torrenting/



### Alt-Tor


- i2p	https://geti2p.net/en/
- フリーネット	https://freenetproject.org/
- ジョンドフォックス	https://anonymous-proxy-servers.net/en/jondofox.html
	https://cdn.comparitech.com/wp-content/uploads/2016/10/gnunet-1.png
- グヌネット	https://gnunet.org/
- アクア 	https://aqua.mpi-sws.org/
- アルペンホルン	https://github.com/vuvuzela/alpenhorn


I2P	https://geti2p.net/en/

Freenet	https://freenetproject.org/

JonDoFox	https://anonymous-proxy-servers.net/en/jondofox.html

- GNUnet	https://gnunet.org/

- Aqua 	https://aqua.mpi-sws.org/

- Herd	http://www.sigcomm.org/node/3865

- Alpenhorn	https://github.com/vuvuzela/
alpenhorn

- Dissent	http://motherboard.vice.com/read/dissent-a-new-type-of-security-tool-could-markedly-improve-online-anonymity

- Riffle 	http://www.theinquirer.net/inquirer/news/2464646/riffle-is-a-new-anonymous-sharing-technique-10-times-faster-than-predecessors

- Riposte was inspired by Dissent	http://www.scs.stanford.edu/~dm/home/papers/corrigan-gibbs:riposte.pdf


### Tor related 

- https://www.comparitech.com/blog/vpn-privacy/ultimate-guide-to-tor/

- https://github.com/OnionUI/Onion



## Misc 

- [http://kcyhxvi4467xmpobjwggngm6hle4bv7u4cr3fdxsklmslj3vpmg5wiqd.onion/dwango/](http://kcyhxvi4467xmpobjwggngm6hle4bv7u4cr3fdxsklmslj3vpmg5wiqd.onion/dwango/ "http://kcyhxvi4467xmpobjwggngm6hle4bv7u4cr3fdxsklmslj3vpmg5wiqd.onion/dwango/")
- https://blog.smaranjitghose.com/mullvad-browser-a-first-glance
