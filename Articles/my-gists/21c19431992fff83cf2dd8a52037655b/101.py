import gradio as gr
import subprocess

def run_tldr(command):
    try:
        result = subprocess.run(['tldr', command], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')
        formatted_output = f"#### {command}: {''.join(output[2])}\n```sh\n{result.stdout.strip()}\n```\n\n---\n\n"
        return formatted_output
    except Exception as e:
        return ""

def handle_input(input):
    if input['files'] and input['files'][0].endswith('.txt'):
        with open(input['files'][0], 'r') as file:
            commands = file.readlines()
    else:
        commands = input['text'].splitlines()

    result = ""
    for command in commands:
        command = command.strip()
        if command:
            result += run_tldr(command)
    return result

input_box = gr.MultimodalTextbox(label="Enter Command List")
output_box = gr.Textbox(label="Output", lines=20, interactive=False)

cmds = '''
0trace
affcat
afl
airbase-ng
aircrack-ng
airdecap-ng
airdecloak-ng
aireplay-ng
airgeddon
airmon-ng
airodump-ng
airolib-ng
airserv-ng
airtun-ng
amap
amass
apache-users
apktool
armitage
arping
asc2log
asleep
autopsy (root)
backdoor-factory
bed
beef start
beef stop
binwalk
blkcalc
blkcat
blkls
blkstat
bluelog
blueranger
bluesnarfer
braa
brutespray
btscanner
bulk_extractor
bully
Burpsuite CE
bytecode-viewer
cadaver
can-calc-bit-timing
canbusload
candump
canfdtest
cangen
cangw
canlogserver
canplayer
cansend
cansniffer
cewl
changeme
chaosreader
CherryTree
chirp
chkrootkit
chntpw
cisco-auditing-tool
cisco-global-exploiter
cisco-ocs
cisco-torch
clang
clang++
cloud-enum
commix
cowpathy
crackle
crackmapexec
crunch
cutycapt
darkstat
davtest
dbd
dc3dd
dcfldd
ddrescue
denial6
detect-new-ip6
detect-sniffer6
device-pharmer
dex2jar
dhcpig
dirb
dirbuster
dmitry
dns2tcpc
dns2tcpd
dnschef
dnsdict6
dnsenum
dnsmap
dnsrecon
dnsspoof
dnstracer
dnswalk
dos-new-ip6
driftnet
dsniff
eapmd5pass
emailharvester
enum4linux
enumax
etherape
ettercap-graphical
evil-winrm
evilgrade
ewfacquire
exe2hex
extundelete
fake_advertise6
fake_dhcps6
fake_dns6d
fake_dnsupdate6
fake_mid26
fake_mid6
fake_midrouter6
fake_mipv6
fake_mld26
fake_mld6
fake_mldrouter6
fake_router26
fake_router6
fake_solicitate6
faraday start
fcrackzip
fern wifi cracker
ferret
ffind
ffuf
fierce
fiked
flood_advertise6
flood_dhcpc6
flood_mid26
flood_mid6
flood_midrouter6
flood_router26
flood_router6
flood_solicitate6
fls
foremost
fping
fragmentation6
fragrouter
fsstat
ftest
fuzz_ip6
galleta
genkeys
genpmk
gobuster
guymager (root)
GVM Check Setup
GVM Setup
GVM Update Database
hackrf_info
hamster
hash-identifier
hashcat
hashdeep
hashid
hexinject
hfind
hping3
httrack
hydra
hydra-graphycal
iaxflood
icat
icat-sleuthkit
ifind
ike-scan
ils-sleuthkit
img_cat
img_stat
impacket
implementation6
implementation6d
inspectrum
inspy
instaloader-Insragram
intrace
inverse_ip6
inverse_lookup6
inviteflood
iodine
irpas-ass
irpass-cdp
ismtp
isotpdump
isotpperf
isotprecv
isotpsend
isotpserver
isotpsniffer
isotptun
istat
jadx-gui
javasnoop
jboss-autopwn-linux
jboss-autopwn-win
jcat
jls
john
johnny
joomscan
jSQL Injection
kill_router6
kismet
laudanum
lbd
legion (root)
linux-exploit-suggester
lynis
macchanger
macof
mactime-sleuthkit
magicrescue
mailsnarf
maltego
maskgen
masscan
mbd-sql
mdb-export
mdb-hexdump
mdb-parsecsv
mdb-sql
mdb-tables
mdk3
medusa
merge-router-config
Metasploit Console
metasploit framework
mfcuk
mfoc
mfterm
mifare-classic-format
mimikatz
minicom
miredo
missidentify
mitmproxy
mmcat
mmls
mmstat
msf payload creater
msfvenom
msgsnarf
nasm
NASM Shell
nbtscan
ncrack
netcat
netdiscover
netmask
netsniff-ng
nfc-list
nfc-mfcclassic
nikto
nishang
nmap
Nmapsi4-QT GUI for Nmap
ohrwurm
onesixtyone
ophcrack
ophcrack-cli
oscanner
OSINT tool
p0f
padbuster
parasite6
paros
parsero
pasco
passive_discovery6
patator
pdf-parser
pdf2john
pdfcrack
pdfid
pev
pipal
pixiewps
polenum
policygen
pompem
powershell empire
Powershell-empire Server
Powershell-empire-CLI
powersploit
protos-sip
proxychains
proxychains4
proxytunnel
pth-curl
pth-net
pth-rpcclient
pth-smbclient
pth-smbget
pth-sqsh
pth-winexe
pth-wmic
pth-wmis
pth-xfreerdo
pth-xfreerdp
ptunnel
pwnat
radare2
randicmp6
rarcrack
rcracki_mt
readpst
reaver
rebind
recon-ng
recordmydesktop
recoverjpeg
redfang
redir6
reglookup
responder
rfcat
rifiuti
rifiuti2
rsmangler
rsmurf6
rtlsdr-scanner
rtpbreak
rtpflood
rtpinsertsound
rtpmixsound
s3scanner
safescopy
samdump2
sbd
scalpel
scapy
scrounge-ntfs
searchsploit
sfuzz
shellnoob
sherlock
Shodan
sidguesser
siege
sigfind
siparmyknife
sipcrack
sipp
skipfish
slcan_attach
slcand
slcanpty
slowhttptest
smbmap
smtp-user-enum
smurf6
sniffjoke
snmp-check
socat
social engineering toolkit
sorter
spiderfoot
spiderfoot-cli
spike-generic_chunked
spike-generic_listen_tcp
spike-generic_send_tcp
spike-generic_send_udp
spooftooph
SQL Injection tool
SQLite database browser
sqlmap
sqlmap-automatic
sqlninja
sqlsus
srch_strings
ssldump
sslh
sslscan
sslsniff
sslsplit
sslze
starkiller
Start GVM Service
statsgen
Stop GVM Service
stunnel4
sucrack
svcrack
svcrash
svmap
svreport
svwar
swaks
t50
tcpdump
tcpflow
tcpreplay
terminater
thc-pptp-bruter
thc-ssl-dos
thcping6
theharvester
tlssled
tnscmd10g
trace6
truecrack
tsk_comparedir
tsk_gettimes
tsk_loaddb
tsk_recover
twofi
ubertooth util
udptunnel
unicorn-magic
unicornscan
uniscan-gui
unix- privesc – check
urlcrazy
urlsnarf
vinetto
voiphopper
wafw00f
wapiti
webacoo
webmitm
webscarab
webshells
websploit
webspy
weevely
wfuzz
whatweb
wifi-honey
wifite
wig
wireshark
wordlists
wpscan
xprobe2
xspy
xsser
yersinia
yersinia-graphical (root)
zap (OWASP zap)
zip2john
'''

interface = gr.Interface(
    fn=handle_input,
    inputs=input_box,
    outputs=output_box,
    title="TLDR Command Executor",
    examples=[{'text': cmds}])
interface.launch()