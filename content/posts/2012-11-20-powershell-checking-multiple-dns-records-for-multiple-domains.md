---
title: 'Powershell: Checking multiple dns records for multiple domains'
author: nerenther
 
date: 2012-11-20T09:25:09+00:00
url: /index.php/2012/11/20/powershell-checking-multiple-dns-records-for-multiple-domains/
wp-syntax-cache-content:
  - |
    a:3:{i:1;s:750:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$domains</span> <span style="color: pink;">=</span> <span style="color: pink;">@</span><span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;domainA.com&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;domainB.com&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;domainC.com&quot;</span><span style="color: #000000;">&#41;</span> ```</td></tr></table><p class="theCode" style="display:none;">$domains = @(&quot;domainA.com&quot;, &quot;domainB.com&quot;, &quot;domainC.com&quot;)</p></div>
    ";i:2;s:881:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #0000FF;">foreach</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span> <span style="color: #0000FF;">in</span> <span style="color: #800080;">$domains</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
    Resolve<span style="color: pink;">-</span>DnsName <span style="color: pink;">-</span>server 8.8.8.8 record.$<span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#125;</span> ```</td></tr></table><p class="theCode" style="display:none;">foreach ($element in $domains)
    {
    Resolve-DnsName -server 8.8.8.8 record.$($element)
    }</p></div>
    ";i:3;s:2782:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$domains</span> <span style="color: pink;">=</span> <span style="color: pink;">@</span><span style="color: #000000;">&#40;</span><span style="color: #800000;">&quot;domainA.com&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;domainB.com&quot;</span><span style="color: pink;">,</span> <span style="color: #800000;">&quot;domainC.com&quot;</span> <span style="color: #000000;">&#41;</span>
    &nbsp;
    <span style="color: #0000FF;">foreach</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span> <span style="color: #0000FF;">in</span> <span style="color: #800080;">$domains</span><span style="color: #000000;">&#41;</span> 
    <span style="color: #000000;">&#123;</span>
    Resolve<span style="color: pink;">-</span>DnsName <span style="color: pink;">-</span>server 8.8.8.8 <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> srv _h323cs._tcp.$<span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span><span style="color: #000000;">&#41;</span>
    Resolve<span style="color: pink;">-</span>DnsName <span style="color: pink;">-</span>server 8.8.8.8 <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> srv _h323ls._udp.$<span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span><span style="color: #000000;">&#41;</span>
    Resolve<span style="color: pink;">-</span>DnsName <span style="color: pink;">-</span>server 8.8.8.8 <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> srv _sip._tcp.$<span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span><span style="color: #000000;">&#41;</span>
    Resolve<span style="color: pink;">-</span>DnsName <span style="color: pink;">-</span>server 8.8.8.8 <span style="color: pink;">-</span><span style="color: #008080; font-weight: bold;">type</span> srv _sips._tcp.$<span style="color: #000000;">&#40;</span><span style="color: #800080;">$element</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#125;</span> ```</td></tr></table><p class="theCode" style="display:none;">$domains = @(&quot;domainA.com&quot;, &quot;domainB.com&quot;, &quot;domainC.com&quot; )
    
    foreach ($element in $domains) 
    {
    Resolve-DnsName -server 8.8.8.8 -type srv _h323cs._tcp.$($element)
    Resolve-DnsName -server 8.8.8.8 -type srv _h323ls._udp.$($element)
    Resolve-DnsName -server 8.8.8.8 -type srv _sip._tcp.$($element)
    Resolve-DnsName -server 8.8.8.8 -type srv _sips._tcp.$($element)
    }</p></div>
    ";}
categories:
  - Microsoft
  - Powershell
tags:
  - dns
  - Powershell
  - Resolve-DnsName

---
I don&#8217;t know how useful this will be for others, but in our case we had a need to check a few public dns records on some of our domains. Doing so by using a web portal will be time consuming and straight out boring. Luckily you can use Powershell for such things:

First we need to to save our domains in an array:

 ```
$domains = @("domainA.com", "domainB.com", "domainC.com")
 ```

Then we send that array into a foreach loop:

 ```
foreach ($element in $domains)
{
Resolve-DnsName -server 8.8.8.8 record.$($element)
} 
```

You might notice that I use Google&#8217;s public dns servere here, but you can use whatever dns server you want, or just leave the -server part out.

The example above is pretty basic and only checks for an A record. In our case we needed to check several SRV records for each of the domains, so I had to extend the script a little. The cmdlet Resolve-DnsName is equivalent to the good ol&#8217; nslookup so it&#8217;s quite powerful, given the right swithces.

Heres the script I ended up with for our case (10 points if you guess what the SRV records are for 🙂 ):

 ```
$domains = @("domainA.com", "domainB.com", "domainC.com" )

foreach ($element in $domains) 
{
Resolve-DnsName -server 8.8.8.8 -type srv _h323cs._tcp.$($element)
Resolve-DnsName -server 8.8.8.8 -type srv _h323ls._udp.$($element)
Resolve-DnsName -server 8.8.8.8 -type srv _sip._tcp.$($element)
Resolve-DnsName -server 8.8.8.8 -type srv _sips._tcp.$($element)
} 
```