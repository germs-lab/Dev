#!/usr/bin/python
#
# python MakeAbunRing.py input output
# python MakeAbunRing.py SoilAbundance.txt SoilAbunAnno.txt

import sys
import math
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')

header = fread.readline().strip().split('\t')
labelNumStart = 2
tempNum = labelNumStart
for i in range(2,len(header)):
    fwrite.write("ring_label"+'\t'+str(tempNum)+'\t'+header[i]+'\n')
    tempNum = tempNum+1
tempNum = labelNumStart
for line in fread:
    tempcol = line.strip().split('\t')
    tempNum = labelNumStart
    for i in range(2,len(tempcol)):
        tempAlpha = math.log(float(tempcol[i]),10)
        fwrite.write(tempcol[0]+'\t'+"ring_alpha"+'\t'+str(tempNum)+'\t'+str(tempAlpha)+'\n')
        tempNum = tempNum + 1
