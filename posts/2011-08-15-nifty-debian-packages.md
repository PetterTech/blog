---
title: Nifty Debian packages
author: nerenther
type: post
date: 2011-08-15T13:24:08+00:00
url: /index.php/2011/08/15/nifty-debian-packages/
categories:
  - Linux
tags:
  - Debian
  - Linux
  - Packages

---
A little list of some nifty packages for Debian:

**sudo**  
Oddly enough this isn&#8217;t installed by default. Well known for most Linux users, but it enables regular users to perform commands as root without actually logging in as root.

**molly-guard  
** Protects you from shutting down wrong server when using ssh to a server. What it does is ask you which server you want to shutdown when you run the command shutdown. If you type in wrong hostname it won&#8217;t run the command. Handy if you have a bunch of ssh sessions open and you type shutdown in the wrong session.

**pwgen  
** Generates random passwords. Configurable what kind of passwords you want, for example high complexity and so on.

**hdparm  
** Can be used to check the performance of harddrives

**dovecot  
** Widely used imap/pop server

**postfix  
** Widely used smtp server. Often used in conjunction with dovecot

**roundcube  
** A package for webmail. Requires of course a webserver, for example apache

**zenoss-stack  
** A genius monitoring software, can monitor just about anything using smtp, ping, telnet and so on. For more information, check <a href="http://zenoss.org" target="_blank" rel="noopener">zenoss.org</a>

**vnstat  
** A network traffic monitor. It gathers statistics provided by the kernel and can present them to user either by text output or graphs.

**vlock  
** Can lock on or more sessions on the console allowing others to use the console.

**ccze  
** Log colorizer. Useful when investigating large logs

**cron-apt  
** Rather flexible package for automating e.g. download of package updates. Can be configured to check updates every night and send an email containing the list of updates for example

**screen  
** Can be used to open up multiple terminal windows, which can be detached and resumed later

**fail2ban  
** Examines a range of logs and if and IP makes too many bad logins, fail2ban creates firewall rules to reject traffic from that IP

**webmin  
** A web based administrative tool. Can be used to administer apache, file sharing, dns and so on

**samba  
** File and print services for any client using smb/cifs, e.g. windows

**open-vm-tools  
** Opensource vmware tools. Follow the guide on this site: <a href="http://www.surlyjake.com/2011/02/install-open-vm-tools-on-debian-6-squeeze/" target="_blank" rel="noopener">http://www.surlyjake.com/2011/02/install-open-vm-tools-on-debian-6-squeeze/</a>**  
** 

I will update this post with more as I remember them 😛