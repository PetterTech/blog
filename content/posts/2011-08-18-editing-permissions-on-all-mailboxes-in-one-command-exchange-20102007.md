---
title: Editing permissions on all mailboxes in one command, Exchange 2010/2007
author: nerenther
 
date: 2011-08-18T07:44:23+00:00
url: /index.php/2011/08/18/editing-permissions-on-all-mailboxes-in-one-command-exchange-20102007/
categories:
  - Exchange
  - Microsoft
tags:
  - Exchange
  - microsoft
  - Permissions
  - Powershell

---
If you have some sort of 3rd-party application that needs access to all of your mailboxes, it can be a pain to set the permissions on all of your mailboxes.

Except if you use this nice little powershell command:

 ```
 Get-Mailbox -ResultSize unlimited | Add-MailboxPermission -User admin -AccessRights FullAccess -InheritanceType all 
 ```

What this command will do is to add Full mailbox access to every mailbox in your Exchange organization for the user admin.

You can of course change the -AccessRights  setting to your liking, e.g. SendAs.  
You can also narrow down the number of mailboxes affected by changing the search parameter after Get-Mailbox

For example if you only want to set SendAs permission on a mailboxes in a specific OU for the user admin:

 ```
 get-mailbox -OrganizationalUnit domain.local/ou/Users/ | Add-MailboxPermission -User admin -AccessRights SendAs -InheritanceType all 
 ```