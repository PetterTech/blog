---
title: Powershell function for showing some system information
author: nerenther
 
date: 2012-09-12T09:32:24+00:00
url: /index.php/2012/09/12/powershell-function-for-showing-some-system-information/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:7827:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #0000FF;">function</span> Show<span style="color: pink;">-</span>Debug
     <span style="color: #000000;">&#123;</span>
     <span style="color: #0000FF;">Param</span><span style="color: #000000;">&#40;</span>
     <span style="color: #000000;">&#91;</span><span style="color: #0000FF;">switch</span><span style="color: #000000;">&#93;</span><span style="color: #800080;">$KeepTempFile</span>
     <span style="color: #000000;">&#41;</span>
     <span style="color: #800080;">$tempfile</span> <span style="color: pink;">=</span> <span style="color: #800000;">&quot;$env:userprofilepstempfile.txt&quot;</span>
     <span style="color: #008080; font-weight: bold;">New-Item</span> <span style="color: #800080;">$tempfile</span> <span style="color: #008080; font-style: italic;">-ItemType</span> file <span style="color: #008080; font-style: italic;">-Force</span>
     <span style="color: #008080; font-weight: bold;">Get-WmiObject</span> <span style="color: #008080; font-style: italic;">-Class</span> Win32_ComputerSystem <span style="color: pink;">|</span><span style="color: #008080; font-weight: bold;">fl</span> Manufacturer<span style="color: pink;">,</span>Model<span style="color: pink;">,</span>Name<span style="color: pink;">,</span>Domain<span style="color: pink;">,</span>PrimaryOwnerName <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Out<span style="color: #FF0000;">-File</span></span> <span style="color: #800080;">$tempfile</span> <span style="color: #008080; font-style: italic;">-Append</span>
     <span style="color: #008080; font-weight: bold;">Get-WmiObject</span> <span style="color: #008080; font-style: italic;">-class</span> <span style="color: #800000;">&quot;Win32_BIOS&quot;</span> <span style="color: #008080; font-style: italic;">-namespace</span> <span style="color: #800000;">&quot;rootCIMV2&quot;</span> <span style="color: #008080; font-style: italic;">-computername</span> localhost <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">fl</span> BIOSVersion<span style="color: pink;">,</span>Serialnumber<span style="color: pink;">,</span>Status <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Out<span style="color: #FF0000;">-File</span></span> <span style="color: #800080;">$tempfile</span> <span style="color: #008080; font-style: italic;">-Append</span>
     <span style="color: #008080; font-weight: bold;">Get-WmiObject</span> Win32_OperatingSystem <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">fl</span> <span style="color: pink;">@</span><span style="color: #000000;">&#123;</span>Expression<span style="color: pink;">=</span><span style="color: #000000;">&#123;</span><span style="color: #000080;">$_</span>.Caption<span style="color: #000000;">&#125;</span>;Label<span style="color: pink;">=</span><span style="color: #800000;">&quot;OS Name&quot;</span><span style="color: #000000;">&#125;</span><span style="color: pink;">,</span>SerialNumber<span style="color: pink;">,</span>OSArchitecture<span style="color: pink;">,</span>Version <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Out<span style="color: #FF0000;">-File</span></span> <span style="color: #800080;">$tempfile</span> <span style="color: #008080; font-style: italic;">-Append</span>
     <span style="color: #008080; font-weight: bold;">Get-WmiObject</span> Win32_PhysicalMemory <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">ft</span> Tag<span style="color: pink;">,</span>Capacity<span style="color: pink;">,</span>Speed <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Out<span style="color: #FF0000;">-File</span></span> <span style="color: #800080;">$tempfile</span> <span style="color: #008080; font-style: italic;">-Append</span>
     <span style="color: #008080; font-weight: bold;">Get-WmiObject</span> Win32_Processor <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">fl</span> DeviceID<span style="color: pink;">,</span>Manufacturer<span style="color: pink;">,</span>Caption<span style="color: pink;">,</span>Name<span style="color: pink;">,</span>NumberOfCores<span style="color: pink;">,</span>NumberOfLogicalProcessors<span style="color: pink;">,</span>MaxClockSpeed<span style="color: pink;">,</span>CurrentClockSpeed<span style="color: pink;">,</span>L2CacheSize<span style="color: pink;">,</span>L3CacheSize<span style="color: pink;">,</span>Status <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Out<span style="color: #FF0000;">-File</span></span> <span style="color: #800080;">$tempfile</span> <span style="color: #008080; font-style: italic;">-Append</span>
     <span style="color: #008080; font-weight: bold;">Get-Content</span> <span style="color: #800080;">$tempfile</span> <span style="color: pink;">|</span> Out<span style="color: pink;">-</span>GridView
     <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$KeepTempFile</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#123;</span>
     <span style="color: #008080; font-weight: bold;">Write-Host</span> <span style="color: #800000;">&quot;Log file is now saved as $tempfile&quot;</span>
     <span style="color: #000000;">&#125;</span>
     <span style="color: #0000FF;">Else</span> <span style="color: #000000;">&#123;</span>
     <span style="color: #008080; font-weight: bold;">Remove-Item</span> <span style="color: #800080;">$tempfile</span>
     <span style="color: #000000;">&#125;</span>
     <span style="color: #008000;"><#
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
     http://cloud.kemta.net
     #></span>
     <span style="color: #000000;">&#125;</span> ```</td></tr></table><p class="theCode" style="display:none;">function Show-Debug
     {
     Param(
     [switch]$KeepTempFile
     )
     $tempfile = &quot;$env:userprofilepstempfile.txt&quot;
     New-Item $tempfile -ItemType file -Force
     Get-WmiObject -Class Win32_ComputerSystem |fl Manufacturer,Model,Name,Domain,PrimaryOwnerName | Out-File $tempfile -Append
     Get-WmiObject -class &quot;Win32_BIOS&quot; -namespace &quot;rootCIMV2&quot; -computername localhost | fl BIOSVersion,Serialnumber,Status | Out-File $tempfile -Append
     Get-WmiObject Win32_OperatingSystem | fl @{Expression={$_.Caption};Label=&quot;OS Name&quot;},SerialNumber,OSArchitecture,Version | Out-File $tempfile -Append
     Get-WmiObject Win32_PhysicalMemory | ft Tag,Capacity,Speed | Out-File $tempfile -Append
     Get-WmiObject Win32_Processor | fl DeviceID,Manufacturer,Caption,Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,CurrentClockSpeed,L2CacheSize,L3CacheSize,Status | Out-File $tempfile -Append
     Get-Content $tempfile | Out-GridView
     if ($KeepTempFile){
     Write-Host &quot;Log file is now saved as $tempfile&quot;
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
     http://cloud.kemta.net
     #>
     }</p></div>
    ";}
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

```
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
 http://cloud.kemta.net
 #>
 } 
```