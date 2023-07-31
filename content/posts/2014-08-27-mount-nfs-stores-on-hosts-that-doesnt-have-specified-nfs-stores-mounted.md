---
title: 'PowerCLI: Mount NFS stores on multiple hosts'
author: nerenther
 
date: 2014-08-27T07:26:32+00:00
url: /index.php/2014/08/27/mount-nfs-stores-on-hosts-that-doesnt-have-specified-nfs-stores-mounted/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - mount nfs
  - Mount-NFSstores
  - powercli
  - Powershell

---
Ever had a bunch of vmware hosts that you want to add a NFS datastore on? It can be quite time consuming to say the least.  
In our environment we have a couple of NFS stores that should be available on all vmware hosts and I really don&#8217;t want to browse around all 50 or so hosts and check if they have them and then mount them if they&#8217;re not available.

So, of course, I wrote a small powercli script to check if the NFS stores are mounted and then mount them if they&#8217;re not mounted:

 ```
 $vmhosts = Get-View -ViewType HostSystem -Filter @{"Runtime.ConnectionState" = "connected"} -Property name

$progress = 1
$mounts = 1
foreach ($vmhost in $vmhosts) {
    Write-Progress -Activity "Checking $($vmhost.Name)" -PercentComplete ($progress/$vmhosts.count*100)
    if ((Get-Datastore -VMHost $vmhost.name | Where-Object {$_.name -eq "MGMT-ISO"}) -eq $NULL){
        New-Datastore -vmhost $vmhost.name -Name MGMT-ISO -Nfs -NfsHost &lt;nfsHost&gt; -Path /MGMT-ISO
        $mounts++
        }
    if ((Get-Datastore -VMHost $vmhost.name | Where-Object {$_.name -eq "USER-ISO"}) -eq $NULL){
        New-Datastore -vmhost $vmhost.name -Name USER-ISO -Nfs -NfsHost  -Path /USER-ISO
        $mounts++
        }
    $progress++
    }
if ($mounts = "1") {
    Write-Host "All hosts have the NFS stores already mounted" -ForegroundColor green
    } 
```

While I am pretty comfortable with writing and executing scripts like this on the fly, other people who are not as familiar with powershell might be a bit intimidated by it.  
That&#8217;s why I like to create functions of them and put them in the powershell profile for all users on our jumpstation (C:WindowsSystem32WindowsPowerShellv1.0profile.ps1).

If I were to create a function out of this script, it would look something like this (very basic):

 ```
 function Mount-NFSstores {
    $vmhosts = Get-View -ViewType HostSystem -Filter @{"Runtime.ConnectionState" = "connected"} -Property name

    $progress = 1
    $mounts = 1
    foreach ($vmhost in $vmhosts) {
        Write-Progress -Activity "Checking $($vmhost.Name)" -PercentComplete ($progress/$vmhosts.count*100)
        if ((Get-Datastore -VMHost $vmhost.name | Where-Object {$_.name -eq "MGMT-ISO"}) -eq $NULL){
            New-Datastore -vmhost $vmhost.name -Name MGMT-ISO -Nfs -NfsHost 10.64.0.8 -Path /MGMT-ISO
            $mounts++
            }
        if ((Get-Datastore -VMHost $vmhost.name | Where-Object {$_.name -eq "USER-ISO"}) -eq $NULL){
            New-Datastore -vmhost $vmhost.name -Name USER-ISO -Nfs -NfsHost 10.64.0.8 -Path /USER-ISO
            $mounts++
            }
        $progress++
        }
    if ($mounts = "1") {
        Write-Host "All hosts have the NFS stores already mounted" -ForegroundColor green
        }
&lt;#
 .Synopsis
  Mounts MGMT-ISO and USER-ISO on vmhosts
 .Description
  Checks every vmhost for NFS stores, if MGMT-ISO or USER-ISO isn't mounted, the function will mount it
 .Example
  Mount-NFSstores
  Mounts MGMT-ISO and USER-ISO on vmhosts
 .Link
  http://cloud.kemta.net
 #>
    }
 ```