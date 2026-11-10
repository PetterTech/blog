---
title: 'PowerCLI: Getting the status of vmware tools on all VMs'
date: 2014-09-05T12:06:17+00:00
url: /index.php/2014/09/05/powercli-getting-the-status-of-vmware-tools-on-all-vms/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - function
  - get-vmtoolsstatus
  - powercli
  - Powershell
  - vmware
  - vmware tools
---
I'm sure I don't need to explain to you guys why VMware tools is a good idea to have installed on your VMs, and probably not why it's a good idea to keep VMware tools updated.  
However, I haven't found a good way to get a neat list of which VMs need to have their VMware tools upgraded. While working on my vCenter health check script I found that I had to make my own little script to get that list. And, in addition, I wanted the list to include the VM version.

I ended up with creating a function to provide me with that list:

 ```powershell
function Get-VMToolsStatus
    {
        [CmdletBinding()]
        Param (
            [ValidateSet('NeedUpgrade','NotInstalled','Unsupported')][string]$Filter
            )

    $VMs = Get-View -ViewType VirtualMachine -Property name,guest,config.version,runtime.PowerState
    $report = @()
    $progress = 1
    foreach ($VM in $VMs) {
        Write-Progress -Activity "Checking vmware tools status" -Status "Working on $($VM.Name)" -PercentComplete ($progress/$VMs.count*100) -ErrorAction SilentlyContinue
        $object = New-Object PSObject
        Add-Member -InputObject $object NoteProperty VM $VM.Name
        if ($VM.runtime.powerstate -eq "PoweredOff") {Add-Member -InputObject $object NoteProperty ToolsStatus "$($VM.guest.ToolsStatus) (PoweredOff)"}
        else {Add-Member -InputObject $object NoteProperty ToolsStatus $VM.guest.ToolsStatus}
        Add-Member -InputObject $object NoteProperty ToolsVersionStatus ($VM.Guest.ToolsVersionStatus).Substring(10)
        Add-Member -InputObject $object NoteProperty SupportState ($VM.Guest.ToolsVersionStatus2).Substring(10)
        if ($object.ToolsStatus -eq "NotInstalled") {Add-Member -InputObject $object NoteProperty Version ""}
        else {Add-Member -InputObject $object NoteProperty Version $VM.Guest.ToolsVersion}
        Add-Member -InputObject $object NoteProperty "HW Version" $VM.config.version
        $report += $object
        $progress++
        }
    Write-Progress -Activity "Checking vmware tools" -Status "All done" -Completed -ErrorAction SilentlyContinue

    if ($Filter -eq 'NeedUpgrade') {
        $report | Sort-Object vm | Where-Object {$_.ToolsVersionStatus -eq "NeedUpgrade"}
        }
    elseif ($Filter -eq 'NotInstalled') {
        $report | Sort-Object vm | Where-Object {$_.ToolsVersionStatus -eq "NotInstalled"}
        }
    elseif ($Filter -eq 'Unsupported') {
        $report | Sort-Object vm | Where-Object {($_.SupportState -eq "Blacklisted") -or ($_.SupportState -eq "TooNew") -or ($_.SupportState -eq "TooOld") -or ($_.SupportState -eq "Unmanaged")}
        }
    else {$report | Sort-Object vm}

<#
 .Synopsis
  List vm tools status for all VMs
 .Description
  Lists the status and version for all VMs, also tells whether the version is supported and also the vm version
 .Parameter Filter
  Filters the list based on if the VMware tools "NeedUpgrade", is "NotInstalled" or if they are "Unsupported"
 .Example
  Get-VMToolsStatus
  List vm tools status for all VMs
 .Example
  Get-VMToolsStatus -Filter NeedUpgrade
  Show only VMs needing update of vm tools
 .Link
  https://pettertech.com/blog/
 #>
}
 ```

The function will create an output that look kinda like this:

{{< unavailable "Screenshot no longer available" >}}

You can also use a basic filter on the function by specifying -Filter &lt;filtername&gt;. The different filters is documented in the help section.  
For example, if you only want a list of VMs who need an upgrade of their VMware tools version:

{{< unavailable "Screenshot no longer available" >}}

In case you don't want to use this as a function, here's the script version:

 ```powershell
$VMs = Get-View -ViewType VirtualMachine -Property name,guest,config.version,runtime.PowerState
    $report = @()
    $progress = 1
    foreach ($VM in $VMs) {
        Write-Progress -Activity "Checking vmware tools status" -Status "Working on $($VM.Name)" -PercentComplete ($progress/$VMs.count*100) -ErrorAction SilentlyContinue
        $object = New-Object PSObject
        Add-Member -InputObject $object NoteProperty VM $VM.Name
        if ($VM.runtime.powerstate -eq "PoweredOff") {Add-Member -InputObject $object NoteProperty ToolsStatus "$($VM.guest.ToolsStatus) (PoweredOff)"}
        else {Add-Member -InputObject $object NoteProperty ToolsStatus $VM.guest.ToolsStatus}
        Add-Member -InputObject $object NoteProperty ToolsVersionStatus ($VM.Guest.ToolsVersionStatus).Substring(10)
        Add-Member -InputObject $object NoteProperty SupportState ($VM.Guest.ToolsVersionStatus2).Substring(10)
        if ($object.ToolsStatus -eq "NotInstalled") {Add-Member -InputObject $object NoteProperty Version ""}
        else {Add-Member -InputObject $object NoteProperty Version $VM.Guest.ToolsVersion}
        Add-Member -InputObject $object NoteProperty "HW Version" $VM.config.version
        $report += $object
        $progress++
        }
    Write-Progress -Activity "Checking vmware tools" -Status "All done" -Completed -ErrorAction SilentlyContinue

    $report
 ```

Depending on the number of VMs in your environment, the list might now even fit on the screen. So you should probably pipe it to where-object to filter it down further, like this:

{{< unavailable "Screenshot no longer available" >}}
