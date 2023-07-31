---
title: Using remote desktop over an ssh tunnel
author: nerenther
 
date: 2011-08-24T12:55:32+00:00
url: /index.php/2011/08/24/using-remote-desktop-over-an-ssh-tunnel/
categories:
  - Linux
  - PuTTY
tags:
  - PuTTY
  - remote desktop
  - ssh tunnel

---
This is kinda the nerdy way of remoting a pc on a remote network. Usually a vpn connection would be preffered, but in my case I don&#8217;t want to forward the rdp port of security reasons.

Lets use my setup as an example:  
At home I have a server running Debian linux, I also have several windows pc&#8217;s  that I want to be able to use remote desktop to. Since I have already forwarded the ssh port (22) to my Debian server I figured I could use it as a jumpstation.

The way I solved this is somewhat similar to the [PuTTY proxy trick][1] guide that I posted earlier.

Fire up PuTTY, enter the hostname or ip-adress of your remote network. Then navigate to Connection&#8211;>SSH&#8211;>Tunnels

In the Source port field, type 127.0.0.3:3390 and in the Destination field type the internal ip of the pc you want to remote followed by :3389, e.g. 10.0.0.3:3389

Connect and log on. Then fire up remote desktop.

In the remote desktop window you now need to type 127.0.0.3:3390 and connect.

All done!

Note: You don&#8217;t have to have a linux server running at home to do this, any device running an ssh server will do. For example if you only have windows devices, you can use [MobaSSH][2]

 [1]: http://cloud.kemta.net/?p=24
 [2]: http://mobassh.mobatek.net/