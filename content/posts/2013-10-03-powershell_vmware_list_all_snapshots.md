---
title: 'PowerCLI: List all snapshots'
author: nerenther
 
date: 2013-10-03T10:27:41+00:00
url: /index.php/2013/10/03/powershell_vmware_list_all_snapshots/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - date created
  - get-snapshot
  - get-vm
  - powercli
  - Powershell
  - size
  - snapshot
  - vmware

---
It&#8217;s been a while since last update, again, so I figured I should at least provide something..

I recently started in a new job, and one of the first things I looked into was the amount of snapshots in our vmware environments. Not surprisingly there was a lot of snapshots, and very few of them had any hints of when they were taken and why.

The vsphere console doesn&#8217;t provide this info so I had to turn to PowerCLI to get the info I needed. PowerCLI is really just a snap-in to powershell so I felt right at home 🙂

After you start PowerCLI, you need to first connect to your vcenter server:

 ```
Connect-VIServer &lt;vcenter server&gt; 
```

You will be promted for username and password for vcenter. After powershell has connected to the vcenter server, all you need to is run this one-liner:

 ```
Get-VM | Get-Snapshot | Select VM,Name,@{N="SizeGB";E={@([math]::Round($_.SizeGB))}},Created 
```

This will return a list of all vm&#8217;s, their snapshots, size of the snapshots and the date the snapshot was taken.