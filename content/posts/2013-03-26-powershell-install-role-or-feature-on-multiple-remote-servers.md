---
title: 'Powershell: Install role or feature on multiple remote servers'
date: 2013-03-26T12:48:09+00:00
url: /index.php/2013/03/26/powershell-install-role-or-feature-on-multiple-remote-servers/
categories:
  - Microsoft
  - Powershell
tags:
  - Powershell
  - Server Manager
  - Windows Server
---
Today I was presented with a task that sounded pretty boring and repetitive: Install the Windows Search service on all our citrix servers.

Now, I could just log on each and every one of our citrix servers, open Server Manager and then install the role service but where's the fun in that?

As always Powershell is a lot more fun:

First I had to find the name of all our citrix servers. Luckily we have a strict naming convention so I could just poll Active Directory and store the names in an array:

 ```powershell
$servers = Get-ADComputer -Filter 'Name -like "ctx_srv*"' | select name 
```

Next I only had to create a foreach loop that enters a PSSession on each of the servers and install the role service:

 ```powershell
 $servers | ForEach-Object {
 Enter-PSSession -ComputerName $_.name
 import-module servermanager
 Add-WindowsFeature FS-Search-Service
 Exit-PSSession
 } 
 ```

It is worth mentioning that you can't connect to remote servers using the Enter-PSSession cmdlet if you haven't enabled remote management, if you want to enable it you can check this guide: <http://blog.powershell.no/2010/03/04/enable-and-configure-windows-powershell-remoting-using-group-policy/>