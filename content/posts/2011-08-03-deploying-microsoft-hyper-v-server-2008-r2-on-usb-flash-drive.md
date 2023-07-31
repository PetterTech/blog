---
title: Deploying Microsoft Hyper-V Server 2008 R2 on USB Flash Drive
author: nerenther
 
date: 2011-08-03T12:04:31+00:00
url: /index.php/2011/08/03/deploying-microsoft-hyper-v-server-2008-r2-on-usb-flash-drive/
categories:
  - Hyper-V
  - Microsoft
tags:
  - Hyper-V
  - microsoft

---
Just thought I should share this link:

<http://technet.microsoft.com/en-us/library/ee731893(WS.10).aspx>

I have tried this on a HP DL380 G6 and it worked like a charm.  
One of the advantages of using that kind of server is that it has internal usb ports so you don&#8217;t have to worry about someone accidentally unplugging the usb drive.

Why should I run a server os from a usb drive you may ask. Well, the biggest advantage is that if your storing all virtual machines on e.g. a SAN anyway you don&#8217;t have to buy internal disks for your Hyper-V hosts.  
Another advantage is that is that usb drives are like ssd disks, they have no movable parts that can break, and they have a much lower power consumption.