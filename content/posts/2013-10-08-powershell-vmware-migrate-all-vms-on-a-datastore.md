---
title: "PowerCLI: Migrate all vm's on a datastore"
author: nerenther
 
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

This simple one-liner migrates all vm's off one datastore to a new one:

 ```
Get-VM -Datastore <datastore1> | Move-VM -Datastore <datastore2>
 ```

You can also move vm's off one datastore and place them in any datastore within a specified datastore cluster:

 ```
$DatastoreCluster1 = Get-DatastoreCluster -Name 'DatastoreCluster1'
Get-VM -Datastore <datastore1> | Move-VM -Datastore $DatastoreCluster1 
```