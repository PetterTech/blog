---
title: 'PowerCLI: Getting datastore alarms'
author: nerenther
 
date: 2014-08-31T10:16:36+00:00
url: /index.php/2014/08/31/powercli-getting-datastore-alarms/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - alarms
  - function
  - get-datastorealarms
  - powercli
  - Powershell
  - vmware

---
Next in the series on getting alarms is getting datastore alarms.  
Again, the code is pretty similar:

 ```
$Datastores = Get-View -ViewType Datastore -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyDatastores = $Datastores | Where-Object {$_.TriggeredAlarmState -ne "{}"}

$progress = 1
$report = @()
if ($FaultyDatastores -ne $null) {
    foreach ($FaultyDatastore in $FaultyDatastores) {
        foreach ($TriggeredAlarm in $FaultyDatastore.TriggeredAlarmstate) {
            Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyDatastore.Name)" -PercentComplete ($progress/$FaultyDatastores.count*100) -Id 1 -ErrorAction SilentlyContinue
            $entity = $TriggeredAlarm.Entity.ToString()
            $alarmID = $TriggeredAlarm.Alarm.ToString()
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty Datastore $FaultyDatastore.Name
            Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
            $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

$report | Where-Object {$_.TriggeredAlarms -ne ""} 
```

And the output is pretty similar:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-615" alt="get-datastorealarms" src="http://cloud.kemta.net/wp-uploads/get-datastorealarms.png" width="714" height="250" />][1]

The function code is this:

 ```
function Get-DatastoreAlarms
{
$Datastores = Get-View -ViewType Datastore -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyDatastores = $Datastores | Where-Object {$_.TriggeredAlarmState -ne "{}"}

$progress = 1
$report = @()
if ($FaultyDatastores -ne $null) {
    foreach ($FaultyDatastore in $FaultyDatastores) {
        foreach ($TriggeredAlarm in $FaultyDatastore.TriggeredAlarmstate) {
            Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyDatastore.Name)" -PercentComplete ($progress/$FaultyDatastores.count*100) -Id 1 -ErrorAction SilentlyContinue
            $entity = $TriggeredAlarm.Entity.ToString()
            $alarmID = $TriggeredAlarm.Alarm.ToString()
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty Datastore $FaultyDatastore.Name
            Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
            $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

$report | Where-Object {$_.TriggeredAlarms -ne ""}

<#
 .Synopsis
  Lists all triggered Cluster alarms that haven't been acknowledged
 .Description
  Outputs a list of Cluster and the unacknowledged alarms they have triggered
 .Example
  Get-VMHostAlarms
  Outputs a list of Cluster and the unacknowledged alarms they have triggered
 .Link
  http://cloud.kemta.net
 #>
} 
```

&nbsp;

 [1]: http://cloud.kemta.net/wp-uploads/get-datastorealarms.png