---
title: 'PowerCLI: Getting host alarms'
author: nerenther
 
date: 2014-08-29T07:41:13+00:00
url: /index.php/2014/08/29/powercli-get-host-alarms/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - alarms
  - function
  - get-vmhostalarms
  - powercli
  - Powershell
  - vmware

---
Yesterday I wrote a post about getting vm alarms through PowerCLI. Today it&#8217;s time for getting host alarms 🙂  
The code is very similar to the one for getting vm alarms, since they both use get-view to grab all info:

 ```
$VMHosts = Get-View -ViewType HostSystem -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyVMHosts = $VMHosts | Where-Object {$_.TriggeredAlarmState -ne "{}"}

$progress = 1
$report = @()
if ($FaultyVMHosts -ne $null) {
    foreach ($FaultyVMHost in $FaultyVMHosts) {
        foreach ($TriggeredAlarm in $FaultyVMHost.TriggeredAlarmstate) {
            Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyVMHost.Name)" -PercentComplete ($progress/$FaultyVMHosts.count*100) -Id 1 -ErrorAction SilentlyContinue
            $alarmID = $TriggeredAlarm.Alarm.ToString()
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty VMHost $FaultyVMHost.Name
            Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
            $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

$report | Where-Object {$_.TriggeredAlarms -ne ""} 
```

The output will look something like this:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-602" alt="get-vmhostalarms" src="http://cloud.kemta.net/wp-uploads/get-vmhostalarms.png" width="920" height="73" />][1]

And here&#8217;s the function code:

 ```
function Get-VMHostAlarms
{
$VMHosts = Get-View -ViewType HostSystem -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyVMHosts = $VMHosts | Where-Object {$_.TriggeredAlarmState -ne "{}"}

$progress = 1
$report = @()
if ($FaultyVMHosts -ne $null) {
    foreach ($FaultyVMHost in $FaultyVMHosts) {
        foreach ($TriggeredAlarm in $FaultyVMHost.TriggeredAlarmstate) {
            Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyVMHost.Name)" -PercentComplete ($progress/$FaultyVMHosts.count*100) -Id 1 -ErrorAction SilentlyContinue
            $alarmID = $TriggeredAlarm.Alarm.ToString()
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty VMHost $FaultyVMHost.Name
            Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
            $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

$report | Where-Object {$_.TriggeredAlarms -ne ""}

&lt;#
 .Synopsis
  Lists all triggered VMHost alarms that haven't been acknowledged
 .Description
  Outputs a list of VMHosts and the unacknowledged alarms they have triggered
 .Example
  Get-VMHostAlarms
  Outputs a list of VMHosts and the unacknowledged alarms they have triggered
 .Link
  http://cloud.kemta.net
 #>
} 
```

&nbsp;

 [1]: http://cloud.kemta.net/wp-uploads/get-vmhostalarms.png