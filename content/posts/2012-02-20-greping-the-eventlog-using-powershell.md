---
title: "Grep'ing the eventlog using powershell"
author: nerenther
 
date: 2012-02-20T09:27:42+00:00
url: /index.php/2012/02/20/greping-the-eventlog-using-powershell/
categories:
  - Microsoft
  - Powershell
tags:
  - get-eventlog
  - microsoft
  - Powershell

---
If you are used to working with Linux you're probably familiar with using tail, grep and such for gathering stuff from logs and other files. Those are quite useful tools and work very well when you want to find out e.g. why a user fails to log in.

In Windows it's a little different, if we want to find something in the event logs we have always had to resort to a console.  
But with powershell you can search through the event logs from a command line:

Get-EventLog is quite the useful cmdlet. You can specify which log you want to search, a time window, usernames, entrytypes and even computername.

If you are a little more experienced with powershell you can even dig down further by piping the command to a where-object cmdlet, for example if you want to see all entries in the system log with the event id 7036 you would type:

 ```
 Get-EventLog -LogName System | Where-Object {$_.EventID -eq 7036} 
 ```

You probably end up with a long list, so to just show the last 5 entries:

 ```
 Get-EventLog -LogName System -Newest 5 | Where-Object {$_.EventID -eq 7036} 
 ```

Note that this will only grab the last 5 entries from the system event log, not necessarily the last 5 entries with event id 7036. So it might be better to use the After parameter to get events since yesterday:

 ```
 $yesterday = get-date 19/02/12
 Get-EventLog -LogName System -After $yesterday | Where-Object {$_.EventID -eq 7036} 
 ```

As you can see I define a variable for yesterday, thats just because I'm lazy and want to keep the commands as little complex as I can.

One of the things I commonly use get-eventlog for is figuring out why a user fails to log in through one of our radius servers. Heres one example of a command I would use for that:

 ```
 $yesterday = get-date 19/02/12
 Get-EventLog -LogName security -computername radiusserver -after $yesterday | Where-Object {$_.entrytype -eq "FailureAudit" -and $_.Message -like "*username*"} | fl 
 ```

So as you can see, the get-eventlog cmdlet is quite useful, especially when you combine it with where-object. Also remember that you can always output any data you receive to a csv by piping the command: | export-csv c:filname.csv