---
title: 'Powershell: Creating strong passwords'
author: nerenther
 
date: 2016-05-26T10:40:20+00:00
url: /index.php/2016/05/26/powershell-creating-strong-passwords/
categories:
  - Microsoft
  - Powershell
tags:
  - password
  - Powershell
  - regex

---
A tweet from @JanEgilRing caught my eye this morning, it was showing how you can use powershell to create passwords. The link in the tweet pointed here: <a href="http://powershell.com/cs/blogs/tips/archive/2016/05/23/one-liner-random-password-generator.aspx" target="_blank" rel="noopener">http://powershell.com/cs/blogs/tips/archive/2016/05/23/one-liner-random-password-generator.aspx</a>

Seeing that line and realizing how simple it was, it got me thinking on how I could implement this in my scripts.  
The only issue I saw with that one-liner was that the passwords it creates do not necessarily comply with high complexity rules.

So, how can we approve on this?

Firstly, we need to create a regex that we can use to validate that the password created complies with our rules.  
In our environment this means 12 characters, uppercase, lowercase and either a number or special character.  
The regex I ended up with is this one: ^.\*(?=.{12,})(?=.\*\d)(?=.\*[a-z])(?=.\*[A-Z])(?=.\*[@#$%^&+=]).\*$  
(which I found here: <a href="https://nilangshah.wordpress.com/2007/06/26/password-validation-via-regular-expression/" target="_blank" rel="noopener">https://nilangshah.wordpress.com/2007/06/26/password-validation-via-regular-expression/</a> )

Now that we have our regex we can simple throw the one-liner into a while loop:

<pre lang="PowerShell">while ($pass -notmatch "^.*(?=.{12,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$") {
 $pass = -join ('abcdefghkmnrstuvwxyzABCDEFGHKLMNPRSTUVWXYZ23456789$%&*#'.ToCharArray() | Get-Random -count 12)
 }</pre>

This means that as long as the password created doesn&#8217;t comply with the regex, it creates a new one.

And guess what? It can also be written as a one-liner:

<pre lang="PowerShell">while ($pass -notmatch "^.*(?=.{12,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$") {$pass = -join ('abcdefghkmnrstuvwxyzABCDEFGHKLMNPRSTUVWXYZ23456789$%&*#'.ToCharArray() | Get-Random -count 12)}</pre>

Not exactly a simple one-liner, but a one-liner still 🙂