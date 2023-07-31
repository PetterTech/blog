---
title: Function for locating an email address
author: nerenther
type: post
date: 2012-08-28T10:41:15+00:00
url: /index.php/2012/08/28/function-for-locating-an-email-address/
wp-syntax-cache-content:
  - |
    a:3:{i:1;s:744:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">get<span style="color: pink;">-</span>recipient <span style="color: pink;">-</span>ResultSize unlimited <span style="color: pink;">|</span> <span style="color: #0000FF;">where</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.emailaddresses <span style="color: #FF0000;">-match</span> <span style="color: #800000;">&quot;email@address.com&quot;</span><span style="color: #000000;">&#125;</span></pre></td></tr></table><p class="theCode" style="display:none;">get-recipient -ResultSize unlimited | where {$_.emailaddresses -match &quot;email@address.com&quot;}</p></div>
    ";i:2;s:1102:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #0000FF;">function</span> Get<span style="color: pink;">-</span>EmailAddress <span style="color: #000000;">&#40;</span><span style="color: #800080;">$emailaddress</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    Get<span style="color: pink;">-</span>Recipient <span style="color: pink;">-</span>ResultSize unlimited <span style="color: pink;">|</span> <span style="color: #0000FF;">where</span> <span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.emailaddresses <span style="color: #FF0000;">-match</span> <span style="color: #800000;">&quot;$emailaddress&quot;</span><span style="color: #000000;">&#125;</span>
    <span style="color: #000000;">&#125;</span></pre></td></tr></table><p class="theCode" style="display:none;">function Get-EmailAddress ($emailaddress)
    {
    Get-Recipient -ResultSize unlimited | where {$_.emailaddresses -match &quot;$emailaddress&quot;}
    }</p></div>
    ";i:3;s:348:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">Get<span style="color: pink;">-</span>EmailAddress somone<span style="color: pink;">@</span>company.com</pre></td></tr></table><p class="theCode" style="display:none;">Get-EmailAddress somone@company.com</p></div>
    ";}
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

<pre lang="powershell">get-recipient -ResultSize unlimited | where {$_.emailaddresses -match "email@address.com"}

</pre>

But wouldn&#8217;t it be easier to have it in a function? In Powershell, creating functions isn&#8217;t all that hard. Basically all you need to do is wrap the command or script block with a function statement, see here:

<pre lang="powershell">function Get-EmailAddress ($emailaddress)
{
Get-Recipient -ResultSize unlimited | where {$_.emailaddresses -match "$emailaddress"}
}

</pre>

See how easy that was?  
First you tell powershell that you want to configure a function, then the command you want to associate the function with. Within the ( ) you define what parameters the function will need. Then there&#8217;s only a { to start defining what the function will do and a } to end the function.

Now all you have to do in order to find out who or what has a given email address is:

<pre lang="powershell">Get-EmailAddress somone@company.com

</pre>

That will tell you what object has the email address and what kind of object it is (UserMailbox, PublicFolder etc.)