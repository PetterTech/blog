---
title: Powershell function for rotating event logs
author: nerenther
type: post
date: 2012-09-06T10:13:33+00:00
url: /index.php/2012/09/06/powershell-function-for-rotating-event-logs/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:4974:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #0000FF;">function</span> Rotate<span style="color: pink;">-</span>EventLogs
    <span style="color: #000000;">&#123;</span>
    <span style="color: #800080;">$today</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">get-date</span> <span style="color: #008080; font-style: italic;">-UFormat</span> <span style="color: pink;">%</span>d<span style="color: pink;">%</span>m<span style="color: pink;">%</span>Y
    &nbsp;
    <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Test-Path</span> c:eventlogs<span style="color: #000000;">&#41;</span> <span style="color: #FF0000;">-eq</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    <span style="color: #008080; font-weight: bold;">New-Item</span> c:eventlogs <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> directory
    <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Test-Path</span> c:eventlogssystem<span style="color: #000000;">&#41;</span> <span style="color: #FF0000;">-eq</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    <span style="color: #008080; font-weight: bold;">New-Item</span> c:eventlogssystem <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> directory
    <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Test-Path</span> c:eventlogsapplication<span style="color: #000000;">&#41;</span> <span style="color: #FF0000;">-eq</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    <span style="color: #008080; font-weight: bold;">New-Item</span> c:eventlogsapplication <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> directory
    <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #0000FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#40;</span><span style="color: #008080; font-weight: bold;">Test-Path</span> c:eventlogssecurity<span style="color: #000000;">&#41;</span> <span style="color: #FF0000;">-eq</span> <span style="color: #800080;">$False</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    <span style="color: #008080; font-weight: bold;">New-Item</span> c:eventlogssecurity <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> directory
    <span style="color: #000000;">&#125;</span>
    &nbsp;
    <span style="color: #008080; font-weight: bold;">Get-EventLog</span> system <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">export-clixml</span> c:eventlogssystem<span style="color: #800080;">$today</span>.xml
    <span style="color: #008080; font-weight: bold;">Get-EventLog</span> application <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">export-clixml</span> c:eventlogsapplication<span style="color: #800080;">$today</span>.xml
    <span style="color: #008080; font-weight: bold;">Get-EventLog</span> security <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">export-clixml</span> c:eventlogssecurity<span style="color: #800080;">$today</span>.xml
    &nbsp;
    Clear<span style="color: pink;">-</span>EventLog system<span style="color: pink;">,</span>application<span style="color: pink;">,</span>security
    &nbsp;
    <span style="color: #000000;">&#125;</span></pre></td></tr></table><p class="theCode" style="display:none;">function Rotate-EventLogs
    {
    $today = get-date -UFormat %d%m%Y
    
    if ((Test-Path c:eventlogs) -eq $False)
    {
    New-Item c:eventlogs -type directory
    }
    
    if ((Test-Path c:eventlogssystem) -eq $False)
    {
    New-Item c:eventlogssystem -type directory
    }
    
    if ((Test-Path c:eventlogsapplication) -eq $False)
    {
    New-Item c:eventlogsapplication -type directory
    }
    
    if ((Test-Path c:eventlogssecurity) -eq $False)
    {
    New-Item c:eventlogssecurity -type directory
    }
    
    Get-EventLog system | export-clixml c:eventlogssystem$today.xml
    Get-EventLog application | export-clixml c:eventlogsapplication$today.xml
    Get-EventLog security | export-clixml c:eventlogssecurity$today.xml
    
    Clear-EventLog system,application,security
    
    }</p></div>
    ";}
categories:
  - Microsoft
  - Powershell
tags:
  - event logs
  - function
  - microsoft
  - Powershell
  - rotate-eventlogs

---
A friend of mine came to me with an interesting powershell challenge today: how can I use powershell to archive and clear event logs?

Well, challenge accepted!

The reason the challenge arose is due to maintenance he performs on a number of customer servers. Every month he saves each eventlog and clears it manually, a time consuming task if you have more than a few servers.

So here&#8217;s what I came up with:  
A powershell function, Rotate-EventLogs, that exports the application, system and security logs to xml files with todays date as filename, then the logs are cleared.

The function isn&#8217;t really all that advanced, it checks if the folders where the logs will be saved exists, if not it will create them.  
Then it will export each log to c:eventlogs<logname>%d%m%Y.xml For example the system log exported today would be located at c:eventlogssystem 6092012.xml.  
After the export of the three eventlogs it will clear them.

What he will have to do manually is to add the function code to %windir%system32WindowsPowerShellv1.0profile.ps1 on each server.

He can then set up a scheduled task that only runs Rotate-Eventlogs in a powershell window every month.

Challenge completed!

Here&#8217;s the code for the function:

<pre lang="Powershell">function Rotate-EventLogs
{
$today = get-date -UFormat %d%m%Y

if ((Test-Path c:eventlogs) -eq $False)
{
New-Item c:eventlogs -type directory
}

if ((Test-Path c:eventlogssystem) -eq $False)
{
New-Item c:eventlogssystem -type directory
}

if ((Test-Path c:eventlogsapplication) -eq $False)
{
New-Item c:eventlogsapplication -type directory
}

if ((Test-Path c:eventlogssecurity) -eq $False)
{
New-Item c:eventlogssecurity -type directory
}

Get-EventLog system | export-clixml c:eventlogssystem$today.xml
Get-EventLog application | export-clixml c:eventlogsapplication$today.xml
Get-EventLog security | export-clixml c:eventlogssecurity$today.xml

Clear-EventLog system,application,security

}</pre>

Have fun with it if you want. If not, don&#8217;t 🙂

UPDATE: If you want to do this remotely you can take a look at this file: <a href="https://dl.dropbox.com/u/33041052/bloggting/scriptstuff/powershell/function/rotate-eventlogs_espen_style.ps1" target="_blank" rel="noopener">https://dl.dropbox.com/u/33041052/bloggting/scriptstuff/powershell/function/rotate-eventlogs_espen_style.ps1</a>  
It adds the capability to do it on a remote server, see the help section of the function