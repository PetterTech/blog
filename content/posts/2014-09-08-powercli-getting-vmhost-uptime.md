---
title: 'PowerCLI: Getting vmhost uptime'
author: nerenther
 
date: 2014-09-08T07:26:38+00:00
url: /index.php/2014/09/08/powercli-getting-vmhost-uptime/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - function
  - get-vmhostuptime
  - powercli
  - Powershell
  - uptime
  - vmhost
  - vmware

---
I love a powershell challenge, and last week a colleague of mine asked me for assistance in getting the uptime of vmware hosts. My initial response did the trick:

<pre lang="Powershell">Get-View  -ViewType hostsystem -Property name,runtime.boottime | Select-Object Name, @{N="UptimeDays"; E={((((get-date) - ($_.runtime).BootTime).TotalDays).Tostring()).Substring(0,5)}}
</pre>

However, I wasn&#8217;t completely satisfied by the the output or the ease of use.  
So today I went back and rewrote the code and made a function of it.  
Instead of using the ToString and Substring methods I went for the built-in class Math, which has a method called Round. You can learn more about the Math class here: <a href="http://www.madwithpowershell.com/2013/10/math-in-powershell.html" target="_blank" rel="noopener">http://www.madwithpowershell.com/2013/10/math-in-powershell.html</a>

Anyways, here&#8217;s the function I came up with:

<pre lang="Powershell">function Get-VMHostUptime
    {
        [CmdletBinding()]
            Param (
                [Parameter(ValueFromPipeline=$True,ValueFromPipelineByPropertyName=$True)][Alias('Name')][string]$VMHosts,
                [string]$Cluster
                  )
    Process{
         If ($VMHosts) {
            foreach ($VMHost in $VMHosts) {Get-View  -ViewType hostsystem -Property name,runtime.boottime -Filter @{"name" = "$VMHost"} | Select-Object Name, @{N="UptimeDays"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalDays),1)}}, @{N="UptimeHours"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalHours),1)}}, @{N="UptimeMinutes"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalMinutes),1)}}}
            }

         elseif ($Cluster) {
            foreach ($VMHost in (Get-VMHost -Location $Cluster)) {Get-View  -ViewType hostsystem -Property name,runtime.boottime -Filter @{"name" = "$VMHost"} | Select-Object Name, @{N="UptimeDays"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalDays),1)}}, @{N="UptimeHours"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalHours),1)}}, @{N="UptimeMinutes"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalMinutes),1)}}}
            }

         else {
            Get-View  -ViewType hostsystem -Property name,runtime.boottime | Select-Object Name, @{N="UptimeDays"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalDays),1)}}, @{N="UptimeHours"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalHours),1)}}, @{N="UptimeMinutes"; E={[math]::round((((Get-Date) - ($_.Runtime.BootTime)).TotalMinutes),1)}}
            }
        }
&lt;#
 .Synopsis
  Shows the uptime of VMHosts
 .Description
  Calculates the uptime of VMHosts provided, or VMHosts in the cluster provided
 .Parameter VMHosts
  The VMHosts you want to get the uptime of. Can be a single host or multiple hosts provided by the pipeline
 .Example
  Get-VMHostUptime
  Shows the uptime of all VMHosts in your vCenter
 .Example
  Get-VMHostUptime vmhost1
  Shows the uptime of vmhost1
 .Example
  Get-VMHostUptime -cluster cluster1
  Shows the uptime of all vmhosts in cluster1
 .Example
  Get-VMHost -location folder1 | Get-VMHostUptime
  Shows the uptime of VMHosts in folder1
 .Link
  http://cloud.kemta.net
 #>
}
</pre>

You can use it in a couple of different ways, as documented in its help section (get-help get-vmhostuptime -expamples). But if you provide no input to it, it will generate an output like this:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-627" alt="get-vmhostuptime" src="http://4.234.145.218/wp-content/uploads/2014/09/get-vmhostuptime.png" width="1224" height="712" srcset="http://4.234.145.218/wp-content/uploads/2014/09/get-vmhostuptime.png 1224w, http://4.234.145.218/wp-content/uploads/2014/09/get-vmhostuptime-300x175.png 300w, http://4.234.145.218/wp-content/uploads/2014/09/get-vmhostuptime-1024x596.png 1024w, http://4.234.145.218/wp-content/uploads/2014/09/get-vmhostuptime-768x447.png 768w" sizes="(max-width: 1224px) 100vw, 1224px" />][1]

Hopefully, you don&#8217;t have an uptime as long as some of these hosts 🙂

 [1]: http://4.234.145.218/wp-content/uploads/2014/09/get-vmhostuptime.png