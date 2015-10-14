#!/usr/bin/python
#
# python SummaryToAbundance.py ../EMP/soil_loam.biom.summary soil.abundance.txt

import sys
inputRead = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')

flag = 0
for line in inputRead:
    if (flag == 0):
        if (line.strip() == "Counts/sample detail:"):
            flag = 1
    elif (flag == 1):
        tempcol = line.strip().split(': ')
        fwrite.write(tempcol[0]+'\t'+tempcol[1]+'\n')
