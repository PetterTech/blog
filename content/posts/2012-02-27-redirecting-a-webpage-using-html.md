---
title: Redirecting a webpage using html
date: 2012-02-27T07:55:57+00:00
url: /index.php/2012/02/27/redirecting-a-webpage-using-html/
categories:
  - Web code
tags:
  - html
  - iis
  - microsoft
---
The redirect function in IIS 7 and 7.5 is in my experience pretty buggy. More often than not it will send the visitor into an eternal redirect loop.

Because of that I have used this simple html code for redirecting, instead of using the built in function in IIS.

Use it at your own will, I'm just posting it so I know where to find it the next time I need it 🙂

```html


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