#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os


from os.path import dirname, abspath
d = os.path.abspath(__file__ + "/../../")

print d
search_term = 'amphtml'
search_file = '{0}/{1}'.format(d,sys.argv[1])
for line in open(search_file, 'r'):
    if re.search(search_term, line):
        print bcolors.WARNING "jinja file {0} modified. AMP template should"
                                "modified as well".format(search_file)
