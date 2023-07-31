---
title: 'Powershell: Listing activated clients on KMS server'
author: nerenther
type: post
date: 2014-08-26T07:14:29+00:00
url: /index.php/2014/08/26/powershell-listing-activated-clients-on-kms-server/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:1372:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">$<span style="color: #000000;">&#40;</span><span style="color: #0000FF;">foreach</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$entry</span> <span style="color: #0000FF;">in</span> <span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Get-EventLog</span> <span style="color: #008080; font-style: italic;">-Logname</span> <span style="color: #800000;">&quot;Key Management Service&quot;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span><span style="color: #800080;">$entry</span>.ReplacementStrings<span style="color: #000000;">&#91;</span><span style="color: #804000;">3</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#125;</span><span style="color: #000000;">&#41;</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">sort-object</span> <span style="color: #008080; font-style: italic;">-Unique</span></pre></td></tr></table><p class="theCode" style="display:none;">$(foreach ($entry in (Get-EventLog -Logname &quot;Key Management Service&quot;)) {$entry.ReplacementStrings[3]}) | sort-object -Unique</p></div>
    ";}
categories:
  - Microsoft
  - Powershell
tags:
  - get-eventlog
  - KMS
  - Powershell

---
If you are using a KMS server for activating servers and clients in your environment, you may have noticed that there&#8217;s really no obvious way to get a list of all the clients that have been activated by the KMS server.

One way to get that overview is by using VAMT (<a href="http://technet.microsoft.com/en-us/library/hh824953.aspx" target="_blank" rel="noopener">http://technet.microsoft.com/en-us/library/hh824953.aspx</a>), but since that tool is based on pulling info from clients and not from the KMS server it is not suitable for everyone.

Thankfully, there&#8217;s PowerShell 🙂  
Getting a list of all activated KMS clients through PowerShell is actually a simple one-liner:

<pre lang="PowerShell">$(foreach ($entry in (Get-EventLog -Logname "Key Management Service")) {$entry.ReplacementStrings[3]}) | sort-object -Unique</pre>

What this does is look through the Key Management Service eventlog, grab only the client name and then remove all duplicates (since a client activates itself at regular intervals, there will be duplicates).