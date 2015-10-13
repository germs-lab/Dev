#!/usr/bin/python
#
# python MakeAbunRing.py input output
# python MakeAbunRing.py SoilAbundance.txt SoilAbunAnno.txt

import sys
import math
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')

ringcolor = ['k','r','g','b','#0000FF','#696969','#FF0000','#FFA500','#0000FF','#696969','#FF0000','#FFA500']

# read abundance file
header = fread.readline().strip().split('\t')
labelNumStart = 2
tempNum = labelNumStart
for i in range(2,len(header)):
    fwrite.write("ring_label"+'\t'+str(tempNum)+'\t'+header[i]+'\n')
    fwrite.write("ring_label_color"+'\t'+str(tempNum)+'\t'+ringcolor[tempNum]+'\n')
    fwrite.write("ring_label_font_size"+'\t'+str(tempNum)+'\t'+"20"+'\n')
    fwrite.write("ring_color"+'\t'+str(tempNum)+'\t'+ringcolor[tempNum]+'\n')
    tempNum = tempNum+1
tempNum = labelNumStart

table = []
for line in fread:
    tempcol = line.strip().split('\t')
    tempTable = []
    for i in range(len(tempcol)):
        tempTable.append(tempcol[i])
    table.append(tempTable)

# get large
lar = []
for i in range(len(header)):
    lar.append(0.0)

for i in range(len(table)):
    for j in range(2,len(table[i])):
        if (lar[j] < float(table[i][j])):
            lar[j]=float(table[i][j])

# Write annotation file
for i in range(len(table)):
    tempNum = labelNumStart
    for j in range(2,len(table[i])):
        tempAlpha = math.log(float(table[i][j]),10)/math.log(lar[j])
        fwrite.write(table[i][0]+'\t'+"ring_alpha"+'\t'+str(tempNum)+'\t'+str(tempAlpha)+'\n')
        #fwrite.write(table[i][0]+'\t'+"ring_color"+'\t'+str(tempNum)+'\t'+ringcolor[tempNum]+'\n')
        tempNum = tempNum + 1
