---
title: Install and configure Exchange 2010 using Powershell
author: nerenther
 
date: 2011-09-29T06:51:38+00:00
url: /index.php/2011/09/29/install-and-configure-exchange-2010-using-powershell/
wp-syntax-cache-content:
  - |
    a:12:{i:1;s:298:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">import<span style="color: pink;">-</span>module servermanager ```</td></tr></table><p class="theCode" style="display:none;">import-module servermanager</p></div>
    ";i:2;s:2250:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">Add<span style="color: pink;">-</span>WindowsFeature Web<span style="color: pink;">-</span>Metabase<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Lgcy<span style="color: pink;">-</span>Mgmt<span style="color: pink;">-</span>Console<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Server<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>ISAPI<span style="color: pink;">-</span>Ext<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Metabase<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Lgcy<span style="color: pink;">-</span>Mgmt<span style="color: pink;">-</span>Console<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Basic<span style="color: pink;">-</span>Auth<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>ASP<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Digest<span style="color: pink;">-</span>Auth<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Windows<span style="color: pink;">-</span>Auth<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Dyn<span style="color: pink;">-</span>Compression<span style="color: pink;">,</span> Web<span style="color: pink;">-</span>Net<span style="color: pink;">-</span>Ext<span style="color: pink;">,</span> RPC<span style="color: pink;">-</span>over<span style="color: pink;">-</span>HTTP<span style="color: pink;">-</span>proxy<span style="color: pink;">,</span> AS<span style="color: pink;">-</span>NET<span style="color: pink;">-</span>Framework<span style="color: pink;">,</span> NET<span style="color: pink;">-</span>HTTP<span style="color: pink;">-</span>Activation ```</td></tr></table><p class="theCode" style="display:none;">Add-WindowsFeature Web-Metabase, Web-Lgcy-Mgmt-Console, Web-Server, Web-ISAPI-Ext, Web-Metabase, Web-Lgcy-Mgmt-Console, Web-Basic-Auth, Web-ASP, Web-Digest-Auth, Web-Windows-Auth, Web-Dyn-Compression, Web-Net-Ext, RPC-over-HTTP-proxy, AS-NET-Framework, NET-HTTP-Activation</p></div>
    ";i:3;s:427:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008080; font-weight: bold;">Set-service</span> NetTcpPortSharing <span style="color: #008080; font-style: italic;">-startuptype</span> automatic ```</td></tr></table><p class="theCode" style="display:none;">Set-service NetTcpPortSharing -startuptype automatic</p></div>
    ";i:4;s:360:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">.setup <span style="color: pink;">/</span>PrepareAD <span style="color: pink;">/</span>OrganizationName:Kemta ```</td></tr></table><p class="theCode" style="display:none;">.setup /PrepareAD /OrganizationName:Kemta</p></div>
    ";i:5;s:424:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">Import<span style="color: pink;">-</span>Module ServerManager
    Add<span style="color: pink;">-</span>WindowsFeature RSAT<span style="color: pink;">-</span>ADDS ```</td></tr></table><p class="theCode" style="display:none;">Import-Module ServerManager
    Add-WindowsFeature RSAT-ADDS</p></div>
    ";i:6;s:364:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">.setup  <span style="color: pink;">/</span>PrepareAD <span style="color: pink;">/</span>OrganizationName:Kemta ```</td></tr></table><p class="theCode" style="display:none;">.setup  /PrepareAD /OrganizationName:Kemta</p></div>
    ";i:7;s:426:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">.setup.com <span style="color: pink;">/</span>mode:install <span style="color: pink;">/</span>roles:mb<span style="color: pink;">,</span>ht<span style="color: pink;">,</span>ca ```</td></tr></table><p class="theCode" style="display:none;">.setup.com /mode:install /roles:mb,ht,ca</p></div>
    ";i:8;s:388:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008080; font-weight: bold;">Add-PSSnapin</span>  Microsoft.Exchange.Management.PowerShell.E2010 ```</td></tr></table><p class="theCode" style="display:none;">Add-PSSnapin  Microsoft.Exchange.Management.PowerShell.E2010</p></div>
    ";i:9;s:656:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">new<span style="color: pink;">-</span>AcceptedDomain <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #800000;">'Kemta.net'</span> <span style="color: pink;">-</span>DomainName <span style="color: #800000;">'Kemta.net'</span> <span style="color: pink;">-</span>DomainType <span style="color: #800000;">'Authoritative'</span> ```</td></tr></table><p class="theCode" style="display:none;">new-AcceptedDomain -Name 'Kemta.net' -DomainName 'Kemta.net' -DomainType 'Authoritative'</p></div>
    ";i:10;s:1438:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">new<span style="color: pink;">-</span>SendConnector <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #800000;">'Internet'</span> <span style="color: pink;">-</span>Usage <span style="color: #800000;">'Internet'</span> <span style="color: pink;">-</span>AddressSpaces <span style="color: #800000;">'SMTP:*;1'</span> <span style="color: pink;">-</span>IsScopedConnector <span style="color: #800080;">$false</span> <span style="color: pink;">-</span>DNSRoutingEnabled <span style="color: #800080;">$false</span> <span style="color: pink;">-</span>SmartHosts <span style="color: #800000;">'smarthost.kemta.net'</span> <span style="color: pink;">-</span>SmartHostAuthMechanism <span style="color: #800000;">'None'</span> <span style="color: pink;">-</span>UseExternalDNSServersEnabled <span style="color: #800080;">$false</span> <span style="color: pink;">-</span>SourceTransportServers <span style="color: #800000;">'TESTEX1'</span> ```</td></tr></table><p class="theCode" style="display:none;">new-SendConnector -Name 'Internet' -Usage 'Internet' -AddressSpaces 'SMTP:*;1' -IsScopedConnector $false -DNSRoutingEnabled $false -SmartHosts 'smarthost.kemta.net' -SmartHostAuthMechanism 'None' -UseExternalDNSServersEnabled $false -SourceTransportServers 'TESTEX1'</p></div>
    ";i:11;s:1814:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">new<span style="color: pink;">-</span>EmailAddressPolicy <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #800000;">'Kemta.net'</span> <span style="color: pink;">-</span>RecipientContainer <span style="color: #800000;">'test.local/Kemta.net'</span> <span style="color: pink;">-</span>IncludedRecipients <span style="color: #800000;">'AllRecipients'</span> <span style="color: pink;">-</span>Priority <span style="color: #800000;">'Lowest'</span> <span style="color: pink;">-</span>EnabledEmailAddressTemplates <span style="color: #800000;">'SMTP:%g.%s@Kemta.net'</span>
    new<span style="color: pink;">-</span>EmailAddressPolicy <span style="color: #008080; font-style: italic;">-Name</span> <span style="color: #800000;">'hr.kemta.net'</span> <span style="color: pink;">-</span>RecipientContainer <span style="color: #800000;">'test.local/Kemta.net/Users/HR'</span> <span style="color: pink;">-</span>IncludedRecipients <span style="color: #800000;">'AllRecipients'</span> <span style="color: pink;">-</span>Priority <span style="color: #800000;">'1'</span> <span style="color: pink;">-</span>EnabledEmailAddressTemplates <span style="color: #800000;">'SMTP:%g.%s@Kemta.net'</span> ```</td></tr></table><p class="theCode" style="display:none;">new-EmailAddressPolicy -Name 'Kemta.net' -RecipientContainer 'test.local/Kemta.net' -IncludedRecipients 'AllRecipients' -Priority 'Lowest' -EnabledEmailAddressTemplates 'SMTP:%g.%s@Kemta.net'
    new-EmailAddressPolicy -Name 'hr.kemta.net' -RecipientContainer 'test.local/Kemta.net/Users/HR' -IncludedRecipients 'AllRecipients' -Priority '1' -EnabledEmailAddressTemplates 'SMTP:%g.%s@Kemta.net'</p></div>
    ";i:12;s:344:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;">New<span style="color: pink;">-</span>DistributionGroup
    New<span style="color: pink;">-</span>Mailbox ```</td></tr></table><p class="theCode" style="display:none;">New-DistributionGroup
    New-Mailbox</p></div>
    ";}
categories:
  - Exchange
  - Microsoft
  - Powershell
tags:
  - Exchange
  - microsoft
  - Powershell

---
In this guide I will show you how to install and configure a simple Exchange 2010 environment using no gui at all.  
Installing exchange 2010 without gui may seem kinda nerdy, but it's quite useful for quickly setting up a test environment for example.

Remember to run Windows update prior to the installation.

Start powershell as administrator and type:

 ```
 import-module servermanager 
 ```

First we need to install all of the prerequisites:

 ```
 Add-WindowsFeature Web-Metabase, Web-Lgcy-Mgmt-Console, Web-Server, Web-ISAPI-Ext, Web-Metabase, Web-Lgcy-Mgmt-Console, Web-Basic-Auth, Web-ASP, Web-Digest-Auth, Web-Windows-Auth, Web-Dyn-Compression, Web-Net-Ext, RPC-over-HTTP-proxy, AS-NET-Framework, NET-HTTP-Activation 
 ```

We also need to set the NetTcpPortSharing service to automatic start, the command for this is:

 ```
 Set-service NetTcpPortSharing -startuptype automatic 
 ```

If you already haven't you need to raise the forest functional level to at least Windows Server 2003 native.

Before you start to install Exchange you need to prepare your Schema. If you are installing exchange on a domain controller, all you need to do is navigate to the exchange installation media and run this command:

 ```
 .setup /PrepareAD /OrganizationName:Kemta 
 ```

PS: You probably want to change /OrganizationName to something better 🙂

If your soon-to-be exchange server isn't a domain controller you have to choices:

  * Copy the exchange installation files to a domain controller and run the above command
  * Install RSAT for ActiveDirectory on your soon-to-be exchange server

If you are going for the lather you need to run the following commands to install RSAT:

 ```
 Import-Module ServerManager
Add-WindowsFeature RSAT-ADDS 
```

Reboot your server and run the following command to prepare the schema:

 ```
 .setup  /PrepareAD /OrganizationName:Kemta 
 ```

After the schema is updated you can install exchange 2010, the command for installing the hub, cas and mailbox role is:

 ```
 .setup.com /mode:install /roles:mb,ht,ca 
 ```

There you go! Exchange should now be successfully installed.

However, there is still a few things you should configure. You can perform these next tasks by starting the Exchange Management Shell or by adding the pssnapin for exchange using this command:

 ```
 Add-PSSnapin  Microsoft.Exchange.Management.PowerShell.E2010 
 ```

Then you can create these things:  
A new Accepted domain:

 ```
 new-AcceptedDomain -Name 'Kemta.net' -DomainName 'Kemta.net' -DomainType 'Authoritative' 
 ```

A send connector:

 ```
 new-SendConnector -Name 'Internet' -Usage 'Internet' -AddressSpaces 'SMTP:*;1' -IsScopedConnector $false -DNSRoutingEnabled $false -SmartHosts 'smarthost.kemta.net' -SmartHostAuthMechanism 'None' -UseExternalDNSServersEnabled $false -SourceTransportServers 'TESTEX1' 
 ```

Maybe some email address policies:

 ```
 new-EmailAddressPolicy -Name 'Kemta.net' -RecipientContainer 'test.local/Kemta.net' -IncludedRecipients 'AllRecipients' -Priority 'Lowest' -EnabledEmailAddressTemplates 'SMTP:%g.%s@Kemta.net'
new-EmailAddressPolicy -Name 'hr.kemta.net' -RecipientContainer 'test.local/Kemta.net/Users/HR' -IncludedRecipients 'AllRecipients' -Priority '1' -EnabledEmailAddressTemplates 'SMTP:%g.%s@Kemta.net' 
```

That should just about do it! Your Exchange server should now be fully functioning!  
There is no users, distribution groups and such, but you can use these cmdlets to create them:

 ```
New-DistributionGroup
New-Mailbox 
```