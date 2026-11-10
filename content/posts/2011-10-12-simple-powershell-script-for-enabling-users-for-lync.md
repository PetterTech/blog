---
title: Simple powershell script for enabling users for Lync
date: 2011-10-12T15:59:45+00:00
url: /index.php/2011/10/12/simple-powershell-script-for-enabling-users-for-lync/
categories:
  - Lync
  - Microsoft
  - Powershell
tags:
  - Lync
  - microsoft
  - Powershell
---
I wrote this simple little script for enabling users for Lync. It asks for input on name, sipdomain and line uri. The rest is set using variables defined at the start of the script.  
If you only have one sipdomain you can change the script so that it doesn't ask for it.

Here's the script in all its glory:

 ```powershell
$UI = (Get-Host).UI.RawUI
$UI.WindowTitle = "Enable lync user"
Import-Module Lync

#Setting some variables
$registrarpool = lyncpool.test.local
$csdialplan = DialPlanSIPtrunk
$csvoicepolicy = "SIP Trunk Service"
$csconferencingpolicy = Conference

#Ask for the rest of the information
$name = Read-Host "Who do you want to Lync enable?"
$sipdomain = Read-Host "Enter SIP domain"
$lineuri = Read-Host "Enter line uri"

Write-Host "Working..."

#Enabling the user for Lync
enable-csuser -identity $name -RegistrarPool $registrarpool -SipAddressType UserPrincipalName -SipDomain $sipdomain

#Sleep for a few seconds (otherwise the next command might fail)
Start-Sleep -s 3

#Setting settings on the user
set-csuser -identity $name -EnterpriseVoiceEnabled $True -LineUri $lineuri
Grant-CsDialPlan –Identity $name -PolicyName $csdialplan
Grant-CsVoicePolicy –Identity $name –PolicyName $csvoicepolicy
Grant-CsConferencingPolicy -identity $name -PolicyName $csconferencingpolicy

#Show the result
get-csuser -identity $name

Write-Host "Press any key to quit"

cmd /c pause | out-null 
```

You can also download it here:  {{< unavailable "File no longer available" >}}