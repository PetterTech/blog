---
title: 'Powershell: Measuring latency on DNS queries'
author: nerenther
 
date: 2014-08-15T08:39:40+00:00
url: /index.php/2014/08/15/powershell-measuring-latency-on-dns-queries/
categories:
  - Microsoft
  - Powershell
tags:
  - dns
  - dns latency
  - function
  - Measure-DNSLatency
  - Powershell

---
A little while ago we have some issues with one of our Exchange environments. The symptoms was that basically everything was slow, opening address books, owa, sending mails and so on.  
After some digging it occurred to me that this may be DNS related, so I used a one-liner in powershell to see how fast our DNS servers responded:

 ```
Measure-Command {Resolve-DnsName google.com -DnsOnly -Type A -NoHostsFile -server x.x.x.x} 
```

And sure enough, we were seeing response times in the range of 5-7 seconds. Way more than enough to cause our problems. After rebooting the DNS servers ours problems disappeared.

But, as always, I had to play around with created a powershell function.

The function resolves a few records from locally defined DNS servers and some publicly available DNS servers (or a custom list if you want) and measures the average latency (in milliseconds). The results are put in a list and sorted by latency.

Here's the code:

 ```
function Measure-DNSLatency
{
    [CmdletBinding()]
        Param (
            [string[]]$CustomDNSServer
            )

    try {
        Get-DnsClientServerAddress -ErrorAction Stop | Out-Null
        }
    catch [System.Management.Automation.CommandNotFoundException] {
        Throw "You need at least PowerShell v4.0, your version is: $(($PSVersionTable.psversion).Major)"
        }

    $report = @()

    if ($CustomDNSServer.count -eq "0") {
        Write-Verbose "Grabbing a list of locally defined dns servers"
        $LocalDNSServers = (Get-DnsClientServerAddress).serveraddresses | Select-Object -Unique
        $LocalDNSServers = $LocalDNSServers | Where-Object {$_ -ne "fec0:0:0:ffff::1"}
        $LocalDNSServers = $LocalDNSServers | Where-Object {$_ -ne "fec0:0:0:ffff::2"}
        $LocalDNSServers = $LocalDNSServers | Where-Object {$_ -ne "fec0:0:0:ffff::3"}

        Write-Verbose "Measuring locally defined dns servers"
        $progress = 1
        foreach ($DNSServer in $LocalDNSServers) {
            Write-Progress -ErrorAction SilentlyContinue -Activity "Measuring Latency on locally defined servers" -Status "Measuring $((Resolve-DnsName $DNSServer -Server $DNSServer).NameHost)" -PercentComplete ($progress/$LocalDNSServers.count*100) -Id 1
            $results = @()
            $results += (Measure-Command {Resolve-DnsName cloud.kemta.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName google.com -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName a.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName b.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName c.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty DNSServerName (Resolve-DnsName $DNSServer -Server $DNSServer).NameHost
            Add-Member -InputObject $object NoteProperty DNSServerIP $DNSServer
            Add-Member -InputObject $object NoteProperty LatencyInMS ($results | Measure-Object -Average).Average
            $report += $object
            $progress++
            }
        Write-Progress -ErrorAction SilentlyContinue -Activity "Measuring Latency on locally defined servers" -Status "Done" -Id 1 -Completed


        Write-Verbose "Measuring well known and publicly open dns servers"
        $PublicDNSServers = New-Object System.Collections.ArrayList
        $PublicDNSServers.Add("8.8.8.8") | Out-Null
        $PublicDNSServers.Add("8.8.4.4") | Out-Null
        $PublicDNSServers.Add("208.67.220.123") | Out-Null
        $PublicDNSServers.Add("208.67.220.220") | Out-Null
        $PublicDNSServers.Add("208.67.220.222") | Out-Null
        $PublicDNSServers.Add("208.67.222.222") | Out-Null
        $PublicDNSServers.Add("4.2.2.1") | Out-Null
        $PublicDNSServers.Add("4.2.2.2") | Out-Null
        $PublicDNSServers.Add("4.2.2.3") | Out-Null
        $PublicDNSServers.Add("4.2.2.4") | Out-Null
        $PublicDNSServers.Add("4.2.2.5") | Out-Null
        $PublicDNSServers.Add("4.2.2.6") | Out-Null
        $PublicDNSServers.Add("68.4.16.30") | Out-Null
        $PublicDNSServers.Add("68.4.16.25") | Out-Null
        $PublicDNSServers.Add("8.26.56.26") | Out-Null
        $PublicDNSServers.Add("8.20.247.20") | Out-Null
        $PublicDNSServers.Add("156.154.70.1") | Out-Null
        $PublicDNSServers.Add("156.154.71.1") | Out-Null

        $progress = 1
        foreach ($DNSServer in $PublicDNSServers) {
            Write-Progress -ErrorAction SilentlyContinue -Activity "Measuring Latency on publicly available servers" -Status "Measuring $((Resolve-DnsName $DNSServer -Server $DNSServer).NameHost)" -PercentComplete ($progress/$PublicDNSServers.count*100) -Id 1
            $results = @()
            $results += (Measure-Command {Resolve-DnsName cloud.kemta.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName google.com -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName a.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName b.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName c.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty DNSServerName (Resolve-DnsName $DNSServer -Server $DNSServer).NameHost
            Add-Member -InputObject $object NoteProperty DNSServerIP $DNSServer
            Add-Member -InputObject $object NoteProperty LatencyInMS ($results | Measure-Object -Average).Average
            $report += $object
            $progress++
            }
        Write-Progress -ErrorAction SilentlyContinue -Activity "Measuring Latency on publicly available servers" -Status "Done" -Id 1 -Completed
        }

    else {
        Write-Verbose "Measuring custom dns servers"
        $progress = 1
        foreach ($DNSServer in $CustomDNSServer) {
            Write-Progress -ErrorAction SilentlyContinue -Activity "Measuring Latency on custom servers" -Status "Measuring $((Resolve-DnsName $DNSServer -Server $DNSServer).NameHost)" -PercentComplete ($progress/$CustomDNSServer.count*100) -Id 1
            $results = @()
            $results += (Measure-Command {Resolve-DnsName cloud.kemta.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName google.com -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName a.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName b.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $results += (Measure-Command {Resolve-DnsName c.root-servers.net -DnsOnly -Type A -NoHostsFile -server $DNSServer -ErrorAction SilentlyContinue}).TotalMilliSeconds
            $object = New-Object PSObject
            Add-Member -InputObject $object NoteProperty DNSServerName (Resolve-DnsName $DNSServer -Server $DNSServer).NameHost
            Add-Member -InputObject $object NoteProperty DNSServerIP $DNSServer
            Add-Member -InputObject $object NoteProperty LatencyInMS ($results | Measure-Object -Average).Average
            $report += $object
            $progress++
            }
    }

    $report | Sort-Object LatencyInMS

<#
 .Synopsis
  Measures DNS Latency
 .Description
  Grabs locally defined dns servers and some publicly available dns servers and measures the Latency (in milliseconds) on DNS queries from your computer to them
 .Parameter CustomDNSServer
  Specifies a custom list of DNS servers to measure, or it could be a single server
 .Example
  Measure-DNSLatency
  Measures DNS latency on locally defined DNS servers og some public available DNS servers
 .Example
  Measure-DNSLatency 8.8.8.8
  Measures the DNS latency only on the DNS server 8.8.8.8
 .Example
  Measure-DNSLatency 8.8.8.8,8.8.4.4
  Measures the DNS latency only on the DNS servers 8.8.8.8 and 8.8.4.4
 .Link
  http://cloud.kemta.net
 #>
} 
```

The different outputs will look something like this:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-579" alt="2014-08-15_10-25-49" src="http://cloud.kemta.net/wp-uploads/2014-08-15_10-25-491.png" width="1191" height="607" />][1]

&nbsp;

 [1]: http://cloud.kemta.net/wp-uploads/2014-08-15_10-25-491.png