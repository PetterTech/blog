---
title: 'PowerCli: Finding amount of GB used by VMs in a folder/vApp/datacenter'
author: nerenther
 
date: 2014-01-29T09:02:28+00:00
url: /index.php/2014/01/29/powercli-finding-amount-of-gb-used-by-vms-in-a-foldervappdatacenter/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - disk space
  - get-harddisk
  - powercli

---
Sometimes it can be useful to know how much space the VMs in a specific folder (or vApp/datacenter) is occupying. For example if you are a hosting provider of some sort and need to know how much space a customer is using.

It&#8217;s a simple one-liner!

<div>
  <div>
     ```Get-VM -Location &lt;name of folder/vApp/datacenter&gt; | foreach {Get-HardDisk -VM $_.name} | Measure-Object CapacityGB -Sum ```
  </div>
  
  <p>
    That will give an output that looks something like this:<br /> <a href="http://cloud.kemta.net/wp-uploads/temp.png"><img decoding="async" loading="lazy" class="aligncenter size-full wp-image-545" alt="temp" src="http://cloud.kemta.net/wp-uploads/temp.png" width="830" height="267" /></a><br /> Meaning, in this case, that the folder named &#8220;Templates&#8221; has 2 VMs occupying 140GB of disk space
  </p>
  
  <p>
    You can also get a list per vm with this one-liner:
  </p>
  
   ```
  get-vm -Location &lt;folder&gt; | select name,@{Name="Size";Expression={(Get-HardDisk -VM $_.name |
Measure-Object CapacityGB -sum).Sum}} 
```
</div>