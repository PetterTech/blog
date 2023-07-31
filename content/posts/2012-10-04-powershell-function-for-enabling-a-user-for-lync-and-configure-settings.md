---
title: Powershell function for enabling a user for Lync and configure settings
author: nerenther
 
date: 2012-10-04T12:07:10+00:00
url: /index.php/2012/10/04/powershell-function-for-enabling-a-user-for-lync-and-configure-settings/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:11101:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #0000FF;">function</span> Enable<span style="color: pink;">-</span>LyncUser <span style="color: #000000;">&#123;</span>
    <span style="color: #000000;">&#91;</span>CmdletBinding<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#93;</span>
     <span style="color: #0000FF;">Param</span> <span style="color: #000000;">&#40;</span>
     <span style="color: #000000;">&#91;</span>parameter<span style="color: #000000;">&#40;</span>Mandatory<span style="color: pink;">=</span><span style="color: #800080;">$True</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#91;</span><span style="color: #008080;">string</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$Identity</span><span style="color: pink;">,</span>
     <span style="color: #000000;">&#91;</span><span style="color: #008080;">string</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$Pool</span> <span style="color: pink;">=</span> <span style="color: #800000;">'lyncpool1.test.local'</span><span style="color: pink;">,</span>
     <span style="color: #000000;">&#91;</span><span style="color: #008080;">string</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$DialPlan</span> <span style="color: pink;">=</span> <span style="color: #800000;">'DialPlanSIPtrunk'</span><span style="color: pink;">,</span>
     <span style="color: #000000;">&#91;</span><span style="color: #008080;">string</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$Voice</span> <span style="color: pink;">=</span> <span style="color: #800000;">'SIP Trunk Service'</span><span style="color: pink;">,</span>
     <span style="color: #000000;">&#91;</span><span style="color: #008080;">string</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$Conference</span> <span style="color: pink;">=</span> <span style="color: #800000;">'Conference'</span><span style="color: pink;">,</span>
     <span style="color: #000000;">&#91;</span><span style="color: #008080;">string</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$LineURI</span>
     <span style="color: #000000;">&#41;</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Enabling user...&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Importing the Lync PowerShell module</span>
    Import<span style="color: pink;">-</span>Module Lync
    &nbsp;
    <span style="color: #008000;">#Trying to enable the user for Lync</span>
    try <span style="color: #000000;">&#123;</span>
     Enable<span style="color: pink;">-</span>CsUser <span style="color: pink;">-</span>identity <span style="color: #800080;">$Identity</span> <span style="color: pink;">-</span>RegistrarPool <span style="color: #800080;">$Pool</span> <span style="color: pink;">-</span>SipAddressType emailaddress
     <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Catching errors, aborting if the user is not found</span>
    catch <span style="color: #000000;">&#91;</span>Microsoft.Rtc.Management.AD.ManagementException<span style="color: #000000;">&#93;</span> <span style="color: #000000;">&#123;</span>
     <span style="color: #0000FF;">throw</span> <span style="color: #800000;">&quot;User not found, check username&quot;</span>
     <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Sleeping, so that the next command doesn't fail</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Sleeping... Please wait...&quot;</span>
    <span style="color: #008080; font-weight: bold;">Start-Sleep</span> <span style="color: pink;">-</span>s <span style="color: #804000;">4</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Configuring user...&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Setting the user as EnterpriseVoice enabled</span>
    Set<span style="color: pink;">-</span>CsUser <span style="color: pink;">-</span>identity <span style="color: #800080;">$Identity</span> <span style="color: pink;">-</span>EnterpriseVoiceEnabled <span style="color: #800080;">$True</span>
    <span style="color: #008000;">#Setting dial plan</span>
    Grant<span style="color: pink;">-</span>CsDialPlan –Identity <span style="color: #800080;">$Identity</span> <span style="color: pink;">-</span>PolicyName <span style="color: #800080;">$DialPlan</span>
    <span style="color: #008000;">#Setting voice policy</span>
    Grant<span style="color: pink;">-</span>CsVoicePolicy –Identity <span style="color: #800080;">$Identity</span> –PolicyName <span style="color: #800080;">$Voice</span>
    <span style="color: #008000;">#Setting conferenceing policy</span>
    Grant<span style="color: pink;">-</span>CsConferencingPolicy <span style="color: pink;">-</span>identity <span style="color: #800080;">$Identity</span> <span style="color: pink;">-</span>PolicyName <span style="color: #800080;">$Conference</span>
    &nbsp;
    <span style="color: #008000;">#Trying to set the optional Line URI</span>
    try <span style="color: #000000;">&#123;</span>
     Set<span style="color: pink;">-</span>CsUser <span style="color: pink;">-</span>identity <span style="color: #800080;">$Identity</span> <span style="color: pink;">-</span>LineUri <span style="color: #800080;">$LineURI</span>
     <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Cathing errors and continuing</span>
    catch <span style="color: #000000;">&#91;</span>System.FormatException<span style="color: #000000;">&#93;</span> <span style="color: #000000;">&#123;</span>
     <span style="color: #008080; font-weight: bold;">Write-Error</span> <span style="color: #008080; font-style: italic;">-Message</span> <span style="color: #800000;">&quot;Wrong format on LineURI, it should be tel:+xxxxxxxx.&quot;</span> <span style="color: #008080; font-style: italic;">-Category</span> SyntaxError
     <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Config finished&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Grabbing the Lync login for the user and writing it to the host</span>
    <span style="color: #800080;">$SipAddress</span> <span style="color: pink;">=</span> Get<span style="color: pink;">-</span>CsUser <span style="color: pink;">-</span>Identity <span style="color: #800080;">$Identity</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Select-Object</span> SipAddress
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;The user may now log in to Lync as $($SipAddress.SipAddress.substring(4))&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> Green
    &nbsp;
    <span style="color: #008000;">&lt;#
     .Synopsis
      Enables given user for Lync and sets config
     .Description
      The function will enable the user for Lync and add the given config, if no config is given the default values will be used.
     .Parameter Identity
      The user who you want to enable for Lync
     .Parameter Pool
      The Lync pool you want to assign a user to. Default is lyncpool1.test.local
     .Parameter DialPlan
      The dialplan you want to associate the user with. Default is DialPlanSIPtrunk
     .Parameter Voice
      The voice policy you want to associate the user with. Default is SIP Trunk Service
     .Parameter Conference
      The conference policy you want to associate the user with. Default is Conference
     .Parameter LineURI
      If you want to specify a Line URI, do so in the format of tel:&lt;number&gt;
     .Example
      Enable-LyncUser user1
      This will enable user1 with default settings
     .Example
      Enable-Lyncuser user2 -LineURI tel:+4712345678
      This will enable user2 and set the lineuri to tel:+4712345678
     .Link
      http://cloud.kemta.net
     #&gt;</span>
    <span style="color: #000000;">&#125;</span> ```</td></tr></table><p class="theCode" style="display:none;">function Enable-LyncUser {
    [CmdletBinding()]
     Param (
     [parameter(Mandatory=$True)][string]$Identity,
     [string]$Pool = 'lyncpool1.test.local',
     [string]$DialPlan = 'DialPlanSIPtrunk',
     [string]$Voice = 'SIP Trunk Service',
     [string]$Conference = 'Conference',
     [string]$LineURI
     )
    
    Write-Host &quot;Enabling user...&quot;
    
    #Importing the Lync PowerShell module
    Import-Module Lync
    
    #Trying to enable the user for Lync
    try {
     Enable-CsUser -identity $Identity -RegistrarPool $Pool -SipAddressType emailaddress
     }
    
    #Catching errors, aborting if the user is not found
    catch [Microsoft.Rtc.Management.AD.ManagementException] {
     throw &quot;User not found, check username&quot;
     }
    
    #Sleeping, so that the next command doesn't fail
    Write-Host &quot;Sleeping... Please wait...&quot;
    Start-Sleep -s 4
    
    Write-Host &quot;Configuring user...&quot;
    
    #Setting the user as EnterpriseVoice enabled
    Set-CsUser -identity $Identity -EnterpriseVoiceEnabled $True
    #Setting dial plan
    Grant-CsDialPlan –Identity $Identity -PolicyName $DialPlan
    #Setting voice policy
    Grant-CsVoicePolicy –Identity $Identity –PolicyName $Voice
    #Setting conferenceing policy
    Grant-CsConferencingPolicy -identity $Identity -PolicyName $Conference
    
    #Trying to set the optional Line URI
    try {
     Set-CsUser -identity $Identity -LineUri $LineURI
     }
    
    #Cathing errors and continuing
    catch [System.FormatException] {
     Write-Error -Message &quot;Wrong format on LineURI, it should be tel:+xxxxxxxx.&quot; -Category SyntaxError
     }
    
    Write-Host &quot;Config finished&quot;
    
    #Grabbing the Lync login for the user and writing it to the host
    $SipAddress = Get-CsUser -Identity $Identity | Select-Object SipAddress
    Write-Host &quot;The user may now log in to Lync as $($SipAddress.SipAddress.substring(4))&quot; -ForegroundColor Green
    
    &lt;#
     .Synopsis
      Enables given user for Lync and sets config
     .Description
      The function will enable the user for Lync and add the given config, if no config is given the default values will be used.
     .Parameter Identity
      The user who you want to enable for Lync
     .Parameter Pool
      The Lync pool you want to assign a user to. Default is lyncpool1.test.local
     .Parameter DialPlan
      The dialplan you want to associate the user with. Default is DialPlanSIPtrunk
     .Parameter Voice
      The voice policy you want to associate the user with. Default is SIP Trunk Service
     .Parameter Conference
      The conference policy you want to associate the user with. Default is Conference
     .Parameter LineURI
      If you want to specify a Line URI, do so in the format of tel:&lt;number&gt;
     .Example
      Enable-LyncUser user1
      This will enable user1 with default settings
     .Example
      Enable-Lyncuser user2 -LineURI tel:+4712345678
      This will enable user2 and set the lineuri to tel:+4712345678
     .Link
      http://cloud.kemta.net
     #&gt;
    }</p></div>
    ";}
categories:
  - Lync
  - Microsoft
  - Powershell
tags:
  - catch
  - Enable-LyncUser
  - error handling
  - function
  - Lync
  - microsoft
  - Powershell
  - throw

---
A little while ago I posted a script for enabling users for Lync and settings some settings for that user. That script has been used here ever since I posted it and it has worked like a charm. However there&#8217;s always room for improvement, right?.

So I have made a function out of it and for the first time (I think) I have even implemented some error handling. The function is also improved quit a bit on the help section and the info that is shown to the user after the function completes.

As in the script, this function will enable the user for Lync and set some default settings like Dial Plan, Voice Policy, Conferencing Policy. It also gives you the option to specify a Line URI.  
The difference is that this function will use the default settings only if nothing else is specified, so you can change the settings if you like, using parameters. Of course theres also the possibility to pipe input from a csv file.

Here&#8217;s the code:

```
function Enable-LyncUser {
[CmdletBinding()]
 Param (
 [parameter(Mandatory=$True)][string]$Identity,
 [string]$Pool = 'lyncpool1.test.local',
 [string]$DialPlan = 'DialPlanSIPtrunk',
 [string]$Voice = 'SIP Trunk Service',
 [string]$Conference = 'Conference',
 [string]$LineURI
 )

Write-Host "Enabling user..."

#Importing the Lync PowerShell module
Import-Module Lync

#Trying to enable the user for Lync
try {
 Enable-CsUser -identity $Identity -RegistrarPool $Pool -SipAddressType emailaddress
 }

#Catching errors, aborting if the user is not found
catch [Microsoft.Rtc.Management.AD.ManagementException] {
 throw "User not found, check username"
 }

#Sleeping, so that the next command doesn't fail
Write-Host "Sleeping... Please wait..."
Start-Sleep -s 4

Write-Host "Configuring user..."

#Setting the user as EnterpriseVoice enabled
Set-CsUser -identity $Identity -EnterpriseVoiceEnabled $True
#Setting dial plan
Grant-CsDialPlan –Identity $Identity -PolicyName $DialPlan
#Setting voice policy
Grant-CsVoicePolicy –Identity $Identity –PolicyName $Voice
#Setting conferenceing policy
Grant-CsConferencingPolicy -identity $Identity -PolicyName $Conference

#Trying to set the optional Line URI
try {
 Set-CsUser -identity $Identity -LineUri $LineURI
 }

#Cathing errors and continuing
catch [System.FormatException] {
 Write-Error -Message "Wrong format on LineURI, it should be tel:+xxxxxxxx." -Category SyntaxError
 }

Write-Host "Config finished"

#Grabbing the Lync login for the user and writing it to the host
$SipAddress = Get-CsUser -Identity $Identity | Select-Object SipAddress
Write-Host "The user may now log in to Lync as $($SipAddress.SipAddress.substring(4))" -ForegroundColor Green

&lt;#
 .Synopsis
  Enables given user for Lync and sets config
 .Description
  The function will enable the user for Lync and add the given config, if no config is given the default values will be used.
 .Parameter Identity
  The user who you want to enable for Lync
 .Parameter Pool
  The Lync pool you want to assign a user to. Default is lyncpool1.test.local
 .Parameter DialPlan
  The dialplan you want to associate the user with. Default is DialPlanSIPtrunk
 .Parameter Voice
  The voice policy you want to associate the user with. Default is SIP Trunk Service
 .Parameter Conference
  The conference policy you want to associate the user with. Default is Conference
 .Parameter LineURI
  If you want to specify a Line URI, do so in the format of tel:&lt;number>
 .Example
  Enable-LyncUser user1
  This will enable user1 with default settings
 .Example
  Enable-Lyncuser user2 -LineURI tel:+4712345678
  This will enable user2 and set the lineuri to tel:+4712345678
 .Link
  http://cloud.kemta.net
 #>
} 
```

&nbsp;

You may wonder why the Start-Sleep command is there. The reason is that my testing indicated that the function will work to fast for Active Directory if it isn&#8217;t there. During my testing I found that without the sleep the next command, Set-CsUser, will fail because the object cannot be found. Running the function again resultet in no errors.  
Therefore I tested adding a few seconds of sleep to prevent the Set-CsUser command (and the following commands) from failing. Depending on you environment you can decrease the seconds or even remove the sleep, but I found that 3 seconds was just a bit to short (sometimes it would fail, sometimes not) so I ended up with 4.

I am kinda proud of the error handling in this function, given that I have never used error handling in Powershell before. But please let me know if there are improvements to be made or errors in my code.