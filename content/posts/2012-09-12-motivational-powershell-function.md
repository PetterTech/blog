---
title: Motivational Powershell function
author: nerenther
 
date: 2012-09-12T11:06:18+00:00
url: /index.php/2012/09/12/motivational-powershell-function/
categories:
  - Microsoft
  - Powershell
tags:
  - function
  - Motivate-Me
  - Powershell

---
If you are ever in need of some motivation, here is a very simple Powershell function for that:

 ```
function Motivate-Me
 {
 $motivator = Get-Random -Minimum 1 -Maximum 5
 if ($motivator -eq 1)
 {Write-Host "You are a Powershell God!"}
 if ($motivator -eq 2)
 {Write-Host "You rule dude!"}
 if ($motivator -eq 3)
 {Write-Host "I wish I could errorhandle like you"}
 if ($motivator -eq 4)
 {Write-Host "I am nothing compared to you"}
 if ($motivator -eq 5)
 {Write-Host "Are you sure you intirely human? 'cause you seem to cool to be real"}
 &lt;#
 .Synopsis
 Show som motivational words on the screen
 .Description
 This function will print some motivational words on the screen
 .Example
 Motivate-Me
 Show som motivational words on the screen
 .Link
 http://cloud.kemta.net
 #>
 } 
```

Now all you need to do is write Motivate-Me in the powershell window to receive some inspirational words 🙂