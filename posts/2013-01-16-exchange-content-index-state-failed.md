---
title: 'Exchange: Content index state failed'
author: nerenther
type: post
date: 2013-01-16T09:17:13+00:00
url: /index.php/2013/01/16/exchange-content-index-state-failed/
categories:
  - Exchange
  - Microsoft
  - Powershell
tags:
  - Content index state failed
  - DAG
  - Exchange
  - Powershell

---
If you ever had problems with corrupt databases in an Exchange 2010 DAG setup you might have encountered this error. Trying to activate the database on a server where it has this state will fail.

However there is a quite simple fix given that you have a healthy copy of the database on a different server:

Update-MailboxDatabaseCopy -Identity DB<server with failed content index state> -SourceServer <server with healty copy> -CatalogOnly

Run the command in the Exchange Management Shell and it should fix the Content index state and allow you to activate the database again.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;