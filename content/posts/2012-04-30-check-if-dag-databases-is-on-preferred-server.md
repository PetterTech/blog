---
title: Check if DAG databases is on preferred server
author: nerenther
 
date: 2012-04-30T10:35:57+00:00
url: /index.php/2012/04/30/check-if-dag-databases-is-on-preferred-server/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:4014:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008000;">#Add the needed exchange snapin</span>
    <span style="color: #008080; font-weight: bold;">add-pssnapin</span> Microsoft.Exchange.Management.PowerShell.E2010
    &nbsp;
    <span style="color: #008000;">#Navigate to the exchange script repository</span>
    <span style="color: #008080; font-weight: bold;">cd</span> <span style="color: #800000;">&quot;C:Program FilesMicrosoftExchange ServerV14Scripts&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Gather info on how many databases is on a less preferred server</span>
    <span style="color: #800080;">$result</span> <span style="color: pink;">=</span> .RedistributeActiveDatabases.ps1 <span style="color: pink;">-</span>dagname dag01 <span style="color: pink;">-</span>ShowDatabaseCurrentActives
    &nbsp;
    <span style="color: #008000;">#Turn the results into a number</span>
    <span style="color: #800080;">$count</span> <span style="color: pink;">=</span> <span style="color: #800080;">$result</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Select-Object</span> IsOnMostPreferredCopy <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Select-String</span> False <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Measure-Object</span>
    &nbsp;
    <span style="color: #008000;">#Turn the number into a format that fits nicely into the mail (only for looks :))</span>
    <span style="color: #800080;">$body</span> <span style="color: pink;">=</span> <span style="color: #800080;">$count</span>.count <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out-string</span>
    &nbsp;
    <span style="color: #008000;">#Sends mail if there is databases that are mounted on less preferred server</span>
    <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$count</span>.Count <span style="color: #FF0000;">-gt</span> <span style="color: #804000;">0</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>send<span style="color: pink;">-</span>mailmessage <span style="color: pink;">-</span>smtpserver <span style="color: #800000;">'hub transport server'</span> <span style="color: pink;">-</span>to some<span style="color: pink;">@</span>recipient.com<span style="color: pink;">,</span>some.other<span style="color: pink;">@</span>recipient <span style="color: pink;">-</span>from some<span style="color: pink;">@</span>mailaddress.com <span style="color: pink;">-</span>subject <span style="color: #800000;">&quot;DAG unbalanced&quot;</span> <span style="color: #008080; font-style: italic;">-Body</span> <span style="color: #800000;">&quot;The following number of databases is not on their prefered server: $body&quot;</span><span style="color: #000000;">&#125;</span> ```</td></tr></table><p class="theCode" style="display:none;">#Add the needed exchange snapin
    add-pssnapin Microsoft.Exchange.Management.PowerShell.E2010
    
    #Navigate to the exchange script repository
    cd &quot;C:Program FilesMicrosoftExchange ServerV14Scripts&quot;
    
    #Gather info on how many databases is on a less preferred server
    $result = .RedistributeActiveDatabases.ps1 -dagname dag01 -ShowDatabaseCurrentActives
    
    #Turn the results into a number
    $count = $result | Select-Object IsOnMostPreferredCopy | Select-String False | Measure-Object
    
    #Turn the number into a format that fits nicely into the mail (only for looks :))
    $body = $count.count | out-string
    
    #Sends mail if there is databases that are mounted on less preferred server
    if ($count.Count -gt 0)
    {send-mailmessage -smtpserver 'hub transport server' -to some@recipient.com,some.other@recipient -from some@mailaddress.com -subject &quot;DAG unbalanced&quot; -Body &quot;The following number of databases is not on their prefered server: $body&quot;}</p></div>
    ";}
categories:
  - Exchange
  - Microsoft
  - Powershell
tags:
  - DAG
  - Exchange
  - microsoft
  - Powershell

---
If you are using DAG in exchange 2010 for high availability on your mailboxes there may be one thing you might have noticed, the databases can fail over to a less preferred server at any time without you noticing.  
Microsoft have provided you with a script for balancing these databases, RedistributeActiveDatabases.ps1. With this script you can activate the databases on their preferred server again. But how do you know when they have failed over?

That has been an issue for us for some time now. None of our monitoring solutions were able to detect this, so I decided to write a simple powershell script for this.

The script uses the RedistributeActiveDatabases.ps1 script to check how many, if any, databases is mounted on a less preferred server. If more than 0 databases is mounted on a less preferred server it sends a mail to a given mail address with how many databases is on a less preferred server.

We run this script as a scheduled task on one of our hub transport servers, but you can run it on any server/computer that has exchange management tools installed. It has really helped us so far, so heres the script:

 ```
#Add the needed exchange snapin
add-pssnapin Microsoft.Exchange.Management.PowerShell.E2010

#Navigate to the exchange script repository
cd "C:Program FilesMicrosoftExchange ServerV14Scripts"

#Gather info on how many databases is on a less preferred server
$result = .RedistributeActiveDatabases.ps1 -dagname dag01 -ShowDatabaseCurrentActives

#Turn the results into a number
$count = $result | Select-Object IsOnMostPreferredCopy | Select-String False | Measure-Object

#Turn the number into a format that fits nicely into the mail (only for looks :))
$body = $count.count | out-string

#Sends mail if there is databases that are mounted on less preferred server
if ($count.Count -gt 0)
{send-mailmessage -smtpserver 'hub transport server' -to some@recipient.com,some.other@recipient -from some@mailaddress.com -subject "DAG unbalanced" -Body "The following number of databases is not on their prefered server: $body"} 
```