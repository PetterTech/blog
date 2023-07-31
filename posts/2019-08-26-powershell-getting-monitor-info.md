---
title: 'Powershell: Getting monitor info'
author: nerenther
type: post
date: 2019-08-26T12:12:56+00:00
url: /index.php/2019/08/26/powershell-getting-monitor-info/
categories:
  - Microsoft
  - Powershell
tags:
  - Get-WmiObject
  - Powershell

---
Today I got a request from a colleague of mine that was doing inventory: What are the make, model, serial number and purchase date of your monitors?

Seeing as this wasn&#8217;t something I had readily in my head I had to figure it out, but being the automation enthusiast that I am, I refused to bend over my monitors and snap a photo of it all. I wanted to find it a cooler way, the powershell way 🙂

This information is stored in WMI, so all I had to do was to grab it using Get-WmiObject and then format it rather nicely for him.

The powershell script I came up with isn&#8217;t my most beautiful work, but here it is:

<pre class="wp-block-preformatted">$progress = 1
foreach ($monitor in (Get-WmiObject WmiMonitorID -Namespace root\wmi)) {
    Write-Host "Monitor #$($progress):" -ForegroundColor Green
    Write-Host "Manufactur: $(($monitor.ManufacturerName | ForEach-Object {[char]$_}) -join '')"
    Write-Host "PN: " ($($monitor.UserFriendlyName | ForEach-Object {[char]$_}) -join '')
    Write-Host "SN: " ($($monitor.SerialNumberID | ForEach-Object {[char]$_}) -join '')
    Write-Host "WeekOfManufacture: $($monitor.WeekOfManufacture)"
    Write-Host "YearOfManufacture: $($monitor.YearOfManufacture)"
    $progress++
    } </pre>