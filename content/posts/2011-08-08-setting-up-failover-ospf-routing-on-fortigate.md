---
title: Setting up failover ospf routing on Fortigate
author: nerenther
 
date: 2011-08-08T08:43:02+00:00
url: /index.php/2011/08/08/setting-up-failover-ospf-routing-on-fortigate/
categories:
  - Fortinet
tags:
  - failover
  - Fortigate
  - Fortinet
  - ospf

---
I&#8217;ve put together a small guide for setting up two Fortigates with failover ospf routing. This example is based on a small lab, but you can easily adapt it to your own environment.

This is the scenario:  
<a href="http://cloud.kemta.net/?attachment_id=70" rel="attachment wp-att-70"><img decoding="async" loading="lazy" class="aligncenter size-full wp-image-70" title="fgt_ospf" src="http://cloud.kemta.net/wp-uploads/fgt_ospf1.png" alt="" width="873" height="332" /></a>  
In this scenario we want the 100Mb line to be prioritized.

Start of with setting up the two Fortigates with ip-adresses as shown. Also make sure to create firewall rules for traffic from internal to wan1 and wan2 and back (make sure not to enabel NAT).

Then you have to enter the following config to enable ospf:  
On FGT1:  
config router ospf  
config area  
edit 0.0.0.0  
next  
end  
config network  
edit 1  
set prefix 0.0.0.0 0.0.0.0  
next  
end  
config ospf-interface  
edit &#8220;wan1&#8221;  
set cost 2  
set interface &#8220;wan1&#8221;  
next  
edit &#8220;wan2&#8221;  
set interface &#8220;wan2&#8221;  
next  
end  
config redistribute &#8220;connected&#8221;  
end  
config redistribute &#8220;static&#8221;  
end  
config redistribute &#8220;rip&#8221;  
end  
config redistribute &#8220;bgp&#8221;  
end  
set router-id 0.0.0.2  
end

On FGT2:  
config router ospf  
config area  
edit 0.0.0.0  
next  
end  
set default-information-originate enable  
config network  
edit 1  
set prefix 0.0.0.0 0.0.0.0  
next  
end  
config ospf-interface  
edit &#8220;wan1&#8221;  
set cost 2  
set interface &#8220;wan1&#8221;  
next  
edit &#8220;wan2&#8221;  
set interface &#8220;wan2&#8221;  
next  
end  
config redistribute &#8220;connected&#8221;  
end  
config redistribute &#8220;static&#8221;  
end  
config redistribute &#8220;rip&#8221;  
end  
config redistribute &#8220;bgp&#8221;  
end  
set router-id 0.0.0.1  
end

That should do it. To check that it is working, you can run the following command on FGT2:  
info routing-table all

Then you will get an output similar to this:  
Codes: K &#8211; kernel, C &#8211; connected, S &#8211; static, R &#8211; RIP, B &#8211; BGP  
O &#8211; OSPF, IA &#8211; OSPF inter area  
N1 &#8211; OSPF NSSA external type 1, N2 &#8211; OSPF NSSA external type 2  
E1 &#8211; OSPF external type 1, E2 &#8211; OSPF external type 2  
i &#8211; IS-IS, L1 &#8211; IS-IS level-1, L2 &#8211; IS-IS level-2, ia &#8211; IS-IS inter area  
* &#8211; candidate default

C 10.0.1.0/30 is directly connected, wan1  
C 10.0.1.4/30 is directly connected, wan2  
O 10.10.5.0/24 [110/102] via 10.0.1.1, wan1, 00:48:44  
C 10.10.16.0/24 is directly connected, internal

From this we can see that the route to 10.10.5.0/24 is acquired via ospf.

You can find some more reading material here:  
<http://kb.fortinet.com/kb/microsites/microsite.do?cmd=displayKC&externalId=FD30030>  
<http://docs.fortinet.com/fgt/handbook/fortigate-dynamic-routing-40-mr1.pdf>