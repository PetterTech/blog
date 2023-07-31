---
title: Locate a computer/server/printer in a cisco environment
author: nerenther
type: post
date: 2011-07-29T11:17:20+00:00
url: /index.php/2011/07/29/locate-a-computerserverprinter-in-a-cisco-environment/
categories:
  - Cisco
  - Network
tags:
  - cisco
  - network

---
At work I was recently assigned some more network related task.  
One of the task I fine myself repeating over and over is locating a computer on the network. The only info you need is the ip-address of the computer.

<p style="text-align: left;">
  This is how I do it:<br /> 1. Telnet core switch<br /> 2. show ip arp | include <ip-address><br /> <em>This gives me the mac address of the computer</em><br /> 3. show mac address-table address <mac address><br /> <em>This shows what port the computer is behind</em><br /> 4. show cdp neighbors <port on core><br /> <em>This shows the name of the switch that is connected on that port</em><br /> 5. Telnet to that switch<br /> 6. Repeat step 3-5 until step 4 returns no switches, that means the computer is directly connected to that port!
</p>