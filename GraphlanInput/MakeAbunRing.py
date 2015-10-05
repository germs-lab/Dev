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

table = []
for line in fread:
    tempcol = line.strip().split('\t')
    tempTable = []
    for i in range(len(tempcol)):
        tempTable.append(tempcol[i])
    table.append(tempTable)
lar = []
for i in range(len(header)):
    lar.append(0.0)

for i in range(len(table)):
    for j in range(2,len(table[i])):
        if (lar[j] < float(table[i][j])):
            lar[j]=float(table[i][j])

for i in range(len(table)):
    tempNum = labelNumStart
    for j in range(2,len(table[i])):
        tempAlpha = math.log(float(table[i][j]),10)
        fwrite.write(table[i][0]+'\t'+"ring_alpha"+'\t'+str(tempNum)+'\t'+str(tempAlpha)+'\n')
        tempNum = tempNum + 1
