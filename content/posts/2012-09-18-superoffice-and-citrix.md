---
title: SuperOffice and Citrix
author: nerenther
 
date: 2012-09-18T08:13:48+00:00
url: /index.php/2012/09/18/superoffice-and-citrix/
categories:
  - SuperOffice
tags:
  - Citrix
  - different databases
  - inipath
  - SuperOffice

---
I&#8217;m just gonna start by putting this out there: I have never been a fan of SuperOffice, and I probably never will be either.

Now that thats out there, heres the situation: We have one citrix farm, and three different SuperOffice instances. The goal with our citrix farm is to have each citrix server completely the same as the others. Because of that, only one of the SuperOffice instance have been accessible from the citrix farm. Until yesterday&#8230;

When we first set up the citrix farm, we installed that one SuperOffice instance and didn&#8217;t put much effort into getting the other two instances accessible. What we did try was using the -inipath parameter for socrm.exe and soadmin.exe as stated here: <a href="http://cs.superoffice.com/scripts/customer.exe?_sf=0&custSessionKey=&customerLang=no&noCookies=true&action=viewKbEntry&id=2388" target="_blank" rel="noopener">http://cs.superoffice.com/scripts/customer.exe?_sf=0&custSessionKey=&customerLang=no&noCookies=true&action=viewKbEntry&id=2388</a>

That didn&#8217;t work at all so we didn&#8217;t bother trying anymore as the other two instances isn&#8217;t that much used anyway.

But yesterday I did another attempt and it turns out that the documentation from SuperOffice is flawed, it clearly states that the inipath parameter should be used like this:

socrm.exe -inipath=c:superoffice.ini

But when in fact the correct way would be like this:

socrm.exe -inipath=c:

As far as I can see, SuperOffice is coded to look for superoffice.ini in the folder specified by the inipath parameter. It also will not recognize i.e. c:superoffice as a folder, you would need to specify c:superoffice

Another thing that is important, and that I have found no documentation on, is that superoffice.config needs to be in the same folder as superoffice.ini.

&nbsp;

So to sum up: If you want to run a SuperOffice client and connect to different databases, you need to use the -inipath parameter. You should create a superoffice.ini and a superoffice.config file, store it somewhere (a network share works fine), and then start SuperOffice or SuperOffice Admin with the following switch: -inipath=\serversharefolder