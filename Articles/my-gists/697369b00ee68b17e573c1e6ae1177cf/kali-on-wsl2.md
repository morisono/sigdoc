# Kali on WSL2 Settiing UP

### Install
```pwsh
wsl --install -d kali-linux
wsl -d kali-linux kex --wtstart -s -m
```

### Setting up
```sh
# Download Tools
cat /etc/apt/sources.list
sudo nano /etc/apt/sources.list # Remove sharp to added `deb-src`
---

deb http://http.kali.org/kali kali-rolling main non-free contrib
#deb-src http://http.kali.org/kali kali-rolling main non-free contrib  <-
```

```sh
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y kali-linux-large

sudo apt install kali-win-kex -y
sudo kex --win -s -m
sudo kex --esm -s -ip

cat /etc/os-release

sudo apt install openssh-server

localectl set-locale "LANG=ja_JP.UTF-8"
timedatectl set-timezone Asia/Tokyo
# apt install task-japanese task-japanese-desktop
reboot

kex --win -m -s

```

### HTB Academy
```sh
# Save file to \\wsl.localhost\kali-linux\home\<username>

sudo openvpn academy-regular.ovpn
```

  - https://academy.hackthebox.com/course/preview/linux-fundamentals

### Connect
```sh
ssh [username]@[IP address]

# Machine hardware name
uname -m

# Shell for htb-student user
getent passwd htb-student | cut -d: -f7

# Network interface with MTU 1500
ip link show | awk '/mtu 1500/ {print $2}' | tr -d ':'
```

