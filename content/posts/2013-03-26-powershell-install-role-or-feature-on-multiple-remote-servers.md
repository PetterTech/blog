---
title: 'Powershell: Install role or feature on multiple remote servers'
author: nerenther
 
date: 2013-03-26T12:48:09+00:00
url: /index.php/2013/03/26/powershell-install-role-or-feature-on-multiple-remote-servers/
wp-syntax-cache-content:
  - |
    a:2:{i:1;s:675:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$servers</span> <span style="color: pink;">=</span> Get<span style="color: pink;">-</span>ADComputer <span style="color: pink;">-</span><span style="color: #0000FF;">Filter</span> <span style="color: #800000;">'Name -like &quot;ctx_srv*&quot;'</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">select</span> name</pre></td></tr></table><p class="theCode" style="display:none;">$servers = Get-ADComputer -Filter 'Name -like &quot;ctx_srv*&quot;' | select name</p></div>
    ";i:2;s:1023:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$servers</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ForEach-Object</span> <span style="color: #000000;">&#123;</span>
     Enter<span style="color: pink;">-</span>PSSession <span style="color: #008080; font-style: italic;">-ComputerName</span> <span style="color: #000080;">$_</span>.name
     import<span style="color: pink;">-</span>module servermanager
     Add<span style="color: pink;">-</span>WindowsFeature FS<span style="color: pink;">-</span>Search<span style="color: pink;">-</span>Service
     Exit<span style="color: pink;">-</span>PSSession
     <span style="color: #000000;">&#125;</span></pre></td></tr></table><p class="theCode" style="display:none;">$servers | ForEach-Object {
     Enter-PSSession -ComputerName $_.name
     import-module servermanager
     Add-WindowsFeature FS-Search-Service
     Exit-PSSession
     }</p></div>
    ";}
categories:
  - Microsoft
  - Powershell
tags:
  - Powershell
  - Server Manager
  - Windows Server

---
Today I was presented with a task that sounded pretty boring and repetitive: Install the Windows Search service on all our citrix servers.

Now, I could just log on each and every one of our citrix servers, open Server Manager and then install the role service but where&#8217;s the fun in that?

As always Powershell is a lot more fun:

First I had to find the name of all our citrix servers. Luckily we have a strict naming convention so I could just poll Active Directory and store the names in an array:

<pre lang="Powershell">$servers = Get-ADComputer -Filter 'Name -like "ctx_srv*"' | select name</pre>

Next I only had to create a foreach loop that enters a PSSession on each of the servers and install the role service:

<pre lang="Powershell">$servers | ForEach-Object {
 Enter-PSSession -ComputerName $_.name
 import-module servermanager
 Add-WindowsFeature FS-Search-Service
 Exit-PSSession
 }</pre>

It is worth mentioning that you can&#8217;t connect to remote servers using the Enter-PSSession cmdlet if you haven&#8217;t enabled remote management, if you want to enable it you can check this guide: <a title="http://blog.powershell.no/2010/03/04/enable-and-configure-windows-powershell-remoting-using-group-policy/" href="http://blog.powershell.no/2010/03/04/enable-and-configure-windows-powershell-remoting-using-group-policy/" target="_blank" rel="noopener">http://blog.powershell.no/2010/03/04/enable-and-configure-windows-powershell-remoting-using-group-policy/</a>