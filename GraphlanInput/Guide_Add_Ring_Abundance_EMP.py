#!/usr/bin/python
# python Guide_Add_Ring_Abundance_EMP.py Soil_EMP_guideNB.txt soil.emp.abundance.txt anno.EMP.Abundance.Ring.txt

import sys, os
import modules
import math
Guidein = open(sys.argv[1],'r')
Abunin = sys.argv[2]

fwrite = open(sys.argv[3],'w')
log = 1
#read table
Table = modules.ReadTableSep(Abunin,'\t')

for line in Guidein:
    lineTemp = line.strip()
    for i in range(len(Table)):
        if (lineTemp == Table[i][0]):
            fwrite.write(lineTemp+'\t'+"ring_width"+'\t'+"9"+'\t'+"1"+'\n')
            height = Table[i][2]
            if(log == 1):
                x = math.log(float(height),10)
                height = str(x)
            fwrite.write(lineTemp+'\t'+"ring_height"+'\t'+"9"+'\t'+height+'\n')
            fwrite.write(lineTemp+'\t'+"ring_color"+'\t'+"2"+'\t'+"g"+'\n')
