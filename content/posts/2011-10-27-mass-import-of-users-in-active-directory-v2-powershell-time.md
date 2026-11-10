---
title: Mass import of users in Active Directory v2 – Powershell time
date: 2011-10-27T19:54:21+00:00
url: /index.php/2011/10/27/mass-import-of-users-in-active-directory-v2-powershell-time/
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
If you want a script for enabling users for lync, you can see my previous post [here](/index.php/2011/10/12/simple-powershell-script-for-enabling-users-for-lync/).

The cool thing about this script is that is pretty fast. In my test environment, consisting of two virtual machines, one domain controller and one exchange server, it took only 1 minute to create 100 users and mailboxes, 8 OUs and 5 security and distribution groups.  
I think thats quite impressive taking in consideration that the two virtual machines both run on my computer and with only 2GB ram each.

The only thing thats quite sad is that there's no powershell commands for sharing and setting share permissions in powershell 2.0. Thats why I have used one powershell 3.0 command in the script , new-smbshare. It is only used once, for sharing the homefolder root.

You can download the powershell 3.0 community preview and install it on the server you will run the script on. Or you can just comment out that command and rather share the root homefolder manually if you don't want to install powershell 3.0 on your server.

This script uses two csv files, one for groups and OUs and one for the users. You can download a zip containing all files {{< unavailable "File no longer available" >}}

Anyway, the script is shown below, have fun with it 🙂

 ```powershell
#Change the window title
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

cmd /c pause | out-null 
```
