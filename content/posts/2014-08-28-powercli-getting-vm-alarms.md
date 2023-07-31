---
title: 'PowerCLI: Getting vm alarms'
author: nerenther
 
date: 2014-08-28T06:42:12+00:00
url: /index.php/2014/08/28/powercli-getting-vm-alarms/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - alarms
  - function
  - get-vmalarms
  - powercli
  - Powershell
  - vmware

---
A few weeks ago I started to put together a health check script for our vmware environments and the first thing I wanted to have in that report is a list of triggered alarms. To my surprise there was no native cmdlet to retrieve alarms using PowerCLI, instead I had to write a short script to retrieve alarms.

So here&#8217;s the the script for retrieving vm alarms:

<pre lang="PowerShell">$VMs = Get-View -ViewType VirtualMachine -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyVMs = $VMs | Where-Object {$_.OverallStatus -ne "Green"}

$progress = 1
$report = @()
if ($FaultyVMs -ne $null) {
    foreach ($FaultyVM in $FaultyVMs) {
            foreach ($TriggeredAlarm in $FaultyVM.TriggeredAlarmstate) {
                Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyVM.Name)" -PercentComplete ($progress/$FaultyVMs.count*100) -Id 1 -ErrorAction SilentlyContinue
                $alarmID = $TriggeredAlarm.Alarm.ToString()
                $object = New-Object PSObject
                Add-Member -InputObject $object NoteProperty VM $FaultyVM.Name
                Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
                $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering VM alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

$report | Where-Object {$_.TriggeredAlarms -ne ""}</pre>

This will provide an output like this:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-598" alt="get-vmalarms" src="http://cloud.kemta.net/wp-uploads/get-vmalarms.png" width="1234" height="570" />][1]

But, as always, to make it easier for my colleagues to use I make a function out of it:

<pre lang="PowerShell">function Get-VMAlarms
{
$VMs = Get-View -ViewType VirtualMachine -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyVMs = $VMs | Where-Object {$_.OverallStatus -ne "Green"}

$progress = 1
$report = @()
if ($FaultyVMs -ne $null) {
    foreach ($FaultyVM in $FaultyVMs) {
            foreach ($TriggeredAlarm in $FaultyVM.TriggeredAlarmstate) {
                Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyVM.Name)" -PercentComplete ($progress/$FaultyVMs.count*100) -Id 1 -ErrorAction SilentlyContinue
                $alarmID = $TriggeredAlarm.Alarm.ToString()
                $object = New-Object PSObject
                Add-Member -InputObject $object NoteProperty VM $FaultyVM.Name
                Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
                $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering VM alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

$report | Where-Object {$_.TriggeredAlarms -ne ""}

&lt;#
 .Synopsis
  Lists all triggered VM alarms that haven't been acknowledged
 .Description
  Outputs a list of VMs and the unacknowledged alarms they have triggered
 .Example
  Get-VMAlarms
  Outputs a list of VMs and the unacknowledged alarms they have triggered
 .Link
  http://cloud.kemta.net
 #>
}</pre>

Beside the fact that a function is easier to use, it also makes it easier to manipulate the data further. For example if you only want alarms for vm whose name start with &#8220;smart&#8221;:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-597" alt="get-vmalarms_filter" src="http://cloud.kemta.net/wp-uploads/get-vmalarms_filter.png" width="962" height="211" />][2]

 [1]: http://cloud.kemta.net/wp-uploads/get-vmalarms.png
 [2]: http://cloud.kemta.net/wp-uploads/get-vmalarms_filter.png