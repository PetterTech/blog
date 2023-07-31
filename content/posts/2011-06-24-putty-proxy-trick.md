---
title: PuTTY proxy trick
author: nerenther
 
date: 2011-06-24T08:35:16+00:00
url: /index.php/2011/06/24/putty-proxy-trick/
categories:
  - PuTTY
tags:
  - proxy
  - PuTTY

---
Did you know you use an SSH connection as a proxy using PuTTY? I didn&#8217;t until today 🙂

Fire up PuTTY but before you connect navigate to Connection&#8211;>SSH&#8211;>Tunnels.  
Here you can specify a port you want PuTTY to respond to proxy requests. Choose a port that is not in use on your localhost, I will use 8080 in this example. Choose Dynamic on Destination and click Add.

In the forwarded ports part of the windows you will now see D8080.  
Connect to your host and open up your browser of choice.

Specify the following in SOCKS proxy: 127.0.0.1:8080

Now you will tunnel your traffic through the SSH host you connected to.  
This trick works for all applications that support SOCKS proxy, not just browsers.