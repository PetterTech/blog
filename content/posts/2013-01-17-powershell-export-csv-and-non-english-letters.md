---
title: 'Powershell: Export-Csv and non-English letters'
author: nerenther
 
date: 2013-01-17T12:06:53+00:00
url: /index.php/2013/01/17/powershell-export-csv-and-non-english-letters/
categories:
  - Microsoft
  - Powershell
tags:
  - Encoding
  - Export-Csv
  - Powershell
  - Unicode

---
The Export-Csv cmdlet is a really nice tool if you want to gather info from e.g. Active Directory that you later want to import to Excel. But as you might have noticed it doesn&#8217;t play well with non-English letters.

Working in Norway with users from all the Nordic countries means that we have a lot of users i Active Directory who have non-English letters in their names (æ ø å ö ä and so on). Unless you specify which encoding Export-Csv should use they will show in the csv as ?.

The magical switch to Export-Csv is -encoding. E.g. for us we would use unicode as encoding as this will export the Nordic letters:

 ```
Export-Csv &lt;filename&gt; -Encoding unicode 
```

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;