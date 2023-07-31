---
title: Set event logging for the offline address list generator to medium
author: nerenther
 
date: 2011-08-03T06:48:06+00:00
url: /index.php/2011/08/03/set-event-logging-for-the-offline-address-list-generator-to-medium/
categories:
  - Exchange
  - Microsoft
tags:
  - Address list
  - Exchange
  - GAL
  - microsoft
  - oab
  - Powershell

---
In a default exchange 2007/2010 installation the logging level for OALGen is set to lowest. That means that if you have users who do not show up in the Global address list (GAL) or they are missing some info, you will only see the following events in the event log:

Log Name: Application  
Source: MSExchangeSA  
Date: 03.08.2011 08:15:18  
Event ID: 9320 Task Category: (13)  
Level: Warning  
Keywords: Classic  
User: N/A  
Computer: <servername>  
Description:  
OABGen could not generate full details for some entries in the offline address list for address list &#8216;Global Address List'. To see which entries are affected, set event logging for the offline address list generator to at least medium.

Log Name: Application  
Source: MSExchangeSA  
Date: 03.08.2011 08:15:18  
Event ID: 9327  
Task Category: (13)  
Level: Warning  
Keywords: Classic  
User: N/A  
Computer: <servername>  
Description:  
OALGen skipped some entries in the offline address list &#8216;Global Address List'. To see which entries are affected, event logging for the OAL Generator must be set to at least medium. &#8211; Default Offline Address Book

In some cases you might want to see which users are affected. To do this you have to increase the log level for MSExchangeSAOAL Generator. Thats done by running this simple little powershell command:

Set-EventLogLevel &#8220;MSExchangeSAOAL Generator&#8221; -level medium

The next time the address lists are being generated you will see an event for every user that gets dropped from the address list or users that have their properties truncated in the address list.

If you don't want to wait for the next scheduled generation of the address lists you can run these commands in powershell:

Update-GlobalAddressList &#8220;Default Global Address List&#8221;  
Update-OfflineAddressBook &#8220;Default Offline Address Book&#8221;