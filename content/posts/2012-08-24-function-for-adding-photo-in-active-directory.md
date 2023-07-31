---
title: Function for adding photo in Active Directory
author: nerenther
 
date: 2012-08-24T13:16:30+00:00
url: /index.php/2012/08/24/function-for-adding-photo-in-active-directory/
categories:
  - Active Directory
  - Microsoft
  - Powershell
tags:
  - function
  - microsoft
  - Powershell
  - Set-ADPhoto

---
I have always been careful to avoid the really advanced and cool stuff in Powershell, like functions, arrays and such.

But as I created the last script it hit me that it would be really cool to have it in a command, like set-adphoto. After some googling I found that funtions aren&#8217;t hard at all!

Basically all I really had to do with the ad photo import script was to add &#8220;function Set-ADPhoto { &#8221; in front of the script and end it with a }

But since I already was at it I decided to to a little more, I added some argument handling and a little help file.

Here is the result:

 ```
 function Set-ADPhoto ($user,$photopath) {
Import-Module active*

$error = "The file is bigger than 12KB. Shrink it or choose another file"
$file = Get-Item "$photopath"
$filesize = $file.length/1KB



if ($filesize -gt 12)
    {
    Write-Host $error
        }
else {
    $photo = [byte[]](get-content $file -Encoding byte)
    Set-ADUser $user -Replace @{thumbnailPhoto=$photo}
        }
<#
.SYNOPSIS
This function will add a photo to a users Active Directory user object. It also verifies that the file is less than 12KB
.DESCRIPTION
This funtion checks the filesize of the file given. If it is too big it will output an error message.
If the file is less than 12KB it will add the given file to the given users thumbnailPhoto attribute in Active Directory
.EXAMPLE
Set-ADPhoto username p:photo.jpg
Will set the thumbnailPhoto attribute for the user username to the content of p:photo.jpg
.NOTES
.LINK
http://cloud.kemta.net/2012/08/function-for-adding-photo-in-active-directory
#>
}
 ```

&nbsp;