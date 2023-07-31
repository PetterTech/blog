---
title: HP ACU cli quick guide
author: nerenther
 
date: 2012-10-03T05:46:20+00:00
url: /index.php/2012/10/03/hp-acu-cli-quick-guide/
categories:
  - ACU
  - HP
tags:
  - ACU
  - array
  - cli
  - create
  - disk
  - HP

---
Guess what? It's time for something different than powershell 😛

I finally got myself a server to play around with Hyper-V on. This has been sorely missed for a long time. I worked a lot with Hyper-V in my previous job, and even built a small data center running on Hyper-V. But at my current job we only use vmware, which is a great product but to expensive in my book. Especially when we are finally looking at a datacenter license from Microsoft and we already have the System Center suite. This means that we can save a ton of money on switching from vmware to Hyper-V.

Anyway&#8230;In this blogpost I want to show you a little about the HP Array Configuration Utility command-line interface.  
I usually use the graphical interface for creating volumes and such, but for some reason I couldn't get it working on my Hyper-V test server. So instead of looking on how to fix that I decided to give the cli a shot. What I want to achieve with this post is to show you how the steps you need after putting one or more new disks in the server.

The ACU cli can be launched by running C:Program Files (x86)CompaqHpacucliBinhpacucli.exe.

The first command you should know about is &#8220;controller all show&#8221;, this will show you all the controllers installed in the server. The output will look something like this:

 ```
 => controller all show 
 ```

 ```
 Smart Array P410i in Slot 0 (Embedded) (sn: 50014380124xxxxx) 
 ```

This show that my controller is installed in slot 0, to get some more info on this controller I could run &#8220;controller slot=0 show&#8221;, the output should look something like this:

 ```
  => controller slot=0 show

Smart Array P410i in Slot 0 (Embedded)
 Bus Interface: PCI
 Slot: 0
 Serial Number: 50014380124D5620
 Cache Serial Number: PBCDF0CRHZU5D4
 RAID 6 (ADG) Status: Disabled
 Controller Status: OK
 Hardware Revision: C
 Firmware Version: 5.70
 Rebuild Priority: Medium
 Expand Priority: Medium
 Surface Scan Delay: 15 secs
 Surface Scan Mode: Idle
 Queue Depth: Automatic
 Monitor and Performance Delay: 60 min
 Elevator Sort: Enabled
 Degraded Performance Optimization: Disabled
 Inconsistency Repair Policy: Disabled
 Wait for Cache Room: Disabled
 Surface Analysis Inconsistency Notification: Disabled
 Post Prompt Timeout: 0 secs
 Cache Board Present: True
 Cache Status: OK
 Cache Ratio: 25% Read / 75% Write
 Drive Write Cache: Disabled
 Total Cache Size: 1024 MB
 Total Cache Memory Available: 912 MB
 No-Battery Write Cache: Disabled
 Cache Backup Power Source: Capacitors
 Battery/Capacitor Count: 1
 Battery/Capacitor Status: OK
 SATA NCQ Supported: True 
 ```

On my test server I have already created a mirrored volume on which I have installed Hyper-V. I have only one extra disk, so I cannot show you how to create a fancy raid configuration but nevertheless I will show you how to create an array and a logical disk.

The first thing we need to do is to find any unassigned disk connected to the controller. This is done by running the command &#8220;controller slot=0 physicaldrive allunassigned show&#8221; (replace slot=0 with the slot where your controller is connected). The output will look something like this:

 ```
 => controller slot=0 physicaldrive allunassigned show

Smart Array P410i in Slot 0 (Embedded)

 unassigned

 physicaldrive 1I:1:3 (port 1I:box 1:bay 3, SATA, 500 GB, OK) 
```

So here we see that I have one unassigned disk that I can use. Given that I want to use all unassigned disks to create a new logical disk in a new array I can run the command &#8220;controller slot=0 create type=ld drives=allunassigned raid=0&#8221;  
This will create a new array and a new logical drive that uses all unassigned drives, the raid level is 0 (striping)

Thats basically what you need to do from the acu. But before you can use the disk in Windows you need to initialize it, create a partition and so on, the required steps could be something like this:

 ```
DISKPART> list disk
DISKPART> select disk 1
DISKPART> attributes disk clear readonly
DISKPART> online disk
DISKPART> create partition primary
DISKPART> list volume
DISKPART> select volume 4
DISKPART> assign letter=e:
DISKPART> EXIT
C:UsersAdministrator> format E: /Q 
```

&nbsp;