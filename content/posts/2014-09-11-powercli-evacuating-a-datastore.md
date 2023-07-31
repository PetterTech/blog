---
title: 'PowerCLI: Evacuating a datastore'
author: nerenther
 
date: 2014-09-11T10:54:40+00:00
url: /index.php/2014/09/11/powercli-evacuating-a-datastore/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - one-liner
  - powercli
  - Powershell
  - storage vmotion
  - vmware

---
In case you ever need to empty out a datastore in you vmware environment, there is a nice little one-liner in PowerCLI for that:

<pre>Get-VM -Datastore "datastore1" | Move-VM -Datastore (Get-VMHost -Location 'cluster1' | Select-Object -First 1 | Get-Datastore | Where-Object {($_.Name -ne 'datastore1') -and ($_.FreeSpaceGB -gt '500')} | Sort-Object FreeSpaceGB -Descending | Select-Object -First 1)</pre>

Where &#8220;datastore1&#8221; is the datastore you want to empty out and &#8220;cluster1&#8221; is the cluster where the datastore is available.

The command will move VMs from datastore1 to the datastore in cluster1 with the most available space (minimum 500GB)