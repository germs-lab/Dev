#!/usr/bin/python
#usage: python rdp_to_guide.py rdpfile > output

import sys
import read_rdp_taxonomy
filename = sys.argv[1]

tax = read_rdp_taxonomy.get_tax(filename)

for item in tax:
    print item[1]+'.'+item[2]+'.'+item[3]+'.'+item[4]+'.'+item[5]+'.'+item[6]

