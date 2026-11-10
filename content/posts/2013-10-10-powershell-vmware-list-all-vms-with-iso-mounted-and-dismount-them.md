---
title: "PowerCLI: List all vm's with ISO mounted and dismount them"
date: 2013-10-10T12:46:48+00:00
url: /index.php/2013/10/10/powershell-vmware-list-all-vms-with-iso-mounted-and-dismount-them/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - dismount iso
  - get-vm
  - powercli
  - Powershell
  - set-cddrive
  - vmware
---
Easy-peasy and a pretty short post&#8230;

To get all vm's with iso mounted:

 ```powershell
Get-VM | Get-CDDrive | select @{N="VM";E="Parent"},IsoPath | where {$_.IsoPath -ne $null} 
```

Then, to dismount those:

 ```powershell
Get-VM | Get-CDDrive | where {$_.IsoPath -ne $null} | Set-CDDrive -NoMedia -Confirm:$False 
```