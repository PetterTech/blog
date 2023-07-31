---
title: Simple script for adding user photo in Active Directory
author: nerenther
 
date: 2012-08-16T12:24:00+00:00
url: /index.php/2012/08/16/simple-script-for-adding-user-photo-in-active-directory/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:4324:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008000;">#Imports the Active Directory module</span>
    Import<span style="color: pink;">-</span>Module active<span style="color: pink;">*</span>
    &nbsp;
    <span style="color: #008000;">#Asks the user for a filename</span>
    <span style="color: #800080;">$photopath</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Read-Host</span> <span style="color: #800000;">&quot;Please input filepath and filename&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Converts the users input to an object</span>
    <span style="color: #800080;">$file</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Get-Item</span> <span style="color: #800000;">&quot;$photopath&quot;</span>
    &nbsp;
    <span style="color: #008000;">#Calculates the filesize</span>
    <span style="color: #800080;">$filesize</span> <span style="color: pink;">=</span> <span style="color: #800080;">$file</span>.length<span style="color: pink;">/</span>1KB
    &nbsp;
    <span style="color: #008000;">#If the file is largers than 12KB you get a message stating that the file is too large</span>
    <span style="color: #008000;">#If the file is smaller than 12KB it asks for a username and imports the file to Active Directory</span>
    <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$filesize</span> <span style="color: #FF0000;">-gt</span> <span style="color: #804000;">12</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Filesize to large, shrink it to under 12KB and try again&quot;</span>
    <span style="color: #000000;">&#125;</span>
    <span style="color: #0000FF;">else</span> <span style="color: #000000;">&#123;</span>
    <span style="color: #800080;">$user</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Read-Host</span> <span style="color: #800000;">&quot;Please input username&quot;</span>
    <span style="color: #800080;">$photo</span> <span style="color: pink;">=</span> <span style="color: #000000;">&#91;</span><span style="color: #008080;">byte</span><span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">get-content</span> <span style="color: #800080;">$file</span> <span style="color: #008080; font-style: italic;">-Encoding</span> byte<span style="color: #000000;">&#41;</span>
    Set<span style="color: pink;">-</span>ADUser <span style="color: #800080;">$user</span> <span style="color: #FF0000;">-Replace</span> <span style="color: pink;">@</span><span style="color: #000000;">&#123;</span>thumbnailPhoto<span style="color: pink;">=</span><span style="color: #800080;">$photo</span><span style="color: #000000;">&#125;</span>
    <span style="color: #008080; font-weight: bold;">Write-host</span> <span style="color: #800000;">&quot;All done&quot;</span>
    <span style="color: #000000;">&#125;</span>
    &nbsp;
    cmd <span style="color: pink;">/</span>c pause <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">out-null</span> ```</td></tr></table><p class="theCode" style="display:none;">#Imports the Active Directory module
    Import-Module active*
    
    #Asks the user for a filename
    $photopath = Read-Host &quot;Please input filepath and filename&quot;
    
    #Converts the users input to an object
    $file = Get-Item &quot;$photopath&quot;
    
    #Calculates the filesize
    $filesize = $file.length/1KB
    
    #If the file is largers than 12KB you get a message stating that the file is too large
    #If the file is smaller than 12KB it asks for a username and imports the file to Active Directory
    if ($filesize -gt 12)
    {
    Write-Host &quot;Filesize to large, shrink it to under 12KB and try again&quot;
    }
    else {
    $user = Read-Host &quot;Please input username&quot;
    $photo = [byte[]](get-content $file -Encoding byte)
    Set-ADUser $user -Replace @{thumbnailPhoto=$photo}
    Write-host &quot;All done&quot;
    }
    
    cmd /c pause | out-null</p></div>
    ";}
categories:
  - Active Directory
  - Microsoft
  - Powershell
tags:
  - active directory
  - Powershell
  - script

---
It&#8217;s been a while since I posted here so I thought it might be time to add some content.

This script is a simple script that adds a photo to a user&#8217;s active directory user object. It also checks the filesize to prevent users adding large photos (you can of course change this limit).

The requirements for this script is the Active Directory module and permission to edit a user object in Active Directory

The script:

 ```
#Imports the Active Directory module
Import-Module active*

#Asks the user for a filename
$photopath = Read-Host "Please input filepath and filename"

#Converts the users input to an object
$file = Get-Item "$photopath"

#Calculates the filesize
$filesize = $file.length/1KB

#If the file is largers than 12KB you get a message stating that the file is too large
#If the file is smaller than 12KB it asks for a username and imports the file to Active Directory
if ($filesize -gt 12)
{
Write-Host "Filesize to large, shrink it to under 12KB and try again"
}
else {
$user = Read-Host "Please input username"
$photo = [byte[]](get-content $file -Encoding byte)
Set-ADUser $user -Replace @{thumbnailPhoto=$photo}
Write-host "All done"
}

cmd /c pause | out-null 
```