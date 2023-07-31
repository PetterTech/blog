---
title: Resetting the Discretionary Access Control List (DACL) in a Windows Service security descriptor
author: ricmik
 
date: 2013-01-14T12:00:42+00:00
url: /index.php/2013/01/14/resetting-the-discretionary-access-control-list-dacl-in-a-windows-service-security-descriptor/
wp-syntax-cache-content:
  - |
    a:3:{i:1;s:273:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="reg" style="font-family:monospace;">HKLMSYSTEMCurrentControlSetServices ```</td></tr></table><p class="theCode" style="display:none;">HKLMSYSTEMCurrentControlSetServices</p></div>
    ";i:2;s:237:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="dos" style="font-family:monospace;">PsExec.exe /s cmd ```</td></tr></table><p class="theCode" style="display:none;">PsExec.exe /s cmd</p></div>
    ";i:3;s:654:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="dos" style="font-family:monospace;">sc sdset service_name D:<span style="color: #33cc33;">(</span>A;;CCLCSWRPWPDTLOCRRC;;;SY<span style="color: #33cc33;">)(</span>A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA<span style="color: #33cc33;">)(</span>A;;CCLCSWLOCRRC;;;IU<span style="color: #33cc33;">)(</span>A;;CCLCSWLOCRRC;;;SU<span style="color: #33cc33;">)</span> ```</td></tr></table><p class="theCode" style="display:none;">sc sdset service_name D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)</p></div>
    ";}
categories:
  - Microsoft
tags:
  - 2008R2
  - Access List
  - ACL
  - DACL
  - PsExec
  - PsTools
  - registry
  - Windows Server

---
#### OpenService FAILED 5: Access is denied. &#8212; &#8220;Oh crap!&#8221;

If you ever see this error and need to reset the DACL on a Windows service, let&#8217;s say in case you (or someone else) accidentally deletes it, or configure it to something that prevents you from reading it&#8217;s security settings, this might do the trick:

First of all, get a cup of coffee.

Download PsExec (a tool in [PsTools][1]), which among other things allow you  to run commands as the &#8220;local system&#8221; account.  
Find out what the real name of the service is by looking in the following registry key:

```
HKLMSYSTEMCurrentControlSetServices 
```

The real name (not the display name) of the service is the name of the key itself.

Start a Command Prompt (cmd) window as administrator.  
Start a new cmd session as the system account:

```
PsExec.exe /s cmd 
```

Now it&#8217;s time to set a new DACL, this is done by using the command &#8220;sc sdset&#8221; followed by the service name and the new security descriptor using SDDL-format (Security Descriptor Definition Language). If you are unsure what parameters to use here, you can either run &#8220;sc sdshow&#8221; on another service that most likely are configured the same way as the service you are changing were, or try the command in the example below.

The command below will give access to Local System (SY), Built-in administrators (BA), Interactively logged-on user (IU) and Service logon user (SU).

```
sc sdset service_name D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU) 
```

You should be looking at the relieving message: [SC] SetServiceObjectSecurity SUCCESS

Now, enjoy your coffee 😉

&nbsp;

&#8211;ricmik

 [1]: http://technet.microsoft.com/en-us/sysinternals/bb896649.aspx