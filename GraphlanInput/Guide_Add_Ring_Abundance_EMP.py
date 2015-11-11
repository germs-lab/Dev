#!/usr/bin/python
# python Guide_Add_Ring_Abundance_EMP.py Soil_EMP_guideNB.txt soil.emp.abundance.txt anno.EMP.Abundance.Ring.txt

import sys, os
import modules

Guidein = open(sys.argv[1],'r')
Abunin = sys.argv[2]

fwrite = open(sys.argv[3],'w')

#read table
Table = ReadTableSep(Abunin,'\t')
