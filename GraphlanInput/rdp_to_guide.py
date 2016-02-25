#!/usr/bin/python
#usage: python rdp_to_guide.py rdpfile > output

import sys
import read_rdp_taxonomy
filename = sys.argv[1]

tax = read_rdp_taxonomy.get_tax(filename)
dict = {}
for item in tax:
    guide = item[1]+'.'+item[2]+'.'+item[3]+'.'+item[4]+'.'+item[5]+'.'+item[6]
    if (dict.has_key(guide)):
        temp = dict[guide]
        newtemp = temp+','+item[0]
        dict[guide] = newtemp
    else:
        dict[guide] = item[0]

for x in dict.keys():
    print x
#print len(dict)
