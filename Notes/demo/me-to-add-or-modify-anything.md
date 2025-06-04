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

- [LibreTranslate](http://lt.vernccvbvyi5qhfzyqengccj7lkove6bjot2xhh5kajhwvidqafczrad.onion/)
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

- [Tutanota and Tor: Security and privacy go hand in hand](https://tuta.com/blog/tutanota-and-tor)
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
Onionちゃんねる、ダークちゃんねる+、0chiaki、OZOZ管理人、BLACK板、淡kgl v 路島、LibreJP、筑波のけしからん登、LAChan、匿名シリーズ、俺メモ、たいやき、珊瑚、今井、まーくん、ときえのき、テク子、小豆チャット、JPちゃんねるv3、陰翳シリーズ、ActiveTK、カタツムリ okojo、bibis 昆布くん

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


- https://blog.smaranjitghose.com/mullvad-browser-a-first-glance



### Misc 

1. [List of Tor onion services - Wikipedia](https://en.wikipedia.org/wiki/List_of_Tor_hidden_services)
2. [Should You Use Tor Over VPN or VPN Over Tor?](https://www.howtogeek.com/845840/should-you-use-tor-over-vpn-or-vpn-over-tor/)
1. [https://tails.net/](https://tails.net/ "https://tails.net/")
2. [GitHub - umutcamliyurt/Anon-File-Upload: A tool for uploading/downloading files anonymously with client-side encryption](https://github.com/umutcamliyurt/Anon-File-Upload)

1. [Perfect Privacy VPN: Fast, anonymous & safe on the Internet](https://www.perfect-privacy.com/en/)
2. [Perfect Privacy VPN: Fast, anonymous & safe on the Internet](https://restoreprivacy.com/go/perfect-privacy)
3. [Perfect Privacy Review - Secure, But Worth the Price?](https://restoreprivacy.com/vpn/reviews/perfect-privacy/)

tuta.com/privacy-policy
```
Tuta has a brand new logo. Read more here.
PRICING
BUSINESS
WHY TUTA
RESOURCES
SUPPORT
JOBS
SIGN UP
Terms and Conditions
Paragraphs, paragraphs, paragraphs…
Privacy Statement of Tutao GmbH

This Data Privacy Statement is provided in English for your convenience. Please note that in case of a dispute or discrepancy between the German Data Privacy Statement and the English translation, the German version shall prevail.

Status: September 26, 2022
General

We are responsible for the protection of your personal data, and we take this responsibility very seriously. Therefore

    Tutanota is based on the data privacy principles "data minimization" and "privacy by design".
    All user data is stored end-to-end encrypted in Tutanota (except for email addresses of users as well as senders and recipients of emails).
    We have technical and organizational measures in place which protect your data best possible.
    All data is stored in ISO 27001 certified data centers in Germany.

Processing of personal data takes place in compliance with the General Data Protection Regulation (GDPR) as well as with the country-specific data protection laws applicable to Tutao GmbH.

We are always at your disposal for any questions about privacy. Please contact us via email: hello@tutao.de.
Name and Address of the controller

Tutao GmbH Deisterstr. 17a 30449 Hannover Germany

Email address: hello@tutao.de
Data protection officer

We have appointed a data protection officer for our company. You can reach him at: privacy@tutao.de
Personal data

All personal data is kept secure by us and thus protected from unauthorized access.

For the initiation of a contractual relationship and for service provision we collect

    the newly registered email address

as inventory data.

For invoicing and determining the VAT we collect for paid product variants

    the domicile of the customer (country)
    the name and invoicing address (for private users optional)
    the VAT identification number (only for business customers of some countries)

as inventory data.

For the transaction of payments we collect depending on the chosen payment method the following payment data (inventory data):

    Banking details (account number and sort code and IBAN/BIC, if necessary bank name, account holder),
    credit card data,
    PayPal user name.

This inventory data is processed for the performance of the contract with the customer according to Art. 6 para. 1 p. 1 lit. b) GDPR. For the execution of direct debiting we will share your banking details with the authorized credit institution. For the execution of PayPal payments we will share your PayPal data with PayPal (Europe).

    Address: PayPal (Europe) S.à r.l. et Cie, S.C.A.,22-24 Boulevard Royal, L-2449 Luxembourg
    Paypal privacy statement
    Paypal contact for questions about privacy

For the execution of credit card payments your credit card data will be shared with our payment service provider Braintree. This includes the transfer of personal data into a third country (USA). An agreement entered into with Braintree defines appropriate safeguards and demands that the data is only processed in compliance with the GDPR and only for the purpose of execution of payments.

Tutanota provides services for saving, editing, presentation and electronic transmission of data, such as email service, contact management and data storage. This content data is voluntarily entered into Tutanota by the customer. When signing up for a Tutanota account, you give consent to the processing of this data according to Art. 6 para. 1 p. 1 lit. a) GDPR. All textual content is encrypted for the user and its communication partners in a way that even Tutao GmbH has no access to the data. This data can be deleted by the user.

In order to maintain email server operations, for error diagnosis and for prevention of abuse, mail server logs are stored max. 7 days. These logs contain sender and recipient email addresses and time of connection but no customer IP addresses. Storage takes place for the purposes of the legitimate interests pursued by the controller according to Art. 6 para. 1 p. 1 lit. f) GDPR.

In order to maintain operations, for prevention of abuse and and for visitors analysis, IP addresses of users are processed. Storage only takes place for IP addresses made anonymous which are therefore not personal data any more. This processing takes place for the purposes of the legitimate interests pursued by the controller according to Art. 6 para. 1 p. 1 lit. f) GDPR.

With the exception of payment data, we will not disclose your personal data including your email address to third parties. However, we can be legally bound to provide content data (in case of a valid court order) and inventory data to prosecution services. There will be no sale of data.
Period of data storage

The personal data shall be deleted no later than 30 days after termination of the contract, unless specific reasons to the contrary apply in an individual case. In case a customer objected to the amount of the charged fees, the accounting data may be stored until the objections are terminally clarified. Furthermore, inventory data can be stored for up to two years if the handling of a complaint and other reasons require this for an orderly settlement of the contract. Moreover the deletion of inventory and billing data may be omitted provided that legal regulations or the prosecution of claims require this. Order-related data and the addresses associated with the order are stored in respect to tax, contract and commercial law retention periods and erased at the end of those periods.
Cookies

We do not use cookies.
Usage statistics

We use technical analysis options very sparingly and only if you have consented in advance and to the extent that this is necessary for the further development and improvement of Tutanota. In particular, we do not use analysis tools such as Google Analytics or other third-party tools.

Our goal is to improve the user interface and the handling of Tutanota. For this it is necessary to identify the places in Tutanota that do not yet work perfectly.

If you have given consent in advance, your anonymized usage data will be sent to our servers. For this purpose, we generate and store a random ID on your device, which is shared by all accounts logged in on this device. This ID is sent along wih the usage test data to the server in case usage statistics are performed for the function used in the client. The anonymized usage data is stored by us in such a way that no conclusion can be drawn about the user. The usage statistics can refer to the following data, for example:

    sequence of certain actions
    the time required for certain actions
    points at which a certain sequence in the client is aborted

For individual usage statistics, we may subsequently ask you for an evaluation of the functionality, which can optionally be sent to us. Participation in such a survey is voluntary and also anonymous. It is not possible to draw conclusions about the participating person.

Third parties have no access to the random ID stored on your device.

You can revoke your consent to participate in the anonymized usage statistics at any time by deactivating this function in the settings of your account. The random ID stored on your device is used only as long as users of the device participate in the collection of usage statistics.

You can delete the random ID stored locally on your device yourself at any time, for instance, like this:

    In the web client (https://app.tuta.com): In the browser's menu settings by clearing the website data (e.g., "Clear browsing data" or "Clear cookies and other site data").
    Mobile apps (Android/iOS): In the app settings by clearing the app's stored data.
    Installed desktop clients: In the file system by deleting the app's stored data.

The anonymized usage data may be used for research purposes. Otherwise, the usage data is not passed on to third parties.
Campaign analysis

In order to be able to evaluate campaigns with partners and advertising campaigns (e.g. advertising via Google or other search engines), we store an ID of the campaign with your Tutanota account when you reach Tutanota via a campaign link and register a Tutanota account. To be able to assign returning users to a campaign, we store a cryptographic hash of the IP address and the user agent (including information about the user's browser and operating system) together with the campaign ID when you visit our website via a campaign link. If you visit our website via a search query and an advertising campaign, we also store the keywords and the search query together with the hash and the campaign ID. By using the hash, it is no longer possible to infer the IP address or the user agent. The keywords and the search query are not stored with the Tutanota account.

The hash and the campaign ID, keywords and search query stored together with the hash are deleted after 72 hours. Beyond this period of 72 hours, for the purpose of evaluating the campaign and until the completion of the evaluation, only completely anonymized campaign data (keywords and search query) are stored and processed without any link to the hash.

Insofar as we process personal data during the campaign analysis, this is done on the basis of Art 6 para. 1 p. lit. f) GDPR. Our interest in being able to evaluate advertising campaigns and to improve our marketing activities constitute a legitimate interest within the meaning of Art. 6 para. 1 p. lit. f) GDPR.
Rights of the data subject

According to European data protection law, you have the right

    in accordance with Art. 7 (3) GDPR, to revoke your consent once given to us at any time. This has the consequence that we may no longer continue the data processing based on this consent for the future;
    to request information about your personal data processed by us in accordance with Art. 15 GDPR. In particular, you may request information about the processing purposes, the category of personal data, the categories of recipients to whom your data have been or will be disclosed, the planned storage period, the existence of a right to rectification, erasure, restriction of processing or objection, the existence of a right of complaint, the origin of your data if it has not been collected by us, and the existence of automated decision-making, including profiling, and, if applicable, meaningful information about its details;
    in accordance with Art. 16 GDPR, to request the correction of incorrect or incomplete personal data stored by us without undue delay;
    in accordance with Art. 17 GDPR, to request the erasure of your personal data stored by us, unless the processing is necessary for the exercise of the right to freedom of expression and information, for compliance with a legal obligation, for reasons of public interest or for the establishment, exercise or defense of legal claims;
    in accordance with Art. 18 GDPR, to request the restriction of the processing of your personal data, insofar as the accuracy of the data is disputed by you, the processing is unlawful, but you object to its erasure and we no longer require the data, but you need it for the assertion, exercise or defense of legal claims or you have objected to the processing pursuant to Art. 21 GDPR;
    in accordance with Art. 20 GDPR, to receive your personal data that you have provided to us in a structured, common and machine-readable format or to request the transfer to another controller; and
    to complain to a supervisory authority in accordance with Art. 77 GDPR. As a rule, you can contact the supervisory authority of your usual place of residence or workplace or our company headquarters for this purpose.

Right of objection

Insofar as your personal data is processed on the basis of legitimate interests pursuant to Art. 6 para. 1 p. 1 lit. f GDPR you have the right to object to the processing of your personal data pursuant to Art. 21 GDPR, insofar as there are grounds for doing so that arise from your particular situation.

If you would like to exercise your right to object, it is sufficient to send an email to: hello@tutao.de.
Contact from web page

On our web pages we offer the opportunity to get in contact with us via email or contact form. In doing so personal data is voluntarily transferred to us, stored automatically and only used for the purpose of dealing with the request and getting in contact with the affected person. We will not disclose this personal data to third parties.


```
tuta.com/imprint

```
Disclaimer
Liability for contents

The contents of our pages were created with the greatest care. However, we cannot assume any liability for the correctness, completeness and topicality of the contents. As a service provider, we are responsible for our own content on these pages according to § 7 paragraph 1 TMG (German Telemedia Act) and general laws. According to §§ 8 to 10 TMG, we are not obliged to monitor transmitted or stored external information or to investigate circumstances that indicate illegal activity. Obligations to remove or block the use of information according to general laws remain unaffected. However, liability in this respect is only possible from the time of knowledge of a concrete infringement. If we become aware of any such infringements, we will remove such content immediately.
Liability for links

Our offer contains links to external websites of third parties, on whose contents we have no influence. Therefore we cannot assume any liability for these external contents. The respective provider or operator of the sites is always responsible for the contents of the linked sites. The linked pages were checked for possible legal violations at the time of linking. Illegal contents were not recognizable at the time of linking. However, a permanent control of the contents of the linked pages is not reasonable without concrete evidence of a violation of the law. If we become aware of any infringements, we will remove such links immediately.
Copyright

The contents and works on these pages created by the site operators are subject to German copyright law. The reproduction, editing, distribution and any kind of use outside the limits of copyright law require the written consent of the respective author or creator. Downloads and copies of these pages are only permitted for private, non-commercial use. Insofar as the content on this site was not created by the operator, the copyrights of third parties are respected. In particular, third-party content is marked as such. Should you nevertheless become aware of a copyright infringement, please inform us accordingly. If we become aware of any infringements, we will remove such contents immediately.
```