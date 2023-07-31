---
title: 'Powershell: Write-Progress, a step-by-step guide'
author: nerenther
type: post
date: 2014-01-15T12:55:36+00:00
url: /index.php/2014/01/15/powershell-write-progress-a-step-by-step-guide/
wp-syntax-cache-content:
  - |
    a:8:{i:1;s:922:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> <span style="color: #800000;">&quot;Something&quot;</span> <span style="color: #008080; font-style: italic;">-Status</span> <span style="color: #800000;">&quot;Something else&quot;</span> <span style="color: #008080; font-style: italic;">-CurrentOperation</span> <span style="color: #800000;">&quot;thinking&quot;</span> <span style="color: #008080; font-style: italic;">-PercentComplete</span> <span style="color: #804000;">30</span></pre></td></tr></table><p class="theCode" style="display:none;">Write-Progress -Activity &quot;Something&quot; -Status &quot;Something else&quot; -CurrentOperation &quot;thinking&quot; -PercentComplete 30</p></div>
    ";i:2;s:2379:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$wmiQuery</span> <span style="color: pink;">=</span> <span style="color: #800000;">&quot;Select name from win32_service where state = 'running'&quot;</span>
    <span style="color: #800080;">$colItems</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Get-WmiObject</span> <span style="color: #008080; font-style: italic;">-Query</span> <span style="color: #800080;">$wmiQuery</span>
    <span style="color: #0000FF;">For</span><span style="color: #000000;">&#40;</span><span style="color: #800080;">$i</span> <span style="color: pink;">=</span> <span style="color: #804000;">1</span>; <span style="color: #800080;">$i</span> <span style="color: #FF0000;">-le</span> <span style="color: #800080;">$colItems</span>.count; <span style="color: #800080;">$i</span><span style="color: pink;">++</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span> <span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> <span style="color: #800000;">&quot;Gathering Services&quot;</span> <span style="color: #008080; font-style: italic;">-status</span> <span style="color: #800000;">&quot;Found Service $i&quot;</span> `
    <span style="color: #008080; font-style: italic;">-percentComplete</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$i</span> <span style="color: pink;">/</span> <span style="color: #800080;">$colItems</span>.count<span style="color: pink;">*</span><span style="color: #804000;">100</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#125;</span>
    <span style="color: #800080;">$colItems</span> <span style="color: pink;">|</span> <span style="color: #008080; font-weight: bold;">Select</span> name</pre></td></tr></table><p class="theCode" style="display:none;">$wmiQuery = &quot;Select name from win32_service where state = 'running'&quot;
    $colItems = Get-WmiObject -Query $wmiQuery
    For($i = 1; $i -le $colItems.count; $i++)
    { Write-Progress -Activity &quot;Gathering Services&quot; -status &quot;Found Service $i&quot; `
    -percentComplete ($i / $colItems.count*100)}
    $colItems | Select name</p></div>
    ";i:3;s:922:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> <span style="color: #800000;">&quot;Something&quot;</span> <span style="color: #008080; font-style: italic;">-Status</span> <span style="color: #800000;">&quot;Something else&quot;</span> <span style="color: #008080; font-style: italic;">-CurrentOperation</span> <span style="color: #800000;">&quot;thinking&quot;</span> <span style="color: #008080; font-style: italic;">-PercentComplete</span> <span style="color: #804000;">30</span></pre></td></tr></table><p class="theCode" style="display:none;">Write-Progress -Activity &quot;Something&quot; -Status &quot;Something else&quot; -CurrentOperation &quot;thinking&quot; -PercentComplete 30</p></div>
    ";i:4;s:1803:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> Something <span style="color: #008080; font-style: italic;">-Status</span> <span style="color: #800000;">&quot;Something else&quot;</span> <span style="color: #008080; font-style: italic;">-CurrentOperation</span> Thinking <span style="color: #008080; font-style: italic;">-PercentComplete</span> <span style="color: #804000;">30</span> <span style="color: #008080; font-style: italic;">-Id</span> <span style="color: #804000;">1</span>
     <span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> <span style="color: #800000;">&quot;Another thing&quot;</span> <span style="color: #008080; font-style: italic;">-Status</span> <span style="color: #800000;">&quot;Something different&quot;</span> <span style="color: #008080; font-style: italic;">-CurrentOperation</span> Sleeping <span style="color: #008080; font-style: italic;">-PercentComplete</span> <span style="color: #804000;">30</span> <span style="color: #008080; font-style: italic;">-Id</span> <span style="color: #804000;">2</span> <span style="color: #008080; font-style: italic;">-ParentId</span> <span style="color: #804000;">1</span></pre></td></tr></table><p class="theCode" style="display:none;">Write-Progress -Activity Something -Status &quot;Something else&quot; -CurrentOperation Thinking -PercentComplete 30 -Id 1
     Write-Progress -Activity &quot;Another thing&quot; -Status &quot;Something different&quot; -CurrentOperation Sleeping -PercentComplete 30 -Id 2 -ParentId 1</p></div>
    ";i:5;s:375:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$data</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Get-Process</span></pre></td></tr></table><p class="theCode" style="display:none;">$data = Get-Process</p></div>
    ";i:6;s:344:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$progress</span> <span style="color: pink;">=</span> <span style="color: #804000;">1</span></pre></td></tr></table><p class="theCode" style="display:none;">$progress = 1</p></div>
    ";i:7;s:1728:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$data</span> <span style="color: pink;">|</span> <span style="color: #0000FF;">foreach</span> <span style="color: #000000;">&#123;</span>
     <span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> Sleeping <span style="color: #008080; font-style: italic;">-Status</span> <span style="color: #000080;">$_</span>.ProcessName <span style="color: #008080; font-style: italic;">-CurrentOperation</span> <span style="color: #000080;">$_</span>.Id <span style="color: #008080; font-style: italic;">-PercentComplete</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$progress</span><span style="color: pink;">/</span><span style="color: #800080;">$data</span>.count<span style="color: pink;">*</span><span style="color: #804000;">100</span><span style="color: #000000;">&#41;</span> <span style="color: #008080; font-style: italic;">-Id</span> <span style="color: #804000;">1</span>
     <span style="color: #008080; font-weight: bold;">Start-Sleep</span> <span style="color: #008080; font-style: italic;">-Milliseconds</span> <span style="color: #804000;">50</span>
     <span style="color: #800080;">$progress</span><span style="color: pink;">++</span>
     <span style="color: #000000;">&#125;</span></pre></td></tr></table><p class="theCode" style="display:none;">$data | foreach {
     Write-Progress -Activity Sleeping -Status $_.ProcessName -CurrentOperation $_.Id -PercentComplete ($progress/$data.count*100) -Id 1
     Start-Sleep -Milliseconds 50
     $progress++
     }</p></div>
    ";i:8;s:2031:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="powershell" style="font-family:monospace;"><span style="color: #800080;">$progress</span> <span style="color: pink;">=</span> <span style="color: #804000;">1</span>
    <span style="color: #800080;">$data</span> <span style="color: pink;">=</span> <span style="color: #008080; font-weight: bold;">Get-Process</span>
    <span style="color: #800080;">$data</span> <span style="color: pink;">|</span> <span style="color: #0000FF;">foreach</span> <span style="color: #000000;">&#123;</span>
     <span style="color: #008080; font-weight: bold;">Write-Progress</span> <span style="color: #008080; font-style: italic;">-Activity</span> Sleeping <span style="color: #008080; font-style: italic;">-Status</span> <span style="color: #000080;">$_</span>.ProcessName <span style="color: #008080; font-style: italic;">-CurrentOperation</span> <span style="color: #000080;">$_</span>.Id <span style="color: #008080; font-style: italic;">-PercentComplete</span> <span style="color: #000000;">&#40;</span><span style="color: #800080;">$progress</span><span style="color: pink;">/</span><span style="color: #800080;">$data</span>.count<span style="color: pink;">*</span><span style="color: #804000;">100</span><span style="color: #000000;">&#41;</span> <span style="color: #008080; font-style: italic;">-Id</span> <span style="color: #804000;">1</span>
     <span style="color: #008080; font-weight: bold;">Start-Sleep</span> <span style="color: #008080; font-style: italic;">-Milliseconds</span> <span style="color: #804000;">50</span>
     <span style="color: #800080;">$progress</span><span style="color: pink;">++</span>
     <span style="color: #000000;">&#125;</span></pre></td></tr></table><p class="theCode" style="display:none;">$progress = 1
    $data = Get-Process
    $data | foreach {
     Write-Progress -Activity Sleeping -Status $_.ProcessName -CurrentOperation $_.Id -PercentComplete ($progress/$data.count*100) -Id 1
     Start-Sleep -Milliseconds 50
     $progress++
     }</p></div>
    ";}
categories:
  - Microsoft
  - Powershell
tags:
  - guide
  - Powershell
  - write-progress

---
For whatever reason, I had a really difficult time wrapping my head around the usage of Write-Progress. The basic usage is off-course quite easy:

<pre lang="Powershell">Write-Progress -Activity "Something" -Status "Something else" -CurrentOperation "thinking" -PercentComplete 30</pre>

This will show a quick progress bar stating that &#8220;Something&#8221; is going on, the status is &#8220;Something else&#8221; and it has gotten to 30%. However, when I wanted to use Write-Progress in a large script I quickly got confused when I looked at some of the examples out there. I mean, look at this for example:

<pre lang="Powershell">$wmiQuery = "Select name from win32_service where state = 'running'"
$colItems = Get-WmiObject -Query $wmiQuery
For($i = 1; $i -le $colItems.count; $i++)
{ Write-Progress -Activity "Gathering Services" -status "Found Service $i" `
-percentComplete ($i / $colItems.count*100)}
$colItems | Select name</pre>

I&#8217;m sure that if I had a stronger background in programming and/or scripting I could have figured it out quite easily (for what it&#8217;s worth: I understand the code now 😉 ). But since I haven&#8217;t really been scripting before Powershell came along I just sat there scratching my head.

So let&#8217;s write a simpler guide!

Let&#8217;s start by explaining a briefly how Write-Progress works:  
If you type the command in your Powershell console it will display the progress bar, but it will disappear again in a split second.  
If you put your Write-Progress snippet in a script, the progress bar will be displayed until another Write-Progress snippet comes along, or until the script finishes.

The basic usage of Write-Progress is, as I wrote further up, something like this:

<pre lang="Powershell">Write-Progress -Activity "Something" -Status "Something else" -CurrentOperation "thinking" -PercentComplete 30</pre>

That will create an output looking something like this:

<p style="text-align: center;">
  <a href="https://dl.dropboxusercontent.com/u/33041052/bloggting/img/write-progress/1.PNG"><img decoding="async" loading="lazy" class="aligncenter" alt="" src="https://dl.dropboxusercontent.com/u/33041052/bloggting/img/write-progress/1.PNG" width="100%" height="130" /></a>
</p>

It&#8217;s also quite easy to create a child progress bar by using the Id and ParentId parameters:

<pre lang="Powershell">Write-Progress -Activity Something -Status "Something else" -CurrentOperation Thinking -PercentComplete 30 -Id 1
 Write-Progress -Activity "Another thing" -Status "Something different" -CurrentOperation Sleeping -PercentComplete 30 -Id 2 -ParentId 1</pre>

This will create an output looking something like this:

<p style="text-align: center;">
  <a href="https://dl.dropboxusercontent.com/u/33041052/bloggting/img/write-progress/2.PNG"><img decoding="async" loading="lazy" class="aligncenter" alt="" src="https://dl.dropboxusercontent.com/u/33041052/bloggting/img/write-progress/2.PNG" width="100%" height="239" /></a>
</p>

Cool ey?

Now, this is all fine and dandy as a starting point, and you CAN use write-progress this way in your scripts, but thats not exactly a dynamic way of doing it.  
Often in your script you will have one or more foreach loops. Those are a great place to put your write-progress snippet and have PercentComplete and perhaps even Status or CurrentOperation filled out automagically.

First off we will need some data to parse through, I like to use Get-Process for that:

<pre lang="Powershell">$data = Get-Process</pre>

Then we create a variable for our progress and set it to 1:

<pre lang="Powershell">$progress = 1</pre>

This way PercentComplete will start at 1, you&#8217;ll see why in a bit.

Now we can create our foreach loop (I assume you know how they work):

<pre lang="Powershell">$data | foreach {
 Write-Progress -Activity Sleeping -Status $_.ProcessName -CurrentOperation $_.Id -PercentComplete ($progress/$data.count*100) -Id 1
 Start-Sleep -Milliseconds 50
 $progress++
 }</pre>

This Write-Progress line will show Activity as &#8220;Sleeping&#8221;, the status will be the name of the process and currentoperation will be the ID of the process. Percentagecomplete will the correct progress (since $progress++ will increment $progress by 1 for each time the loop runs).  
Start-Sleep is only there to delay the operation, so you can actually see whats going on.

So the final result will be:

<pre lang="Powershell">$progress = 1
$data = Get-Process
$data | foreach {
 Write-Progress -Activity Sleeping -Status $_.ProcessName -CurrentOperation $_.Id -PercentComplete ($progress/$data.count*100) -Id 1
 Start-Sleep -Milliseconds 50
 $progress++
 }</pre>

And it will look something like this:

<p style="text-align: center;">
  <a href="https://dl.dropboxusercontent.com/u/33041052/bloggting/img/write-progress/3.PNG"><img decoding="async" loading="lazy" class="aligncenter" alt="" src="https://dl.dropboxusercontent.com/u/33041052/bloggting/img/write-progress/3.PNG" width="100%" height="172" /></a>
</p>

Comments?