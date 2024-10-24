# Install Chocolatey (Package Manager for Windows)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install VirtualBox
choco install virtualbox -y

# Download Ubuntu Server ISO
$ubuntuIsoUrl = "https://releases.ubuntu.com/20.04.3/ubuntu-20.04.3-live-server-amd64.iso"
$ubuntuIsoPath = "C:\ubuntu-20.04.3-live-server-amd64.iso"
Invoke-WebRequest -Uri $ubuntuIsoUrl -OutFile $ubuntuIsoPath

# Install Ubuntu Server in VirtualBox
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "createvm --name 'Ubuntu Server' --ostype Ubuntu_64 --register"
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "modifyvm 'Ubuntu Server' --memory 2048 --vram 128 --cpus 2 --nic1 nat"
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "storagectl 'Ubuntu Server' --name 'SATA Controller' --add sata --controller IntelAHCI"
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "storageattach 'Ubuntu Server' --storagectl 'SATA Controller' --port 0 --device 0 --type hdd --medium $ubuntuIsoPath"
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "modifyvm 'Ubuntu Server' --boot1 dvd --boot2 disk --boot3 none --boot4 none"
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "startvm 'Ubuntu Server'"

# Wait for Ubuntu Server installation to complete
Write-Host "Please follow the Ubuntu Server installation process in VirtualBox."
Write-Host "Once installation is complete, shut down the VM and press any key to continue..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')

# Start Ubuntu Server VM
Start-Process "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" -ArgumentList "startvm 'Ubuntu Server'"

# Script ends
Write-Host "MaaS demonstration environment setup complete."
