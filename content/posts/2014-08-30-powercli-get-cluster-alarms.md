---
title: 'PowerCLI: Getting cluster alarms'
author: nerenther
 
date: 2014-08-30T08:21:59+00:00
url: /index.php/2014/08/30/powercli-get-cluster-alarms/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - alarms
  - function
  - get-clusteralarms
  - powercli
  - Powershell
  - vmware

---
The next step in my short series on getting vCenter alarms using PowerCLI is to get cluster alarms.

Here's the code:

 ```
$Clusters = Get-View -ViewType ComputeResource -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyClusters = $Clusters | Where-Object {$_.TriggeredAlarmState -ne "{}"}
$report = @()
$progress = 1
if ($FaultyClusters -ne $NULL) {
    foreach ($FaultyCluster in $FaultyClusters) {
        foreach ($TriggeredAlarm in $FaultyCluster.TriggeredAlarmstate) {
            Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyCluster.Name)" -PercentComplete ($progress/$FaultyClusters.count*100) -Id 1 -ErrorAction SilentlyContinue
            $entity = $TriggeredAlarm.Entity.ToString()
            $alarmID = $TriggeredAlarm.Alarm.ToString()
            if ($entity -like "ClusterComputeResource-*") {
                $entityName = $FaultyCluster.Name
                $type = "Cluster"
                }
            elseif ($entity -like "HostSystem-host*") {
                $entityName = (Get-View -ViewType HostSystem -Property Name | Where-Object {$_.MoRef -eq $entity}).Name
                $type = "VMHost"
                }
            elseif ($entity -like "VirtualMachine-vm*") {
                $entityName = (Get-View -ViewType VirtualMachine -Property Name | Where-Object {$_.MoRef -eq $entity}).Name
                $type = "VM"
                }
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty Cluster $FaultyCluster.Name
            Add-Member -InputObject $object NoteProperty Entity $entityName
            Add-Member -InputObject $object NoteProperty Type $type
            Add-Member -InputObject $object NoteProperty TriggeredAlarms ("$(Get-AlarmDefinition -Id $alarmID)")
            $report += $object
            }
        $progress++
        }
    }
Write-Progress -Activity "Gathering alarms" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue
$report | Where-Object {$_.TriggeredAlarms -ne ""}
```

And the output will look something like this:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-606" alt="get-clusteralarms" src="http://cloud.kemta.net/wp-uploads/get-clusteralarms.png" width="1298" height="214" />][1]

As you can see, this will also list vm alarms and host alarms. So you could argue that you only need this and not separate scripts/functions for getting vm alarms and host alarms.

Anyways, here's the function code:

 ```
function Get-ClusterAlarms
{
$Clusters = Get-View -ViewType ComputeResource -Property Name,OverallStatus,TriggeredAlarmstate
$FaultyClusters = $Clusters | Where-Object {$_.TriggeredAlarmState -ne "{}"}
$report = @()
$progress = 1
if ($FaultyClusters -ne $NULL) {
    foreach ($FaultyCluster in $FaultyClusters) {
        foreach ($TriggeredAlarm in $FaultyCluster.TriggeredAlarmstate) {
            Write-Progress -Activity "Gathering alarms" -Status "Working on $($FaultyCluster.Name)" -PercentComplete ($progress/$FaultyClusters.count*100) -Id 1 -ErrorAction SilentlyContinue
            $entity = $TriggeredAlarm.Entity.ToString()
            $alarmID = $TriggeredAlarm.Alarm.ToString()
            if ($entity -like "ClusterComputeResource-*") {
                $entityName = $FaultyCluster.Name
                $type = "Cluster"
                }
            elseif ($entity -like "HostSystem-host*") {
                $entityName = (Get-View -ViewType HostSystem -Property Name | Where-Object {$_.MoRef -eq $entity}).Name
                $type = "VMHost"
                }
            elseif ($entity -like "VirtualMachine-vm*") {
                $entityName = (Get-View -ViewType VirtualMachine -Property Name | Where-Object {$_.MoRef -eq $entity}).Name
                $type = "VM"
                }
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty Cluster $FaultyCluster.Name
            Add-Member -InputObject $object NoteProperty Entity $entityName
            Add-Member -InputObject $object NoteProperty Type $type
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

The output will be the same, but since it's a function you can manipulate the data further. For example if you only want alarms related to the clusters themselves:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-607" alt="get-clusteralarms-filter" src="http://cloud.kemta.net/wp-uploads/get-clusteralarms-filter.png" width="890" height="141" />][2]

 [1]: http://cloud.kemta.net/wp-uploads/get-clusteralarms.png
 [2]: http://cloud.kemta.net/wp-uploads/get-clusteralarms-filter.png