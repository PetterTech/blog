---
title: Install and configure Exchange 2010 using Powershell
date: 2011-09-29T06:51:38+00:00
url: /index.php/2011/09/29/install-and-configure-exchange-2010-using-powershell/
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

 ```powershell
 import-module servermanager 
 ```

First we need to install all of the prerequisites:

 ```powershell
 Add-WindowsFeature Web-Metabase, Web-Lgcy-Mgmt-Console, Web-Server, Web-ISAPI-Ext, Web-Metabase, Web-Lgcy-Mgmt-Console, Web-Basic-Auth, Web-ASP, Web-Digest-Auth, Web-Windows-Auth, Web-Dyn-Compression, Web-Net-Ext, RPC-over-HTTP-proxy, AS-NET-Framework, NET-HTTP-Activation 
 ```

We also need to set the NetTcpPortSharing service to automatic start, the command for this is:

 ```powershell
 Set-service NetTcpPortSharing -startuptype automatic 
 ```

If you already haven't you need to raise the forest functional level to at least Windows Server 2003 native.

Before you start to install Exchange you need to prepare your Schema. If you are installing exchange on a domain controller, all you need to do is navigate to the exchange installation media and run this command:

 ```powershell
 .setup /PrepareAD /OrganizationName:Kemta 
 ```

PS: You probably want to change /OrganizationName to something better 🙂

If your soon-to-be exchange server isn't a domain controller you have to choices:

  * Copy the exchange installation files to a domain controller and run the above command
  * Install RSAT for ActiveDirectory on your soon-to-be exchange server

If you are going for the lather you need to run the following commands to install RSAT:

 ```powershell
 Import-Module ServerManager
Add-WindowsFeature RSAT-ADDS 
```

Reboot your server and run the following command to prepare the schema:

 ```powershell
 .setup  /PrepareAD /OrganizationName:Kemta 
 ```

After the schema is updated you can install exchange 2010, the command for installing the hub, cas and mailbox role is:

 ```powershell
 .setup.com /mode:install /roles:mb,ht,ca 
 ```

There you go! Exchange should now be successfully installed.

However, there is still a few things you should configure. You can perform these next tasks by starting the Exchange Management Shell or by adding the pssnapin for exchange using this command:

 ```powershell
 Add-PSSnapin  Microsoft.Exchange.Management.PowerShell.E2010 
 ```

Then you can create these things:  
A new Accepted domain:

 ```powershell
 new-AcceptedDomain -Name 'Kemta.net' -DomainName 'Kemta.net' -DomainType 'Authoritative' 
 ```

A send connector:

 ```powershell
 new-SendConnector -Name 'Internet' -Usage 'Internet' -AddressSpaces 'SMTP:*;1' -IsScopedConnector $false -DNSRoutingEnabled $false -SmartHosts 'smarthost.kemta.net' -SmartHostAuthMechanism 'None' -UseExternalDNSServersEnabled $false -SourceTransportServers 'TESTEX1' 
 ```

Maybe some email address policies:

 ```powershell
 new-EmailAddressPolicy -Name 'Kemta.net' -RecipientContainer 'test.local/Kemta.net' -IncludedRecipients 'AllRecipients' -Priority 'Lowest' -EnabledEmailAddressTemplates 'SMTP:%g.%s@Kemta.net'
new-EmailAddressPolicy -Name 'hr.kemta.net' -RecipientContainer 'test.local/Kemta.net/Users/HR' -IncludedRecipients 'AllRecipients' -Priority '1' -EnabledEmailAddressTemplates 'SMTP:%g.%s@Kemta.net' 
```

That should just about do it! Your Exchange server should now be fully functioning!  
There is no users, distribution groups and such, but you can use these cmdlets to create them:

 ```powershell
New-DistributionGroup
New-Mailbox 
```