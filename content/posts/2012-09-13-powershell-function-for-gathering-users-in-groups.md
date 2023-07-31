---
title: Powershell function for gathering users in groups
author: nerenther
 
date: 2012-09-13T12:02:13+00:00
url: /index.php/2012/09/13/powershell-function-for-gathering-users-in-groups/
categories:
  - Active Directory
  - Microsoft
  - Powershell
tags:
  - active directory
  - function
  - Get-MembersInADGroups
  - Powershell

---
A friend of mine asked me a couple of days ago if I knew a way to gather users who are members of given groups. I thought to myself &#8220;Hmm, challenge accepted!&#8221; and started writing a small powershell script.

After he confirmed that the script worked as planned I decided to make a function of it (Yes, I know it has been a lot of them on this blog lately).  
The function accepts two parameters: GroupNames and Filelocation. In addition there is an optional switch called KeepCSV.  
Rest of the function isn&#8217;t that interesting, if you want to use it you can always consult the help (get-help get-membersinadgroups) that I actually have created 🙂

Heres the code:

```
function Get-MembersInADGroups
 {
 Param
 (
 [parameter(Mandatory=$True)][string[]]$GroupNames,
 [parameter(Mandatory=$True)][string[]]$Filelocation,
 [switch]$KeepCSV
 )
 Get-ADGroup -LDAPFilter "(name=$GroupNames)" | export-csv $FileLocationtemp.csv -NoTypeInformation

 $groups = Import-Csv $FileLocationtemp.csv

 $groups | ForEach-Object {
 $groupname = $_.SamAccountname
 Get-ADGroupMember -Identity $_.SamAccountName | select-object name,samaccountname | Out-File $Filelocation$groupname.txt -Encoding utf8
 }
 if ($KeepCSV)
    {
    Write-Host "CSV file is now saved as $filelocationtemp.csv"
    }
 Else
    {
    Remove-Item $FileLocationtemp.csv
    }
 &lt;#
 .Synopsis
 Gathers members in given group(s) and puts the result in txt files
 .Description
 This function will gather all users in the group(s) you specify and write a txt file for each group containing the users who are member of that group. The function accepts wildcards in group name
 .Parameter Groupnames
 This parameter defines what group(s) to look for
 .Parameter FileLocation
 This parameter defines where the output files should be saved
 .Parameter KeepCSV
 Defining this switch will not delete the temp.csv file containing the groups which are polled
 .Example
 Get-MembersInADGroups -GroupNames some_group -Filelocation c:test
 This command will poll Active Directory for the members of some_group and write a file called some_group.txt in c:test
 .Example
 Get-MembersInADGroups -GroupNames some_group* -Filelocation c:test
 This command will poll Active Directory for members of groups whose name begins with some_group and write a txt file for each of them in c:test
 .Link
 http://cloud.kemta.net
 #>
 } 
```

PS: the function requires that you already have loaded the Active Directory module in powershell