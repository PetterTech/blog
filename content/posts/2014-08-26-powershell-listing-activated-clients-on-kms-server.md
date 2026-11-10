---
title: 'Powershell: Listing activated clients on KMS server'
date: 2014-08-26T07:14:29+00:00
url: /index.php/2014/08/26/powershell-listing-activated-clients-on-kms-server/
categories:
  - Microsoft
  - Powershell
tags:
  - get-eventlog
  - KMS
  - Powershell
---
If you are using a KMS server for activating servers and clients in your environment, you may have noticed that there's really no obvious way to get a list of all the clients that have been activated by the KMS server.

One way to get that overview is by using VAMT (<http://technet.microsoft.com/en-us/library/hh824953.aspx>), but since that tool is based on pulling info from clients and not from the KMS server it is not suitable for everyone.

Thankfully, there's PowerShell 🙂  
Getting a list of all activated KMS clients through PowerShell is actually a simple one-liner:

 ```powershell
$(foreach ($entry in (Get-EventLog -Logname "Key Management Service")) {$entry.ReplacementStrings[3]}) | sort-object -Unique 
```

What this does is look through the Key Management Service eventlog, grab only the client name and then remove all duplicates (since a client activates itself at regular intervals, there will be duplicates).