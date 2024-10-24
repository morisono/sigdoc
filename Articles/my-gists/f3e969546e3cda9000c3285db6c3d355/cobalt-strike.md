https://book.hacktricks.xyz/v/jp/c2/cobalt-strike

```
# Linux (Kali 2018.4, Ubuntu 18.04)
## 1. Update APT:
sudo apt-get update
## 2. Install OpenJDK 11 with APT:
sudo apt-get install openjdk-11-jdk
## 3. Make OpenJDK 11 the default:
sudo update-java-alternatives -s java-1.11.0-openjdk-amd64

#Linux (Other)
## 1. Uninstall the current OpenJDK package(s).
## 2. Download OpenJDK for Linux/x64 at: https://jdk.java.net/archive/.
## 3. Extract the OpenJDK binary:
tar zxvf openjdk-11.0.1_linux-x64_bin.tar.gz
## 4. Move the OpenJDK folder to /usr/local:
Cobalt Strike Installation Guide www.fortra.com page: 4
Before You Begin / Installing OpenJDK
mv jdk-11.0.1 /usr/local
## 5. Add the following to ~/.bashrc:
JAVA_HOME="/usr/local/jdk-11.0.1"
PATH=$PATH:$JAVA_HOME/bin
## 6. Refresh your ~/.bashrc to make the new environment variables take effect:
source ~/.bashrc

a. For Linux:
i. Extract the cobaltstrike-dist.tgz:
tar zxvf cobaltstrike-dist.tgz
b. For MacOS X:
i. Double-click the cobaltstrike-dist.dmg file to mount it.
ii. Drag the Cobalt Strike folder to the Applications folder.
c. For Windows:
i. Disable anti-virus before you install Cobalt Strike.
ii. Use your preferred zip tool to extract the cobaltstike.zip file to an install
location.
```
- https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/cobalt-strike-install.pdf