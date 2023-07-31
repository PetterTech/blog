---
title: 'PowerCLI: Locate a MAC-address in vCenter'
author: nerenther
 
date: 2013-10-23T09:50:09+00:00
url: /index.php/2013/10/23/powercli-locate-a-mac-address-in-vcenter/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - function
  - get-macaddress
  - get-vm
  - powercli
  - Powershell
  - vmware

---
To find out to which vm a MAC address belongs, you can use a simple one-liner:

<pre lang="Powershell">Get-vm | Select Name, @{N=“Network“;E={$_ | Get-networkAdapter | ? {$_.macaddress -eq“00:50:56:A4:22:F4“}}} |Where {$_.Network-ne “”}</pre>

(Courtesy of this page: <a href="http://www.virtu-al.net/2009/07/07/powercli-more-one-liner-power/" target="_blank" rel="noopener">http://www.virtu-al.net/2009/07/07/powercli-more-one-liner-power/</a> )

Thats really great, and you can easily extend the one-liner to include more data if you like. But for someone who isn&#8217;t comfortable with using PowerCLI yet, it can seem a bit terrifying. Therefore I usually create functions for long one-liners like this one.

A basic function doing the same thing can look something like this:

<pre lang="Powershell">function Get-MACAddress ($MAC)
 {
 Get-vm | Select Name,Folder,PowerState, @{N="Network";E={$_ | Get-networkAdapter | ? {$_.macaddress -eq $MAC}}} | Where {$_.Network-ne ""}
 }</pre>

That way, it enough to type Get-MACAddress 00:50:56:A1:50:43

Or, you can take the time to create a proper function:

<pre lang="Powershell">function Get-MACAddress
{
 [CmdletBinding()]
 Param (
 [parameter(Mandatory=$True,ValueFromPipeline=$True)][Validatelength(17,17)][string]$MAC,
 [string]$Location = '*'
 )
 Get-VM -Location $Location | Select Name,Folder,PowerState, @{N="Network";E={$_ | Get-networkAdapter | ? {$_.macaddress -eq $MAC}}} | Where {$_.Network -ne ""}
&lt;#
 .Synopsis
 Searches vCentre for the given MAC address
 .Description
 This function searches the entire vCentre, or the given folder,datasenter,cluster,vApp or ResourcePool for VMs using the given MAC address. VMs with the given MAC address will be listed with Name,Folder,PowerState and to which network adapter the MAC address is assigned
 .Parameter MACAddress
 The MAC address you want to search for. Use the following format: 00:00:00:00:00:00
 .Parameter Location
 If you want to narrow the search to a specific folder,datasenter,cluster,vApp or ResourcePool
 .Example
 Get-MACAddress 00:50:56:a4:04:ce
 Searches the entire vCentre for VMs with the mac address 00:50:56:a4:04:ce
 .Example
 Get-MACAddress 00:50:56:a4:04:ce -Location vApp01
 Searches the vApp called vApp01 for VMs with the mac address 00:50:56:a4:04:ce
 .Link
 http://cloud.kemta.net
 #>
}</pre>

This more advanced function will allow you to narrow the search, it will check that the mac address you type is the correct length and it provides a little help section that you can call with get-help get-macaddress.

&nbsp;

&nbsp;