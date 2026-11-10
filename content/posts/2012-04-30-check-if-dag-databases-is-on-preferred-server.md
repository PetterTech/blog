---
title: Check if DAG databases is on preferred server
date: 2012-04-30T10:35:57+00:00
url: /index.php/2012/04/30/check-if-dag-databases-is-on-preferred-server/
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

 ```powershell
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