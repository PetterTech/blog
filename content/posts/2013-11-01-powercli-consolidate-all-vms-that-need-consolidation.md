---
title: 'PowerCLI: Consolidate all VMs that need consolidation'
author: nerenther
 
date: 2013-11-01T09:37:48+00:00
url: /index.php/2013/11/01/powercli-consolidate-all-vms-that-need-consolidation/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - disk consolidation
  - powercli
  - Start-Consolidation
  - vmware
  - vsphere

---
Robert van den Nieuwendijk has a nice post on how to use PowerCLI to find VMs that need consolidation and then how to start consolidation. You can that post here: <a href="http://rvdnieuwendijk.com/2012/09/26/use-powercli-to-consolidate-snapshots-in-vsphere-5/" target="_blank" rel="noopener">http://rvdnieuwendijk.com/2012/09/26/use-powercli-to-consolidate-snapshots-in-vsphere-5/</a>

But, as always, I prefer to make a function of these kind of things. A function is much easier to remember than a bunch of parameters and cmdlets.  
So here&#8217;s the code for a function that will search through the vCentre for VMs that need disk consolidation:

 ```
function Start-Consolidation
{
    [CmdletBinding()]
        Param (
            [string]$Location = '*',
            [switch]$ListOnly
              )

        $VMs = Get-VM -Location $Location | Where-Object {$_.Extensiondata.Runtime.ConsolidationNeeded}

        if ($ListOnly) {
              $VMs
              }

        else {
            $VMs | ForEach-Object {
                Write-Host "Starting disk consolidation on $_.Name"
                $_.ExtensionData.ConsolidateVMDisks()
                Write-Host "Finished disk consolidation on $_.Name"
                                  }
              }
        }
<#
 .Synopsis
  Searches vCentre for VMs in need of disk consolidation and starts disk consolidation
 .Description
  This function searches the entire vCentre, or the given folder,datasenter,cluster,vApp or ResourcePool for VMs that is in need of disk consolidation. It will then start disk consolidation on those that need it
 .Parameter Location
  If you want to narrow the search to a specific folder,datasenter,cluster,vApp or ResourcePool
 .Example
  Start-Consolidation
  Searches the entire vCentre for VMs that need consolidation and starts consolidating them
 .Example
  Start-Consolidation -Location vApp01
  Searches through vApp01 for VMs that need consolidation and starts consolidation on them
 .Link
  http://cloud.kemta.net
 #>
 ```

Any input is much appreciated 🙂