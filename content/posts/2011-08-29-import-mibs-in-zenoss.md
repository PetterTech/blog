---
title: Import MIBs in Zenoss
author: nerenther
 
date: 2011-08-29T11:02:57+00:00
url: /index.php/2011/08/29/import-mibs-in-zenoss/
categories:
  - Zenoss
tags:
  - Linux
  - MIB
  - Zenoss

---
If you are using Zenoss as a monitoring solution, chances are you are sending snmp traps to it, right?  
In that case you should always remember to import the MIBs for the devices you are monitoring. Because if you don&#8217;t it can be a real pain in the ass to figure what it is wrong when all you see is a &#8220;warning snmp trap enterprises.2.6.211.4.11&#8221;.

Sadly there is no way to import MIBs using the gui in Zenoss, you have to use the cli. So here&#8217;s a short guide:

First you need to download the MIBs.  
The easiest way to do that is to google the oid that is sent to Zenoss, there are a bunch of sites that provide MIBs for download. One example being [oidview][1]

Next you need to copy the MIB to the server running Zenoss.  
If you are experienced with Linux that shouldn&#8217;t be a problem 🙂  
If not, you can use software like WinSCP to transfer the file.

The last step is to import the MIB into Zenoss.  
To do this you first need to log in on the server running Zenoss, preferably as zenoss (default password is zenoss).  
Then run the following command:

 ```
 /usr/local/zenoss/zenoss/bin/zenmib run <path to MIB file> 
 ```

Note: This example is for a default Debian installation, if you are using other distros you need to adapt the path. For the virtual appliance the command would be:

 ```
 /opt/zenoss/bin/zenmib run <path to MIB file> 
 ```

 [1]: http://www.oidview.com/mibs/detail.html