---
title: 'Exchange: Activate Database Copy fails'
author: nerenther
 
date: 2013-01-16T09:07:50+00:00
url: /index.php/2013/01/16/activate-database-copy-fails/
categories:
  - Exchange
  - Microsoft
tags:
  - DAG
  - database action failed
  - Exchange
  - hr=0x80004005 ec=-1216
  - Unable to mount database

---
After some exchange services failed on one of the nodes in our Exchange 2010 DAG we got some problems with one database. The database was mounted on server2 where it has an activation preference of 2.  
Trying to manually activate the database on server1, where is has an activation preference of 1, resulted in the following error:

&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;  
Microsoft Exchange Error  
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;  
Cannot activate database copy &#8216;Activate Database Copy&#8230;&#8217;.

Activate Database Copy&#8230;  
Failed  
Error:  
An Active Manager operation failed. Error: The database action failed. Error: Operation failed with message: MapiExceptionJetErrorAttachedDatabaseMismatch: Unable to mount database. (hr=0x80004005, ec=-1216)  
. [Database: DB1, Server: server1]

An Active Manager operation failed. Error: Operation failed with message: MapiExceptionJetErrorAttachedDatabaseMismatch: Unable to mount database. (hr=0x80004005, ec=-1216)  
. [Server: server1]

MapiExceptionJetErrorAttachedDatabaseMismatch: Unable to mount database. (hr=0x80004005, ec=-1216)

&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;  
OK  
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;

&nbsp;

The solution is actually quite simple:

Suspend the database copy on server1 and update the database copy. Then try to activate the database copy again.

More detailed steps:  
Using the Exchange management shell:  
Suspend-MailboxDatabaseCopy -Identity DB1Server1  
Update-MailboxDatabaseCopy -Identity DB1Server1 -SourceServer Server2  
Move-ActiveMailboxDatabase DB2 -ActivateOnServer MBX1

Using the Exchange Management Console:  
Navigate to Server Configuration&#8211;>Mailbox and select Server1  
Right click the database and click Suspend Database Copy  
Right click the database and click Update Database Copy  
In the wizard select server2 as the source server and click Update  
When the job completes right click the database again and click Activate Database Copy

&nbsp;

&nbsp;

&nbsp;