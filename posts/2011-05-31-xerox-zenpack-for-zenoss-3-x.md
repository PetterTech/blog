---
title: Xerox ZenPack for Zenoss 3.x
author: nerenther
type: post
date: 2011-05-31T11:12:33+00:00
url: /index.php/2011/05/31/xerox-zenpack-for-zenoss-3-x/
categories:
  - Zenoss
  - Zenpack
tags:
  - Xerox
  - Zenoss
  - Zenpack

---
At the company where I currently work we lease a bunch of Xerox copiers. Those leasing contracts are based on number of prints per device.  
That means that once a month we have to gather pagecounts from all our printers (about 100 of them) and report them to our supplier, which takes a lot of time.

Since we already were using Zenoss for monitoring of the printers I figured I could try and gather the information via snmp.  
That resulted in this ZenPack.

It creates a device class, /Printer/Laser/Xerox and assigns a Monitoring Template called XeroxPageCounts.  
The monitoring template consist of 3 DataPoints, BlackPageCount, ColorPageCount and TotalPageCount. It also includes a graph using the 3 DataPoints.

What I did after creating this ZenPack is create a new view which contains all these graphs. So now we simply open the new view and all the info we need is right there, instead of opening the web console of every printer.  
Feel free to use and distribute this ZenPack. Download [here][1] (rename to .egg)

**Update:**  
Version 1.0 of this zenpack does not work with zenoss 3.2.1.  
Version 1.1 works, download <a href="http://dl.dropbox.com/u/33041052/bloggting/zenoss/ZenPacks.nerenther.XeroxPageCounts-1.1-py2.6.egg" target="_blank" rel="noopener">here</a>

 [1]: http://cloud.kemta.net/wp-uploads/2011/05/ZenPacks.nerenther.XeroxPageCounts-1.0-py2.6.egg