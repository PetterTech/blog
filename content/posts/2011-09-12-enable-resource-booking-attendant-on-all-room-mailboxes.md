---
title: Enable Resource Booking Attendant on all Room Mailboxes
author: nerenther
 
date: 2011-09-12T12:28:56+00:00
url: /index.php/2011/09/12/enable-resource-booking-attendant-on-all-room-mailboxes/
categories:
  - Exchange
  - Microsoft
tags:
  - Exchange
  - microsoft
  - Powershell
  - Resource Booking Attendant
  - Room mailbox

---
The Resource Booking Attendant should be enabled on all your Room Mailboxes. If it is not, the room will not accept or decline incoming meeting requests. Which is somewhat the whole point right?

Heres a powershell command to enable it on all the Room Mailboxes in an exchange organization:

 ```
 Get-Mailbox -RecipientTypeDetails roommailbox | Set-CalendarProcessing -AutomateProcessing AutoAccept 
 ```