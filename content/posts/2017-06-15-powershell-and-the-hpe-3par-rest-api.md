---
title: Powershell and the HPE 3PAR REST API
author: nerenther
 
date: 2017-06-15T12:01:01+00:00
url: /index.php/2017/06/15/powershell-and-the-hpe-3par-rest-api/
categories:
  - HPE 3PAR
  - Powershell
tags:
  - 3PAR
  - boot lun
  - HPE 3PAR
  - Invoke-RestMethod
  - Powershell
  - REST

---
Lately, I've had the pleasure of using Powershell to automate some of the basic tasks we do on our HPE 3PAR systems: creating volumes, adding them to volume sets, exporting them and so on.

Since my experience with REST APIs was rather limited it was quite daunting at first but once you get the hang of how REST works and the Invoke-RestMethod cmdlet it's really not that bad.

_Disclaimer: The examples below will vary somewhat in how I do certain things, simply because I had to learn all this from scratch. Hence, the first examples will sometimes do things &#8220;less correct&#8221; than the later examples since this also was quite the learning curve for me._

The first step in doing anything with the REST API will always be to create a session key. If you're not familiar with APIs, think of a session key as username and password combined into one string. You will need to add the session key to every REST call you do later on in order to authenticate yourself.  
To create a session key from powershell you can use the following line:

 ```
 $key = (Invoke-RestMethod -Method post -Uri "http://<3PAR ip/hostname>:8008/api/v1/credentials" -Body '{"user":"<username>","password":"<password>"}' -ContentType 'application/json').key 
 ```

This will store you session key in the $key variable which you will need to add to the header of future REST calls.

Keep in mind that each session key is valid for 15 minutes by default, but you should always delete it after each use.

To delete a session key you can use the following line, given that your key is still stored in $key:

 ```
 Invoke-RestMethod -Method delete -Uri "http://<3PAR ip/hostname>:8008/api/v1/credentials/$($key)" -Headers @{'Accept'='application/json'} 
 ```

Now that you have your session key you can start to do some more interesting stuff, like creating a volume:

 ```
 $body = '{"name":"'
 $body = $body + "3parDatastore01"
 $body = $body + '","cpg":"SSD_r5","sizeMiB":2097152,"tdvv":true}'

 Invoke-RestMethod -Method Post -Uri "http://<3PAR ip/hostname>:8008/api/v1/volumes" -Headers @{'X-HP3PAR-WSAPI-SessionKey'=$key} -ContentType application/json -Body $body 
 ```

The above example will create a datastore named &#8220;3parDatastore01&#8221; in the cpg named &#8220;SSD_r5&#8221; with 2TB of space and dedupe enabled. As you can see our session key is passed in the header as X-HP3PAR-WSAPI-SessionKey.

_If your well versed in JSON and powershell you can probably tell that I'm not 🙂_  
_The body you're sending in the REST call is supposed to be formatted as a JSON object and in the above example I'm creating the JSON object manually by building it up as a string. In a later example I'll show a more &#8220;correct&#8221; way to do it._

The next step will usually be to export the volume or to add it to a volume set. Let's look at an example where I add a volume to an existing volume set:

 ```
 $body = '{"action":1,"setmembers":["'
 $body = $body + "3parDatastore01"
 $body = $body + '"]}'
 Invoke-RestMethod -Method Put -Uri "http://<3PAR ip/hostname>:8008/api/v1/volumesets/testVVSet" -Headers @{'X-HP3PAR-WSAPI-SessionKey'=$key} -ContentType application/json -Body $body 
 ```

_Again, I'm building the JSON object as a string here instead of doing it the correct way._

The above example will add the volume called &#8220;3parDatastore01&#8221; (which we created in the previous example) to the existing volumeset called &#8220;testVVSet&#8221;. If you already have exported the volume set to a host or host set it is now available for the host(s) to use.

The next step for me now was to query the created volume since I had to find the wwn of the volume. There are two ways I have done this: By querying all volumes and by querying a single volume.  
To query all volumes you can use this line:

 ```
 Invoke-RestMethod -Method get -Uri "http://<3PAR ip/hostname>:8008/api/v1/volumes" -Headers @{'X-HP3PAR-WSAPI-SessionKey'=$key} -ContentType "application/json" 
 ```

To query a single volume you can use this line:

 ```
 Invoke-RestMethod -Method get -Uri "http://<3PAR ip/hostname>:8008/api/v1/volumes/<volumename>" -Headers @{'X-HP3PAR-WSAPI-SessionKey'=$key} -ContentType "application/json" 
 ```

You can also build a query directly in the uri you're accessing by adding ?query=&#8221;<your query>&#8221; after /volumes. Here's an example from HPE's own guide:

 ```
 https://<storage_system>:8080/api/v1/volumes?query=”wwn EQ value1 OR wwn EQ value2 OR userCPG EQ value3 OR snapCPG EQ value4 OR wwn EQ valueN” 
 ```

Of course, you can also do filtering in powershell if you're more comfortable with that (I know I am) but then you will have wasted computing power on both the SAN and the machine you're running powershell on 😉

<p style="padding-left: 60px;">
  Bonus:<br /> If you're running vmware you can now use powercli to create the datastore. Example:
</p>

```
$volume = Invoke-RestMethod -Method get -Uri "http://<3PAR ip/hostname>:8008/api/v1/volumes/3parDatastore01" -Headers @{'X-HP3PAR-WSAPI-SessionKey'=$key} -ContentType "application/json"
$wwn = "naa." + ($volume.members).wwn
Get-VMHostStorage <esxHost> -RescanAllHba
Start-Sleep -Seconds 10
New-Datastore -VMHost <esxHost> -Name "3parDatastore01" -Path $wwn.ToLower() -Vmfs -FileSystemVersion "5" 
```

<p style="padding-left: 60px;">
  This will query the REST API for info on the volume named 3parDatastore01 (which we created earlier), start a rescan of all HBAs and then create a datastore with the same name as the volume.<br /> You can test without the Start-Sleep, but in my case it was needed.
</p>

If you are not using volume sets and exporting those to hosts, the next logical step would be to export the newly created volume to a host or hostset. To export a volume to a single host you can do something like this:

 ```
 $Header = @{}
 $Header.Add("accept","application/json")
 $Header.Add("x-hp3par-wsapi-sessionkey",$key)
 $Body = @{
 "lun" = 255
 "volumeName" = "3parDatastore01"
 "hostname" = "esx01"
 }
Invoke-RestMethod -Method Post -Uri http://<3PAR ip/hostname>:8008/api/v1/vluns -Headers $header -Body ($Body | ConvertTo-Json) -ContentType "application/json" 
```

_Notice the difference in the way I format the body? This is the more correct way to do it, creating a hashtable and converting it to JSON with ConvertTo-Json._  
_I also create the header before the Invoke-RestMethod line here._

The example above will export 3parDatastore01 to esx01 with a lun id of 255.

Lastly, I would like to provide you with an example on how we create our boot luns. This is an extract of a powershell function I wrote, in the original function there's a lot more automation, error handling and logging but I removed it here for the sake of readability.

 ```
$3PARHostname = "3Par01"
$ESXiHostname = "newEsxi01"
$3PARcred = @{
user="fakeUser"
password="fakePassword"
 }

$APIkey = (Invoke-RestMethod -Method Post -Uri "http://$($3PARHostname):8008/api/v1/credentials" -Body ($3PARcred | ConvertTo-Json) -ContentType 'application/json').key

$Header = @{}
$Header.Add("accept","application/json")
$Header.Add("x-hp3par-wsapi-sessionkey",$APIkey)

$Body = @{
 "tdvv" = $true
 "cpg" = "SSD_r5"
 "name" = "$($ESXiHostname)"
 "sizeMiB" = 10240
 "policies" = @{
 oneHost = $true
 }
 }

Invoke-RestMethod -Method Post -Uri http://$($3PARHostname):8008/api/v1/volumes -Headers $Header -Body ($Body | ConvertTo-Json) -ContentType "application/json"

Clear-Variable Body

$Body = @{
"lun" = 255
"volumeName" = "$($ESXiHostname)"
"hostname" = "$($ESXiHostname)"
 }

Invoke-RestMethod -Method Post -Uri http://$($3PARHostname):8008/api/v1/vluns -Headers $header -Body ($Body | ConvertTo-Json) -ContentType "application/json" ```

The key thing here is the policy (oneHost) that we set on the volume when we create it. This prevents the bootlun being exported to additional hosts.

Sources:  
HPE 3PAR API doc: <a href="http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=c03606339" target="_blank" rel="noopener">http://h20564.www2.hpe.com/hpsc/doc/public/display?docId=c03606339</a>