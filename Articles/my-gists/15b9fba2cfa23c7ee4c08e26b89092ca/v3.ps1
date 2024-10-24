# Variables
$vmName = "MaaS-VM"
$isoPath = "C:\path\to\ubuntu.iso"
$vhdPath = "C:\path\to\VHDs\MaaS-VM.vhdx"
$memorySize = 4GB
$vmSwitch = "Default Switch"

# Create a new virtual machine
New-VM -Name $vmName -MemoryStartupBytes $memorySize -VHDPath $vhdPath -SwitchName $vmSwitch

# Set the VM to boot from the ISO
Set-VMFirmware -VMName $vmName -FirstBootDevice $(Get-VMDvdDrive -VMName $vmName)

# Add DVD drive and mount the ISO
Add-VMDvdDrive -VMName $vmName -Path $isoPath

# Start the VM
Start-VM -Name $vmName

# Wait for user to install the OS manually, then proceed

# Install necessary tools on the VM
Invoke-Command -VMName $vmName -ScriptBlock {
    sudo apt update
    sudo apt install -y curl git docker.io
    sudo systemctl enable docker
    sudo systemctl start docker

    # Install MaaS
    sudo snap install maas --channel=2.9/stable
    sudo maas init
}

# Print the status
Write-Output "MaaS environment setup is complete. Please configure MaaS through the web UI."
