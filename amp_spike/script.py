import sys, os
import re
from enum import Enum
from os.path import (
        dirname,
        abspath)



class Bcolors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


d = os.path.abspath(__file__ + "/../../")
search_term = 'amphtml'
msg = '{0}jinja file {1} modified. AMP template should be modified as well{2}'

for f in sys.argv:
    if not f.endswith('.jinja'):
        continue
    search_file = '{0}/{1}'.format(d,f)
    with open(search_file, 'r') as file:
        for line in file:
            if re.search(search_term, line):
                print msg.format(Bcolors.WARNING.value, f,
                Bcolors.ENDC.value)
