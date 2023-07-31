---
title: "PowerCLI: Migrate all vm's on a datastore"
author: nerenther
type: post
date: 2013-10-08T11:24:34+00:00
url: /index.php/2013/10/08/powershell-vmware-migrate-all-vms-on-a-datastore/
categories:
  - PowerCLI
  - Powershell
  - VMware
tags:
  - datastore
  - get-vm
  - migrate
  - move-vm
  - vmware

---
PowerCLI is just awsome 🙂

This simple one-liner migrates all vm&#8217;s off one datastore to a new one:

<pre>Get-VM -Datastore &lt;datastore1&gt; | Move-VM -Datastore &lt;datastore2&gt;</pre>

You can also move vm&#8217;s off one datastore and place them in any datastore within a specified datastore cluster:

<pre>$DatastoreCluster1 = Get-DatastoreCluster -Name 'DatastoreCluster1'
Get-VM -Datastore &lt;datastore1&gt; | Move-VM -Datastore $DatastoreCluster1</pre>