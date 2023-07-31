---
title: Receive connector allowing anonymous relay on exchange 2010/2007
author: nerenther
 
date: 2011-08-17T14:27:32+00:00
url: /index.php/2011/08/17/receive-connector-allowing-anonymous-relay-on-exchange-20102007/
categories:
  - Exchange
  - Microsoft
tags:
  - Anonymous relay
  - Exchange
  - microsoft
  - Powershell

---
Often it&#8217;s a good idea to have a receive connector allowing certain devices to send mail through you exchange server without having to authenticate.

One example from where I currently work is printers.  
We never set up the printers ourselves, that job is done by the provider. And do we want to give them a username and password allowing for mail relay through our servers? No, we don&#8217;t.

It&#8217;s a better practice to have them only input the name/ip-address of one exchange server with the cas role. Then all we have to do is add the ip-address of the printer to the list of allowed ip&#8217;s on our receive connector. Here&#8217;s a short guide on how to do it:

  * Open up the EMC on a exchange server with the cas role and navigate to Server Configuration&#8211;>Hub transport.
  * On the right side, click New Receive Connector&#8230;
  * Give the new receive connector a suitable name, for example Anonymous, and choose Custom as the intended use.
  * On the next page you are prompted to choose which local ip-addresses the receive connector should receive mail on and what fqdn the server should respond with. I usually leave the default settings here, but if your server has multiple ip-addresses connecting to different secured/unsecured networks it is a good idea to not accept mail on all ip-addresses.
  * Next you will choose what ip-addresses are allowed to send mail to the receive connector, the default is all ip-addresses (baad idea in our case). Here you would, in our example, remove the default setting and input the ip-address of our printer.
  * Click New on the next page and the connector is created, but we still have to do some configuring.
  * When back at EMC, hit properties on the newly created receive connector.
  * On the Permissions tab you can remove everything but Anonymous users and click OK.

Then you are good to go. If you want to allow more ip-addresses to relay, you can always enter more of them on the Properties&#8211;>Network for the receive connector.

And, as always, here&#8217;s the nerdy way of doing it in powershell:

<pre>New-ReceiveConnector -Name "Anonymous" -Usage Custom -PermissionGroups AnonymousUsers -Bindings 0.0.0.0:25 -RemoteIpRanges &lt;ip of printer&gt; -server &lt;name of your server&gt;</pre>