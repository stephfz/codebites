#!/usr/bin/env python
# -*- coding: utf-8 -*-

#path = "howto/templates/howto/guide.jinja"
path = "/Users/stephaniefrias/Projects/consumeraffairs/howto/templates/howto/guide.jinja"
source_file = open(path,"r")
contents = source_file.readlines()
has_amp = False
#look for tag amphtml
for line in contents:
    if 'amphtml' in line:
        print line
