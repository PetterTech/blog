---
title: Mass import of users in Active Directory
author: nerenther
 
date: 2011-09-06T23:10:38+00:00
url: /index.php/2011/09/07/mass-import-of-users-in-active-directory/
categories:
  - Active Directory
  - Microsoft
tags:
  - active directory
  - cacls
  - dsadd
  - import
  - microsoft
  - script

---
Tried sleeping&#8230;&#8230;That obviously didn&#8217;t work out, so here&#8217;s a guide on how to import a number of users in Active Directory and then creating and sharing out their home folder.

Note: This guide uses dsadd for creating users and cacls for setting ntfs permissions. Thats kind of old fashioned, I will try to write a new guide using powershell later on.

In the scenario I have created this script for we have a domain controller who happens to also be the file server, file01. The domain is called test.local and have 5 OUs in addition to the default ones, those are:  
Sales  
Management  
HR  
IT  
groups

Files are stored on a drive called e: under a folder named users. Each homefolder is shared with a trailing $.  
In the OU called groups, there are a few groups with identical names to the rest of our OUs.

Now that we have set the scenario heres the script:

```
dsadd user "CN=<username>,OU=<department>,DC=test,DC=local" -samid <username> -upn <username>@test.local -fn <firstname> -ln <lastname> -pwd eeh7at3R -memberof "CN=<department>,OU=groups,DC=test,DC=local" -hmdir \file01<username>$ -hmdrv h:
md e:users<username>
net share <username>$=e:users<username> /grant:<username>,CHANGE /grant:"domain admins",FULL /grant:administrator,FULL
cacls e:users<username> /T /E /G test<username>:C
cacls e:users<username> /T /E /G builtinadministrators:F
cacls e:users<username> /T /E /G SYSTEM:F 
```

A little explanation:  
Using dsadd we first specify that it is a user we want to add, followed by the distinguished name for that user. We also specify the sam id, upn, firstname, lastname and password. The -memberof switch sets which groups the user should be a member of, in this case there is only one, but you can specify multiple groups separated by , just remember to use the distinguished name of the group.  
The last switches are for setting home folder and drive in ad. I put it in here because thats the way most admins specify home folders, event though I recommend doing via the login script.

I hope you all are familiar with the md and net share commands, but thats for creating the folder and sharing it.

Cacls sets ntfs permissions on the users home folder for the user, administrators and system.

Now if you want to add say 1000 users, you might want to use something like Word&#8217;s Mailings feature (that is, if you don&#8217;t loove to sit and punch usernames and such all day long).

For that I have created a couple of example files, you can download them here:  <a title="http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/example.zip" href="http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/example.zip" target="_blank" rel="noopener">http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/example.zip</a>

The files you will find in that zip file are:  
script.docx &#8211; The template used for the mailings process  
users.xlsx &#8211; Excel file containg info on the users we want to create  
script.txt &#8211; How the finished script will look like using my example users.