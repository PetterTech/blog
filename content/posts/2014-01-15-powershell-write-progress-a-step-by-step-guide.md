---
title: 'Powershell: Write-Progress, a step-by-step guide'
date: 2014-01-15T12:55:36+00:00
url: /index.php/2014/01/15/powershell-write-progress-a-step-by-step-guide/
categories:
  - Microsoft
  - Powershell
tags:
  - guide
  - Powershell
  - write-progress
---
For whatever reason, I had a really difficult time wrapping my head around the usage of Write-Progress. The basic usage is off-course quite easy:

 ```powershell
Write-Progress -Activity "Something" -Status "Something else" -CurrentOperation "thinking" -PercentComplete 30 
```

This will show a quick progress bar stating that &#8220;Something&#8221; is going on, the status is &#8220;Something else&#8221; and it has gotten to 30%. However, when I wanted to use Write-Progress in a large script I quickly got confused when I looked at some of the examples out there. I mean, look at this for example:

 ```powershell
$wmiQuery = "Select name from win32_service where state = 'running'"
$colItems = Get-WmiObject -Query $wmiQuery
For($i = 1; $i -le $colItems.count; $i++)
{ Write-Progress -Activity "Gathering Services" -status "Found Service $i" `
-percentComplete ($i / $colItems.count*100)}
$colItems | Select name 
```

I'm sure that if I had a stronger background in programming and/or scripting I could have figured it out quite easily (for what it's worth: I understand the code now 😉 ). But since I haven't really been scripting before Powershell came along I just sat there scratching my head.

So let's write a simpler guide!

Let's start by explaining a briefly how Write-Progress works:  
If you type the command in your Powershell console it will display the progress bar, but it will disappear again in a split second.  
If you put your Write-Progress snippet in a script, the progress bar will be displayed until another Write-Progress snippet comes along, or until the script finishes.

The basic usage of Write-Progress is, as I wrote further up, something like this:

 ```powershell
Write-Progress -Activity "Something" -Status "Something else" -CurrentOperation "thinking" -PercentComplete 30 
```

That will create an output looking something like this:

{{< unavailable "Screenshot no longer available" >}}

It's also quite easy to create a child progress bar by using the Id and ParentId parameters:

 ```powershell
Write-Progress -Activity Something -Status "Something else" -CurrentOperation Thinking -PercentComplete 30 -Id 1
 Write-Progress -Activity "Another thing" -Status "Something different" -CurrentOperation Sleeping -PercentComplete 30 -Id 2 -ParentId 1 
 ```

This will create an output looking something like this:

{{< unavailable "Image no longer available" >}}

Cool ey?

Now, this is all fine and dandy as a starting point, and you CAN use write-progress this way in your scripts, but thats not exactly a dynamic way of doing it.  
Often in your script you will have one or more foreach loops. Those are a great place to put your write-progress snippet and have PercentComplete and perhaps even Status or CurrentOperation filled out automagically.

First off we will need some data to parse through, I like to use Get-Process for that:

 ```powershell
$data = Get-Process 
```

Then we create a variable for our progress and set it to 1:

 ```powershell
$progress = 1 
```

This way PercentComplete will start at 1, you'll see why in a bit.

Now we can create our foreach loop (I assume you know how they work):

 ```powershell
$data | foreach {
 Write-Progress -Activity Sleeping -Status $_.ProcessName -CurrentOperation $_.Id -PercentComplete ($progress/$data.count*100) -Id 1
 Start-Sleep -Milliseconds 50
 $progress++
 } 
```

This Write-Progress line will show Activity as &#8220;Sleeping&#8221;, the status will be the name of the process and currentoperation will be the ID of the process. Percentagecomplete will the correct progress (since $progress++ will increment $progress by 1 for each time the loop runs).  
Start-Sleep is only there to delay the operation, so you can actually see whats going on.

So the final result will be:

 ```powershell
$progress = 1
$data = Get-Process
$data | foreach {
 Write-Progress -Activity Sleeping -Status $_.ProcessName -CurrentOperation $_.Id -PercentComplete ($progress/$data.count*100) -Id 1
 Start-Sleep -Milliseconds 50
 $progress++
 } 
```

And it will look something like this:

{{< unavailable "Image no longer available" >}}

Comments?