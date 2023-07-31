---
title: Setting NTFS permissions using Powershell
author: nerenther
 
date: 2011-09-23T11:19:28+00:00
url: /index.php/2011/09/23/setting-ntfs-permissions-using-powershell/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:5314:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$acl</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Get-Acl</span> c:test
    <span style="color: #800080;">$acl</span>.SetAccessRuleProtection<span style="color: #000000;">&#40;</span><span style="color: #800080;">$True</span><span style="color: pink;">,</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    &nbsp;
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;Administrators&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;SYSTEM&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;testuser&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;Users&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;Read&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Set-Acl</span> c:test <span style="color: #800080;">$acl</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Get-Acl</span> c:test <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">format-list</span></pre></td></tr></table><p class="theCode" style="display:none;">$acl = Get-Acl c:test
    $acl.SetAccessRuleProtection($True, $False)
    
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;Administrators&quot;,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    (&quot;SYSTEM&quot;,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;testuser&quot;,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;Users&quot;,&quot;Read&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    
    Set-Acl c:test $acl
    
    Get-Acl c:test | format-list</p></div>
    ";}
categories:
  - Microsoft
  - Powershell
tags:
  - microsoft
  - ntfs
  - Permissions
  - Powershell

---
I am currently working on a script similar to the <a href="http://cloud.kemta.net/2011/09/mass-import-of-users-in-active-directory/" target="_blank" rel="noopener">Mass import of users in Active Direcory</a> post I published earlier (as promised 🙂 ). In the new script I wanted to only use powershell, so I had to find a way to set ntfs permissions using powershell. After all, the cacls way is pretty outdated.

After some googling I came up with a rather extensive script, it is a little more complicated than I wanted but here goes:

<pre lang="powershell">$acl = Get-Acl c:test
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
</pre>

What it does it set the default permissions (in win7) that are inherited, in addition to full controll for &#8220;testuser&#8221;, on the folder c:test.

You can download the script <a href="http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/settingntfspermissions.ps1" target="_blank" rel="noopener">here</a>

Next step is to get this into an _foreach_ loop&#8230;