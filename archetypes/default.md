---
{{- $slug := replaceRE `^\d{4}-\d{2}-\d{2}-` "" .File.ContentBaseName }}
title: "{{ replace $slug "-" " " | title }}"
date: {{ .Date }}
url: /index.php/{{ time.Format "2006/01/02" .Date }}/{{ $slug }}/
categories: []
tags: []
draft: true
---
