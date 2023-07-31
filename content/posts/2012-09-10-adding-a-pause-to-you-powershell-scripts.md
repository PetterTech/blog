---
title: Adding a pause to you Powershell scripts
author: nerenther
 
date: 2012-09-10T13:57:52+00:00
url: /index.php/2012/09/10/adding-a-pause-to-you-powershell-scripts/
categories:
  - Microsoft
  - Powershell
tags:
  - pause
  - Powershell

---
If you have taken a look at some of the scripts I have posted earlier you might have noticed a rather strange line, usually at the end of the script:

```
cmd /c pause | out-null
```

This was actually just to get the script to wait for the user to press a key. It is equivalent to the good ol' pause in batch scripting.  
The reason I used this method was that I just didn't know how to do this in Powershell (yes, I am ashamed). But now I have stumbled upon the Powershell way to do it:

```
$null = $host.ui.rawui.readkey("NoEcho,Includekeydown") 
```

This will do exactly the same as pause in batch scripting 🙂