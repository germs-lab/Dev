#!/usr/bin/python
#python LogTransform.py input output
#python LogTransform.py abunTable.txt abunTable.log.txt
import sys
import math
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')

for line in fread:
    tempcol = line.strip().split('\t')
    x = math.log(float(tempcol[2]),10)
    fwrite.write(tempcol[0]+'\t'+tempcol[1]+'\t'+str(x)+'\n')
