# Linux Command 101
# Essential

## Table of Contents

<!-- vscode-markdown-toc -->
1. [Essential](#Essential)
	1.1. [ls:   List directory contents.](#ls:Listdirectorycontents.)
	1.2. [find:   Find files or directories under a directory tree, recursively.](#find:Findfilesordirectoriesunderadirectorytreerecursively.)
	1.3. [chmod:   Change the access permissions of a file or directory.](#chmod:Changetheaccesspermissionsofafileordirectory.)
	1.4. [chown:   Change user and group ownership of files and directories.](#chown:Changeuserandgroupownershipoffilesanddirectories.)
	1.5. [scp:   Secure copy.](#scp:Securecopy.)
	1.6. [rsync:   Transfer files either to or from a remote host (but not between two remote hosts), by default using SSH.](#rsync:TransferfileseithertoorfromaremotehostbutnotbetweentworemotehostsbydefaultusingSSH.)
	1.7. [diff:   Compare files and directories.](#diff:Comparefilesanddirectories.)
	1.8. [sort:   Sort lines of text files.](#sort:Sortlinesoftextfiles.)
	1.9. [xargs:   Execute a command with piped arguments coming from another command, a file, etc.](#xargs:Executeacommandwithpipedargumentscomingfromanothercommandafileetc.)
	1.10. [sed:   Edit text in a scriptable manner.](#sed:Edittextinascriptablemanner.)
	1.11. [awk:   A versatile programming language for working on files.](#awk:Aversatileprogramminglanguageforworkingonfiles.)
	1.12. [tr:   Translate characters: run replacements based on single characters and character sets.](#tr:Translatecharacters:runreplacementsbasedonsinglecharactersandcharactersets.)
	1.13. [grep:   Find patterns in files using regular expressions.](#grep:Findpatternsinfilesusingregularexpressions.)
	1.14. [curl:   Transfers data from or to a server.](#curl:Transfersdatafromortoaserver.)
	1.15. [wget:   Download files from the Web.](#wget:DownloadfilesfromtheWeb.)
	1.16. [ncdu:   Disk usage analyzer with an ncurses interface.](#ncdu:Diskusageanalyzerwithanncursesinterface.)
	1.17. [pdfimages:   Utility for extracting images from PDFs.](#pdfimages:UtilityforextractingimagesfromPDFs.)
	1.18. [tar:   Archiving utility.](#tar:Archivingutility.)
	1.19. [zip:   Package and compress (archive) files into a Zip archive.](#zip:PackageandcompressarchivefilesintoaZiparchive.)
	1.20. [top:   Display dynamic real-time information about running processes.](#top:Displaydynamicreal-timeinformationaboutrunningprocesses.)
	1.21. [htop:   Display dynamic real-time information about running processes. An enhanced version of top.](#htop:Displaydynamicreal-timeinformationaboutrunningprocesses.Anenhancedversionoftop.)
	1.22. [ps:   Information about running processes.](#ps:Informationaboutrunningprocesses.)
	1.23. [cron:   A system scheduler for running jobs or tasks unattended.](#cron:Asystemschedulerforrunningjobsortasksunattended.)
	1.24. [reboot:   Reboot the system.](#reboot:Rebootthesystem.)
	1.25. [tmux:   Terminal multiplexer.](#tmux:Terminalmultiplexer.)
	1.26. [screen:   Hold a session open on a remote server. Manage multiple windows with a single SSH connection.](#screen:Holdasessionopenonaremoteserver.ManagemultiplewindowswithasingleSSHconnection.)
	1.27. [ping:   Send ICMP ECHO_REQUEST packets to network hosts.](#ping:SendICMPECHO_REQUESTpacketstonetworkhosts.)
	1.28. [telnet:   Connect to a specified port of a host using the telnet protocol.](#telnet:Connecttoaspecifiedportofahostusingthetelnetprotocol.)
	1.29. [traceroute:   Print the route packets trace to network host.](#traceroute:Printtheroutepacketstracetonetworkhost.)
	1.30. [tcpdump:   Dump traffic on a network.](#tcpdump:Dumptrafficonanetwork.)
	1.31. [netstat:   Display network-related information such as open connections, open socket ports, etc.](#netstat:Displaynetwork-relatedinformationsuchasopenconnectionsopensocketportsetc.)
	1.32. [ifconfig:   Network Interface Configurator.](#ifconfig:NetworkInterfaceConfigurator.)
	1.33. [route:   Use route cmd to set the route table.](#route:Useroutecmdtosettheroutetable.)
	1.34. [ip:   Show/manipulate routing, devices, policy routing and tunnels.](#ip:Showmanipulateroutingdevicespolicyroutingandtunnels.)
	1.35. [ss:   Utility to investigate sockets.](#ss:Utilitytoinvestigatesockets.)
	1.36. [iw:   Show and manipulate wireless devices.](#iw:Showandmanipulatewirelessdevices.)
	1.37. [arp:   Show and manipulate your system's ARP cache.](#arp:ShowandmanipulateyoursystemsARPcache.)
	1.38. [nc:   Redirect I/O into a network stream through this versatile tool.](#nc:RedirectIOintoanetworkstreamthroughthisversatiletool.)
	1.39. [nslookup:   Query name servers for various domain records.](#nslookup:Querynameserversforvariousdomainrecords.)
	1.40. [dig:   DNS lookup utility.](#dig:DNSlookuputility.)
	1.41. [whois:   Command-line client for the WHOIS (RFC 3912) protocol.](#whois:Command-lineclientfortheWHOISRFC3912protocol.)
	1.42. [ncat:   Read, write, redirect, and encrypt data across a network.](#ncat:Readwriteredirectandencryptdataacrossanetwork.)
	1.43. [perl:   The Perl 5 language interpreter.](#perl:ThePerl5languageinterpreter.)
	1.44. [pwsh:   Command-line shell and scripting language designed especially for system administration.](#pwsh:Command-lineshellandscriptinglanguagedesignedespeciallyforsystemadministration.)
	1.45. [xonsh:   Python-powered, cross-platform, Unix-gazing shell.](#xonsh:Python-poweredcross-platformUnix-gazingshell.)
	1.46. [nmap:   Network exploration tool and security/port scanner.](#nmap:Networkexplorationtoolandsecurityportscanner.)
	1.47. [masscan:   Network scanner for scanning as fast as possible.](#masscan:Networkscannerforscanningasfastaspossible.)
	1.48. [dirsearch:   Web path scanner.](#dirsearch:Webpathscanner.)
	1.49. [gitleaks:   Detect secrets and API keys leaked in Git repositories.](#gitleaks:DetectsecretsandAPIkeysleakedinGitrepositories.)
	1.50. [naabu:   A fast port scanner written in Go with a focus on reliability and simplicity.](#naabu:AfastportscannerwritteninGowithafocusonreliabilityandsimplicity.)
	1.51. [nuclei:   Fast and customizable vulnerability scanner based on a simple YAML based DSL.](#nuclei:FastandcustomizablevulnerabilityscannerbasedonasimpleYAMLbasedDSL.)
	1.52. [trivy:   Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.](#trivy:ScannerforvulnerabilitiesincontainerimagesfilesystemsandGitrepositoriesaswellasforconfigurationissues.)
	1.53. [rustscan:   Fast Port Scanner written in Rust with nmap built in.](#rustscan:FastPortScannerwritteninRustwithnmapbuiltin.)
	1.54. [exiftool:   Read and write meta information in files.](#exiftool:Readandwritemetainformationinfiles.)
	1.55. [trufflehog:   Find and verify credentials in files, Git repositories, S3 buckets, and Docker images.](#trufflehog:FindandverifycredentialsinfilesGitrepositoriesS3bucketsandDockerimages.)
	1.56. [steghide:   Steganography tool for JPEG, BMP, WAV and AU file formats.](#steghide:SteganographytoolforJPEGBMPWAVandAUfileformats.)
	1.57. [rkhunter:   Searches for rootkits and malware.](#rkhunter:Searchesforrootkitsandmalware.)
	1.58. [tshark:   Packet analysis tool, CLI version of Wireshark.](#tshark:PacketanalysistoolCLIversionofWireshark.)
	1.59. [tcpkill:   Kill specified in-progress TCP connections.](#tcpkill:Killspecifiedin-progressTCPconnections.)
	1.60. [openssl:   OpenSSL cryptographic toolkit.](#openssl:OpenSSLcryptographictoolkit.)
	1.61. [cryptsetup:   Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes.](#cryptsetup:Manageplaindm-cryptandLUKSLinuxUnifiedKeySetupencryptedvolumes.)
	1.62. [zip2john:   Extract password hashes from Zip archives for use with John the Ripper password cracker.](#zip2john:ExtractpasswordhashesfromZiparchivesforusewithJohntheRipperpasswordcracker.)
	1.63. [jq:   A JSON processor that uses a domain-specific language (DSL).](#jq:AJSONprocessorthatusesadomain-specificlanguageDSL.)
	1.64. [yq:   A lightweight and portable command-line YAML processor.](#yq:Alightweightandportablecommand-lineYAMLprocessor.)
	1.65. [xsv:   A CSV command-line toolkit written in Rust.](#xsv:ACSVcommand-linetoolkitwritteninRust.)
	1.66. [passwd:   Change a user's password.](#passwd:Changeauserspassword.)
	1.67. [nginx:   Nginx web server.](#nginx:Nginxwebserver.)
	1.68. [sqlite3:   The command-line interface to SQLite 3, which is a self-contained file-based embedded SQL engine.](#sqlite3:Thecommand-lineinterfacetoSQLite3whichisaself-containedfile-basedembeddedSQLengine.)
	1.69. [vim:   Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.](#vim:VimViIMprovedacommand-linetexteditorprovidesseveralmodesfordifferentkindsoftextmanipulation.)
	1.70. [nano:   Command-line text editor. An enhanced Pico clone.](#nano:Command-linetexteditor.AnenhancedPicoclone.)
	1.71. [sshd:   Secure Shell Daemon - allows remote machines to securely log in to the current machine.](#sshd:SecureShellDaemon-allowsremotemachinestosecurelylogintothecurrentmachine.)
	1.72. [ngrok:   Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.](#ngrok:Reverseproxythatcreatesasecuretunnelfromapublicendpointtoalocallyrunningwebservice.)
	1.73. [pup:   Command-line HTML parsing tool.](#pup:Command-lineHTMLparsingtool.)
	1.74. [chisel:   Create TCP/UDP tunnels, transported over HTTP, secured via SSH.](#chisel:CreateTCPUDPtunnelstransportedoverHTTPsecuredviaSSH.)
	1.75. [createdb:   Create a PostgreSQL database.](#createdb:CreateaPostgreSQLdatabase.)
	1.76. [subfinder:   Discover valid subdomains for websites.](#subfinder:Discovervalidsubdomainsforwebsites.)
	1.77. [sublist3r:   Fast subdomains enumeration tool for penetration testers.](#sublist3r:Fastsubdomainsenumerationtoolforpenetrationtesters.)
2. [Alternatives in Rust](#AlternativesinRust)
	2.1. [exa:   A modern replacement for ls (List directory contents).](#exa:AmodernreplacementforlsListdirectorycontents.)
	2.2. [fd:   An alternative to find.](#fd:Analternativetofind.)
	2.3. [fselect:   Find files with SQL-like queries.](#fselect:FindfileswithSQL-likequeries.)
	2.4. [lsd:   List directory contents.](#lsd:Listdirectorycontents.)
	2.5. [ranger:   Console file manager with VI key bindings.](#ranger:ConsolefilemanagerwithVIkeybindings.)
	2.6. [broot:   Navigate directory trees interactively.](#broot:Navigatedirectorytreesinteractively.)
	2.7. [dua:   Dua (Disk Usage Analyzer): get the disk space usage of a directory.](#dua:DuaDiskUsageAnalyzer:getthediskspaceusageofadirectory.)
	2.8. [dust:   Dust gives an instant overview of which directories are using disk space.](#dust:Dustgivesaninstantoverviewofwhichdirectoriesareusingdiskspace.)
		2.8.1. [drill: Perform various DNS queries.](#drill:PerformvariousDNSqueries.)
	2.9. [choose:   A human-friendly and fast alternative to cut and (sometimes) awk.](#choose:Ahuman-friendlyandfastalternativetocutandsometimesawk.)
	2.10. [ripgrep:   ripgrep is the common name for the command rg.](#ripgrep:ripgrepisthecommonnameforthecommandrg.)
	2.11. [rga:   Ripgrep wrapper with rich file type searching capabilities.](#rga:Ripgrepwrapperwithrichfiletypesearchingcapabilities.)
	2.12. [sd:   Intuitive find and replace.](#sd:Intuitivefindandreplace.)
	2.13. [grex:   Generate regular expressions.](#grex:Generateregularexpressions.)
	2.14. [delta:   A viewer for Git and diff output.](#delta:AviewerforGitanddiffoutput.)
	2.15. [gitui:   A lightweight keyboard-only TUI for Git.](#gitui:Alightweightkeyboard-onlyTUIforGit.)
	2.16. [neofetch:   Display information about your operating system, software and hardware.](#neofetch:Displayinformationaboutyouroperatingsystemsoftwareandhardware.)
	2.17. [procs:   Display information about the active processes.](#procs:Displayinformationabouttheactiveprocesses.)
	2.18. [py-spy:   A sampling profiler for Python programs.](#py-spy:AsamplingprofilerforPythonprograms.)
	2.19. [dog:   DNS lookup utility.](#dog:DNSlookuputility.)
	2.20. [drill:   Perform various DNS queries.](#drill:PerformvariousDNSqueries.-1)
	2.21. [hyperfine:   A command-line benchmarking tool.](#hyperfine:Acommand-linebenchmarkingtool.)
	2.22. [topgrade:   Update all applications on the system.](#topgrade:Updateallapplicationsonthesystem.)
	2.23. [gh:   Work seamlessly with GitHub.](#gh:WorkseamlesslywithGitHub.)
	2.24. [asdf:   Command-line interface for managing versions of different packages.](#asdf:Command-lineinterfaceformanagingversionsofdifferentpackages.)
	2.25. [fnm:   Fast Node.js version manager.](#fnm:FastNode.jsversionmanager.)
	2.26. [volta:   A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm.](#volta:AJavaScriptToolManagerthatinstallsNode.jsruntimesnpmandYarnpackagemanagersoranybinariesfromnpm.)
	2.27. [silicon:   Create an image of source code.](#silicon:Createanimageofsourcecode.)
	2.28. [mcfly:   A smart command history search and management tool.](#mcfly:Asmartcommandhistorysearchandmanagementtool.)
	2.29. [zoxide:   Keep track of the most frequently used directories.](#zoxide:Keeptrackofthemostfrequentlyuseddirectories.)
	2.30. [fuck:   Corrects your previous console command.](#fuck:Correctsyourpreviousconsolecommand.)
	2.31. [asciinema:   Record and replay terminal sessions, and optionally share them on https://asciinema.org.](#asciinema:Recordandreplayterminalsessionsandoptionallysharethemonhttps:asciinema.org.)
	2.32. [navi:   An interactive cheatsheet tool for the command line and application launchers.](#navi:Aninteractivecheatsheettoolforthecommandlineandapplicationlaunchers.)
	2.33. [hexyl:   A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.](#hexyl:Asimplehexviewerfortheterminal.Usescoloredoutputtodistinguishdifferentcategoriesofbytes.)
	2.34. [tokei:   Display statistics about code.](#tokei:Displaystatisticsaboutcode.)
	2.35. [xh:   Friendly and fast tool for sending HTTP requests.](#xh:FriendlyandfasttoolforsendingHTTPrequests.)
	2.36. [rargs:   Execute a command for each line of standard input.](#rargs:Executeacommandforeachlineofstandardinput.)
	2.37. [paru: An AUR helper and pacman wrapper.](#paru:AnAURhelperandpacmanwrapper.)
	2.38. [starship:   The minimal, blazing-fast, and infinitely customizable prompt for any shell.](#starship:Theminimalblazing-fastandinfinitelycustomizablepromptforanyshell.)
	2.39. [fastmod:   A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.](#fastmod:Afastpartialreplacementforthecodemodtoolreplaceandreplaceallinthewholecodebase.)
	2.40. [zellij:   Terminal multiplexer with batteries included.](#zellij:Terminalmultiplexerwithbatteriesincluded.)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

---

##  1. <a name='Essential'></a>Essential

###  1.1. <a name='ls:Listdirectorycontents.'></a>ls:   List directory contents.
```sh
ls

  List directory contents.
  More information: https://www.gnu.org/software/coreutils/ls.

  - List files one per line:
    ls -1

  - List all files, including hidden files:
    ls -a

  - List all files, with trailing / added to directory names:
    ls -F

  - Long format list (permissions, ownership, size, and modification date) of all files:
    ls -la

  - Long format list with size displayed using human-readable units (KiB, MiB, GiB):
    ls -lh

  - Long format list sorted by size (descending) recursively:
    ls -lSR

  - Long format list of all files, sorted by modification date (oldest first):
    ls -ltr

  - Only list directories:
    ls -d */
```

---

###  1.2. <a name='find:Findfilesordirectoriesunderadirectorytreerecursively.'></a>find:   Find files or directories under a directory tree, recursively.
```sh
find

  Find files or directories under a directory tree, recursively.
  More information: https://manned.org/find.

  - Find files by extension:
    find root_path -name '*.ext'

  - Find files matching multiple path/name patterns:
    find root_path -path '**/path/**/*.ext' -or -name '*pattern*'

  - Find directories matching a given name, in case-insensitive mode:
    find root_path -type d -iname '*lib*'

  - Find files matching a given pattern, excluding specific paths:
    find root_path -name '*.py' -not -path '*/site-packages/*'

  - Find files matching a given size range, limiting the recursive depth to "1":
    find root_path -maxdepth 1 -size +500k -size -10M

  - Run a command for each file (use {} within the command to access the filename):
    find root_path -name '*.ext' -exec wc -l {} \;

  - Find all files modified today and pass the results to a single command as arguments:
    find root_path -daystart -mtime -1 -exec tar -cvf archive.tar {} \+

  - Find empty (0 byte) files and delete them:
    find root_path -type f -empty -delete
```

---

###  1.3. <a name='chmod:Changetheaccesspermissionsofafileordirectory.'></a>chmod:   Change the access permissions of a file or directory.
```sh
chmod

  Change the access permissions of a file or directory.
  More information: https://www.gnu.org/software/coreutils/chmod.

  - Give the [u]ser who owns a file the right to e[x]ecute it:
    chmod u+x path/to/file

  - Give the [u]ser rights to [r]ead and [w]rite to a file/directory:
    chmod u+rw path/to/file_or_directory

  - Remove e[x]ecutable rights from the [g]roup:
    chmod g-x path/to/file

  - Give [a]ll users rights to [r]ead and e[x]ecute:
    chmod a+rx path/to/file

  - Give [o]thers (not in the file owner's group) the same rights as the [g]roup:
    chmod o=g path/to/file

  - Remove all rights from [o]thers:
    chmod o= path/to/file

  - Change permissions recursively giving [g]roup and [o]thers the ability to [w]rite:
    chmod -R g+w,o+w path/to/directory

  - Recursively give [a]ll users [r]ead permissions to files and e[X]ecute permissions to sub-directories within a directory:
    chmod -R a+rX path/to/directory
```

---

###  1.4. <a name='chown:Changeuserandgroupownershipoffilesanddirectories.'></a>chown:   Change user and group ownership of files and directories.
```sh
chown

  Change user and group ownership of files and directories.
  More information: https://www.gnu.org/software/coreutils/chown.

  - Change the owner user of a file/directory:
    chown user path/to/file_or_directory

  - Change the owner user and group of a file/directory:
    chown user:group path/to/file_or_directory

  - Change the owner user and group to both have the name user:
    chown user: path/to/file_or_directory

  - Recursively change the owner of a directory and its contents:
    chown -R user path/to/directory

  - Change the owner of a symbolic link:
    chown -h user path/to/symlink

  - Change the owner of a file/directory to match a reference file:
    chown --reference path/to/reference_file path/to/file_or_directory
```

---

###  1.5. <a name='scp:Securecopy.'></a>scp:   Secure copy.
```sh
scp

  Secure copy.
  Copy files between hosts using Secure Copy Protocol over SSH.
  More information: https://man.openbsd.org/scp.

  - Copy a local file to a remote host:
    scp path/to/local_file remote_host:path/to/remote_file

  - Use a specific port when connecting to the remote host:
    scp -P port path/to/local_file remote_host:path/to/remote_file

  - Copy a file from a remote host to a local directory:
    scp remote_host:path/to/remote_file path/to/local_directory

  - Recursively copy the contents of a directory from a remote host to a local directory:
    scp -r remote_host:path/to/remote_directory path/to/local_directory

  - Copy a file between two remote hosts transferring through the local host:
    scp -3 host1:path/to/remote_file host2:path/to/remote_directory

  - Use a specific username when connecting to the remote host:
    scp path/to/local_file remote_username@remote_host:path/to/remote_directory

  - Use a specific SSH private key for authentication with the remote host:
    scp -i ~/.ssh/private_key path/to/local_file remote_host:path/to/remote_file

  - Use a specific proxy when connecting to the remote host:
    scp -J proxy_username@proxy_host path/to/local_file remote_host:path/to/remote_file
```

---

###  1.6. <a name='rsync:TransferfileseithertoorfromaremotehostbutnotbetweentworemotehostsbydefaultusingSSH.'></a>rsync:   Transfer files either to or from a remote host (but not between two remote hosts), by default using SSH.
```sh
rsync

  Transfer files either to or from a remote host (but not between two remote hosts), by default using SSH.
  To specify a remote path, use user@host:path/to/file_or_directory.
  More information: https://download.samba.org/pub/rsync/rsync.1.

  - Transfer a file:
    rsync path/to/source path/to/destination

  - Use archive mode (recursively copy directories, copy symlinks without resolving, and preserve permissions, ownership and modification times):
    rsync --archive path/to/source path/to/destination

  - Compress the data as it is sent to the destination, display verbose and human-readable progress, and keep partially transferred files if interrupted:
    rsync --compress --verbose --human-readable --partial --progress path/to/source path/to/destination

  - Recursively copy directories:
    rsync --recursive path/to/source path/to/destination

  - Transfer directory contents, but not the directory itself:
    rsync --recursive path/to/source/ path/to/destination

  - Use archive mode, resolve symlinks and skip files that are newer on the destination:
    rsync --archive --update --copy-links path/to/source path/to/destination

  - Transfer a directory from a remote host running rsyncd and delete files on the destination that do not exist on the source:
    rsync --recursive --delete rsync://host:path/to/source path/to/destination

  - Transfer a file over SSH using a different port than the default (22) and show global progress:
    rsync --rsh 'ssh -p port' --info=progress2 host:path/to/source path/to/destination
```

---

###  1.7. <a name='diff:Comparefilesanddirectories.'></a>diff:   Compare files and directories.
```sh
diff

  Compare files and directories.
  More information: https://man7.org/linux/man-pages/man1/diff.1.html.

  - Compare files (lists changes to turn old_file into new_file):
    diff old_file new_file

  - Compare files, ignoring [w]hite spaces:
    diff -w|--ignore-all-space old_file new_file

  - Compare files, showing the differences side by side:
    diff -y|--side-by-side old_file new_file

  - Compare files, showing the differences in [u]nified format (as used by git diff):
    diff -u|--unified old_file new_file

  - Compare directories [r]ecursively (shows names for differing files/directories as well as changes made to files):
    diff -r|--recursive old_directory new_directory

  - Compare directories, only showing the names of files that differ:
    diff -r|--recursive -q|--brief old_directory new_directory

  - Create a patch file for Git from the differences of two text files, treating nonexistent files as empty:
    diff -a|--text -u|--unified -N|--new-file old_file new_file > diff.patch

  - Compare files, showing output in color and try hard to find smaller set of changes:
    diff -d|--minimal --color=always old_file new_file
```

---

###  1.8. <a name='sort:Sortlinesoftextfiles.'></a>sort:   Sort lines of text files.
```sh
sort

  Sort lines of text files.
  More information: https://www.gnu.org/software/coreutils/sort.

  - Sort a file in ascending order:
    sort path/to/file

  - Sort a file in descending order:
    sort --reverse path/to/file

  - Sort a file in case-insensitive way:
    sort --ignore-case path/to/file

  - Sort a file using numeric rather than alphabetic order:
    sort --numeric-sort path/to/file

  - Sort /etc/passwd by the 3rd field of each line numerically, using ":" as a field separator:
    sort --field-separator=: --key=3n /etc/passwd

  - Sort a file preserving only unique lines:
    sort --unique path/to/file

  - Sort a file, printing the output to the specified output file (can be used to sort a file in-place):
    sort --output=path/to/file path/to/file

  - Sort numbers with exponents:
    sort --general-numeric-sort path/to/file
```

---

###  1.9. <a name='xargs:Executeacommandwithpipedargumentscomingfromanothercommandafileetc.'></a>xargs:   Execute a command with piped arguments coming from another command, a file, etc.
```sh
xargs

  Execute a command with piped arguments coming from another command, a file, etc.
  The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines and end-of-file.
  More information: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html.

  - Run a command using the input data as arguments:
    arguments_source | xargs command

  - Run multiple chained commands on the input data:
    arguments_source | xargs sh -c "command1 && command2 | command3"

  - Delete all files with a .backup extension (-print0 uses a null character to split file names, and -0 uses it as delimiter):
    find . -name '*.backup' -print0 | xargs -0 rm -v

  - Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as _) with the input line:
    arguments_source | xargs -I _ command _ optional_extra_arguments

  - Parallel runs of up to max-procs processes at a time; the default is 1. If max-procs is 0, xargs will run as many processes as possible at a time:
    arguments_source | xargs -P max-procs command
```

---

###  1.10. <a name='sed:Edittextinascriptablemanner.'></a>sed:   Edit text in a scriptable manner.
```sh
sed

  Edit text in a scriptable manner.
  See also: awk, ed.
  More information: https://www.gnu.org/software/sed/manual/sed.html.

  - Replace all apple (basic regex) occurrences with mango (basic regex) in all input lines and print the result to stdout:
    command | sed 's/apple/mango/g'

  - Replace all apple (extended regex) occurrences with APPLE (extended regex) in all input lines and print the result to stdout:
    command | sed -E 's/(apple)/\U\1/g'

  - Replace all apple (basic regex) occurrences with mango (basic regex) in a specific file and overwrite the original file in place:
    sed -i 's/apple/mango/g' path/to/file

  - Execute a specific script [f]ile and print the result to stdout:
    command | sed -f path/to/script.sed

  - Print just the first line to stdout:
    command | sed -n '1p'

  - [d]elete the first line of a file:
    sed -i 1d path/to/file

  - [i]nsert a new line at the first line of a file:
    sed -i '1i\your new line text\' path/to/file


See also: awk, ed
```

---

###  1.11. <a name='awk:Aversatileprogramminglanguageforworkingonfiles.'></a>awk:   A versatile programming language for working on files.
```sh
awk

  A versatile programming language for working on files.
  More information: https://github.com/onetrueawk/awk.

  - Print the fifth column (a.k.a. field) in a space-separated file:
    awk '{print $5}' path/to/file

  - Print the second column of the lines containing "foo" in a space-separated file:
    awk '/foo/ {print $2}' path/to/file

  - Print the last column of each line in a file, using a comma (instead of space) as a field separator:
    awk -F ',' '{print $NF}' path/to/file

  - Sum the values in the first column of a file and print the total:
    awk '{s+=$1} END {print s}' path/to/file

  - Print every third line starting from the first line:
    awk 'NR%3==1' path/to/file

  - Print different values based on conditions:
    awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' path/to/file

  - Print all lines where the 10th column value equals the specified value:
    awk '($10 == value)'

  - Print all the lines which the 10th column value is between a min and a max:
    awk '($10 >= min_value && $10 <= max_value)'
```

---

###  1.12. <a name='tr:Translatecharacters:runreplacementsbasedonsinglecharactersandcharactersets.'></a>tr:   Translate characters: run replacements based on single characters and character sets.
```sh
tr

  Translate characters: run replacements based on single characters and character sets.
  More information: https://www.gnu.org/software/coreutils/tr.

  - Replace all occurrences of a character in a file, and print the result:
    tr find_character replace_character < path/to/file

  - Replace all occurrences of a character from another command's output:
    echo text | tr find_character replace_character

  - Map each character of the first set to the corresponding character of the second set:
    tr 'abcd' 'jkmn' < path/to/file

  - Delete all occurrences of the specified set of characters from the input:
    tr -d 'input_characters' < path/to/file

  - Compress a series of identical characters to a single character:
    tr -s 'input_characters' < path/to/file

  - Translate the contents of a file to upper-case:
    tr "[:lower:]" "[:upper:]" < path/to/file

  - Strip out non-printable characters from a file:
    tr -cd "[:print:]" < path/to/file
```

---

###  1.13. <a name='grep:Findpatternsinfilesusingregularexpressions.'></a>grep:   Find patterns in files using regular expressions.
```sh
grep

  Find patterns in files using regular expressions.
  More information: https://www.gnu.org/software/grep/manual/grep.html.

  - Search for a pattern within a file:
    grep "search_pattern" path/to/file

  - Search for an exact string (disables regular expressions):
    grep --fixed-strings "exact_string" path/to/file

  - Search for a pattern in all files recursively in a directory, showing line numbers of matches, ignoring binary files:
    grep --recursive --line-number --binary-files without-match "search_pattern" path/to/directory

  - Use extended regular expressions (supports ?, +, {}, () and |), in case-insensitive mode:
    grep --extended-regexp --ignore-case "search_pattern" path/to/file

  - Print 3 lines of context around, before, or after each match:
    grep --context|before-context|after-context 3 "search_pattern" path/to/file

  - Print file name and line number for each match with color output:
    grep --with-filename --line-number --color=always "search_pattern" path/to/file

  - Search for lines matching a pattern, printing only the matched text:
    grep --only-matching "search_pattern" path/to/file

  - Search stdin for lines that do not match a pattern:
    cat path/to/file | grep --invert-match "search_pattern"
```

---

###  1.14. <a name='curl:Transfersdatafromortoaserver.'></a>curl:   Transfers data from or to a server.
```sh
curl

  Transfers data from or to a server.
  Supports most protocols, including HTTP, FTP, and POP3.
  More information: https://curl.se/docs/manpage.html.

  - Download the contents of a URL to a file:
    curl http://example.com --output path/to/file

  - Download a file, saving the output under the filename indicated by the URL:
    curl --remote-name http://example.com/filename

  - Download a file, following location redirects, and automatically continuing (resuming) a previous file transfer and return an error on server error:
    curl --fail --remote-name --location --continue-at - http://example.com/filename

  - Send form-encoded data (POST request of type application/x-www-form-urlencoded). Use --data @file_name or --data @'-' to read from STDIN:
    curl --data 'name=bob' http://example.com/form

  - Send a request with an extra header, using a custom HTTP method:
    curl --header 'X-My-Header: 123' --request PUT http://example.com

  - Send data in JSON format, specifying the appropriate content-type header:
    curl --data '{"name":"bob"}' --header 'Content-Type: application/json' http://example.com/users/1234

  - Pass a username and prompt for a password to authenticate to the server:
    curl --user username http://example.com

  - Pass client certificate and key for a resource, skipping certificate validation:
    curl --cert client.pem --key key.pem --insecure https://example.com
```

---

###  1.15. <a name='wget:DownloadfilesfromtheWeb.'></a>wget:   Download files from the Web.
```sh
wget

  Download files from the Web.
  Supports HTTP, HTTPS, and FTP.
  More information: https://www.gnu.org/software/wget.

  - Download the contents of a URL to a file (named "foo" in this case):
    wget https://example.com/foo

  - Download the contents of a URL to a file (named "bar" in this case):
    wget --output-document bar https://example.com/foo

  - Download a single web page and all its resources with 3-second intervals between requests (scripts, stylesheets, images, etc.):
    wget --page-requisites --convert-links --wait=3 https://example.com/somepage.html

  - Download all listed files within a directory and its sub-directories (does not download embedded page elements):
    wget --mirror --no-parent https://example.com/somepath/

  - Limit the download speed and the number of connection retries:
    wget --limit-rate=300k --tries=100 https://example.com/somepath/

  - Download a file from an HTTP server using Basic Auth (also works for FTP):
    wget --user=username --password=password https://example.com

  - Continue an incomplete download:
    wget --continue https://example.com

  - Download all URLs stored in a text file to a specific directory:
    wget --directory-prefix path/to/directory --input-file URLs.txt
```

---

###  1.16. <a name='ncdu:Diskusageanalyzerwithanncursesinterface.'></a>ncdu:   Disk usage analyzer with an ncurses interface.
```sh
ncdu

  Disk usage analyzer with an ncurses interface.
  More information: https://manned.org/ncdu.

  - Analyze the current working directory:
    ncdu

  - Colorize output:
    ncdu --color dark|off

  - Analyze a given directory:
    ncdu path/to/directory

  - Save results to a file:
    ncdu -o path/to/file

  - Exclude files that match a pattern, argument can be given multiple times to add more patterns:
    ncdu --exclude '*.txt'
```

---

###  1.17. <a name='pdfimages:UtilityforextractingimagesfromPDFs.'></a>pdfimages:   Utility for extracting images from PDFs.
```sh
pdfimages

  Utility for extracting images from PDFs.
  More information: https://manned.org/pdfimages.

  - Extract all images from a PDF file and save them as PNGs:
    pdfimages -png path/to/file.pdf filename_prefix

  - Extract images from pages 3 to 5:
    pdfimages -f 3 -l 5 path/to/file.pdf filename_prefix

  - Extract images from a PDF file and include the page number in the output filenames:
    pdfimages -p path/to/file.pdf filename_prefix

  - List information about all the images in a PDF file:
    pdfimages -list path/to/file.pdf
```

---

###  1.18. <a name='tar:Archivingutility.'></a>tar:   Archiving utility.
```sh
tar

  Archiving utility.
  Often combined with a compression method, such as gzip or bzip2.
  More information: https://www.gnu.org/software/tar.

  - [c]reate an archive and write it to a [f]ile:
    tar cf path/to/target.tar path/to/file1 path/to/file2 ...

  - [c]reate a g[z]ipped archive and write it to a [f]ile:
    tar czf path/to/target.tar.gz path/to/file1 path/to/file2 ...

  - [c]reate a g[z]ipped archive from a directory using relative paths:
    tar czf path/to/target.tar.gz --directory=path/to/directory .

  - E[x]tract a (compressed) archive [f]ile into the current directory [v]erbosely:
    tar xvf path/to/source.tar[.gz|.bz2|.xz]

  - E[x]tract a (compressed) archive [f]ile into the target directory:
    tar xf path/to/source.tar[.gz|.bz2|.xz] --directory=path/to/directory

  - [c]reate a compressed archive and write it to a [f]ile, using the file extension to [a]utomatically determine the compression program:
    tar caf path/to/target.tar.xz path/to/file1 path/to/file2 ...

  - Lis[t] the contents of a tar [f]ile [v]erbosely:
    tar tvf path/to/source.tar

  - E[x]tract files matching a pattern from an archive [f]ile:
    tar xf path/to/source.tar --wildcards "*.html"


See also: gzip, bzip2
```

---

###  1.19. <a name='zip:PackageandcompressarchivefilesintoaZiparchive.'></a>zip:   Package and compress (archive) files into a Zip archive.
```sh
zip

  Package and compress (archive) files into a Zip archive.
  See also: unzip.
  More information: https://manned.org/zip.

  - Add files/directories to a specific archive:
    zip -r path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

  - Remove files/directories from a specific archive:
    zip --delete path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

  - Archive files/directories e[x]cluding specified ones:
    zip path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ... --exclude path/to/excluded_files_or_directories

  - Archive files/directories with a specific compression level (0 - the lowest, 9 - the highest):
    zip -r -0..9 path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

  - Create an encrypted archive with a specific password:
    zip -r --encrypt path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

  - Archive files/directories to a multi-part [s]plit Zip archive (e.g. 3 GB parts):
    zip -r -s 3g path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...

  - Print a specific archive contents:
    zip -sf path/to/compressed.zip


See also: unzip
```

---

###  1.20. <a name='top:Displaydynamicreal-timeinformationaboutrunningprocesses.'></a>top:   Display dynamic real-time information about running processes.
```sh
top

  Display dynamic real-time information about running processes.
  More information: https://manned.org/top.

  - Start top:
    top

  - Do not show any idle or zombie processes:
    top -i

  - Show only processes owned by given user:
    top -u username

  - Sort processes by a field:
    top -o field_name

  - Show the individual threads of a given process:
    top -Hp process_id

  - Show only the processes with the given PID(s), passed as a comma-separated list. (Normally you wouldn't know PIDs off hand. This example picks the PIDs from the process name):
    top -p $(pgrep -d ',' process_name)

  - Display help about interactive commands:
    ?
```

---

###  1.21. <a name='htop:Displaydynamicreal-timeinformationaboutrunningprocesses.Anenhancedversionoftop.'></a>htop:   Display dynamic real-time information about running processes. An enhanced version of top.
```sh
htop

  Display dynamic real-time information about running processes. An enhanced version of top.
  More information: https://htop.dev/.

  - Start htop:
    htop

  - Start htop displaying processes owned by a specific user:
    htop --user username

  - Sort processes by a specified sort_item (use htop --sort help for available options):
    htop --sort sort_item

  - Start htop with the specified delay between updates, in tenths of a second (i.e. 50 = 5 seconds):
    htop --delay 50

  - See interactive commands while running htop:
    ?

  - Switch to a different tab:
    tab

  - Display help:
    htop --help


See also: top
```

---

###  1.22. <a name='ps:Informationaboutrunningprocesses.'></a>ps:   Information about running processes.
```sh
ps

  Information about running processes.
  More information: https://manned.org/ps.

  - List all running processes:
    ps aux

  - List all running processes including the full command string:
    ps auxww

  - Search for a process that matches a string (the brackets will prevent grep from matching itself):
    ps aux | grep [s]tring

  - List all processes of the current user in extra full format:
    ps --user $(id -u) -F

  - List all processes of the current user as a tree:
    ps --user $(id -u) f

  - Get the parent PID of a process:
    ps -o ppid= -p pid

  - Sort processes by memory consumption:
    ps --sort size


See also: grep
```

---

###  1.23. <a name='cron:Asystemschedulerforrunningjobsortasksunattended.'></a>cron:   A system scheduler for running jobs or tasks unattended.
```sh
cron

  A system scheduler for running jobs or tasks unattended.
  The command to submit, edit or delete entries to cron is called crontab.

  - View documentation for managing cron entries:
    tldr crontab


See also: crontab
```

---

###  1.24. <a name='reboot:Rebootthesystem.'></a>reboot:   Reboot the system.
```sh
reboot

  Reboot the system.
  More information: https://manned.org/reboot.8.

  - Reboot the system:
    reboot

  - Power off the system (same as poweroff):
    reboot --poweroff

  - Halt (terminates all processes and shuts down the CPU) the system (same as halt):
    reboot --halt

  - Reboot immediately without contacting the system manager:
    reboot --force

  - Write the wtmp shutdown entry without rebooting the system:
    reboot --wtmp-only


See also: poweroff, halt
```

---

###  1.25. <a name='tmux:Terminalmultiplexer.'></a>tmux:   Terminal multiplexer.
```sh
tmux

  Terminal multiplexer.
  It allows multiple sessions with windows, panes, and more.
  See also: zellij, screen.
  More information: https://github.com/tmux/tmux.

  - Start a new session:
    tmux

  - Start a new named session:
    tmux new -s name

  - List existing sessions:
    tmux ls

  - Attach to the most recently used session:
    tmux attach

  - Detach from the current session (inside a tmux session):
    <Ctrl>-B d

  - Create a new window (inside a tmux session):
    <Ctrl>-B c

  - Switch between sessions and windows (inside a tmux session):
    <Ctrl>-B w

  - Kill a session by name:
    tmux kill-session -t name


See also: zellij, screen
```

---

###  1.26. <a name='screen:Holdasessionopenonaremoteserver.ManagemultiplewindowswithasingleSSHconnection.'></a>screen:   Hold a session open on a remote server. Manage multiple windows with a single SSH connection.
```sh
screen

  Hold a session open on a remote server. Manage multiple windows with a single SSH connection.
  See also tmux and zellij.
  More information: https://manned.org/screen.

  - Start a new screen session:
    screen

  - Start a new named screen session:
    screen -S session_name

  - Start a new daemon and log the output to screenlog.x:
    screen -dmLS session_name command

  - Show open screen sessions:
    screen -ls

  - Reattach to an open screen:
    screen -r session_name

  - Detach from inside a screen:
    <Ctrl> + A, D

  - Kill the current screen session:
    <Ctrl> + A, K

  - Kill a detached screen:
    screen -X -S session_name quit


See also: tmux, zellij
```

---

###  1.27. <a name='ping:SendICMPECHO_REQUESTpacketstonetworkhosts.'></a>ping:   Send ICMP ECHO_REQUEST packets to network hosts.
```sh
ping

  Send ICMP ECHO_REQUEST packets to network hosts.
  More information: https://manned.org/ping.

  - Ping host:
    ping host

  - Ping a host only a specific number of times:
    ping -c count host

  - Ping host, specifying the interval in seconds between requests (default is 1 second):
    ping -i seconds host

  - Ping host without trying to lookup symbolic names for addresses:
    ping -n host

  - Ping host and ring the bell when a packet is received (if your terminal supports it):
    ping -a host

  - Also display a message if no response was received:
    ping -O host
```

---

###  1.28. <a name='telnet:Connecttoaspecifiedportofahostusingthetelnetprotocol.'></a>telnet:   Connect to a specified port of a host using the telnet protocol.
```sh
telnet

  Connect to a specified port of a host using the telnet protocol.
  More information: https://manned.org/telnet.

  - Telnet to the default port of a host:
    telnet host

  - Telnet to a specific port of a host:
    telnet ip_address port

  - Exit a telnet session:
    quit

  - Emit the default escape character combination for terminating the session:
    <Ctrl> + ]

  - Start telnet with "x" as the session termination character:
    telnet -e x ip_address port

  - Telnet to Star Wars animation:
    telnet towel.blinkenlights.nl
```

---

###  1.29. <a name='traceroute:Printtheroutepacketstracetonetworkhost.'></a>traceroute:   Print the route packets trace to network host.
```sh
traceroute

  Print the route packets trace to network host.
  More information: https://manned.org/traceroute.

  - Traceroute to a host:
    traceroute example.com

  - Disable IP address and host name mapping:
    traceroute -n example.com

  - Specify wait time in seconds for response:
    traceroute --wait=0.5 example.com

  - Specify number of queries per hop:
    traceroute --queries=5 example.com

  - Specify size in bytes of probing packet:
    traceroute example.com 42

  - Determine the MTU to the destination:
    traceroute --mtu example.com

  - Use ICMP instead of UDP for tracerouting:
    traceroute --icmp example.com
```

---

###  1.30. <a name='tcpdump:Dumptrafficonanetwork.'></a>tcpdump:   Dump traffic on a network.
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

###  1.31. <a name='netstat:Displaynetwork-relatedinformationsuchasopenconnectionsopensocketportsetc.'></a>netstat:   Display network-related information such as open connections, open socket ports, etc.
```sh
netstat

  Display network-related information such as open connections, open socket ports, etc.
  More information: https://man7.org/linux/man-pages/man8/netstat.8.html.

  - List all ports:
    netstat --all

  - List all listening ports:
    netstat --listening

  - List listening TCP ports:
    netstat --tcp

  - Display PID and program names:
    netstat --program

  - List information continuously:
    netstat --continuous

  - List routes and do not resolve IP addresses to hostnames:
    netstat --route --numeric

  - List listening TCP and UDP ports (+ user and process if you're root):
    netstat --listening --program --numeric --tcp --udp --extend
```

---

###  1.32. <a name='ifconfig:NetworkInterfaceConfigurator.'></a>ifconfig:   Network Interface Configurator.
```sh
ifconfig

  Network Interface Configurator.
  More information: https://net-tools.sourceforge.io/man/ifconfig.8.html.

  - View network settings of an Ethernet adapter:
    ifconfig eth0

  - Display details of all interfaces, including disabled interfaces:
    ifconfig -a

  - Disable eth0 interface:
    ifconfig eth0 down

  - Enable eth0 interface:
    ifconfig eth0 up

  - Assign IP address to eth0 interface:
    ifconfig eth0 ip_address
```

---

###  1.33. <a name='route:Useroutecmdtosettheroutetable.'></a>route:   Use route cmd to set the route table.
```sh
route

  Use route cmd to set the route table.
  More information: https://manned.org/route.

  - Display the information of route table:
    route -n

  - Add route rule:
    sudo route add -net ip_address netmask netmask_address gw gw_address

  - Delete route rule:
    sudo route del -net ip_address netmask netmask_address dev gw_address
```

---

###  1.34. <a name='ip:Showmanipulateroutingdevicespolicyroutingandtunnels.'></a>ip:   Show/manipulate routing, devices, policy routing and tunnels.
```sh
ip

  Show/manipulate routing, devices, policy routing and tunnels.
  Some subcommands such as ip address have their own usage documentation.
  More information: https://www.man7.org/linux/man-pages/man8/ip.8.html.

  - List interfaces with detailed info:
    ip address

  - List interfaces with brief network layer info:
    ip -brief address

  - List interfaces with brief link layer info:
    ip -brief link

  - Display the routing table:
    ip route

  - Show neighbors (ARP table):
    ip neighbour

  - Make an interface up/down:
    ip link set interface up|down

  - Add/Delete an IP address to an interface:
    ip addr add/del ip/mask dev interface

  - Add a default route:
    ip route add default via ip dev interface
```

---

###  1.35. <a name='ss:Utilitytoinvestigatesockets.'></a>ss:   Utility to investigate sockets.
```sh
ss

  Utility to investigate sockets.
  More information: https://manned.org/ss.8.

  - Show all TCP/UDP/RAW/UNIX sockets:
    ss -a -t|-u|-w|-x

  - Filter TCP sockets by states, only/exclude:
    ss state/exclude bucket/big/connected/synchronized/...

  - Show all TCP sockets connected to the local HTTPS port (443):
    ss -t src :443

  - Show all TCP sockets listening on the local 8080 port:
    ss -lt src :8080

  - Show all TCP sockets along with processes connected to a remote SSH port:
    ss -pt dst :ssh

  - Show all UDP sockets connected on specific source and destination ports:
    ss -u 'sport == :source_port and dport == :destination_port'

  - Show all TCP IPv4 sockets locally connected on the subnet 192.168.0.0/16:
    ss -4t src 192.168/16

  - Kill IPv4 or IPv6 Socket Connection with destination IP 192.168.1.17 and destination port 8080:
    ss --kill dst 192.168.1.17 dport = 8080
```

---

###  1.36. <a name='iw:Showandmanipulatewirelessdevices.'></a>iw:   Show and manipulate wireless devices.
```sh
iw

  Show and manipulate wireless devices.
  More information: https://manned.org/iw.

  - Scan for available wireless networks:
    iw dev wlp scan

  - Join an open wireless network:
    iw dev wlp connect SSID

  - Close the current connection:
    iw dev wlp disconnect

  - Show information about the current connection:
    iw dev wlp link
```

---

###  1.37. <a name='arp:ShowandmanipulateyoursystemsARPcache.'></a>arp:   Show and manipulate your system's ARP cache.
```sh
arp

  Show and manipulate your system's ARP cache.
  More information: https://manned.org/arp.

  - Show the current ARP table:
    arp -a

  - [d]elete a specific entry:
    arp -d address

  - [s]et up a new entry in the ARP table:
    arp -s address mac_address
```

---

###  1.38. <a name='nc:RedirectIOintoanetworkstreamthroughthisversatiletool.'></a>nc:   Redirect I/O into a network stream through this versatile tool.
```sh
nc

  Redirect I/O into a network stream through this versatile tool.
  More information: https://manned.org/man/nc.1.

  - Start a listener on the specified TCP port and send a file into it:
    nc -l -p port < filename

  - Connect to a target listener on the specified port and receive a file from it:
    nc host port > received_filename

  - Scan the open TCP ports of a specified host:
    nc -v -z -w timeout_in_seconds host start_port-end_port

  - Start a listener on the specified TCP port and provide your local shell access to the connected party (this is dangerous and can be abused):
    nc -l -p port -e shell_executable

  - Connect to a target listener and provide your local shell access to the remote party (this is dangerous and can be abused):
    nc host port -e shell_executable

  - Act as a proxy and forward data from a local TCP port to the given remote host:
    nc -l -p local_port | nc host remote_port

  - Send an HTTP GET request:
    echo -e "GET / HTTP/1.1\nHost: host\n\n" | nc host 80
```

---

###  1.39. <a name='nslookup:Querynameserversforvariousdomainrecords.'></a>nslookup:   Query name servers for various domain records.
```sh
nslookup

  Query name servers for various domain records.
  More information: https://manned.org/nslookup.

  - Query your system's default name server for an IP address (A record) of the domain:
    nslookup example.com

  - Query a given name server for a NS record of the domain:
    nslookup -type=NS example.com 8.8.8.8

  - Query for a reverse lookup (PTR record) of an IP address:
    nslookup -type=PTR 54.240.162.118

  - Query for ANY available records using TCP protocol:
    nslookup -vc -type=ANY example.com

  - Query a given name server for the whole zone file (zone transfer) of the domain using TCP protocol:
    nslookup -vc -type=AXFR example.com name_server

  - Query for a mail server (MX record) of the domain, showing details of the transaction:
    nslookup -type=MX -debug example.com

  - Query a given name server on a specific port number for a TXT record of the domain:
    nslookup -port=port_number -type=TXT example.com name_server
```

---

###  1.40. <a name='dig:DNSlookuputility.'></a>dig:   DNS lookup utility.
```sh
dig

  DNS lookup utility.
  More information: https://manned.org/dig.

  - Lookup the IP(s) associated with a hostname (A records):
    dig +short example.com

  - Get a detailed answer for a given domain (A records):
    dig +noall +answer example.com

  - Query a specific DNS record type associated with a given domain name:
    dig +short example.com A|MX|TXT|CNAME|NS

  - Specify an alternate DNS server to query and optionally use DNS over TLS (DoT):
    dig +tls @1.1.1.1|8.8.8.8|9.9.9.9|... example.com

  - Perform a reverse DNS lookup on an IP address (PTR record):
    dig -x 8.8.8.8

  - Find authoritative name servers for the zone and display SOA records:
    dig +nssearch example.com

  - Perform iterative queries and display the entire trace path to resolve a domain name:
    dig +trace example.com

  - Query a DNS server over a non-standard [p]ort using the TCP protocol:
    dig +tcp -p port @dns_server_ip example.com
```

---

###  1.41. <a name='whois:Command-lineclientfortheWHOISRFC3912protocol.'></a>whois:   Command-line client for the WHOIS (RFC 3912) protocol.
```sh
whois

  Command-line client for the WHOIS (RFC 3912) protocol.
  More information: https://github.com/rfc1036/whois.

  - Get information about a domain name:
    whois example.com

  - Get information about an IP address:
    whois 8.8.8.8

  - Get abuse contact for an IP address:
    whois -b 8.8.8.8
```

---

###  1.42. <a name='ncat:Readwriteredirectandencryptdataacrossanetwork.'></a>ncat:   Read, write, redirect, and encrypt data across a network.
```sh
ncat

  Read, write, redirect, and encrypt data across a network.
  An alternative implementation of a similar utility called netcat/nc.
  More information: https://nmap.org/ncat/guide/index.html.

  - Listen for input on the specified port and write it to the specified file:
    ncat -l port > path/to/file

  - Accept multiple connections and keep ncat open after they have been closed:
    ncat -lk port

  - Write output of specified file to the specified host on the specified port:
    ncat address port < path/to/file

  - Accept multiple incoming connections on an encrypted channel evading detection of traffic content:
    ncat --ssl -k -l port

  - Connect to an open ncat connection over SSL:
    ncat --ssl host port

  - Check connectivity to a remote host on a particular port with timeout:
    ncat -w seconds -vz host port


See also: netcat, nc
```

---

###  1.43. <a name='perl:ThePerl5languageinterpreter.'></a>perl:   The Perl 5 language interpreter.
```sh
perl

  The Perl 5 language interpreter.
  More information: https://www.perl.org.

  - Print lines from stdin [m/] matching regex1 and case insensitive [/i] regex2:
    perl -n -e 'print if m/regex1/ and m/regex2/i'

  - Say [-E] first match group, using a regexp, ignoring space in regex [/x]:
    perl -n -E 'say $1 if m/before (  group_regex  ) after/x'

  - [-i]n-place, with backup, [s/] substitute all occurrence [/g] of regex with replacement:
    perl -i'.bak' -p -e 's/regex/replacement/g' path/to/files

  - Use perl's inline documentation, some pages also available via manual pages on Linux:
    perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1
```

---

###  1.44. <a name='pwsh:Command-lineshellandscriptinglanguagedesignedespeciallyforsystemadministration.'></a>pwsh:   Command-line shell and scripting language designed especially for system administration.
```sh
pwsh

  Command-line shell and scripting language designed especially for system administration.
  This command refers to PowerShell version 6 and above (also known as PowerShell Core and cross-platform PowerShell).
  To use the original Windows version (5.1 and below, also known as the legacy Windows PowerShell), use powershell instead of pwsh.
  More information: https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh.

  - Start an interactive shell session:
    pwsh

  - Start an interactive shell session without loading startup configs:
    pwsh -NoProfile

  - Execute specific commands:
    pwsh -Command "echo 'powershell is executed'"

  - Execute a specific script:
    pwsh -File path/to/script.ps1

  - Start a session with a specific version of PowerShell:
    pwsh -Version version

  - Prevent a shell from exit after running startup commands:
    pwsh -NoExit

  - Describe the format of data sent to PowerShell:
    pwsh -InputFormat Text|XML

  - Determine how an output from PowerShell is formatted:
    pwsh -OutputFormat Text|XML


See also: powershell
```

---

###  1.45. <a name='xonsh:Python-poweredcross-platformUnix-gazingshell.'></a>xonsh:   Python-powered, cross-platform, Unix-gazing shell.
```sh
xonsh

  Python-powered, cross-platform, Unix-gazing shell.
  Write and mix sh/Python code in Xonsh (pronounced conch).
  More information: https://xon.sh.

  - Start an interactive shell session:
    xonsh

  - Execute a single command and then exit:
    xonsh -c "command"

  - Run commands from a script file and then exit:
    xonsh path/to/script_file.xonsh

  - Define environment variables for the shell process:
    xonsh -Dname1=value1 -Dname2=value2

  - Load the specified .xonsh or .json configuration files:
    xonsh --rc path/to/file1.xonsh path/to/file2.json

  - Skip loading the .xonshrc configuration file:
    xonsh --no-rc
```

---

###  1.46. <a name='nmap:Networkexplorationtoolandsecurityportscanner.'></a>nmap:   Network exploration tool and security/port scanner.
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

###  1.47. <a name='masscan:Networkscannerforscanningasfastaspossible.'></a>masscan:   Network scanner for scanning as fast as possible.
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

###  1.48. <a name='dirsearch:Webpathscanner.'></a>dirsearch:   Web path scanner.
```sh
dirsearch

  Web path scanner.
  More information: https://github.com/maurosoria/dirsearch.

  - Scan a web server for common paths with common extensions:
    dirsearch --url url --extensions-list

  - Scan a list of web servers for common paths with the .php extension:
    dirsearch --url-list path/to/url-list.txt --extensions php

  - Scan a web server for user-defined paths with common extensions:
    dirsearch --url url --extensions-list --wordlist path/to/url-paths.txt

  - Scan a web server using a cookie:
    dirsearch --url url --extensions php --cookie cookie

  - Scan a web server using the HEAD HTTP method:
    dirsearch --url url --extensions php --http-method HEAD

  - Scan a web server, saving the results to a .json file:
    dirsearch --url url --extensions php --json-report path/to/report.json
```

---

###  1.49. <a name='gitleaks:DetectsecretsandAPIkeysleakedinGitrepositories.'></a>gitleaks:   Detect secrets and API keys leaked in Git repositories.
```sh
gitleaks

  Detect secrets and API keys leaked in Git repositories.
  More information: https://github.com/gitleaks/gitleaks.

  - Scan a remote repository:
    gitleaks detect --repo-url https://github.com/username/repository.git

  - Scan a local directory:
    gitleaks detect --source path/to/repository

  - Output scan results to a JSON file:
    gitleaks detect --source path/to/repository --report path/to/report.json

  - Use a custom rules file:
    gitleaks detect --source path/to/repository --config-path path/to/config.toml

  - Start scanning from a specific commit:
    gitleaks detect --source path/to/repository --log-opts --since=commit_id

  - Scan uncommitted changes before a commit:
    gitleaks protect --staged

  - Display verbose output indicating which parts were identified as leaks during the scan:
    gitleaks protect --staged --verbose
```

---

###  1.50. <a name='naabu:AfastportscannerwritteninGowithafocusonreliabilityandsimplicity.'></a>naabu:   A fast port scanner written in Go with a focus on reliability and simplicity.
```sh
naabu

  A fast port scanner written in Go with a focus on reliability and simplicity.
  Note: Some features are only activated when naabu is run with root privileges such as SYN scan.
  More information: https://github.com/projectdiscovery/naabu.

  - Run a SYN scan against default (top 100) ports of remote host:
    sudo naabu -host host

  - Display available network interfaces and public IP address of the local host:
    naabu -interface-list

  - Scan all ports of the remote host (CONNECT scan without sudo):
    naabu -p - -host host

  - Scan the top 1000 ports of the remote host:
    naabu -top-ports 1000 -host host

  - Scan TCP ports 80, 443 and UDP port 53 of the remote host:
    naabu -p 80,443,u:53 -host host

  - Show CDN type the remote host is using, if any:
    naabu -p 80,443 -cdn -host host

  - Run nmap from naabu for additional functionalities (nmap must be installed):
    sudo naabu -v -host host -nmap-cli 'nmap -v -T5 -sC'


See also: sudo, nmap
```

---

###  1.51. <a name='nuclei:FastandcustomizablevulnerabilityscannerbasedonasimpleYAMLbasedDSL.'></a>nuclei:   Fast and customizable vulnerability scanner based on a simple YAML based DSL.
```sh
nuclei

  Fast and customizable vulnerability scanner based on a simple YAML based DSL.
  More information: https://github.com/projectdiscovery/nuclei.

  - [u]pdate nuclei [t]emplates to the latest released version:
    nuclei -ut

  - [l]ist all [t]emplates with a specific [p]rotocol [t]ype:
    nuclei -tl -pt dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript

  - Run an [a]utomatic web [s]can using wappalyzer technology detection specifying a target [u]RL/host to scan:
    nuclei -as -u scanme.nmap.org

  - Run HTTP [p]rotocol [t]ype templates of high and critical severity, [e]xporting results to [m]arkdown files inside a specific directory:
    nuclei -severity high,critical -pt http -u http://scanme.sh -me markdown_directory

  - Run all templates using a different [r]ate [l]imit and maximum [b]ulk [s]ize with silent output (only showing the findings):
    nuclei -rl 150 -bs 25 -c 25 -silent -u http://scanme.sh

  - Run the WordPress [w]orkflow against a WordPress site:
    nuclei -w path/to/nuclei-templates/workflows/wordpress-workflow.yaml -u https://sample.wordpress.site

  - Run one or more specific [t]emplates or directory with [t]emplates with [v]erbose output in stderr and [o]utput detected issues/vulnerabilities to a file:
    nuclei -t path/to/nuclei-templates/http -u http://scanme.sh -v -o results

  - Run scan based on one or more [t]emplate [c]onditions:
    nuclei -tc "contains(tags, 'xss') && contains(tags, 'cve')" -u https://vulnerable.website
```

---

###  1.52. <a name='trivy:ScannerforvulnerabilitiesincontainerimagesfilesystemsandGitrepositoriesaswellasforconfigurationissues.'></a>trivy:   Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
```sh
trivy

  Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
  More information: https://aquasecurity.github.io/trivy.

  - Scan a Docker image for vulnerabilities and exposed secrets:
    trivy image image:tag

  - Scan a Docker image filtering the output by severity:
    trivy image --severity HIGH,CRITICAL alpine:3.15

  - Scan a Docker image ignoring any unfixed/unpatched vulnerabilities:
    trivy image --ignore-unfixed alpine:3.15

  - Scan the filesystem for vulnerabilities and misconfigurations:
    trivy fs --security-checks vuln,config path/to/project_directory

  - Scan a IaC (Terraform, CloudFormation, ARM, Helm and Dockerfile) directory for misconfigurations:
    trivy config path/to/iac_directory

  - Scan a local or remote Git repository for vulnerabilities:
    trivy repo path/to/local_repository_directory|remote_repository_URL

  - Scan a Git repository up to a specific commit hash:
    trivy repo --commit commit_hash repository

  - Generate output with a SARIF template:
    trivy image --format template --template "@sarif.tpl" -o path/to/report.sarif image:tag
```

---

###  1.53. <a name='rustscan:FastPortScannerwritteninRustwithnmapbuiltin.'></a>rustscan:   Fast Port Scanner written in Rust with nmap built in.
```sh
rustscan

  Fast Port Scanner written in Rust with nmap built in.
  More information: https://github.com/RustScan/RustScan.

  - Scan all ports of one or more comma-delimited [a]ddresses using the default values:
    rustscan --addresses ip_or_hostname

  - Scan the [t]op 1000 ports with service and version detection:
    rustscan --top --addresses address_or_addresses

  - Scan a specific list of [p]orts:
    rustscan --ports port1,port2,...,portN --addresses address_or_addresses

  - Scan a specific range of ports:
    rustscan --range start-end --addresses address_or_addresses

  - Add script arguments to nmap:
    rustscan --addresses address_or_addresses -- -A -sC

  - Scan with custom [b]atch size (default: 4500) and [t]imeout (default: 1500ms):
    rustscan --batch-size batch_size --timeout timeout --addresses address_or_addresses

  - Scan with specific port order:
    rustscan --scan-order serial|random --addresses address_or_addresses

  - Scan in greppable mode (only output of the ports, no nmap):
    rustscan --greppable --addresses address_or_addresses


See also: nmap
```

---

###  1.54. <a name='exiftool:Readandwritemetainformationinfiles.'></a>exiftool:   Read and write meta information in files.
```sh
exiftool

  Read and write meta information in files.
  More information: https://exiftool.org.

  - Print the EXIF metadata for a given file:
    exiftool path/to/file

  - Remove all EXIF metadata from the given files:
    exiftool -All= path/to/file1 path/to/file2 ...

  - Remove GPS EXIF metadata from given image files:
    exiftool "-gps*=" path/to/image1 path/to/image2 ...

  - Remove all EXIF metadata from the given image files, then re-add metadata for color and orientation:
    exiftool -All= -tagsfromfile @ -colorspacetags -orientation path/to/image1 path/to/image2 ...

  - Move the date at which all photos in a directory were taken 1 hour forward:
    exiftool "-AllDates+=0:0:0 1:0:0" path/to/directory

  - Move the date at which all JPEG photos in the current directory were taken 1 day and 2 hours backward:
    exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg

  - Only change the DateTimeOriginal field subtracting 1.5 hours, without keeping backups:
    exiftool -DateTimeOriginal-=1.5 -overwrite_original

  - Recursively rename all JPEG photos in a directory based on the DateTimeOriginal field:
    exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e path/to/directory -r -ext jpg
```

---

###  1.55. <a name='trufflehog:FindandverifycredentialsinfilesGitrepositoriesS3bucketsandDockerimages.'></a>trufflehog:   Find and verify credentials in files, Git repositories, S3 buckets, and Docker images.
```sh
trufflehog

  Find and verify credentials in files, Git repositories, S3 buckets, and Docker images.
  More information: https://github.com/trufflesecurity/trufflehog.

  - Scan a Git repository for verified secrets:
    trufflehog git https://github.com/trufflesecurity/test_keys --only-verified

  - Scan a GitHub organization for verified secrets:
    trufflehog github --org=trufflesecurity --only-verified

  - Scan a GitHub repository for verified keys and get JSON output:
    trufflehog git https://github.com/trufflesecurity/test_keys --only-verified --json

  - Scan a GitHub repository along with its Issues and Pull Requests:
    trufflehog github --repo=https://github.com/trufflesecurity/test_keys --issue-comments --pr-comments

  - Scan an S3 bucket for verified keys:
    trufflehog s3 --bucket=bucket name --only-verified

  - Scan S3 buckets using IAM Roles:
    trufflehog s3 --role-arn=iam-role-arn

  - Scan individual files or directories:
    trufflehog filesystem path/to/file_or_directory1 path/to/file_or_directory2 ...

  - Scan a Docker image for verified secrets:
    trufflehog docker --image trufflesecurity/secrets --only-verified
```

---

###  1.56. <a name='steghide:SteganographytoolforJPEGBMPWAVandAUfileformats.'></a>steghide:   Steganography tool for JPEG, BMP, WAV and AU file formats.
```sh
steghide

  Steganography tool for JPEG, BMP, WAV and AU file formats.
  More information: https://github.com/StefanoDeVuono/steghide.

  - Embed data in a PNG, prompting for a passphrase:
    steghide embed --coverfile path/to/image.png --embedfile path/to/data.txt

  - Extract data from a WAV audio file:
    steghide extract --stegofile path/to/sound.wav

  - Display file information, trying to detect an embedded file:
    steghide info path/to/file.jpg

  - Embed data in a JPEG image, using maximum compression:
    steghide embed --coverfile path/to/image.jpg --embedfile path/to/data.txt --compress 9

  - Get the list of supported encryption algorithms and modes:
    steghide encinfo

  - Embed encrypted data in a JPEG image, e.g. with Blowfish in CBC mode:
    steghide embed --coverfile path/to/image.jpg --embedfile path/to/data.txt --encryption blowfish|... cbc|...
```

---

###  1.57. <a name='rkhunter:Searchesforrootkitsandmalware.'></a>rkhunter:   Searches for rootkits and malware.
```sh
rkhunter

  Searches for rootkits and malware.
  More information: https://wiki.archlinux.org/title/Rkhunter.

  - Check a system for rootkits and malware:
    sudo rkhunter --check

  - Update rkhunter:
    sudo rkhunter --update

  - Print all available tests:
    sudo rkhunter --list

  - Display version:
    sudo rkhunter --versioncheck

  - Display help:
    sudo rkhunter --help
```

---

###  1.58. <a name='tshark:PacketanalysistoolCLIversionofWireshark.'></a>tshark:   Packet analysis tool, CLI version of Wireshark.
```sh
tshark

  Packet analysis tool, CLI version of Wireshark.
  More information: https://tshark.dev/.

  - Monitor everything on localhost:
    tshark

  - Only capture packets matching a specific capture filter:
    tshark -f 'udp port 53'

  - Only show packets matching a specific output filter:
    tshark -Y 'http.request.method == "GET"'

  - Decode a TCP port using a specific protocol (e.g. HTTP):
    tshark -d tcp.port==8888,http

  - Specify the format of captured output:
    tshark -T json|text|ps|…

  - Select specific fields to output:
    tshark -T fields|ek|json|pdml -e http.request.method -e ip.src

  - Write captured packet to a file:
    tshark -w path/to/file

  - Analyze packets from a file:
    tshark -r path/to/file.pcap
```

---

###  1.59. <a name='tcpkill:Killspecifiedin-progressTCPconnections.'></a>tcpkill:   Kill specified in-progress TCP connections.
```sh
tcpkill

  Kill specified in-progress TCP connections.
  More information: https://manned.org/tcpkill.

  - Kill in-progress connections at a specified interface, host and port:
    tcpkill -i eth1 host 192.95.4.27 and port 2266
```

---

###  1.60. <a name='openssl:OpenSSLcryptographictoolkit.'></a>openssl:   OpenSSL cryptographic toolkit.
```sh
openssl

  OpenSSL cryptographic toolkit.
  Some subcommands such as openssl req have their own usage documentation.
  More information: https://www.openssl.org.

  - Display help:
    openssl help

  - Display help for a specific subcommand:
    openssl help x509

  - Display version:
    openssl version
```

---

###  1.61. <a name='cryptsetup:Manageplaindm-cryptandLUKSLinuxUnifiedKeySetupencryptedvolumes.'></a>cryptsetup:   Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes.
```sh
cryptsetup

  Manage plain dm-crypt and LUKS (Linux Unified Key Setup) encrypted volumes.
  More information: https://gitlab.com/cryptsetup/cryptsetup/.

  - Initialize a LUKS volume (overwrites all data on the partition):
    cryptsetup luksFormat /dev/sda1

  - Open a LUKS volume and create a decrypted mapping at /dev/mapper/target:
    cryptsetup luksOpen /dev/sda1 target

  - Remove an existing mapping:
    cryptsetup luksClose target

  - Change the LUKS volume's passphrase:
    cryptsetup luksChangeKey /dev/sda1
```

---

###  1.62. <a name='zip2john:ExtractpasswordhashesfromZiparchivesforusewithJohntheRipperpasswordcracker.'></a>zip2john:   Extract password hashes from Zip archives for use with John the Ripper password cracker.
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

---

###  1.63. <a name='jq:AJSONprocessorthatusesadomain-specificlanguageDSL.'></a>jq:   A JSON processor that uses a domain-specific language (DSL).
```sh
jq

  A JSON processor that uses a domain-specific language (DSL).
  More information: https://jqlang.github.io/jq/manual/.

  - Execute a specific expression (print a colored and formatted JSON output):
    cat path/to/file.json | jq '.'

  - Execute a specific script:
    cat path/to/file.json | jq --from-file path/to/script.jq

  - Pass specific arguments:
    cat path/to/file.json | jq --arg "name1" "value1" --arg "name2" "value2" ... '. + $ARGS.named'

  - Print specific keys:
    cat path/to/file.json | jq '.key1, .key2, ...'

  - Print specific array items:
    cat path/to/file.json | jq '.[index1], .[index2], ...'

  - Print all array/object values:
    cat path/to/file.json | jq '.[]'

  - Add/remove specific keys:
    cat path/to/file.json | jq '. +|- {"key1": "value1", "key2": "value2", ...}'
```

---

###  1.64. <a name='yq:Alightweightandportablecommand-lineYAMLprocessor.'></a>yq:   A lightweight and portable command-line YAML processor.
```sh
yq

  A lightweight and portable command-line YAML processor.
  More information: https://mikefarah.gitbook.io/yq/.

  - Output a YAML file, in pretty-print format (v4+):
    yq eval path/to/file.yaml

  - Output a YAML file, in pretty-print format (v3):
    yq read path/to/file.yaml --colors

  - Output the first element in a YAML file that contains only an array (v4+):
    yq eval '.[0]' path/to/file.yaml

  - Output the first element in a YAML file that contains only an array (v3):
    yq read path/to/file.yaml '[0]'

  - Set (or overwrite) a key to a value in a file (v4+):
    yq eval '.key = "value"' --inplace path/to/file.yaml

  - Set (or overwrite) a key to a value in a file (v3):
    yq write --inplace path/to/file.yaml 'key' 'value'

  - Merge two files and print to stdout (v4+):
    yq eval-all 'select(filename == "path/to/file1.yaml") select(filename == "path/to/file2.yaml")' path/to/file1.yaml path/to/file2.yaml

  - Merge two files and print to stdout (v3):
    yq merge path/to/file1.yaml path/to/file2.yaml --colors
```

---

###  1.65. <a name='xsv:ACSVcommand-linetoolkitwritteninRust.'></a>xsv:   A CSV command-line toolkit written in Rust.
```sh
xsv

  A CSV command-line toolkit written in Rust.
  More information: https://github.com/BurntSushi/xsv.

  - Inspect the headers of a file:
    xsv headers path/to/file.csv

  - Count the number of entries:
    xsv count path/to/file.csv

  - Get an overview of the shape of entries:
    xsv stats path/to/file.csv | xsv table

  - Select a few columns:
    xsv select column1,column2 path/to/file.csv

  - Show 10 random entries:
    xsv sample 10 path/to/file.csv

  - Join a column from one file to another:
    xsv join --no-case column1 path/to/file1.csv column2 path/to/file2.csv | xsv table
```

---

###  1.66. <a name='passwd:Changeauserspassword.'></a>passwd:   Change a user's password.
```sh
passwd

  Change a user's password.
  More information: https://manned.org/passwd.

  - Change the password of the current user interactively:
    passwd

  - Change the password of a specific user:
    passwd username

  - Get the current status of the user:
    passwd -S

  - Make the password of the account blank (it will set the named account passwordless):
    passwd -d
```

---

###  1.67. <a name='nginx:Nginxwebserver.'></a>nginx:   Nginx web server.
```sh
nginx

  Nginx web server.
  More information: https://nginx.org/en/.

  - Start server with the default configuration file:
    nginx

  - Start server with a custom configuration file:
    nginx -c configuration_file

  - Start server with a prefix for all relative paths in the configuration file:
    nginx -c configuration_file -p prefix/for/relative/paths

  - Test the configuration without affecting the running server:
    nginx -t

  - Reload the configuration by sending a signal with no downtime:
    nginx -s reload
```

---

###  1.68. <a name='sqlite3:Thecommand-lineinterfacetoSQLite3whichisaself-containedfile-basedembeddedSQLengine.'></a>sqlite3:   The command-line interface to SQLite 3, which is a self-contained file-based embedded SQL engine.
```sh
sqlite3

  The command-line interface to SQLite 3, which is a self-contained file-based embedded SQL engine.
  More information: https://sqlite.org.

  - Start an interactive shell with a new database:
    sqlite3

  - Open an interactive shell against an existing database:
    sqlite3 path/to/database.sqlite3

  - Execute an SQL statement against a database and then exit:
    sqlite3 path/to/database.sqlite3 'SELECT FROM some_table;'
```

---

###  1.69. <a name='vim:VimViIMprovedacommand-linetexteditorprovidesseveralmodesfordifferentkindsoftextmanipulation.'></a>vim:   Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.
```sh
vim

  Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.
  Pressing i in normal mode enters insert mode. Pressing <Esc> goes back to normal mode, which enables the use of Vim commands.
  See also: vimdiff, vimtutor, nvim.
  More information: https://www.vim.org.

  - Open a file:
    vim path/to/file

  - Open a file at a specified line number:
    vim +line_number path/to/file

  - View Vim's help manual:
    :help<Enter>

  - Save and quit the current buffer:
    :wq<Enter>

  - Enter normal mode and undo the last operation:
    <Esc>u

  - Search for a pattern in the file (press n/N to go to next/previous match):
    /search_pattern<Enter>

  - Perform a regular expression substitution in the whole file:
    :%s/regular_expression/replacement/g<Enter>

  - Display the line numbers:
    :set nu<Enter>


See also: vimdiff, vimtutor, nvim, n
```

---

###  1.70. <a name='nano:Command-linetexteditor.AnenhancedPicoclone.'></a>nano:   Command-line text editor. An enhanced Pico clone.
```sh
nano

  Command-line text editor. An enhanced Pico clone.
  More information: https://nano-editor.org.

  - Start the editor:
    nano

  - Start the editor without using configuration files:
    nano --ignorercfiles

  - Open specific files, moving to the next file when closing the previous one:
    nano path/to/file1 path/to/file2 ...

  - Open a file and position the cursor at a specific line and column:
    nano +line,column path/to/file

  - Open a file and enable soft wrapping:
    nano --softwrap path/to/file

  - Open a file and indent new lines to the previous line's indentation:
    nano --autoindent path/to/file

  - Open a file and create a backup file (path/to/file~) on save:
    nano --backup path/to/file
```

---

###  1.71. <a name='sshd:SecureShellDaemon-allowsremotemachinestosecurelylogintothecurrentmachine.'></a>sshd:   Secure Shell Daemon - allows remote machines to securely log in to the current machine.
```sh
sshd

  Secure Shell Daemon - allows remote machines to securely log in to the current machine.
  Remote machines can execute commands as it is executed at this machine.
  More information: https://man.openbsd.org/sshd.

  - Start daemon in the background:
    sshd

  - Run sshd in the foreground:
    sshd -D

  - Run with verbose output (for debugging):
    sshd -D -d

  - Run on a specific port:
    sshd -p port
```

---

###  1.72. <a name='ngrok:Reverseproxythatcreatesasecuretunnelfromapublicendpointtoalocallyrunningwebservice.'></a>ngrok:   Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.
```sh
ngrok

  Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.
  More information: https://ngrok.com.

  - Expose a local HTTP service on a given port:
    ngrok http 80

  - Expose a local HTTP service on a specific host:
    ngrok http foo.dev:80

  - Expose a local HTTPS server:
    ngrok http https://localhost

  - Expose TCP traffic on a given port:
    ngrok tcp 22

  - Expose TLS traffic for a specific host and port:
    ngrok tls -hostname=foo.com 443
```

---

###  1.73. <a name='pup:Command-lineHTMLparsingtool.'></a>pup:   Command-line HTML parsing tool.
```sh
pup

  Command-line HTML parsing tool.
  More information: https://github.com/ericchiang/pup.

  - Transform a raw HTML file into a cleaned, indented, and colored format:
    cat index.html | pup --color

  - Filter HTML by element tag name:
    cat index.html | pup 'tag'

  - Filter HTML by ID:
    cat index.html | pup 'div#id'

  - Filter HTML by attribute value:
    cat index.html | pup 'input[type="text"]'

  - Print all text from the filtered HTML elements and their children:
    cat index.html | pup 'div text{}'

  - Print HTML as JSON:
    cat index.html | pup 'div json{}'
```

---

###  1.74. <a name='chisel:CreateTCPUDPtunnelstransportedoverHTTPsecuredviaSSH.'></a>chisel:   Create TCP/UDP tunnels, transported over HTTP, secured via SSH.
```sh
chisel

  Create TCP/UDP tunnels, transported over HTTP, secured via SSH.
  Includes both client and server in the same chisel executable.
  More information: https://github.com/jpillora/chisel.

  - Run a Chisel server:
    chisel server

  - Run a Chisel server listening to a specific port:
    chisel server -p server_port

  - Run a chisel server that accepts authenticated connections using username and password:
    chisel server --auth username:password

  - Connect to a Chisel server and tunnel a specific port to a remote server and port:
    chisel client server_ip:server_port local_port:remote_server:remote_port

  - Connect to a Chisel server and tunnel a specific host and port to a remote server and port:
    chisel client server_ip:server_port local_host:local_port:remote_server:remote_port

  - Connect to a Chisel server using username and password authentication:
    chisel client --auth username:password server_ip:server_port local_port:remote_server:remote_port

  - Initialize a Chisel server in reverse mode on a specific port, also enabling SOCKS5 proxy (on port 1080) functionality:
    chisel server -p server_port --reverse --socks5

  - Connect to a Chisel server at specific IP and port, creating a reverse tunnel mapped to a local SOCKS proxy:
    chisel client server_ip:server_port R:socks
```

---

###  1.75. <a name='createdb:CreateaPostgreSQLdatabase.'></a>createdb:   Create a PostgreSQL database.
```sh
createdb

  Create a PostgreSQL database.
  More information: https://www.postgresql.org/docs/current/app-createdb.html.

  - Create a database owned by the current user:
    createdb database_name

  - Create a database owned by a specific user with a description:
    createdb --owner username database_name 'description'

  - Create a database from a template:
    createdb --template template_name database_name
```

---

###  1.76. <a name='subfinder:Discovervalidsubdomainsforwebsites.'></a>subfinder:   Discover valid subdomains for websites.
```sh
subfinder

  Discover valid subdomains for websites.
  Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
  More information: https://github.com/projectdiscovery/subfinder.

  - Find subdomains for a specific [d]omain:
    subfinder -d example.com

  - Show only the subdomains found:
    subfinder --silent -d example.com

  - Use a brute-force attack to find subdomains:
    subfinder -d example.com -b

  - Remove wildcard subdomains:
    subfinder -nW -d example.com

  - Use a given comma-separated list of [r]esolvers:
    subfinder -r 8.8.8.8,1.1.1.1,... -d example.com
```

---

###  1.77. <a name='sublist3r:Fastsubdomainsenumerationtoolforpenetrationtesters.'></a>sublist3r:   Fast subdomains enumeration tool for penetration testers.
```sh
sublist3r

  Fast subdomains enumeration tool for penetration testers.
  More information: https://github.com/aboul3la/Sublist3r.

  - Find subdomains for a domain:
    sublist3r --domain domain_name

  - Find subdomains for a domain, also enabling brute force search:
    sublist3r --domain domain_name --bruteforce

  - Save the found subdomains to a text file:
    sublist3r --domain domain_name --output path/to/output_file

  - Display help:
    sublist3r --help
```

---
##  2. <a name='AlternativesinRust'></a>Alternatives in Rust 

###  2.1. <a name='exa:AmodernreplacementforlsListdirectorycontents.'></a>exa:   A modern replacement for ls (List directory contents).
```sh
exa

  A modern replacement for ls (List directory contents).
  More information: https://the.exa.website.

  - List files one per line:
    exa --oneline

  - List all files, including hidden files:
    exa --all

  - Long format list (permissions, ownership, size and modification date) of all files:
    exa --long --all

  - List files with the largest at the top:
    exa --reverse --sort=size

  - Display a tree of files, three levels deep:
    exa --long --tree --level=3

  - List files sorted by modification date (oldest first):
    exa --long --sort=modified

  - List files with their headers, icons, and Git statuses:
    exa --long --header --icons --git

  - Don't list files mentioned in .gitignore:
    exa --git-ignore


See also: ls
```

---

###  2.2. <a name='fd:Analternativetofind.'></a>fd:   An alternative to find.
```sh
fd

  An alternative to find.
  Aims to be faster and easier to use than find.
  More information: https://github.com/sharkdp/fd.

  - Recursively find files matching a specific pattern in the current directory:
    fd "string|regex"

  - Find files that begin with foo:
    fd "^foo"

  - Find files with a specific extension:
    fd --extension txt

  - Find files in a specific directory:
    fd "string|regex" path/to/directory

  - Include ignored and hidden files in the search:
    fd --hidden --no-ignore "string|regex"

  - Execute a command on each search result returned:
    fd "string|regex" --exec command


See also: find
```

---

###  2.3. <a name='fselect:FindfileswithSQL-likequeries.'></a>fselect:   Find files with SQL-like queries.
```sh
fselect

  Find files with SQL-like queries.
  More information: https://github.com/jhspetersson/fselect.

  - Select full path and size from temporary or configuration files in a given directory:
    fselect size, path from path/to/directory where name = '*.cfg' or name = '*.tmp'

  - Find square images:
    fselect path from path/to/directory where width = height

  - Find old-school rap 320kbps MP3 files:
    fselect path from path/to/directory where genre = Rap and bitrate = 320 and mp3_year lt 2000

  - Select only the first 5 results and output as JSON:
    fselect size, path from path/to/directory limit 5 into json

  - Use SQL aggregate functions to calculate minimum, maximum and average size of files in a directory:
    fselect "MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*) from path/to/directory"
```

---

###  2.4. <a name='lsd:Listdirectorycontents.'></a>lsd:   List directory contents.
```sh
lsd

  List directory contents.
  The next generation ls command, written in Rust.
  More information: https://github.com/Peltoche/lsd.

  - List files and directories, one per line:
    lsd -1

  - List all files and directories, including hidden ones, in the current directory:
    lsd -a

  - List all files and directories with trailing / added to directory names:
    lsd -F

  - List all files and directories in long format (permissions, ownership, size, and modification date):
    lsd -la

  - List all files and directories in long format with size displayed using human-readable units (KiB, MiB, GiB):
    lsd -lh

  - List all files and directories in long format, sorted by size (descending):
    lsd -lS

  - List all files and directories in long format, sorted by modification date (oldest first):
    lsd -ltr

  - Only list directories:
    lsd -d */


See also: ls
```

---

###  2.5. <a name='ranger:ConsolefilemanagerwithVIkeybindings.'></a>ranger:   Console file manager with VI key bindings.
```sh
ranger

  Console file manager with VI key bindings.
  See also: clifm, vifm, mc, dolphin.
  More information: https://github.com/ranger/ranger.

  - Launch ranger:
    ranger

  - Show only directories:
    ranger --show-only-dirs

  - Change the configuration directory:
    ranger --confdir=path/to/directory

  - Change the data directory:
    ranger --datadir=path/to/directory

  - Print CPU usage statistics on exit:
    ranger --profile


See also: clifm, vifm, mc, dolphin
```

---

###  2.6. <a name='broot:Navigatedirectorytreesinteractively.'></a>broot:   Navigate directory trees interactively.
```sh
broot

  Navigate directory trees interactively.
  See also: br.
  More information: https://github.com/Canop/broot.

  - Install or reinstall the br shell function:
    broot --install


See also: br
```

---

###  2.7. <a name='dua:DuaDiskUsageAnalyzer:getthediskspaceusageofadirectory.'></a>dua:   Dua (Disk Usage Analyzer): get the disk space usage of a directory.
```sh
dua

  Dua (Disk Usage Analyzer): get the disk space usage of a directory.
  More information: https://github.com/Byron/dua-cli.

  - Analyze specific directory:
    dua path/to/directory

  - Display apparent size instead of disk usage:
    dua --apparent-size

  - Count hard-linked files each time they are seen:
    dua --count-hard-links

  - Aggregate the consumed space of one or more directories or files:
    dua aggregate

  - Launch the terminal user interface:
    dua interactive

  - Format printing byte counts:
    dua --format metric|binary|bytes|GB|GiB|MB|MiB

  - Use a specific number of threads (defaults to the process number of threads):
    dua --threads count
```

---

###  2.8. <a name='dust:Dustgivesaninstantoverviewofwhichdirectoriesareusingdiskspace.'></a>dust:   Dust gives an instant overview of which directories are using disk space.
```sh
dust

  Dust gives an instant overview of which directories are using disk space.
  More information: https://github.com/bootandy/dust.

  - Display information for the current directory:
    dust

  - Display information about one or more directories:
    dust path/to/directory1 path/to/directory2 ...

  - Display 30 directories (defaults to 21):
    dust --number-of-lines 30

  - Display information for the current directory, up to 3 levels deep:
    dust --depth 3

  - Display the biggest directories at the top in descending order:
    dust --reverse

  - Ignore all files and directories with a specific name:
    dust --ignore-directory file_or_directory_name

  - Do not display percent bars and percentages:
    dust --no-percent-bars
```

---

####  2.8.1. <a name='drill:PerformvariousDNSqueries.'></a>drill: Perform various DNS queries.
```sh
  drill

  Perform various DNS queries.
  More information: https://manned.org/drill.

  - Lookup the IP(s) associated with a hostname (A records):
    drill example.com

  - Lookup the mail server(s) associated with a given domain name (MX record):
    drill mx example.com

  - Get all types of records for a given domain name:
    drill any example.com

  - Specify an alternate DNS server to query:
    drill example.com @8.8.8.8

  - Perform a reverse DNS lookup on an IP address (PTR record):
    drill -x 8.8.8.8

  - Perform DNSSEC trace from root servers down to a domain name:
    drill -TD example.com

  - Show DNSKEY record(s) for a domain name:
    drill -s dnskey example.com
```

---

###  2.9. <a name='choose:Ahuman-friendlyandfastalternativetocutandsometimesawk.'></a>choose:   A human-friendly and fast alternative to cut and (sometimes) awk.
```sh
choose

  A human-friendly and fast alternative to cut and (sometimes) awk.
  More information: https://github.com/theryangeary/choose.

  - Print the 5th item from a line (starting from 0):
    choose 4

  - Print the first, 3rd, and 5th item from a line, where items are separated by ':' instead of whitespace:
    choose --field-separator ':' 0 2 4

  - Print everything from the 2nd to 5th item on the line, including the 5th:
    choose 1:4

  - Print everything from the 2nd to 5th item on the line, excluding the 5th:
    choose --exclusive 1:4

  - Print the beginning of the line to the 3rd item:
    choose :2

  - Print all items from the beginning of the line until the 3rd item (exclusive):
    choose --exclusive :2

  - Print all items from the 3rd to the end of the line:
    choose 2:

  - Print the last item from a line:
    choose -1
```

---

###  2.10. <a name='ripgrep:ripgrepisthecommonnameforthecommandrg.'></a>ripgrep:   ripgrep is the common name for the command rg.
```sh
ripgrep

  ripgrep is the common name for the command rg.

  - View documentation for the original command:
    tldr rg


See also: rg
```

---

###  2.11. <a name='rga:Ripgrepwrapperwithrichfiletypesearchingcapabilities.'></a>rga:   Ripgrep wrapper with rich file type searching capabilities.
```sh
rga

  Ripgrep wrapper with rich file type searching capabilities.
  More information: https://github.com/phiresky/ripgrep-all.

  - Search recursively for a pattern in all files in the current directory:
    rga regular_expression

  - List available adapters:
    rga --rga-list-adapters

  - Change which adapters to use (e.g. ffmpeg, pandoc, poppler etc.):
    rga --rga-adapters=adapter1,adapter2 regular_expression

  - Search for a pattern using the mime type instead of the file extension (slower):
    rga --rga-accurate regular_expression

  - Display help:
    rga --help
```

---

###  2.12. <a name='sd:Intuitivefindandreplace.'></a>sd:   Intuitive find and replace.
```sh
sd

  Intuitive find and replace.
  More information: https://github.com/chmln/sd.

  - Trim some whitespace using a regular expression (output stream: stdout):
    echo 'lorem ipsum 23   ' | sd '\s+$' ''

  - Replace words using capture groups (output stream: stdout):
    echo 'cargo +nightly watch' | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'

  - Find and replace in a specific file (output stream: stdout):
    sd -p 'window.fetch' 'fetch' path/to/file.js

  - Find and replace in all files in the current project (output stream: stdout):
    sd 'from "react"' 'from "preact"' "$(find . -type f)"
```

---

###  2.13. <a name='grex:Generateregularexpressions.'></a>grex:   Generate regular expressions.
```sh
grex

  Generate regular expressions.
  More information: https://github.com/pemistahl/grex.

  - Generate a simple regular expression:
    grex space_separated_strings

  - Generate a case-insensitive regular expression:
    grex -i space_separated_strings

  - Replace digits with '\d':
    grex -d space_separated_strings

  - Replace Unicode word character with '\w':
    grex -w space_separated_strings

  - Replace spaces with '\s':
    grex -s space_separated_strings

  - Add {min, max} quantifier representation for repeating sub-strings:
    grex -r space_separated_strings
```

---

###  2.14. <a name='delta:AviewerforGitanddiffoutput.'></a>delta:   A viewer for Git and diff output.
```sh
delta

  A viewer for Git and diff output.
  More information: https://github.com/dandavison/delta.

  - Compare files or directories:
    delta path/to/old_file_or_directory path/to/new_file_or_directory

  - Compare files or directories, showing the line numbers:
    delta --line-numbers path/to/old_file_or_directory path/to/new_file_or_directory

  - Compare files or directories, showing the differences side by side:
    delta --side-by-side path/to/old_file_or_directory path/to/new_file_or_directory

  - Compare files or directories, ignoring any Git configuration settings:
    delta --no-gitconfig path/to/old_file_or_directory path/to/new_file_or_directory

  - Compare, rendering commit hashes, file names, and line numbers as hyperlinks, according to the hyperlink spec for terminal emulators:
    delta --hyperlinks path/to/old_file_or_directory path/to/new_file_or_directory

  - Display the current settings:
    delta --show-config

  - Display supported languages and associated file extensions:
    delta --list-languages
```

---

###  2.15. <a name='gitui:Alightweightkeyboard-onlyTUIforGit.'></a>gitui:   A lightweight keyboard-only TUI for Git.
```sh
gitui

  A lightweight keyboard-only TUI for Git.
  See also: tig, git-gui.
  More information: https://github.com/extrawurst/gitui.

  - Specify the color theme (defaults to theme.ron):
    gitui --theme theme

  - Store logging output into a cache directory:
    gitui --logging

  - Use notify-based file system watcher instead of tick-based update:
    gitui --watcher

  - Generate a bug report:
    gitui --bugreport

  - Use a specific Git directory:
    gitui --directory path/to/directory

  - Use a specific working directory:
    gitui --workdir path/to/directory

  - Display help:
    gitui --help

  - Display version:
    gitui --version


See also: tig, git-gui
```

---

###  2.16. <a name='neofetch:Displayinformationaboutyouroperatingsystemsoftwareandhardware.'></a>neofetch:   Display information about your operating system, software and hardware.
```sh
neofetch

  Display information about your operating system, software and hardware.
  More information: https://github.com/dylanaraps/neofetch.

  - Return the default config, and create it if it's the first time the program runs:
    neofetch

  - Trigger an info line from appearing in the output, where 'infoname' is the function name in the configuration file, e.g. memory:
    neofetch --enable|disable infoname

  - Hide/Show OS architecture:
    neofetch --os_arch on|off

  - Enable/Disable CPU brand in output:
    neofetch --cpu_brand on|off
```

---

###  2.17. <a name='procs:Displayinformationabouttheactiveprocesses.'></a>procs:   Display information about the active processes.
```sh
procs

  Display information about the active processes.
  More information: https://github.com/dalance/procs.

  - List all processes showing the PID, user, CPU usage, memory usage, and the command which started them:
    procs

  - List all processes as a tree:
    procs --tree

  - List information about processes, if the commands which started them contain Zsh:
    procs zsh

  - List information about all processes sorted by CPU time in [a]scending or [d]escending order:
    procs --sorta|--sortd cpu

  - List information about processes with either a PID, command, or user containing 41 or firefox:
    procs --or PID|command|user 41 firefox

  - List information about processes with both PID 41 and a command or user containing zsh:
    procs --and 41 zsh


See also: firefox, zsh
```

---

###  2.18. <a name='py-spy:AsamplingprofilerforPythonprograms.'></a>py-spy:   A sampling profiler for Python programs.
```sh
py-spy

  A sampling profiler for Python programs.
  More information: https://github.com/benfred/py-spy.

  - Show a live view of the functions that take the most execution time of a running process:
    py-spy top --pid pid

  - Start a program and show a live view of the functions that take the most execution time:
    py-spy top -- python path/to/file.py

  - Produce an SVG flame graph of the function call execution time:
    py-spy record -o path/to/profile.svg --pid pid

  - Dump the call stack of a running process:
    py-spy dump --pid pid
```

---

###  2.19. <a name='dog:DNSlookuputility.'></a>dog:   DNS lookup utility.
```sh
dog

  DNS lookup utility.
  It has colorful output, supports DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
  More information: https://dns.lookup.dog.

  - Lookup the IP(s) associated with a hostname (A records):
    dog example.com

  - Query the MX records type associated with a given domain name:
    dog example.com MX

  - Specify a specific DNS server to query (e.g. Cloudflare):
    dog example.com MX @1.1.1.1

  - Query over TCP rather than UDP:
    dog example.com MX @1.1.1.1 --tcp

  - Query the MX records type associated with a given domain name over TCP using explicit arguments:
    dog --query example.com --type MX --nameserver 1.1.1.1 --tcp

  - Lookup the IP(s) associated with a hostname (A records) using DNS over HTTPS (DoH):
    dog example.com --https @https://cloudflare-dns.com/dns-query
```

---

###  2.20. <a name='drill:PerformvariousDNSqueries.-1'></a>drill:   Perform various DNS queries.
```sh
drill

  Perform various DNS queries.
  More information: https://manned.org/drill.

  - Lookup the IP(s) associated with a hostname (A records):
    drill example.com

  - Lookup the mail server(s) associated with a given domain name (MX record):
    drill mx example.com

  - Get all types of records for a given domain name:
    drill any example.com

  - Specify an alternate DNS server to query:
    drill example.com @8.8.8.8

  - Perform a reverse DNS lookup on an IP address (PTR record):
    drill -x 8.8.8.8

  - Perform DNSSEC trace from root servers down to a domain name:
    drill -TD example.com

  - Show DNSKEY record(s) for a domain name:
    drill -s dnskey example.com
```

---

###  2.21. <a name='hyperfine:Acommand-linebenchmarkingtool.'></a>hyperfine:   A command-line benchmarking tool.
```sh
hyperfine

  A command-line benchmarking tool.
  More information: https://github.com/sharkdp/hyperfine/.

  - Run a basic benchmark, performing at least 10 runs:
    hyperfine 'make'

  - Run a comparative benchmark:
    hyperfine 'make target1' 'make target2'

  - Change minimum number of benchmarking runs:
    hyperfine --min-runs 7 'make'

  - Perform benchmark with warmup:
    hyperfine --warmup 5 'make'

  - Run a command before each benchmark run (to clear caches, etc.):
    hyperfine --prepare 'make clean' 'make'

  - Run a benchmark where a single parameter changes for each run:
    hyperfine --prepare 'make clean' --parameter-scan num_threads 1 10 'make -j {num_threads}'
```

---

###  2.22. <a name='topgrade:Updateallapplicationsonthesystem.'></a>topgrade:   Update all applications on the system.
```sh
topgrade

  Update all applications on the system.
  More information: https://github.com/r-darwish/topgrade.

  - Run updates:
    topgrade

  - Say yes to all updates:
    topgrade -y

  - Cleanup temporary/old files:
    topgrade -c

  - Disable a certain update operation:
    topgrade --disable operation

  - Only perform a certain update operation:
    topgrade --only operation

  - Edit the configuration file with default editor:
    topgrade --edit-config
```

---

###  2.23. <a name='gh:WorkseamlesslywithGitHub.'></a>gh:   Work seamlessly with GitHub.
```sh
gh

  Work seamlessly with GitHub.
  Some subcommands such as gh config have their own usage documentation.
  More information: https://cli.github.com/.

  - Clone a GitHub repository locally:
    gh repo clone owner/repository

  - Create a new issue:
    gh issue create

  - View and filter the open issues of the current repository:
    gh issue list

  - View an issue in the default web browser:
    gh issue view --web issue_number

  - Create a pull request:
    gh pr create

  - View a pull request in the default web browser:
    gh pr view --web pr_number

  - Check out a specific pull request locally:
    gh pr checkout pr_number

  - Check the status of a repository's pull requests:
    gh pr status
```

---

###  2.24. <a name='asdf:Command-lineinterfaceformanagingversionsofdifferentpackages.'></a>asdf:   Command-line interface for managing versions of different packages.
```sh
asdf

  Command-line interface for managing versions of different packages.
  More information: https://asdf-vm.com.

  - List all available plugins:
    asdf plugin list all

  - Install a plugin:
    asdf plugin add name

  - List all available versions for a package:
    asdf list all name

  - Install a specific version of a package:
    asdf install name version

  - Set global version for a package:
    asdf global name version

  - Set local version for a package:
    asdf local name version
```

---

###  2.25. <a name='fnm:FastNode.jsversionmanager.'></a>fnm:   Fast Node.js version manager.
```sh
fnm

  Fast Node.js version manager.
  Install, uninstall or switch between Node.js versions.
  More information: https://github.com/Schniz/fnm.

  - Install a specific version of Node.js:
    fnm install node_version

  - List all available Node.js versions and highlight the default one:
    fnm list

  - Use a specific version of Node.js in the current shell:
    fnm use node_version

  - Set the default Node.js version:
    fnm default node_version

  - Uninstall a given Node.js version:
    fnm uninstall node_version
```

---

###  2.26. <a name='volta:AJavaScriptToolManagerthatinstallsNode.jsruntimesnpmandYarnpackagemanagersoranybinariesfromnpm.'></a>volta:   A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm.
```sh
volta

  A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm.
  More information: https://volta.sh.

  - List all installed tools:
    volta list

  - Install the latest version of a tool:
    volta install node|npm|yarn|package_name

  - Install a specific version of a tool:
    volta install node|npm|yarn@version

  - Choose a tool version for a project (will store it in package.json):
    volta pin node|npm|yarn@version

  - Display help:
    volta help

  - Display help for a subcommand:
    volta help fetch|install|uninstall|pin|list|completions|which|setup|run|help
```

---

###  2.27. <a name='silicon:Createanimageofsourcecode.'></a>silicon:   Create an image of source code.
```sh
silicon

  Create an image of source code.
  More information: https://github.com/Aloxaf/silicon.

  - Generate an image from a specific source file:
    silicon path/to/source_file --output path/to/output_image

  - Generate an image from a source file with a specific programming language syntax highlighting (e.g. rust, py, js, etc.):
    silicon path/to/source_file --output path/to/output_image --language language|extension

  - Generate an image from stdin:
    command | silicon --output path/to/output_image
```

---

###  2.28. <a name='mcfly:Asmartcommandhistorysearchandmanagementtool.'></a>mcfly:   A smart command history search and management tool.
```sh
mcfly

  A smart command history search and management tool.
  Replaces your default shell history search (ctrl-r) with an intelligent search engine providing context and relevance to the commands.
  More information: https://github.com/cantino/mcfly.

  - Print the mcfly integration code for the specified shell:
    mcfly init bash|fish|zsh

  - Search the history for a command, with 20 results:
    mcfly search --results 20 "search_terms"

  - Add a new command to the history:
    mcfly add "command"

  - Record that a directory has moved and transfer the historical records from the old path to the new one:
    mcfly move "path/to/old_directory" "path/to/new_directory"

  - Train the suggestion engine (developer tool):
    mcfly train

  - Display help for a specific subcommand:
    mcfly help subcommand
```

---

###  2.29. <a name='zoxide:Keeptrackofthemostfrequentlyuseddirectories.'></a>zoxide:   Keep track of the most frequently used directories.
```sh
zoxide

  Keep track of the most frequently used directories.
  Uses a ranking algorithm to navigate to the best match.
  More information: https://github.com/ajeetdsouza/zoxide.

  - Go to the highest-ranked directory that contains "foo" in the name:
    zoxide query foo

  - Go to the highest-ranked directory that contains "foo" and then "bar":
    zoxide query foo bar

  - Start an interactive directory search (requires fzf):
    zoxide query --interactive

  - Add a directory or increment its rank:
    zoxide add path/to/directory

  - Remove a directory from zoxide's database interactively:
    zoxide remove path/to/directory --interactive

  - Generate shell configuration for command aliases (z, za, zi, zq, zr):
    zoxide init bash|fish|zsh


See also: fzf, z
```

---

###  2.30. <a name='fuck:Correctsyourpreviousconsolecommand.'></a>fuck:   Corrects your previous console command.
```sh
fuck

  Corrects your previous console command.
  More information: https://github.com/nvbn/thefuck.

  - Set the fuck alias to thefuck tool:
    eval "$(thefuck --alias)"

  - Try to match a rule for the previous command:
    fuck

  - Confirm the first choice immediately (correct argument depends on level of annoyance):
    fuck --yes|yeah|hard
```

---

###  2.31. <a name='asciinema:Recordandreplayterminalsessionsandoptionallysharethemonhttps:asciinema.org.'></a>asciinema:   Record and replay terminal sessions, and optionally share them on https://asciinema.org.
```sh
asciinema

  Record and replay terminal sessions, and optionally share them on https://asciinema.org.
  See also: terminalizer.
  More information: https://docs.asciinema.org/manual/cli/usage.

  - Associate the local install of asciinema with an asciinema.org account:
    asciinema auth

  - Make a new recording (finish it with Ctrl+D or type exit, and then choose to upload it or save it locally):
    asciinema rec

  - Make a new recording and save it to a local file:
    asciinema rec path/to/recording.cast

  - Replay a terminal recording from a local file:
    asciinema play path/to/recording.cast

  - Replay a terminal recording hosted on https://asciinema.org:
    asciinema play https://asciinema.org/a/cast_id

  - Make a new recording, limiting any [i]dle time to at most 2.5 seconds:
    asciinema rec -i 2.5

  - Print the full output of a locally saved recording:
    asciinema cat path/to/recording.cast

  - Upload a locally saved terminal session to asciinema.org:
    asciinema upload path/to/recording.cast


See also: terminalizer, exit
```

---

###  2.32. <a name='navi:Aninteractivecheatsheettoolforthecommandlineandapplicationlaunchers.'></a>navi:   An interactive cheatsheet tool for the command line and application launchers.
```sh
navi

  An interactive cheatsheet tool for the command line and application launchers.
  More information: https://github.com/denisidoro/navi.

  - Browse through all available cheatsheets:
    navi

  - Browse the cheatsheet for navi itself:
    navi fn welcome

  - Print a command from the cheatsheet without executing it:
    navi --print

  - Output shell widget source code (It automatically detects your shell if possible, but can also be specified manually):
    navi widget shell

  - Autoselect and execute the snippet that best matches a query:
    navi --query 'query' --best-match
```

---

###  2.33. <a name='hexyl:Asimplehexviewerfortheterminal.Usescoloredoutputtodistinguishdifferentcategoriesofbytes.'></a>hexyl:   A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.
```sh
hexyl

  A simple hex viewer for the terminal. Uses colored output to distinguish different categories of bytes.
  More information: https://github.com/sharkdp/hexyl.

  - Print the hexadecimal representation of a file:
    hexyl path/to/file

  - Print the hexadecimal representation of the first n bytes of a file:
    hexyl -n n path/to/file

  - Print bytes 512 through 1024 of a file:
    hexyl -r 512:1024 path/to/file

  - Print 512 bytes starting at the 1024th byte:
    hexyl -r 1024:+512 path/to/file
```

---

###  2.34. <a name='tokei:Displaystatisticsaboutcode.'></a>tokei:   Display statistics about code.
```sh
tokei

  Display statistics about code.
  More information: https://github.com/XAMPPRocky/tokei.

  - Display a report for the code in a directory and all subdirectories:
    tokei path/to/directory

  - Display a report for a directory excluding .min.js files:
    tokei path/to/directory -e *.min.js

  - Display statistics for individual files in a directory:
    tokei path/to/directory --files

  - Display a report for all files of type Rust and Markdown:
    tokei path/to/directory -t=Rust,Markdown
```

---

###  2.35. <a name='xh:FriendlyandfasttoolforsendingHTTPrequests.'></a>xh:   Friendly and fast tool for sending HTTP requests.
```sh
  xh

  Friendly and fast tool for sending HTTP requests.
  More information: https://github.com/ducaale/xh.

  - Send a GET request:
    xh httpbin.org/get

  - Send a POST request with a JSON body (key-value pairs are added to a top-level JSON object - e.g. {"name": "john", "age": 25}):
    xh post httpbin.org/post name=john age:=25

  - Send a GET request with query parameters (e.g. first_param=5&second_param=true):
    xh get httpbin.org/get first_param==5 second_param==true

  - Send a GET request with a custom header:
    xh get httpbin.org/get header-name:header-value

  - Make a GET request and save the response body to a file:
    xh --download httpbin.org/json --output path/to/file
```

---

###  2.36. <a name='rargs:Executeacommandforeachlineofstandardinput.'></a>rargs:   Execute a command for each line of standard input.
```sh
  rargs

  Execute a command for each line of standard input.
  Like xargs, but with pattern matching support.
  More information: https://github.com/lotabout/rargs.

  - Execute a command for every line of input, just like xargs ({0} indicates where to substitute in the text):
    command | rargs command {0}

  - Do a dry run, which prints the commands that would be run instead of executing them:
    command | rargs -e command {0}

  - Remove the .bak extension from every file in a list:
    command | rargs -p '(.*).bak mv {0} {1}

  - Execute commands in parallel:
    command | rargs -w max-procs

  - Consider each line of input to be separated by a NUL character (\0) instead of a newline (\n):
    command | rargs -0 command {0}

```

---

###  2.37. <a name='paru:AnAURhelperandpacmanwrapper.'></a>paru: An AUR helper and pacman wrapper.
```sh
   paru: 

  An AUR helper and pacman wrapper.
  More information: https://github.com/Morganamilo/paru.

  - Interactively search for and install a package:
    paru package_name_or_search_term

  - Synchronize and update all packages:
    paru

  - Upgrade AUR packages:
    paru -Sua

  - Get information about a package:
    paru -Si package

  - Download PKGBUILD and other package source files from the AUR or ABS:
    paru --getpkgbuild package

  - Display the PKGBUILD file of a package:
    paru --getpkgbuild --print package
```

---

###  2.38. <a name='starship:Theminimalblazing-fastandinfinitelycustomizablepromptforanyshell.'></a>starship:   The minimal, blazing-fast, and infinitely customizable prompt for any shell.
```sh
  starship

  The minimal, blazing-fast, and infinitely customizable prompt for any shell.
  Some subcommands such as starship init have their own usage documentation.
  More information: https://starship.rs.

  - Print the starship integration code for the specified shell:
    starship init bash|elvish|fish|ion|powershell|tcsh|zsh

  - Explain each part of the current prompt and show the time taken to render them:
    starship explain

  - Print the computed starship configuration (use --default to print default configuration instead):
    starship print-config

  - List supported modules:
    starship module --list

  - Edit the starship configuration in the default editor:
    starship configure

  - Create a bug report GitHub issue pre-populated with information about the system and starship configuration:
    starship bug-report

  - Print the completion script for the specified shell:
    starship completions bash|elvish|fish|powershell|zsh

  - Display help for a subcommand:
    starship subcommand --help
```

---

###  2.39. <a name='fastmod:Afastpartialreplacementforthecodemodtoolreplaceandreplaceallinthewholecodebase.'></a>fastmod:   A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
```sh
  fastmod

  A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
  Regexes are matched by Rust regex crate.
  More information: https://github.com/facebookincubator/fastmod.

  - Replace a regex pattern in all files of the current directory, ignoring files on .ignore and .gitignore:
    fastmod regex_pattern replacement

  - Replace a regex pattern in case-insensitive mode in specific files or directories:
    fastmod --ignore-case regex_pattern replacement -- path/to/file path/to/directory ...

  - Replace a regex pattern in a specific directory in files filtered with a case-insensitive glob pattern:
    fastmod regex replacement --dir path/to/directory --iglob '**/*.{js,json}'

  - Replace for an exact string in .js or JSON files:
    fastmod --fixed-strings exact_string replacement --extensions json,js

  - Replace for an exact string without prompt for a confirmation (disables regular expressions):
    fastmod --accept-all --fixed-strings exact_string replacement

  - Replace for an exact string without prompt for a confirmation, printing changed files:
    fastmod --accept-all --print-changed-files --fixed-strings exact_string replacement
```

---

###  2.40. <a name='zellij:Terminalmultiplexerwithbatteriesincluded.'></a>zellij:   Terminal multiplexer with batteries included.
```sh
  zellij

  Terminal multiplexer with batteries included.
  See also tmux and screen.
  More information: https://zellij.dev/documentation/.

  - Start a new named session:
    zellij --session name

  - List existing sessions:
    zellij list-sessions

  - Attach to the most recently used session:
    zellij attach

  - Open a new pane (inside a zellij session):
    <Alt> + N

  - Detach from the current session (inside a zellij session):
    <Ctrl> + O, D
```
