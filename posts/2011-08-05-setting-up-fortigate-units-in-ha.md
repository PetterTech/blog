---
title: Setting up Fortigate units in HA
author: nerenther
type: post
date: 2011-08-05T12:45:25+00:00
url: /index.php/2011/08/05/setting-up-fortigate-units-in-ha/
categories:
  - Fortinet
tags:
  - Fortigate
  - Fortinet
  - HA

---
Setting up an HA cluster on Fortigate devices is surprisingly easy, heres a short little guide:

Set up the first Fortigate the way you want it (or perhaps you already have one in you environment).  
Then click on configure, next to HA Status on the main page.  
Type in the name and password for the HA group you want to create.  
Choose which interfaces you want the heartbeat to be sent over (I recommend at least to interfaces, one of them being dedicated to heartbeat). Also choose what kind of cluster you want (active-active, active-passive).

Connect the new Fortigate (reset it to factory defaults if not already done).  
Repeat the previous steps for the new Fortigate, typen in the same group name and password.  
Connect the cables and in a few minutes the two Fortigate units will start to exchange configs. You can review the status from the main page.

Or, if you want to do it the nerdy way, heres the cli commands:

config system ha  
set group-name &#8220;FGT-HAtest&#8221;  
set mode a-p  
set password ENC 4hkgXeIrLmd2L2XOIZZy+c8jaA8W1BNz66t3ajo5lCT3xLhU3llmt26SbnPLPCSsJoPEsoHZKwHd56SYDDUN9XYQzivP9HdZP3T3mMuzS+I7EyJh  
set hbdev &#8220;dmz&#8221; 50 &#8220;internal&#8221; 0  
set override disable  
end