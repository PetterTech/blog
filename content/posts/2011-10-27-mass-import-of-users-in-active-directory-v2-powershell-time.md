---
title: Mass import of users in Active Directory v2 – Powershell time
author: nerenther
 
date: 2011-10-27T19:54:21+00:00
url: /index.php/2011/10/27/mass-import-of-users-in-active-directory-v2-powershell-time/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:45994:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008000;">#Change the window title</span>
    <span style="color: #800080;">$UI</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-Host</span><span style="color: #000000;">&#41;</span>.UI.RawUI
    <span style="color: #800080;">$UI</span>.WindowTitle <span style="color: pink;">=</span> <span style="color: #800000;">&quot;User import script created by Nerenther, kemta.net&quot;</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">write-host</span> <span style="color: #800000;">&quot;Started at: $(get-date)&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Working...&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Setting some variabels for later use</span>
    <span style="color: #800080;">$ElapsedTime</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#91;</span>System.Diagnostics.Stopwatch<span style="color: #000000;">&#93;</span>::StartNew<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$ScriptStarted</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">get-date</span>
    <span style="color: #800080;">$ScriptPath</span> <span style="color: pink;">=</span> <span style="color: #800000;">&quot;c:scripttesting&quot;</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Import-Csv</span> <span style="color: #800080;">$Scriptpathusers</span>.csv
    <span style="color: #800080;">$Groups</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Import-Csv</span> <span style="color: #800080;">$Scriptpathgroups</span>.csv
    <span style="color: #800080;">$OURoot</span> <span style="color: pink;">=</span> <span style="color: #800000;">&quot;OU=Kemta.net,DC=test,DC=local&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Load Microsoft`s Active Directory module</span>
    Import<span style="color: pink;">-</span>Module ActiveDirectory
    &nbsp;
    <span style="color: #008000;">#Creating some OUs</span>
    New<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: #008080; font-style: italic;">-Name</span> Kemta.net <span style="color: #008080; font-style: italic;">-Path</span> <span style="color: #800000;">&quot;DC=test,DC=local&quot;</span> <span style="color: pink;">-</span>ProtectedFromAccidentalDeletion <span style="color: #800080;">$false</span>
    New<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: #008080; font-style: italic;">-Name</span> SecurityGroups <span style="color: #008080; font-style: italic;">-Path</span> <span style="color: #800080;">$OURoot</span> <span style="color: pink;">-</span>ProtectedFromAccidentalDeletion <span style="color: #800080;">$false</span>
    New<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: #008080; font-style: italic;">-Name</span> DistributionGroups <span style="color: #008080; font-style: italic;">-Path</span> <span style="color: #800080;">$OURoot</span> <span style="color: pink;">-</span>ProtectedFromAccidentalDeletion <span style="color: #800080;">$false</span>
    New<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: #008080; font-style: italic;">-Name</span> Users <span style="color: #008080; font-style: italic;">-Path</span> <span style="color: #800080;">$OURoot</span> <span style="color: pink;">-</span>ProtectedFromAccidentalDeletion <span style="color: #800080;">$false</span>
    <span style="color: #800080;">$Groups</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>New<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #000080;">$_</span>.distribution <span style="color: #008080; font-style: italic;">-path</span> <span style="color: #800000;">&quot;OU=Users,$OURoot&quot;</span> <span style="color: pink;">-</span>ProtectedFromAccidentalDeletion <span style="color: #800080;">$false</span><span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Create the users from the csv file</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>New<span style="color: pink;">-</span>ADUser <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #000000;">&#40;</span><span style="color: #000080;">$_</span>.givenname <span style="color: pink;">+</span> <span style="color: #800000;">&quot; &quot;</span> <span style="color: pink;">+</span> <span style="color: #000080;">$_</span>.surname<span style="color: #000000;">&#41;</span> <span style="color: pink;">-</span>GivenName <span style="color: #000080;">$_</span>.givenname <span style="color: pink;">-</span>Surname <span style="color: #000080;">$_</span>.surname <span style="color: pink;">-</span>homedrive <span style="color: #008080; font-weight: bold;">H</span>: <span style="color: pink;">-</span>homedirectory \testdc1homedir<span style="color: pink;">%</span>username<span style="color: pink;">%</span> <span style="color: #008080; font-style: italic;">-Path</span> <span style="color: #000080;">$_</span>.ou <span style="color: pink;">-</span>AccountPassword <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">ConvertTo-SecureString</span> <span style="color: #000080;">$_</span>.Password <span style="color: #008080; font-style: italic;">-AsPlainText</span> <span style="color: #008080; font-style: italic;">-Force</span><span style="color: #000000;">&#41;</span> <span style="color: pink;">-</span>SamAccountname <span style="color: #000080;">$_</span>.username <span style="color: pink;">-</span>UserPrincipalName <span style="color: #000080;">$_</span>.upn <span style="color: pink;">-</span>Department <span style="color: #000080;">$_</span>.department <span style="color: pink;">-</span>Company Kemta.net <span style="color: pink;">-</span>Enabled <span style="color: #800080;">$true</span><span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Create a security group for everyone</span>
    New<span style="color: pink;">-</span>ADGroup <span style="color: #008080; font-style: italic;">-Name</span> Everybody <span style="color: #008080; font-style: italic;">-path</span> <span style="color: #800000;">&quot;OU=SecurityGroups,$OURoot&quot;</span> <span style="color: pink;">-</span>GroupScope <span style="color: #804000;">1</span>
    &nbsp;
    <span style="color: #008000;">#Add all the users we created to the Everybody group</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>Add<span style="color: pink;">-</span>ADGroupMember <span style="color: pink;">-</span>Identity Everybody <span style="color: pink;">-</span>Members <span style="color: #000080;">$_</span>.username<span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Create groups based on the csv file</span>
    <span style="color: #800080;">$Groups</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>New<span style="color: pink;">-</span>ADGroup <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #000080;">$_</span>.security <span style="color: #008080; font-style: italic;">-path</span> <span style="color: #800000;">&quot;OU=SecurityGroups,$OURoot&quot;</span> <span style="color: pink;">-</span>GroupScope <span style="color: #804000;">1</span><span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Add users to their respective groups</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>Add<span style="color: pink;">-</span>ADGroupMember <span style="color: pink;">-</span>Identity <span style="color: #000080;">$_</span>.securitygroup <span style="color: pink;">-</span>Members <span style="color: #000080;">$_</span>.username<span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Create a homefolder root</span>
    <span style="color: #008080; font-weight: bold;">New-Item</span> e:homedir <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> Directory
    &nbsp;
    <span style="color: #008000;">#Set permissions on the homefolder root</span>
    <span style="color: #800080;">$acl</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Get-Acl</span> e:homedir
    <span style="color: #800080;">$acl</span>.SetAccessRuleProtection<span style="color: #000000;">&#40;</span><span style="color: #800080;">$True</span><span style="color: pink;">,</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;Administrators&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;SYSTEM&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;Users&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;Read&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #008080; font-weight: bold;">Set-Acl</span> e:homedir <span style="color: #800080;">$acl</span>
    &nbsp;
    <span style="color: #008000;">#Share homefolder root and set permissions</span>
        <span style="color: #008000;">#This is not possible in powershell 2.0, so therefore I here use powershell a 3.0 command</span>
    New<span style="color: pink;">-</span>SmbShare <span style="color: #008080; font-style: italic;">-Name</span> homedir <span style="color: #008080; font-style: italic;">-path</span> e:homedir <span style="color: pink;">-</span>FullAccess Everyone
    &nbsp;
    <span style="color: #008000;">#Create homefolders</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #008080; font-weight: bold;">new-item</span> <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> Directory <span style="color: #000080;">$_</span>.homefolder<span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Set NTFS permissions on each homefolder</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>
    <span style="color: #800080;">$acl</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">get-acl</span> <span style="color: #000080;">$_</span>.homefolder
    <span style="color: #800080;">$acl</span>.SetAccessRuleProtection<span style="color: #000000;">&#40;</span><span style="color: #800080;">$False</span><span style="color: pink;">,</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;Administrators&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;SYSTEM&quot;</span><span style="color: pink;">,</span><span style="color: #800000;">&quot;Read&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$rule</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">New-Object</span> System.Security.AccessControl.FileSystemAccessRule<span style="color: #000000;">&#40;</span><span style="color: #000080;">$_</span>.username<span style="color: pink;">,</span><span style="color: #800000;">&quot;FullControl&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;ContainerInherit, ObjectInherit&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;None&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;Allow&quot;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$acl</span>.AddAccessRule<span style="color: #000000;">&#40;</span><span style="color: #800080;">$rule</span><span style="color: #000000;">&#41;</span>
    <span style="color: #008080; font-weight: bold;">Set-Acl</span> <span style="color: #000080;">$_</span>.homefolder <span style="color: #800080;">$acl</span>
    <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Starting the Exchange 2010 part of the script. Comment out if you don't need this part</span>
    &nbsp;
    <span style="color: #008000;">#Starting new Powershell session and importing it</span>
    <span style="color: #800080;">$exsession</span> <span style="color: pink;">=</span> New<span style="color: pink;">-</span>PSSession <span style="color: pink;">-</span>ConfigurationName Microsoft.Exchange <span style="color: pink;">-</span>ConnectionUri http:<span style="color: pink;">//</span>testex1.test.local<span style="color: pink;">/</span>powershell <span style="color: pink;">-</span>Authentication Kerberos
    Import<span style="color: pink;">-</span>PSSession <span style="color: #800080;">$exsession</span>
    &nbsp;
    <span style="color: #008000;">#Setting storage limits on the database</span>
    Set<span style="color: pink;">-</span>MailboxDatabase <span style="color: pink;">-</span>Identity MBDB <span style="color: pink;">-</span>IssueWarningQuota <span style="color: #804000;">1073741824</span> <span style="color: pink;">-</span>ProhibitSendQuota <span style="color: #804000;">2147483648</span> <span style="color: pink;">-</span>ProhibitSendReceiveQuota <span style="color: #804000;">5368709120</span>
    &nbsp;
    <span style="color: #008000;">#Create some mailboxes</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>Enable<span style="color: pink;">-</span>Mailbox <span style="color: pink;">-</span>Identity <span style="color: #000080;">$_</span>.username <span style="color: pink;">-</span>Alias <span style="color: #000080;">$_</span>.username<span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Create some distribution groups</span>
    New<span style="color: pink;">-</span>DistributionGroup <span style="color: #008080; font-style: italic;">-Name</span> AllUsers <span style="color: pink;">-</span>OrganizationalUnit <span style="color: #800000;">&quot;test.local/Kemta.net/DistributionGroups&quot;</span> <span style="color: pink;">-</span>SamAccountName AllUsers <span style="color: pink;">-</span>Alias AllUsers
    <span style="color: #800080;">$Groups</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>New<span style="color: pink;">-</span>DistributionGroup <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #000080;">$_</span>.distribution <span style="color: pink;">-</span>OrganizationalUnit <span style="color: #800000;">&quot;test.local/Kemta.net/DistributionGroups&quot;</span> <span style="color: pink;">-</span>SamAccountName <span style="color: #000080;">$_</span>.distribution <span style="color: pink;">-</span>Alias <span style="color: #000080;">$_</span>.distribution<span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Add the users to their respective distribution groups</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>Add<span style="color: pink;">-</span>DistributionGroupMember  <span style="color: pink;">-</span>Identity <span style="color: #000080;">$_</span>.department <span style="color: pink;">-</span>Member <span style="color: #000080;">$_</span>.username<span style="color: #000000;">&#125;</span>
    <span style="color: #800080;">$users</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>Add<span style="color: pink;">-</span>DistributionGroupMember  <span style="color: pink;">-</span>Identity AllUsers <span style="color: pink;">-</span>Member <span style="color: #000080;">$_</span>.username<span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008000;">#Showing som info to the user</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Some more or less usefull information:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;OUs created:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: pink;">-</span><span style="color: #0000FF;">filter</span> <span style="color: #000000;">&#123;</span>whencreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span> <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>.count
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot; &quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Users created:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>ADUser <span style="color: pink;">-</span><span style="color: #0000FF;">filter</span> <span style="color: #000000;">&#123;</span>whencreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span> <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>.count
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Homefolders created:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #800080;">$HomefoldersCreated</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-ChildItem</span> e:homedir <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Where-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.CreationTime <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$HomefoldersCreated</span>.count
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Mailboxes created:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #800080;">$MailboxesCreated</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>Mailbox <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Where-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.WhenCreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$MailboxesCreated</span>.count
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Distributions groups created:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #800080;">$DistributionGroupsCreated</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>DistributionGroup <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Where-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.WhenCreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$DistributionGroupsCreated</span>.count
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">write-host</span> <span style="color: #800000;">&quot;Time taken:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #800080;">$elapsedtime</span>.elapsed <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">select</span> hours<span style="color: pink;">,</span> minutes<span style="color: pink;">,</span> seconds
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Lines of code run:&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-Content</span> <span style="color: #800080;">$Scriptpathpopulate</span><span style="color: pink;">-</span>ad.ps1<span style="color: #000000;">&#41;</span>.Length
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">write-host</span> <span style="color: #800000;">&quot;All done :)&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Script stopped at $(get-date)&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Press any key to exit&quot;</span> <span style="color: #008080; font-style: italic;">-ForegroundColor</span> <span style="color: #800000;">&quot;green&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Make the windows a little bigger so the user can see all the info presented</span>
    <span style="color: #800080;">$PSWindowSize</span> <span style="color: pink;">=</span> <span style="color: #800080;">$UI</span>.WindowSize
    <span style="color: #800080;">$PSWindowSize</span>.Height <span style="color: pink;">=</span> <span style="color: #804000;">32</span>
    <span style="color: #800080;">$UI</span>.WindowSize <span style="color: pink;">=</span> <span style="color: #800080;">$PSWindowSize</span>
    &nbsp;
    <span style="color: #008000;">#Write a small log file containing the same info as presented</span>
    <span style="color: #008080; font-weight: bold;">New-Item</span> <span style="color: #008080; font-style: italic;">-path</span> <span style="color: #800080;">$ScriptPath</span> <span style="color: #008080; font-style: italic;">-name</span> log.txt
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;OUs created:&quot;</span>
    <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>ADOrganizationalUnit <span style="color: pink;">-</span><span style="color: #0000FF;">filter</span> <span style="color: #000000;">&#123;</span>whencreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span> <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>.count <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out<span style="color: #FF0000;">-file</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;Users created:&quot;</span>
    <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>ADUser <span style="color: pink;">-</span><span style="color: #0000FF;">filter</span> <span style="color: #000000;">&#123;</span>whencreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span> <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>.count <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out<span style="color: #FF0000;">-file</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;Homefolders created:&quot;</span>
    <span style="color: #800080;">$HomefoldersCreated</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-ChildItem</span> e:homedir <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Where-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.CreationTime <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$HomefoldersCreated</span>.count <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out<span style="color: #FF0000;">-file</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;Mailboxes created:&quot;</span>
    <span style="color: #800080;">$MailboxesCreated</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>Mailbox <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Where-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.WhenCreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$MailboxesCreated</span>.count <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out<span style="color: #FF0000;">-file</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;Distributions groups created:&quot;</span>
    <span style="color: #800080;">$DistributionGroupsCreated</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#40;</span>Get<span style="color: pink;">-</span>DistributionGroup <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Where-Object</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.WhenCreated <span style="color: #FF0000;">-ge</span> <span style="color: #800080;">$ScriptStarted</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #800080;">$DistributionGroupsCreated</span>.count <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out<span style="color: #FF0000;">-file</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;Time taken:&quot;</span>
    <span style="color: #800080;">$elapsedtime</span>.elapsed <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">select</span> hours<span style="color: pink;">,</span> minutes<span style="color: pink;">,</span> seconds <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Out<span style="color: #FF0000;">-File</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    <span style="color: #008080; font-weight: bold;">add-content</span> <span style="color: #800080;">$scriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-encoding</span> ASCII <span style="color: #800000;">&quot;Lines of code run:&quot;</span>
    <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-Content</span> <span style="color: #800080;">$Scriptpathpopulate</span><span style="color: pink;">-</span>ad.ps1<span style="color: #000000;">&#41;</span>.Length <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out<span style="color: #FF0000;">-file</span></span> <span style="color: #800080;">$ScriptPathlog</span>.txt <span style="color: #008080; font-style: italic;">-append</span> <span style="color: #008080; font-style: italic;">-encoding</span> ASCII
    &nbsp;
    <span style="color: #008000;">#Disconnecting from Exchange</span>
    Remove<span style="color: pink;">-</span>PSSession <span style="color: #800080;">$exsession</span>
    &nbsp;
    cmd <span style="color: pink;">/</span>c pause <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out-null</span></pre></td></tr></table><p class="theCode" style="display:none;">#Change the window title
    $UI = (Get-Host).UI.RawUI
    $UI.WindowTitle = &quot;User import script created by Nerenther, kemta.net&quot;
    
    write-host &quot;Started at: $(get-date)&quot;
    Write-Host &quot;Working...&quot;
    
    #Setting some variabels for later use
    $ElapsedTime = [System.Diagnostics.Stopwatch]::StartNew()
    $ScriptStarted = get-date
    $ScriptPath = &quot;c:scripttesting&quot;
    $users = Import-Csv $Scriptpathusers.csv
    $Groups = Import-Csv $Scriptpathgroups.csv
    $OURoot = &quot;OU=Kemta.net,DC=test,DC=local&quot;
    
    #Load Microsoft`s Active Directory module
    Import-Module ActiveDirectory
    
    #Creating some OUs
    New-ADOrganizationalUnit -Name Kemta.net -Path &quot;DC=test,DC=local&quot; -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name SecurityGroups -Path $OURoot -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name DistributionGroups -Path $OURoot -ProtectedFromAccidentalDeletion $false
    New-ADOrganizationalUnit -Name Users -Path $OURoot -ProtectedFromAccidentalDeletion $false
    $Groups | ForEach-Object {New-ADOrganizationalUnit -Name $_.distribution -path &quot;OU=Users,$OURoot&quot; -ProtectedFromAccidentalDeletion $false}
    
    #Create the users from the csv file
    $users | ForEach-Object {New-ADUser -Name ($_.givenname + &quot; &quot; + $_.surname) -GivenName $_.givenname -Surname $_.surname -homedrive H: -homedirectory \testdc1homedir%username% -Path $_.ou -AccountPassword (ConvertTo-SecureString $_.Password -AsPlainText -Force) -SamAccountname $_.username -UserPrincipalName $_.upn -Department $_.department -Company Kemta.net -Enabled $true}
    
    #Create a security group for everyone
    New-ADGroup -Name Everybody -path &quot;OU=SecurityGroups,$OURoot&quot; -GroupScope 1
    
    #Add all the users we created to the Everybody group
    $users | ForEach-Object {Add-ADGroupMember -Identity Everybody -Members $_.username}
    
    #Create groups based on the csv file
    $Groups | ForEach-Object {New-ADGroup -Name $_.security -path &quot;OU=SecurityGroups,$OURoot&quot; -GroupScope 1}
    
    #Add users to their respective groups
    $users | ForEach-Object {Add-ADGroupMember -Identity $_.securitygroup -Members $_.username}
    
    #Create a homefolder root
    New-Item e:homedir -type Directory
    
    #Set permissions on the homefolder root
    $acl = Get-Acl e:homedir
    $acl.SetAccessRuleProtection($True, $False)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;Administrators&quot;,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;SYSTEM&quot;,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;Users&quot;,&quot;Read&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    Set-Acl e:homedir $acl
    
    #Share homefolder root and set permissions
        #This is not possible in powershell 2.0, so therefore I here use powershell a 3.0 command
    New-SmbShare -Name homedir -path e:homedir -FullAccess Everyone
    
    #Create homefolders
    $users | ForEach-Object {new-item -type Directory $_.homefolder}
    
    #Set NTFS permissions on each homefolder
    $users | ForEach-Object {
    $acl = get-acl $_.homefolder
    $acl.SetAccessRuleProtection($False, $False)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;Administrators&quot;,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule(&quot;SYSTEM&quot;,&quot;Read&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule($_.username,&quot;FullControl&quot;, &quot;ContainerInherit, ObjectInherit&quot;, &quot;None&quot;, &quot;Allow&quot;)
    $acl.AddAccessRule($rule)
    Set-Acl $_.homefolder $acl
    }
    
    #Starting the Exchange 2010 part of the script. Comment out if you don't need this part
    
    #Starting new Powershell session and importing it
    $exsession = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://testex1.test.local/powershell -Authentication Kerberos
    Import-PSSession $exsession
    
    #Setting storage limits on the database
    Set-MailboxDatabase -Identity MBDB -IssueWarningQuota 1073741824 -ProhibitSendQuota 2147483648 -ProhibitSendReceiveQuota 5368709120
    
    #Create some mailboxes
    $users | ForEach-Object {Enable-Mailbox -Identity $_.username -Alias $_.username}
    
    #Create some distribution groups
    New-DistributionGroup -Name AllUsers -OrganizationalUnit &quot;test.local/Kemta.net/DistributionGroups&quot; -SamAccountName AllUsers -Alias AllUsers
    $Groups | ForEach-Object {New-DistributionGroup -Name $_.distribution -OrganizationalUnit &quot;test.local/Kemta.net/DistributionGroups&quot; -SamAccountName $_.distribution -Alias $_.distribution}
    
    #Add the users to their respective distribution groups
    $users | ForEach-Object {Add-DistributionGroupMember  -Identity $_.department -Member $_.username}
    $users | ForEach-Object {Add-DistributionGroupMember  -Identity AllUsers -Member $_.username}
    
    #Showing som info to the user
    Write-Host &quot;Some more or less usefull information:&quot; -ForegroundColor &quot;green&quot;
    Write-Host &quot;&quot;
    Write-Host &quot;OUs created:&quot; -ForegroundColor &quot;green&quot;
    (Get-ADOrganizationalUnit -filter {whencreated -ge $ScriptStarted }).count
    Write-Host &quot; &quot;
    Write-Host &quot;Users created:&quot; -ForegroundColor &quot;green&quot;
    (Get-ADUser -filter {whencreated -ge $ScriptStarted }).count
    Write-Host &quot;&quot;
    Write-Host &quot;Homefolders created:&quot; -ForegroundColor &quot;green&quot;
    $HomefoldersCreated = (Get-ChildItem e:homedir | Where-Object {$_.CreationTime -ge $ScriptStarted})
    $HomefoldersCreated.count
    Write-Host &quot;&quot;
    Write-Host &quot;Mailboxes created:&quot; -ForegroundColor &quot;green&quot;
    $MailboxesCreated = (Get-Mailbox | Where-Object {$_.WhenCreated -ge $ScriptStarted})
    $MailboxesCreated.count
    Write-Host &quot;&quot;
    Write-Host &quot;Distributions groups created:&quot; -ForegroundColor &quot;green&quot;
    $DistributionGroupsCreated = (Get-DistributionGroup | Where-Object {$_.WhenCreated -ge $ScriptStarted})
    $DistributionGroupsCreated.count
    Write-Host &quot;&quot;
    write-host &quot;Time taken:&quot; -ForegroundColor &quot;green&quot;
    $elapsedtime.elapsed | select hours, minutes, seconds
    Write-Host &quot;&quot;
    Write-Host &quot;Lines of code run:&quot; -ForegroundColor &quot;green&quot;
    (Get-Content $Scriptpathpopulate-ad.ps1).Length
    Write-Host &quot;&quot;
    write-host &quot;All done :)&quot; -ForegroundColor &quot;green&quot;
    Write-Host &quot;&quot;
    Write-Host &quot;Script stopped at $(get-date)&quot; -ForegroundColor &quot;green&quot;
    Write-Host &quot;Press any key to exit&quot; -ForegroundColor &quot;green&quot;
    
    #Make the windows a little bigger so the user can see all the info presented
    $PSWindowSize = $UI.WindowSize
    $PSWindowSize.Height = 32
    $UI.WindowSize = $PSWindowSize
    
    #Write a small log file containing the same info as presented
    New-Item -path $ScriptPath -name log.txt
    add-content $scriptPathlog.txt -encoding ASCII &quot;OUs created:&quot;
    (Get-ADOrganizationalUnit -filter {whencreated -ge $ScriptStarted }).count | out-file $ScriptPathlog.txt -append -encoding ASCII
    add-content $scriptPathlog.txt -encoding ASCII &quot;Users created:&quot;
    (Get-ADUser -filter {whencreated -ge $ScriptStarted }).count | out-file $ScriptPathlog.txt -append -encoding ASCII
    add-content $scriptPathlog.txt -encoding ASCII &quot;Homefolders created:&quot;
    $HomefoldersCreated = (Get-ChildItem e:homedir | Where-Object {$_.CreationTime -ge $ScriptStarted})
    $HomefoldersCreated.count | out-file $ScriptPathlog.txt -append -encoding ASCII
    add-content $scriptPathlog.txt -encoding ASCII &quot;Mailboxes created:&quot;
    $MailboxesCreated = (Get-Mailbox | Where-Object {$_.WhenCreated -ge $ScriptStarted})
    $MailboxesCreated.count | out-file $ScriptPathlog.txt -append -encoding ASCII
    add-content $scriptPathlog.txt -encoding ASCII &quot;Distributions groups created:&quot;
    $DistributionGroupsCreated = (Get-DistributionGroup | Where-Object {$_.WhenCreated -ge $ScriptStarted})
    $DistributionGroupsCreated.count | out-file $ScriptPathlog.txt -append -encoding ASCII
    add-content $scriptPathlog.txt -encoding ASCII &quot;Time taken:&quot;
    $elapsedtime.elapsed | select hours, minutes, seconds | Out-File $ScriptPathlog.txt -append -encoding ASCII
    add-content $scriptPathlog.txt -encoding ASCII &quot;Lines of code run:&quot;
    (Get-Content $Scriptpathpopulate-ad.ps1).Length | out-file $ScriptPathlog.txt -append -encoding ASCII
    
    #Disconnecting from Exchange
    Remove-PSSession $exsession
    
    cmd /c pause | out-null</p></div>
    ";}
categories:
  - Active Directory
  - Exchange
  - Microsoft
  - Powershell
tags:
  - active directory
  - Exchange
  - microsoft
  - Powershell

---
Earlier I posted a script that created users and homefolders and added the users to specified groups. It also set ntfs permissions on the homefolders.  
That script used primarily old fashioned stuff, so I sat down and started looking for a neat way to do the same in powershell.

The powershell script I came up does a lot more than the last one. Here a little list:

  * Creates OUs
  * Creates users
  * Creates security groups
  * Creates distribution groups
  * Creates mailboxes for all users
  * Add specified users to the correct security and distribution groups
  * Creates a homefolder root folder and shares it
  * Creates a homefolder for each user and sets ntfs permissions
  * Set storage limit on the exchange mailbox database

As you can see, it does quite a lot. I could incorporate more in this script, for example sharepoint and lync config, but I figured the script is long enough.  
If you want a script for enabling users for lync, you can see my previous post <a href="http://cloud.kemta.net/2011/10/simple-powershell-script-for-enabling-users-for-lync/" target="_blank" rel="noopener">here</a>.

The cool thing about this script is that is pretty fast. In my test environment, consisting of two virtual machines, one domain controller and one exchange server, it took only 1 minute to create 100 users and mailboxes, 8 OUs and 5 security and distribution groups.  
I think thats quite impressive taking in consideration that the two virtual machines both run on my computer and with only 2GB ram each.

The only thing thats quite sad is that there&#8217;s no powershell commands for sharing and setting share permissions in powershell 2.0. Thats why I have used one powershell 3.0 command in the script , new-smbshare. It is only used once, for sharing the homefolder root.

You can download the powershell 3.0 community preview and install it on the server you will run the script on. Or you can just comment out that command and rather share the root homefolder manually if you don&#8217;t want to install powershell 3.0 on your server.

This script uses two csv files, one for groups and OUs and one for the users. You can download a zip containing all files <a href="http://dl.dropbox.com/u/33041052/bloggting/scriptstuff/powershell/populate-ad.zip" target="_blank" rel="noopener">here</a>

Anyway, the script is shown below, have fun with it 🙂

<pre lang="powershell">#Change the window title
$UI = (Get-Host).UI.RawUI
$UI.WindowTitle = "User import script created by Nerenther, kemta.net"

write-host "Started at: $(get-date)"
Write-Host "Working..."

#Setting some variabels for later use
$ElapsedTime = [System.Diagnostics.Stopwatch]::StartNew()
$ScriptStarted = get-date
$ScriptPath = "c:scripttesting"
$users = Import-Csv $Scriptpathusers.csv
$Groups = Import-Csv $Scriptpathgroups.csv
$OURoot = "OU=Kemta.net,DC=test,DC=local"

#Load Microsoft`s Active Directory module
Import-Module ActiveDirectory

#Creating some OUs
New-ADOrganizationalUnit -Name Kemta.net -Path "DC=test,DC=local" -ProtectedFromAccidentalDeletion $false
New-ADOrganizationalUnit -Name SecurityGroups -Path $OURoot -ProtectedFromAccidentalDeletion $false
New-ADOrganizationalUnit -Name DistributionGroups -Path $OURoot -ProtectedFromAccidentalDeletion $false
New-ADOrganizationalUnit -Name Users -Path $OURoot -ProtectedFromAccidentalDeletion $false
$Groups | ForEach-Object {New-ADOrganizationalUnit -Name $_.distribution -path "OU=Users,$OURoot" -ProtectedFromAccidentalDeletion $false}

#Create the users from the csv file
$users | ForEach-Object {New-ADUser -Name ($_.givenname + " " + $_.surname) -GivenName $_.givenname -Surname $_.surname -homedrive H: -homedirectory \testdc1homedir%username% -Path $_.ou -AccountPassword (ConvertTo-SecureString $_.Password -AsPlainText -Force) -SamAccountname $_.username -UserPrincipalName $_.upn -Department $_.department -Company Kemta.net -Enabled $true}

#Create a security group for everyone
New-ADGroup -Name Everybody -path "OU=SecurityGroups,$OURoot" -GroupScope 1

#Add all the users we created to the Everybody group
$users | ForEach-Object {Add-ADGroupMember -Identity Everybody -Members $_.username}

#Create groups based on the csv file
$Groups | ForEach-Object {New-ADGroup -Name $_.security -path "OU=SecurityGroups,$OURoot" -GroupScope 1}

#Add users to their respective groups
$users | ForEach-Object {Add-ADGroupMember -Identity $_.securitygroup -Members $_.username}

#Create a homefolder root
New-Item e:homedir -type Directory

#Set permissions on the homefolder root
$acl = Get-Acl e:homedir
$acl.SetAccessRuleProtection($True, $False)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators","FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("SYSTEM","FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Users","Read", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
Set-Acl e:homedir $acl

#Share homefolder root and set permissions
    #This is not possible in powershell 2.0, so therefore I here use powershell a 3.0 command
New-SmbShare -Name homedir -path e:homedir -FullAccess Everyone

#Create homefolders
$users | ForEach-Object {new-item -type Directory $_.homefolder}

#Set NTFS permissions on each homefolder
$users | ForEach-Object {
$acl = get-acl $_.homefolder
$acl.SetAccessRuleProtection($False, $False)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators","FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("SYSTEM","Read", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule($_.username,"FullControl", "ContainerInherit, ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
Set-Acl $_.homefolder $acl
}

#Starting the Exchange 2010 part of the script. Comment out if you don't need this part

#Starting new Powershell session and importing it
$exsession = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://testex1.test.local/powershell -Authentication Kerberos
Import-PSSession $exsession

#Setting storage limits on the database
Set-MailboxDatabase -Identity MBDB -IssueWarningQuota 1073741824 -ProhibitSendQuota 2147483648 -ProhibitSendReceiveQuota 5368709120

#Create some mailboxes
$users | ForEach-Object {Enable-Mailbox -Identity $_.username -Alias $_.username}

#Create some distribution groups
New-DistributionGroup -Name AllUsers -OrganizationalUnit "test.local/Kemta.net/DistributionGroups" -SamAccountName AllUsers -Alias AllUsers
$Groups | ForEach-Object {New-DistributionGroup -Name $_.distribution -OrganizationalUnit "test.local/Kemta.net/DistributionGroups" -SamAccountName $_.distribution -Alias $_.distribution}

#Add the users to their respective distribution groups
$users | ForEach-Object {Add-DistributionGroupMember  -Identity $_.department -Member $_.username}
$users | ForEach-Object {Add-DistributionGroupMember  -Identity AllUsers -Member $_.username}

#Showing som info to the user
Write-Host "Some more or less usefull information:" -ForegroundColor "green"
Write-Host ""
Write-Host "OUs created:" -ForegroundColor "green"
(Get-ADOrganizationalUnit -filter {whencreated -ge $ScriptStarted }).count
Write-Host " "
Write-Host "Users created:" -ForegroundColor "green"
(Get-ADUser -filter {whencreated -ge $ScriptStarted }).count
Write-Host ""
Write-Host "Homefolders created:" -ForegroundColor "green"
$HomefoldersCreated = (Get-ChildItem e:homedir | Where-Object {$_.CreationTime -ge $ScriptStarted})
$HomefoldersCreated.count
Write-Host ""
Write-Host "Mailboxes created:" -ForegroundColor "green"
$MailboxesCreated = (Get-Mailbox | Where-Object {$_.WhenCreated -ge $ScriptStarted})
$MailboxesCreated.count
Write-Host ""
Write-Host "Distributions groups created:" -ForegroundColor "green"
$DistributionGroupsCreated = (Get-DistributionGroup | Where-Object {$_.WhenCreated -ge $ScriptStarted})
$DistributionGroupsCreated.count
Write-Host ""
write-host "Time taken:" -ForegroundColor "green"
$elapsedtime.elapsed | select hours, minutes, seconds
Write-Host ""
Write-Host "Lines of code run:" -ForegroundColor "green"
(Get-Content $Scriptpathpopulate-ad.ps1).Length
Write-Host ""
write-host "All done :)" -ForegroundColor "green"
Write-Host ""
Write-Host "Script stopped at $(get-date)" -ForegroundColor "green"
Write-Host "Press any key to exit" -ForegroundColor "green"

#Make the windows a little bigger so the user can see all the info presented
$PSWindowSize = $UI.WindowSize
$PSWindowSize.Height = 32
$UI.WindowSize = $PSWindowSize

#Write a small log file containing the same info as presented
New-Item -path $ScriptPath -name log.txt
add-content $scriptPathlog.txt -encoding ASCII "OUs created:"
(Get-ADOrganizationalUnit -filter {whencreated -ge $ScriptStarted }).count | out-file $ScriptPathlog.txt -append -encoding ASCII
add-content $scriptPathlog.txt -encoding ASCII "Users created:"
(Get-ADUser -filter {whencreated -ge $ScriptStarted }).count | out-file $ScriptPathlog.txt -append -encoding ASCII
add-content $scriptPathlog.txt -encoding ASCII "Homefolders created:"
$HomefoldersCreated = (Get-ChildItem e:homedir | Where-Object {$_.CreationTime -ge $ScriptStarted})
$HomefoldersCreated.count | out-file $ScriptPathlog.txt -append -encoding ASCII
add-content $scriptPathlog.txt -encoding ASCII "Mailboxes created:"
$MailboxesCreated = (Get-Mailbox | Where-Object {$_.WhenCreated -ge $ScriptStarted})
$MailboxesCreated.count | out-file $ScriptPathlog.txt -append -encoding ASCII
add-content $scriptPathlog.txt -encoding ASCII "Distributions groups created:"
$DistributionGroupsCreated = (Get-DistributionGroup | Where-Object {$_.WhenCreated -ge $ScriptStarted})
$DistributionGroupsCreated.count | out-file $ScriptPathlog.txt -append -encoding ASCII
add-content $scriptPathlog.txt -encoding ASCII "Time taken:"
$elapsedtime.elapsed | select hours, minutes, seconds | Out-File $ScriptPathlog.txt -append -encoding ASCII
add-content $scriptPathlog.txt -encoding ASCII "Lines of code run:"
(Get-Content $Scriptpathpopulate-ad.ps1).Length | out-file $ScriptPathlog.txt -append -encoding ASCII

#Disconnecting from Exchange
Remove-PSSession $exsession

cmd /c pause | out-null</pre>

&nbsp;