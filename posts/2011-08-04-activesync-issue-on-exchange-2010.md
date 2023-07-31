---
title: Activesync issue on Exchange 2010
author: nerenther
type: post
date: 2011-08-04T09:56:46+00:00
url: /index.php/2011/08/04/activesync-issue-on-exchange-2010/
categories:
  - Exchange
  - Microsoft
tags:
  - active directory
  - ActiveSync
  - Exchange
  - microsoft

---
At work we are currently migrating to a new active directory domain. The migration hos gone rather smoothly except for a couple of users who are not able to sync mail on their phones.  
After a little research I found the following events in the event log on our exchange CAS server:

Log Name: Application  
Source: MSExchange ActiveSync  
Date: 04.08.2011 11:00:48  
Event ID: 1053  
Task Category: Configuration  
Level: Error  
Keywords: Classic  
User: N/A  
Computer: <servername>  
Description:  
Exchange ActiveSync doesn&#8217;t have sufficient permissions to create the &#8220;CN=<user>,OU=<ou>,DC=<domain>,DC=local&#8221; container under Active Directory user &#8220;Active Directory operation failed on <domain controller>. This error is not retriable. Additional information: Access is denied.  
Active directory response: 00000005: SecErr: DSID-031521D0, problem 4003 (INSUFF\_ACCESS\_RIGHTS), data 0  
&#8220;.  
Make sure the user has inherited permission granted to domainExchange Servers to allow List, Create child, Delete child of object type &#8220;msExchangeActiveSyncDevices&#8221; and doesn&#8217;t have any deny permissions that block such operations.

Details:%3

This, I found, was because the exchange server wants to create a container under the user object in ad. That container shall contain an object for each mobile device the user wants to sync mail on.

I compared the users having trouble syncing to those who are able to sync and found only one difference: The users who cannot sync mail doesn&#8217;t have &#8220;Include inheritable permissions from this object&#8217;s parent&#8221; ticked on the Security&#8211;>Advanced page of the user object. Ticking this resolved the issue.

After a little more digging I found the specific permission the exchange servers need.  
To enable ActiveSync the group &#8220;<domain>Exchange Servers&#8221; need to have these permissions:

Create msExchActiveSyncDevices object  
Delete  msExchActiveSyncDevices object