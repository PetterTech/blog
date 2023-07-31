---
title: 'UCSD: Grabbing a string returned from a Powershell task'
author: nerenther
 
date: 2015-10-13T12:16:20+00:00
url: /index.php/2015/10/13/ucsd-grabbing-a-string-returned-from-a-powershell-task/
categories:
  - Cisco
  - UCS Director
tags:
  - CUSD
  - Powershell
  - Powershell agent
  - PSA
  - UCS Director

---
My last post described how to get around some issues with using Powershell tasks in workflows. While that post surely enables you to uilize powershell to do stuff for you, what about if you want Powershell to grab stuff for you and return them in a usable matter?  
This time I&#8217;m going to show you how you can return a string from Powershell and use it further down in the workflow. Cisco has provided an example on how to do that here: <a title="https://communities.cisco.com/docs/DOC-58250" href="https://communities.cisco.com/docs/DOC-58250" target="_blank" rel="noopener">https://communities.cisco.com/docs/DOC-58250</a>

The example from Cisco is what I started with, but I have modified it a bit since I didn&#8217;t want anything that advanced.

So let&#8217;s set the stage:  
Say you have a workflow that uses the execute powershell command task and you want that task to output something you can utilize further down  in the workflow, e.g. sending that output in an email. In this case we will use powershell to give us a comma separated list of esxi hosts in a given cluster.  
The workflow has 1 defined workflow user input, vspherecluster, and 1 defined workflow user output, PowerShell_output.

There are a few things we need to get this done:

  * A powershell script that only outputs one line with all the hosts
  * A powershell task that runs said script
  * A custom tasks that parses the powershell output and only returns the string returned by the powershell script
  * A send email task sending the output

First off, the powershell script:

 ```
 Param (
 [Parameter(Mandatory=$True,Position=0)][string]$Cluster
 )
#Add the vmware snapin
Add-PSSnapin vmware*

#Connecting to vCenter
Connect-VIServer drt01srv003 -WarningAction Ignore | out-null

#Getting ESXi hosts
$vmhosts = get-vmhost -Location $cluster

#Creating a blank array to put hostnames in
$hostarray =@()

#Looping through all ESXi hosts and adding their names to the array
foreach ($vmhost in $vmhosts) {
 $hostarray += $vmhost.name
 }

#Disconnecting from vCenter
Disconnect-VIServer drt01srv003 -Confirm:$false

#Comma separaing the array and returning it to console
return $hostarray -join "," 
```

The comments should be pretty explanatory, but in essence it connects to vCenter, grabs the name of the esxi hosts in the given cluster and then returns them comma separated.  
This works fine and dandy in a powershell console, but the output from the powershell task will look rather different, we&#8217;ll look at that in a second. Secondly, the powershell task kicking off the script:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-737" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-41-33.png" alt="2015-10-14_13-41-33" width="981" height="472" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-41-33.png 981w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-41-33-300x144.png 300w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-41-33-768x370.png 768w" sizes="(max-width: 981px) 100vw, 981px" />][1]

The output from this task will look something like this:[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-746" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_14-02-07.png" alt="2015-10-14_14-02-07" width="1163" height="146" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_14-02-07.png 1163w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_14-02-07-300x38.png 300w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_14-02-07-1024x129.png 1024w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_14-02-07-768x96.png 768w" sizes="(max-width: 1163px) 100vw, 1163px" />][2]

If you&#8217;re unfamiliar with how UCS Director handles powershell but familiar with powershell, then that&#8217;s probably not what you expected at all.

Now we need to parse that output and return only the string we want. I made a custom task for this, like in the example from Cisco:

Required inputs:  
[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-738" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-42-43.png" alt="2015-10-14_13-42-43" width="1155" height="246" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-42-43.png 1155w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-42-43-300x64.png 300w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-42-43-1024x218.png 1024w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-42-43-768x164.png 768w" sizes="(max-width: 1155px) 100vw, 1155px" />][3]

Outputs:  
[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-739" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-04.png" alt="2015-10-14_13-43-04" width="1087" height="240" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-04.png 1087w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-04-300x66.png 300w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-04-1024x226.png 1024w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-04-768x170.png 768w" sizes="(max-width: 1087px) 100vw, 1087px" />][4]

The beauty of doing it like this is that you can create any kind of output type just by changing the output type. I actually use this to create outputs of other types as well, for example vmwareHostNodeIdentity, vmwareClusterIdentity and so on. It&#8217;s just easier for me to use powershell to put those kind of outputs together instead of using javascript since I really don&#8217;t know javascript.

And then the script:

```
importPackage(com.cloupia.lib.util);
importPackage(java.util);

var xml = input.xml;

// Try and parse the <Objects>...</Objects> section
var objects_xml = XMLUtil.getValue("Objects", xml);
logger.addDebug("Grabbed objects from xml: "+objects_xml);

// Parse the objects list now (should also be a single section):
object_list = XMLUtil.getTag("Object",objects_xml.get(0))
logger.addDebug("Grabbed object_list from xml: "+object_list);

//Convert object_list to string
list = String(object_list);
logger.addDebug("list: "+list);

// Slice off last xml characters
parsedString = list.substring(30);
logger.addDebug("After removing first characters: "+parsedString);
parsedString = parsedString.slice(0,-10);
logger.addDebug("After removing last characters: "+parsedString);

output.parsedString = parsedString; 
```

When using the custom task in a workflow I map the input to the output from the powershell task:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-740" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-32.png" alt="2015-10-14_13-43-32" width="946" height="397" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-32.png 946w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-32-300x126.png 300w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-32-768x322.png 768w" sizes="(max-width: 946px) 100vw, 946px" />][5]

And the output to the defined workflow user output:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-741" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-56.png" alt="2015-10-14_13-43-56" width="597" height="278" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-56.png 597w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-56-300x140.png 300w" sizes="(max-width: 597px) 100vw, 597px" />][6]

Lastly, it&#8217;s the send email task which is pretty simple:

[<img decoding="async" loading="lazy" class="alignnone size-full wp-image-742" src="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-44-27.png" alt="2015-10-14_13-44-27" width="1087" height="625" srcset="http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-44-27.png 1087w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-44-27-300x172.png 300w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-44-27-1024x589.png 1024w, http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-44-27-768x442.png 768w" sizes="(max-width: 1087px) 100vw, 1087px" />][7]

If you want to test this yourself, you can download this example workflow here: <a href="http://4.234.145.218/wp-content/uploads/2015/10/getPowershellOutput.zip" target="_blank" rel="noopener">http://4.234.145.218/wp-content/uploads/2015/10/getPowershellOutput.zip</a>

 [1]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-41-33.png
 [2]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_14-02-07.png
 [3]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-42-43.png
 [4]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-04.png
 [5]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-32.png
 [6]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-43-56.png
 [7]: http://4.234.145.218/wp-content/uploads/2015/10/2015-10-14_13-44-27.png