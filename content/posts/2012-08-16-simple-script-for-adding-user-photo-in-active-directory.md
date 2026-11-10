---
title: Simple script for adding user photo in Active Directory
date: 2012-08-16T12:24:00+00:00
url: /index.php/2012/08/16/simple-script-for-adding-user-photo-in-active-directory/
categories:
  - Active Directory
  - Microsoft
  - Powershell
tags:
  - active directory
  - Powershell
  - script
---
It's been a while since I posted here so I thought it might be time to add some content.

This script is a simple script that adds a photo to a user's active directory user object. It also checks the filesize to prevent users adding large photos (you can of course change this limit).

The requirements for this script is the Active Directory module and permission to edit a user object in Active Directory

The script:

 ```powershell
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