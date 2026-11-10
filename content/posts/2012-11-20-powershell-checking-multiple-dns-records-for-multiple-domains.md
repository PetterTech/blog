---
title: 'Powershell: Checking multiple dns records for multiple domains'
date: 2012-11-20T09:25:09+00:00
url: /index.php/2012/11/20/powershell-checking-multiple-dns-records-for-multiple-domains/
categories:
  - Microsoft
  - Powershell
tags:
  - dns
  - Powershell
  - Resolve-DnsName
---
I don't know how useful this will be for others, but in our case we had a need to check a few public dns records on some of our domains. Doing so by using a web portal will be time consuming and straight out boring. Luckily you can use Powershell for such things:

First we need to to save our domains in an array:

 ```powershell
$domains = @("domainA.com", "domainB.com", "domainC.com")
 ```

Then we send that array into a foreach loop:

 ```powershell
foreach ($element in $domains)
{
Resolve-DnsName -server 8.8.8.8 record.$($element)
} 
```

You might notice that I use Google's public dns servere here, but you can use whatever dns server you want, or just leave the -server part out.

The example above is pretty basic and only checks for an A record. In our case we needed to check several SRV records for each of the domains, so I had to extend the script a little. The cmdlet Resolve-DnsName is equivalent to the good ol' nslookup so it's quite powerful, given the right swithces.

Heres the script I ended up with for our case (10 points if you guess what the SRV records are for 🙂 ):

 ```powershell
$domains = @("domainA.com", "domainB.com", "domainC.com" )

foreach ($element in $domains) 
{
Resolve-DnsName -server 8.8.8.8 -type srv _h323cs._tcp.$($element)
Resolve-DnsName -server 8.8.8.8 -type srv _h323ls._udp.$($element)
Resolve-DnsName -server 8.8.8.8 -type srv _sip._tcp.$($element)
Resolve-DnsName -server 8.8.8.8 -type srv _sips._tcp.$($element)
} 
```