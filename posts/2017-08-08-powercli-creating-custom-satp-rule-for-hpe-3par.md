---
title: 'PowerCLI: Creating custom SATP rule for HPE 3PAR'
author: nerenther
type: post
date: 2017-08-08T12:06:28+00:00
url: /index.php/2017/08/08/powercli-creating-custom-satp-rule-for-hpe-3par/
categories:
  - HPE 3PAR
  - PowerCLI
  - VMware
tags:
  - get-esxcli
  - HPE 3PAR
  - path selection poliocy
  - powercli
  - PSP
  - SATP

---
A while back we migrated from our old EMC VNX to a new HPE 3PAR array. It all went fine but what kinda slipped our mind is that HPE&#8217;s best practice is to create a custom SATP rule that uses RoudRobin as path selection policy and a IOPS limit to 1 in stead of the default 1000.

The steps are documented in the HPE 3PAR VMware ESX/ESXi Implementation Guide, but they only show you how to do it through the esx cli.  
If you have more then a few esx hosts you would be better of using the Get-EsxCli cmdlet. That way you can put it in a script that loops through all your esx hosts.  
_Another thing to keep in mind is that the SATP rules are case sensitive and HPE is using the wrong case for the vendor parameter (3pardata in stead of 3PARdata), at least as of the writing of this post._

The script I wrote will loop through all esx hosts and if the custom rule doesn&#8217;t exist it will create it. In our environment the script only took about 2 minutes (on around 100 hosts).

Here&#8217;s the script:

<pre>$progress = 1
$esxList = Get-View -ViewType hostsystem -Property name | Sort-Object name

foreach ($esx in $esxList) {
 Write-Progress -Activity "Checking SATP rules" -Status "Working on $($esx.name)" -CurrentOperation "Getting EsxCli" -PercentComplete ($progress/$esxList.count*100)
 try {
 $EsxCli = Get-EsxCli -VMHost $esx.name
 }
 catch {
 $Error[0]
 Write-Host "Failed to get EsxCli, see above error" -ForegroundColor Red
 }

 Write-Progress -Activity "Checking SATP rules" -Status "Working on $($esx.name)" -CurrentOperation "Got EsxCli" -PercentComplete ($progress/$esxList.count*100)

 Write-Progress -Activity "Checking SATP rules" -Status "Working on $($esx.name)" -CurrentOperation "Checking if rule already is present" -PercentComplete ($progress/$esxList.count*100)
 if (!($EsxCli.storage.nmp.satp.rule.list() | Where-Object {$_.description -contains "HP 3PAR Custom iSCSI/FC/FCoE ALUA Rule"})) {

 Write-Progress -Activity "Checking SATP rules" -Status "Working on $($esx.name)" -CurrentOperation "Creating rule" -PercentComplete ($progress/$esxList.count*100)
 try {
 $EsxCli.storage.nmp.satp.rule.add($null,"tpgs_on","HP 3PAR Custom iSCSI/FC/FCoE ALUA Rule",$null,$null,$null,"VV",$null,"VMW_PSP_RR","iops=1","VMW_SATP_ALUA",$null,$null,"3PARdata") | Out-Null
 }

catch {
 $Error[0]
 Write-Host "Rule creation failed on $($esx.name), see error above" -ForegroundColor Red
 }

Write-Host "Rule created on $($esx.name)" -ForegroundColor Green

}

else {
 Write-Host "Rule already exists, skipping" -ForegroundColor Yellow
 }

 $progress++
 }</pre>