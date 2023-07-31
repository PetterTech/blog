---
title: ALTools from Microsoft, awesome!
author: nerenther
 
date: 2011-06-09T11:39:13+00:00
url: /index.php/2011/06/09/altools-from-microsoft-awesome/
categories:
  - Active Directory
  - Microsoft
tags:
  - active directory
  - microsoft
  - tools

---
Stumbled upon a tool from Microsoft called ALTools that I thought were absolutely awesome. It&#8217;s over 7 years old so I wonder why I haven&#8217;t seen it before

Nevertheless it&#8217;s as cool now as it was when it was released.  
ALTools consists of several tools, but the coolest of them are:

  * aloinfo &#8211; Displays all user account names and the age of their passwords
  * eventcombMT &#8211; Gathers specific events from event logs of several different machines and saves them in a text file
  * LockoutStatus &#8211; Shows a list of all domain controllers in a given domain and the lockoutstatus of a given user on those

I have used eventcomb a couple of times as it has some predefined searches, for example Account Lockouts.  
That particular search is quit helpful if you have a user that frequently gets locked out.  
Just choose the predfined search, input username and hit search. A few minutes later you have txt files containing only the eventlog entries regarding account lockouts and the given  user.

Download altools from <http://www.microsoft.com/downloads/en/details.aspx?FamilyID=7AF2E69C-91F3-4E63-8629-B999ADDE0B9E&displaylang=en>