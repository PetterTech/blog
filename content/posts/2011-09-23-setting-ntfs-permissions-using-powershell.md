---
title: Setting NTFS permissions using Powershell
date: 2011-09-23T11:19:28+00:00
url: /index.php/2011/09/23/setting-ntfs-permissions-using-powershell/
categories:
  - Microsoft
  - Powershell
tags:
  - microsoft
  - ntfs
  - Permissions
  - Powershell
---
I am currently working on a script similar to the [Mass import of users in Active Direcory](/index.php/2011/09/07/mass-import-of-users-in-active-directory/) post I published earlier (as promised 🙂 ). In the new script I wanted to only use powershell, so I had to find a way to set ntfs permissions using powershell. After all, the cacls way is pretty outdated.

After some googling I came up with a rather extensive script, it is a little more complicated than I wanted but here goes:

 ```powershell
 $acl = Get-Acl c:test
$acl.SetAccessRuleProtection($True, $False)

$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators","FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
("SYSTEM","FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("testuser","FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Users","Read", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)

Set-Acl c:test $acl

Get-Acl c:test | format-list
```

What it does it set the default permissions (in win7) that are inherited, in addition to full controll for &#8220;testuser&#8221;, on the folder c:test.

You can download the script {{< unavailable "File no longer available" >}}

Next step is to get this into an _foreach_ loop&#8230;