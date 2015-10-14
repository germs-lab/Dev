#!/usr/bin/python
#
# python SummaryToAbundance.py ../EMP/soil_loam.biom.summary RefSoil16sHMMFastaNS_tax_assignments.txt soil.abundance.txt

import sys
import modules
inputRead = open(sys.argv[1],'r')
taxRead = sys.argv[2]
fwrite = open(sys.argv[3],'w')

#read count
count = []
flag = 0
for line in inputRead:
    if (flag == 0):
        if (line.strip() == "Counts/sample detail:"):
            flag = 1
    elif (flag == 1):
        tempcol = line.strip().split(': ')
        #fwrite.write(tempcol[0]+'\t'+tempcol[1]+'\n')
        tempCount = [tempcol[0],tempcol[1]]
        count.append(tempCount)

# read Tax
Tax = modules.TaxTable(taxRead)
# taxonomy table to guide table
Guide = modules.TaxToGuide(Tax)

#write result
for i in range(len(count)):
    for j in range(len(Guide)):
        if(count[i][0] == Guide[j][0]):
            fwrite.write(Guide[j][1]+'\t'+Guide[j][0]+'\t'+count[i][1]+'\n')
