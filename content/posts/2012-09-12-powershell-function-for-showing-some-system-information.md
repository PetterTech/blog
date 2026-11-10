---
title: Powershell function for showing some system information
date: 2012-09-12T09:32:24+00:00
url: /index.php/2012/09/12/powershell-function-for-showing-some-system-information/
categories:
  - Microsoft
  - Powershell
tags:
  - function
  - parameter
  - Powershell
  - Show-Debug
  - switch
  - system information
  - wmi
---
This is a function I created just because I wanted to toy around with Powershell and get-wmiobject. Also, this is my first function where I made it possible to use a switch parameter.

What the function does is gather some system information using get-wmiobject. The info is written to a temp file and then shown using out-gridview.  
If the KeepTempFile parameter is used the temp file is saved in the users profile, if not it is deleted after the function finishes.

Heres the code:

```powershell
function Show-Debug
 {
 Param(
 [switch]$KeepTempFile
 )
 $tempfile = "$env:userprofilepstempfile.txt"
 New-Item $tempfile -ItemType file -Force
 Get-WmiObject -Class Win32_ComputerSystem |fl Manufacturer,Model,Name,Domain,PrimaryOwnerName | Out-File $tempfile -Append
 Get-WmiObject -class "Win32_BIOS" -namespace "rootCIMV2" -computername localhost | fl BIOSVersion,Serialnumber,Status | Out-File $tempfile -Append
 Get-WmiObject Win32_OperatingSystem | fl @{Expression={$_.Caption};Label="OS Name"},SerialNumber,OSArchitecture,Version | Out-File $tempfile -Append
 Get-WmiObject Win32_PhysicalMemory | ft Tag,Capacity,Speed | Out-File $tempfile -Append
 Get-WmiObject Win32_Processor | fl DeviceID,Manufacturer,Caption,Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,CurrentClockSpeed,L2CacheSize,L3CacheSize,Status | Out-File $tempfile -Append
 Get-Content $tempfile | Out-GridView
 if ($KeepTempFile){
 Write-Host "Log file is now saved as $tempfile"
 }
 Else {
 Remove-Item $tempfile
 }
 <#
 .Synopsis
 Show some information about your computer
 .Description
 This function will create a txt file which will be populated with some information from wmi. It will then show the info to the user and delete the file
 .Parameter KeepTempFile
 Setting this parameter will keep the txt file with all info
 .Example
 Show-Debug
 Gathers info and show it on screen
 .Link
 https://pettertech.com/blog/
 #>
 } 
```