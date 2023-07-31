---
title: Simple powershell script for enabling users for Lync
author: nerenther
 
date: 2011-10-12T15:59:45+00:00
url: /index.php/2011/10/12/simple-powershell-script-for-enabling-users-for-lync/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:5454:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$UI</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-Host</span><span style="color: #000000;">&#41;</span>.UI.RawUI
    <span style="color: #800080;">$UI</span>.WindowTitle <span style="color: pink;">=</span> <span style="color: #800000;">&quot;Enable lync user&quot;</span>
    Import<span style="color: pink;">-</span>Module Lync
    &nbsp;
    <span style="color: #008000;">#Setting some variables</span>
    <span style="color: #800080;">$registrarpool</span> <span style="color: pink;">=</span> lyncpool.test.local
    <span style="color: #800080;">$csdialplan</span> <span style="color: pink;">=</span> DialPlanSIPtrunk
    <span style="color: #800080;">$csvoicepolicy</span> <span style="color: pink;">=</span> <span style="color: #800000;">&quot;SIP Trunk Service&quot;</span>
    <span style="color: #800080;">$csconferencingpolicy</span> <span style="color: pink;">=</span> Conference
    &nbsp;
    <span style="color: #008000;">#Ask for the rest of the information</span>
    <span style="color: #800080;">$name</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Read-Host</span> <span style="color: #800000;">&quot;Who do you want to Lync enable?&quot;</span>
    <span style="color: #800080;">$sipdomain</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Read-Host</span> <span style="color: #800000;">&quot;Enter SIP domain&quot;</span>
    <span style="color: #800080;">$lineuri</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Read-Host</span> <span style="color: #800000;">&quot;Enter line uri&quot;</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Working...&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Enabling the user for Lync</span>
    enable<span style="color: pink;">-</span>csuser <span style="color: pink;">-</span>identity <span style="color: #800080;">$name</span> <span style="color: pink;">-</span>RegistrarPool <span style="color: #800080;">$registrarpool</span> <span style="color: pink;">-</span>SipAddressType UserPrincipalName <span style="color: pink;">-</span>SipDomain <span style="color: #800080;">$sipdomain</span>
    &nbsp;
    <span style="color: #008000;">#Sleep for a few seconds (otherwise the next command might fail)</span>
    <span style="color: #008080; font-weight: bold;">Start-Sleep</span> <span style="color: pink;">-</span>s <span style="color: #804000;">3</span>
    &nbsp;
    <span style="color: #008000;">#Setting settings on the user</span>
    set<span style="color: pink;">-</span>csuser <span style="color: pink;">-</span>identity <span style="color: #800080;">$name</span> <span style="color: pink;">-</span>EnterpriseVoiceEnabled <span style="color: #800080;">$True</span> <span style="color: pink;">-</span>LineUri <span style="color: #800080;">$lineuri</span>
    Grant<span style="color: pink;">-</span>CsDialPlan –Identity <span style="color: #800080;">$name</span> <span style="color: pink;">-</span>PolicyName <span style="color: #800080;">$csdialplan</span>
    Grant<span style="color: pink;">-</span>CsVoicePolicy –Identity <span style="color: #800080;">$name</span> –PolicyName <span style="color: #800080;">$csvoicepolicy</span>
    Grant<span style="color: pink;">-</span>CsConferencingPolicy <span style="color: pink;">-</span>identity <span style="color: #800080;">$name</span> <span style="color: pink;">-</span>PolicyName <span style="color: #800080;">$csconferencingpolicy</span>
    &nbsp;
    <span style="color: #008000;">#Show the result</span>
    get<span style="color: pink;">-</span>csuser <span style="color: pink;">-</span>identity <span style="color: #800080;">$name</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Press any key to quit&quot;</span>
    &nbsp;
    cmd <span style="color: pink;">/</span>c pause <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out-null</span> ```</td></tr></table><p class="theCode" style="display:none;">$UI = (Get-Host).UI.RawUI
    $UI.WindowTitle = &quot;Enable lync user&quot;
    Import-Module Lync
    
    #Setting some variables
    $registrarpool = lyncpool.test.local
    $csdialplan = DialPlanSIPtrunk
    $csvoicepolicy = &quot;SIP Trunk Service&quot;
    $csconferencingpolicy = Conference
    
    #Ask for the rest of the information
    $name = Read-Host &quot;Who do you want to Lync enable?&quot;
    $sipdomain = Read-Host &quot;Enter SIP domain&quot;
    $lineuri = Read-Host &quot;Enter line uri&quot;
    
    Write-Host &quot;Working...&quot;
    
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
    
    Write-Host &quot;Press any key to quit&quot;
    
    cmd /c pause | out-null</p></div>
    ";}
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

 ```
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

You can also download it here:  <a title="http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/enable_lync_user.ps1" href="http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/enable_lync_user.ps1" target="_blank" rel="noopener">http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/enable_lync_user.ps1</a>