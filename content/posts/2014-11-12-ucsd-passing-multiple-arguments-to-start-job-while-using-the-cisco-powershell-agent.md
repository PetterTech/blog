---
title: 'UCSD: Passing multiple arguments to start-job while using the Cisco PowerShell Agent'
author: nerenther
 
date: 2014-11-12T12:21:03+00:00
url: /index.php/2014/11/12/ucsd-passing-multiple-arguments-to-start-job-while-using-the-cisco-powershell-agent/
categories:
  - Cisco
  - UCS Director
tags:
  - powercli
  - Powershell
  - PSA
  - start-job
  - UCS Director

---
While the Cisco PowerShell Agent (PSA) that can be used in UCS Director isn&#8217;t exactly perfect, it can still be put to good use. As long as you now how to use it properly 😉

The major issue with using the PSA is that it doesn&#8217;t stick around to see if the commands/script was successful or not. As long as it delivered the commands successfully, it&#8217;s happy and your workflow will continue to the next step.

Jon Hildebrand describes a nice way around this in one of his blog posts: <a href="http://snoopj.wordpress.com/2014/11/05/cisco-powershell-agent-service-and-vmware-vum-powercli/" target="_blank" rel="noopener">http://snoopj.wordpress.com/2014/11/05/cisco-powershell-agent-service-and-vmware-vum-powercli/</a>

Using his approach, I was able get the PSA to stick around until the job finishes. However, I ran into a challenge when I wanted to pass multiple arguments to start-job. The solution I came up with was declaring the UCSD inputs I wanted to use as powershell variables in the script, before calling the start-job cmdlet. So the commands/script input looks like this:

 ```
$vm = "${custom_getVMDetails_7494.vmName}"
$annotation = "${Annotation}"
$annotationvalue = "${AnnotationValue}"
Start-Job -FilePath "C:\Powershell\Annotate-VM.ps1" -ArgumentList $vm,$annotation,$annotationvalue | Wait-Job 
```

In case you are wondering, this task is for setting annotations on a vm in vCenter.  
The powershell script I am calling is pretty simple:

 ```
 Param (
 [Parameter(Mandatory=$True,Position=0)][string]$VM,
 [Parameter(Mandatory=$True,Position=1)][string]$Annotation,
 [Parameter(Mandatory=$True,Position=2)][string]$AnnotationValue
 )
Add-PSSnapin vmware*
Connect-VIServer
Set-Annotation -Entity $VM -CustomAttribute "$($Annotation)" -Value "$($AnnotationValue)"
Disconnect-VIServer  -Confirm:$false 
```