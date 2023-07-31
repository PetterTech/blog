---
title: Redirecting a webpage using html
author: nerenther
 
date: 2012-02-27T07:55:57+00:00
url: /index.php/2012/02/27/redirecting-a-webpage-using-html/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:2982:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="xml" style="font-family:monospace;"><span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><html<span style="color: #000000; font-weight: bold;">></span></span></span>
    <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><head<span style="color: #000000; font-weight: bold;">></span></span></span>
     <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><title<span style="color: #000000; font-weight: bold;">></span></span></span>Some title<span style="color: #009900;"><span style="color: #000000; font-weight: bold;"></title<span style="color: #000000; font-weight: bold;">></span></span></span>
     <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><META</span> <span style="color: #000066;">HTTP-EQUIV</span>=<span style="color: #ff0000;">&quot;Refresh&quot;</span></span>
    <span style="color: #009900;"> <span style="color: #000066;">CONTENT</span>=<span style="color: #ff0000;">&quot;1; URL=https://some.domain.com/&quot;</span><span style="color: #000000; font-weight: bold;">></span></span>
     <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><head<span style="color: #000000; font-weight: bold;">></span></span></span>
     <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><body<span style="color: #000000; font-weight: bold;">></span></span></span>
     You are now beeing forwarded to <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><a</span> <span style="color: #000066;">href</span>=<span style="color: #ff0000;">&quot;https://some.domain&quot;</span><span style="color: #000000; font-weight: bold;">></span></span>https://some.domain><span style="color: #009900;"><span style="color: #000000; font-weight: bold;"></a<span style="color: #000000; font-weight: bold;">></span></span><span style="color: #000000; font-weight: bold;"><br<span style="color: #000000; font-weight: bold;">></span></span></span>
     If you are not forwarded automatically, click the above link.
    <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"></body<span style="color: #000000; font-weight: bold;">></span></span><span style="color: #000000; font-weight: bold;"></html<span style="color: #000000; font-weight: bold;">></span></span></span> ```</td></tr></table><p class="theCode" style="display:none;"><html>
    <head>
     <title>Some title</title>
     <META HTTP-EQUIV=&quot;Refresh&quot;
     CONTENT=&quot;1; URL=https://some.domain.com/&quot;>
     <head>
     <body>
     You are now beeing forwarded to <a href=&quot;https://some.domain&quot;>https://some.domain></a><br>
     If you are not forwarded automatically, click the above link.
    </body></html></p></div>
    ";}
categories:
  - Web code
tags:
  - html
  - iis
  - microsoft

---
The redirect function in IIS 7 and 7.5 is in my experience pretty buggy. More often than not it will send the visitor into an eternal redirect loop.

Because of that I have used this simple html code for redirecting, instead of using the built in function in IIS.

Use it at your own will, I&#8217;m just posting it so I know where to find it the next time I need it 🙂

```


<head>
  <title>
    Some title
  </title>
   
  
  <meta HTTP-EQUIV="Refresh"
 CONTENT="1; URL=https://some.domain.com/" />
  
  <head>
    
     You are now beeing forwarded to <a href="https://some.domain">https://some.domain></a><br />
     If you are not forwarded automatically, click the above link.
    </html> 
```