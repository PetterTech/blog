---
title: Function for locating an email address
date: 2012-08-28T10:41:15+00:00
url: /index.php/2012/08/28/function-for-locating-an-email-address/
categories:
  - Exchange
  - Microsoft
  - Powershell
tags:
  - Exchange
  - function
  - Get-EmailAddress
  - Powershell
---
Yesterday I was given a relatively easy task: find out who or what has a given email address.

As this was within our own Exchange organization it proved to be quite simple:

You can achieve the goal with a simple one-liner:

 ```powershell
 get-recipient -ResultSize unlimited | where {$_.emailaddresses -match "email@address.com"}

 ```

But wouldn't it be easier to have it in a function? In Powershell, creating functions isn't all that hard. Basically all you need to do is wrap the command or script block with a function statement, see here:

 ```powershell
function Get-EmailAddress ($emailaddress)
{
Get-Recipient -ResultSize unlimited | where {$_.emailaddresses -match "$emailaddress"}
}

 ```

See how easy that was?  
First you tell powershell that you want to configure a function, then the command you want to associate the function with. Within the ( ) you define what parameters the function will need. Then there's only a { to start defining what the function will do and a } to end the function.

Now all you have to do in order to find out who or what has a given email address is:

 ```powershell
Get-EmailAddress somone@company.com

 ```

That will tell you what object has the email address and what kind of object it is (UserMailbox, PublicFolder etc.)