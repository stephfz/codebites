#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os
#path = "/Users/stephaniefrias/Projects/consumeraffairs/howto/templates/howto/guide.jinja"

#print sys.argv[1]
print os.getcwd()

search_term = 'amphtml'
search_file = sys.argv[1]
for line in open(search_file, 'r'):
    if re.search(search_term, line):
        print 'jinja file {0} modified. AMP template should modified as well'.format(search_file)
