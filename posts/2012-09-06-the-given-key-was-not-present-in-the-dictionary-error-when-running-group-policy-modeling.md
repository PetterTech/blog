---
title: "The given Key was not present in the dictionary" error when running Group Policy Modeling
author: nerenther
type: post
date: 2012-09-06T07:47:55+00:00
url: /index.php/2012/09/06/the-given-key-was-not-present-in-the-dictionary-error-when-running-group-policy-modeling/
categories:
  - Active Directory
  - Microsoft
tags:
  - active directory
  - group policy
  - microsoft
  - preference
  - registry

---
I ran into a rather strange error today when trying to run Group Policy Modeling on a user. Instead of showing me Summary and Settings I received an error stating that The given Key was not present in the dictionary.

At first I thought that maybe we had used some Norwegian characters somewhere in a policy, but after some googling it turns out that this is caused by ticking the parent registry container when using the Registry Wizard to create a gpo registry preference.

Microsoft has published a kb article about it here: <a href="http://support.microsoft.com/kb/2692409" target="_blank" rel="noopener">http://support.microsoft.com/kb/2692409</a>

However the resolution they are presenting is useless for most organizations I think. Recreating all registry collections is not an option, at least it wasn&#8217;t for us.

So here&#8217;s how to do it in a less time consuming manor (but it may still take some time):

<p style="text-align: center;">
  Edit any gpo you have used to set registry settings, navigate to the registry settings and look for entries looking like this:<a href="http://cloud.kemta.net/wp-uploads/Capture21.png"><img decoding="async" loading="lazy" class="size-thumbnail wp-image-340 aligncenter" title="faulty gpo registry settings" src="http://cloud.kemta.net/wp-uploads/Capture21-150x83.png" alt="" width="150" height="83" /></a>
</p>

The setting you need to delete here is TimeZoneInformation, you can spot them by the icon (the regedit icon) and by the fact that they have a blank Type.

After deleting all of this type of entries you can rerun your query and it will work as it should