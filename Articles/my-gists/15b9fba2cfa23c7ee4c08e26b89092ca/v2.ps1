# Define variables
$virtualMachineName = "MaaS-VM"
$virtualDiskPath = "C:\Path\To\Virtual\Disk"
$virtualDiskSizeGB = 50
$networkAdapterName = "Ethernet"
$isoImagePath = "C:\Path\To\ISO\ubuntu.iso"

# Create a new virtual machine
New-VM -Name $virtualMachineName -MemoryStartupBytes 4GB -BootDevice CD -SwitchName $networkAdapterName -Path $virtualDiskPath

# Set the size of the virtual disk
Set-VHD -Path "$virtualDiskPath\$virtualMachineName.vhdx" -SizeBytes $virtualDiskSizeGBGB

# Attach ISO image to the virtual machine
Add-VMDvdDrive -VMName $virtualMachineName -Path $isoImagePath

# Start the virtual machine
Start-VM -Name $virtualMachineName

# Wait for the VM to start and grab its IP address
Start-Sleep -Seconds 60 # Adjust sleep time as needed
$vmIPAddress = (Get-VMNetworkAdapter -VMName $virtualMachineName).IPAddresses | Where-Object {$_ -like "192.168.*"}

# Display the IP address
Write-Host "The IP address of the virtual machine is: $vmIPAddress"
