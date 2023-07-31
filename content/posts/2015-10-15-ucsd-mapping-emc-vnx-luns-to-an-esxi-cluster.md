---
title: 'UCSD: Mapping EMC VNX LUNs to an ESXi cluster'
author: nerenther
 
date: 2015-10-15T13:05:07+00:00
url: /index.php/2015/10/15/ucsd-mapping-emc-vnx-luns-to-an-esxi-cluster/
categories:
  - Cisco
  - UCS Director
tags:
  - CUSD
  - EMC VNX
  - Powershell
  - Powershell agent
  - PSA
  - UCS Director

---
I have been struggling for quite some time with mapping luns from our vnx 5600 to entire clusters in our vCenter. We used to utilize a custom workflow a consultant wrote for us, but that workflow got borked after an update to UCS Director nearly a year ago.  
Revisiting the issue i found this example from Cisco: <a href="https://communities.cisco.com/docs/DOC-57382" target="_blank" rel="noopener">https://communities.cisco.com/docs/DOC-57382</a>

That example seems to work for other people but in our case the custom task in it never gave the correct output, so I had to look for a way around it.

The solution I came up with is overly complicated and can surely be simplified, but my lacking knowledge of javascript limits me quite a bit. My workflow to map luns to vSphere clusters consists roughly of these steps:

  * A powershell task running a script that does the following: 
      * Queries vCenter for esxi hosts in given cluster
      * Queries UCS Directors api for a report on storage groups
      * Putting together a storage group identity for each esxi host
      * Returning all storage group identities in a comma separated matter
  * A custom task to parse and convert the output from the powershell task to an output of the emcStorageGroupIdentity type
  * The builtin &#8220;add vnx lun to storage group&#8221; task

Here's how I have set it up:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-755" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-48-58.png" alt="2015-10-15_14-48-58" width="578" height="609" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-48-58.png 578w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-48-58-285x300.png 285w" sizes="(max-width: 578px) 100vw, 578px" />][1]

The custom task I use to convert the output from the powershell task is built up the way I describe in this blogpost: <a href="http://cloud.kemta.net/cisco-network/ucsd-grabbing-a-string-returned-from-a-powershell-task/" target="_blank" rel="noopener">http://cloud.kemta.net/cisco-network/ucsd-grabbing-a-string-returned-from-a-powershell-task/</a>

The only difference is the name and type of the output.

Now, let's look at the workflow user inputs:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-756" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-17-37.png" alt="2015-10-15_14-17-37" width="947" height="339" />][2]

In this workflow I haven't configured any outputs, so let's move along to the first task: the powershell task.

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-757" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-41-13.png" alt="2015-10-15_14-41-13" width="1213" height="580" />][3]

The reason I have to do a split on the StorageAccount input is that in the script I only want the hostname of the storage system. I could just as well have done it within the script itself.

The powershell script looks like this:

 ```
    Param (
    [Parameter(Mandatory=$True,Position=0)][string]$Pod,
    [Parameter(Mandatory=$True,Position=1)][string]$StorageAccount,
    [Parameter(Mandatory=$True,Position=2)][string]$Cluster
        )
#Add the vmware snapin
Add-PSSnapin vmware*

#Connecting to vCenter
Connect-VIServer vcenter01 -WarningAction Ignore | out-null

#Getting ESXi hosts
$vmhosts = get-vmhost -location $Cluster

#Polling a report on storage groups from UCS Director
$webrequest = Invoke-WebRequest 'https://ucsd01/app/api/rest?opName=userAPIGetTabularReport&opData={param0:"510",param1:"$($StorageAccount);$($Pod)",param2:"STORAGE-GROUPS-T51"}' -Headers @{"X-Cloupia-Request-Key"="ThisIsNotMyAPIKey"}
#Converting the report from json
$convertedData = $webrequest.content | ConvertFrom-Json

#Creating a blank array to store end result in
$VMhostsArray = @()

#Looping through all esxi hosts found
foreach ($vmhost in $vmhosts) {
    $hostname = (($vmhost.name).split("."))[0] #Removing domain name from esxi host name
    $WWN_Name = ($convertedData.serviceresult.rows | where {$_.Name -like "$($hostname)"}).WWN_Name #Grabbing WWN from UCSD report
    $StorageGroupIdentity = "$($StorageAccount);$($Pod);$($WWN_Name);$($hostname)" #Putting together the storage group identity
    $VMhostsArray += $StorageGroupIdentity #Adding the storage group identity to the array
    }

#Disconnecting from vCenter
Disconnect-VIServer vcenter01 -Confirm:$false

#Returning array to console, comma separated
return $VMhostsArray -join ","
 ```

On my test cluster with only two esxi hosts, the output looks like this:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-758" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-54-42.png" alt="2015-10-15_14-54-42" width="1154" height="104" />][4]

After the custom task has converted the powershell output it looks like this in plain text:

 ```
 storageaccount;pod;wwn;esxiHostname1,storageaccount;pod;wwn;esxiHostname2 
 ```

Since the output from the custom task is of the emcStorageGroupIdentity type I can simply map it to the builtin &#8220;add vnx lun to storage group&#8221; task:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-760" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-47-52.png" alt="2015-10-15_14-47-52" width="1004" height="654" />][5]

And that's really all there is to it. If you want to download my example workflow, you can do so here: <http://4.234.145.218/wp-content/uploads/2015/10/mapVNXLunToESXiCluster.zip>

&nbsp;

 [1]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-48-58.png
 [2]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-17-37.png
 [3]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-41-13.png
 [4]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-54-42.png
 [5]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-15_14-47-52.png