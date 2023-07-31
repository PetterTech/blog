---
title: 'PowerCLI: Function for listing snapshots'
author: nerenther
 
date: 2014-09-17T07:16:57+00:00
url: /index.php/2014/09/17/powercli-function-for-listing-snapshots/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - function
  - get-snapshot
  - get-snapshots
  - get-vievent
  - powercli
  - Powershell
  - snapshots
  - vmware

---
My very first PowerCLI related post was about this same topic: listing snapshot info using PowerCLI.  
In my original post (which you can see <a href="http://cloud.kemta.net/2013/10/powershell_vmware_list_all_snapshots/" target="_blank" rel="noopener">here</a>) I only wrote a pretty simple one-liner. Which was kind of okay, but it was missing one crucial thing: who took the snapshot?

Why vmware hasn't found a way to include a username in the get-snapshot cmdlet is something I just can't understand. There's really not much code needed to add this to the output, and there's several ways of doing so.

I found that using Get-Snapshot and Get-VIEvent together was the easiest way to get all the info I want. It's not a perfect solution, seeing as I really wanted to make use of the much faster Get-View instead of Get-Snapshot, but I have yet to figure out a good way to handle snapshot trees using Get-View.

As usual I created a function for this, Get-Snapshots:

 ```
function Get-Snapshots
{
            [CmdletBinding()]
            Param (
                [string]$VM = '*'
                  )

    $collection = @()
    Write-Progress -Activity "Finding snapshots..." -Status "This will tak a while, please wait" -PercentComplete 20 -Id 1 -ErrorAction SilentlyContinue
    $snapshots = Get-Snapshot -vm $VM
    Write-Progress -Activity "Finding snapshots..." -Status "Found all snapshots" -Completed -Id 1 -ErrorAction SilentlyContinue

    $progress = 1
    foreach ($snapshot in $snapshots) {
        Get-VIEvent -Start ($snapshot.Created).addminutes(-5) -Finish ($snapshot.Created).addminutes(5) -Entity $Snapshot.vm.name -Types info -maxsamples 20 | Where-Object {$_.FullFormattedMessage -like "*Create virtual machine snapshot*"} | ForEach-Object {
                Write-Progress -Activity "Finding snapshots" -Status "Working on $($_.Vm.Name)" -PercentComplete ($progress/$snapshots.count*100) -Id 1 -ErrorAction SilentlyContinue
                $object = New-Object PSObject
                Add-Member -InputObject $object NoteProperty VM $_.Vm.Name
                Add-Member -InputObject $object NoteProperty User $_.Username
                Add-Member -InputObject $object NoteProperty "Snapshot name" $Snapshot.Name
                Add-Member -InputObject $object NoteProperty "Snapshot description" $Snapshot.Description
                Add-Member -InputObject $object NoteProperty SizeGB ([math]::Round($Snapshot.SizeGB))
                Add-Member -InputObject $object NoteProperty Time $_.CreatedTime
                $collection += $object
                }
        $progress++
        }

    Write-Progress -Activity "Finding snapshots" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue
    $collection

    <#
     .Synopsis
      Lists snapshots in vCenter
     .Description
      List all snapshots in the entire vCenter
     .Example
      Get-Snapshots
      Lists all snapshots in the vCenter
     .Link
      http://cloud.kemta.net
     #>
}

 ```

You can run the function as it is, without any parameters, or you can specify which vm you want to get the snapshots of:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-642" alt="get-snapshots" src="http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots.png" width="951" height="188" srcset="http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots.png 951w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-300x59.png 300w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-768x152.png 768w" sizes="(max-width: 951px) 100vw, 951px" />][1]

As you can see, the output is a list. If you want it to be more readable for human eyes, I recommend piping it to Format-Table:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-643" alt="get-snapshots-ft" src="http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-ft.png" width="1031" height="172" srcset="http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-ft.png 1031w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-ft-300x50.png 300w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-ft-1024x171.png 1024w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-ft-768x128.png 768w" sizes="(max-width: 1031px) 100vw, 1031px" />][2]

If you would rather run this as a script, instead of using the function, here's the code for that:

 ```
    $collection = @()
    $snapshots = Get-Snapshot -vm *

    $progress = 1
    foreach ($snapshot in $snapshots) {
        Get-VIEvent -Start ($snapshot.Created).addminutes(-5) -Finish ($snapshot.Created).addminutes(5) -Entity $Snapshot.vm.name -Types info -maxsamples 20 | Where-Object {$_.FullFormattedMessage -like "*Create virtual machine snapshot*"} | ForEach-Object {
                Write-Progress -Activity "Finding snapshots" -Status "Working on $($_.Vm.Name)" -PercentComplete ($progress/$snapshots.count*100) -Id 1 -ErrorAction SilentlyContinue
                $object = New-Object PSObject
                Add-Member -InputObject $object NoteProperty VM $_.Vm.Name
                Add-Member -InputObject $object NoteProperty User $_.Username
                Add-Member -InputObject $object NoteProperty "Snapshot name" $Snapshot.Name
                Add-Member -InputObject $object NoteProperty "Snapshot description" $Snapshot.Description
                Add-Member -InputObject $object NoteProperty SizeGB ([math]::Round($Snapshot.SizeGB))
                Add-Member -InputObject $object NoteProperty Time $_.CreatedTime
                $collection += $object
                }
        $progress++
        }

    Write-Progress -Activity "Finding snapshots" -Status "All done" -Completed -Id 1 -ErrorAction SilentlyContinue
    $collection

 ```

The output, $collection, can be piped to Format-Table if you want a nice table of it:

[<img decoding="async" loading="lazy" class="aligncenter size-full wp-image-644" alt="get-snapshots-scripts" src="http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-scripts.png" width="1039" height="125" srcset="http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-scripts.png 1039w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-scripts-300x36.png 300w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-scripts-1024x123.png 1024w, http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-scripts-768x92.png 768w" sizes="(max-width: 1039px) 100vw, 1039px" />][3]

&nbsp;

 [1]: http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots.png
 [2]: http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-ft.png
 [3]: http://4.234.145.218/wp-content/uploads/2014/09/get-snapshots-scripts.png