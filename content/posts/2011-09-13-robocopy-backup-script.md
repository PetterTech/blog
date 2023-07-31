---
title: Robocopy backup script
author: nerenther
 
date: 2011-09-13T13:03:29+00:00
url: /index.php/2011/09/13/robocopy-backup-script/
categories:
  - Microsoft
  - Windows 7
tags:
  - backup
  - microsoft
  - Robocopy
  - Windows 7

---
This is a script I have used on several of my relatives computers for backing up their data. Windows backup won&#8217;t do for them because they feel the need to see the actual files on the external drive&#8230;

Anyway, heres my script:

<pre>robocopy c:users&lt;username&gt; &lt;destination&gt; /MIR /XD templates start-menu "local settings" appdata "internal video" cookies "my music" "my pictures" "my documents" printers programdata recent sendto andrmask /XF ntuser.dat ntuser.dat.log1 ntuser.dat.log2 /R:5 /LOG:&lt;log destination&gt;</pre>

I guess a little explanation is required.

  * The first part, robocopy c:users<username> <destination> tells robocopy what to copy where.
  * /MIR indicates that robocopy should mirror the source to the destination. This means that if you delete a file in the source, it is also deleted at destination. Use with caution as Microsoft would say
  * /XD tells robocopy what folders to skip. This is because robocopy won&#8217;t get access to those folders. They don&#8217;t contain useful data anyway.
  * /XF tells robocopy what files to skip. You won&#8217;t be able to copy i.e. ntuser.dat if you are logged in as that user. Also the files are not needed.
  * /R:5 means robocopy will not try more than 5 time to copy a file. The default is 1 million&#8230;
  * /LOG: specifies a log file for the operation. Useful if you ever need to troubleshoot