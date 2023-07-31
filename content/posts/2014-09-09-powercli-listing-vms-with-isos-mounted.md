---
title: 'PowerCLI: Listing VMs with ISOs mounted'
author: nerenther
 
date: 2014-09-09T05:55:24+00:00
url: /index.php/2014/09/09/powercli-listing-vms-with-isos-mounted/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - dismount iso
  - function
  - get-isomounts
  - iso mount
  - powercl
  - powersh
  - vmware

---
For almost a year ago, I posted a simple one-liner to list all VMs who has ISOs mounted. You can view that post here: <a href="http://cloud.kemta.net/2013/10/powershell-vmware-list-all-vms-with-iso-mounted-and-dismount-them/" target="_blank" rel="noopener">http://cloud.kemta.net/2013/10/powershell-vmware-list-all-vms-with-iso-mounted-and-dismount-them/</a>

That post was written before I truly discovered the major advantages of using Get-View instead of Get-VM, Get-VMHost and so on. If used correctly, there&#8217;s a major difference in speed when using Get-View over Get-VM.  
When writing this post I checked the differences in speed when using the old way that I linked to above and my new function (which I&#8217;ll get to in a second or two..), the result was as follows:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-634" alt="get-isomounts_measured" src="http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts_measured.png" width="972" height="528" srcset="http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts_measured.png 972w, http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts_measured-300x163.png 300w, http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts_measured-768x417.png 768w" sizes="(max-width: 972px) 100vw, 972px" />][1]

As you can see, the difference is pretty clear. 5 seconds vs. 1.6 minutes&#8230;

So, without further ado, I present to you the code for Get-ISOMounts:

<pre lang="PowerShell">function Get-ISOMounts
{
    [CmdletBinding()]
        Param (
            [switch]$Dismount
              )
        $VMs = Get-View -ViewType virtualmachine -Property name,Config.Hardware.Device
        $VMsWithISO = @()
        $progress = 1
        foreach ($VM in $VMs) {
            Write-Progress -Activity "Checking if VMs have ISOs mounted" -Status "Working on $($VM.name)" -PercentComplete ($progress/$VMs.count*100) -Id 1 -ErrorAction SilentlyContinue
            if (($VM | select -ExpandProperty config | select -ExpandProperty hardware | select -ExpandProperty device | select -ExpandProperty deviceinfo | where {$_.Summary -like "ISO*"}) -ne $NULL) {
                $object = New-Object PSObject
                Add-Member -InputObject $object NoteProperty VM $VM.Name
                Add-Member -InputObject $object NoteProperty "ISO mounted" (($VM | select -ExpandProperty config | select -ExpandProperty hardware | select -ExpandProperty device | select -ExpandProperty deviceinfo | where {$_.Summary -like "ISO*"}).Summary).Substring(4)
                $VMsWithISO += $object
                $object
            $progress++
            }
        }
        Write-Progress -Activity "Checking if VMs have ISOs mounted" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue

        if ($Dismount)
            {
            Write-Verbose "Starting to dismount ISOs"
            $progress = 1
            foreach ($VM in $VMsWithISO) {
                Write-Progress -Activity "Dismounting ISOs" -Status "Working on $($VM.name)" -PercentComplete ($progress/$VMsWithISO.count*100) -Id 1 -ErrorAction SilentlyContinue
                Get-CDDrive -VM $VM.Name | Set-CDDrive -NoMedia -Confirm:$False
                }
            Write-Progress -Activity "Dismounting ISOs" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue
            $progress++
            }

&lt;#
 .Synopsis
  Lists all VMs with ISOs mounted, can also dismount them
 .Description
  Lists all VMs with ISOs mounted. If the switch -Dismount is present all mounted ISOs will be dismounted
 .Example
  Get-ISOMounts
  Lists all mounted ISOs in the vCenter
 .Example
  Get-Snapshots -Dismount
  Lists all mounted ISOs on VMs in the vCenter and then dismounts them
 .Link
  http://cloud.kemta.net
 #>
}
</pre>

I feel the help section should speak for itself, but I&#8217;ll provide you a screenshot none the less. Just running Get-ISOMounts will provide you with an output looking like this:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-635" alt="get-isomounts" src="http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts.png" width="1224" height="712" srcset="http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts.png 1224w, http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts-300x175.png 300w, http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts-1024x596.png 1024w, http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts-768x447.png 768w" sizes="(max-width: 1224px) 100vw, 1224px" />][2]

 [1]: http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts_measured.png
 [2]: http://4.234.145.218/wp-content/uploads/2014/09/get-isomounts.png