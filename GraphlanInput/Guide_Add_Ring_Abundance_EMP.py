#!/usr/bin/python
# python Guide_Add_Ring_Abundance_EMP.py soil.emp.abundance.txt anno.EMP.Abundance.Ring.txt

import sys, os
import modules
import math
Abunin = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
log = 0
checkHeight = 1
for line in Abunin:
    tempCol = line.strip().split('\t')
    fwrite.write(tempCol[0]+'\t'+"ring_width"+'\t'+"9"+'\t'+"1"+'\n')
    height = tempCol[2]
    if (checkHeight == 1):
        if(float(height) > 32767):
            height = "32767"
    if(log == 1):
        x = math.log(float(height),10)
        height = str(x)
    fwrite.write(tempCol[0]+'\t'+"ring_height"+'\t'+"9"+'\t'+height+'\n')
    fwrite.write(tempCol[0]+'\t'+"ring_color"+'\t'+"9"+'\t'+"g"+'\n')
