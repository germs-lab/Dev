#!/usr/bin/python
# usage: python MostWanted.py otuList abundance taxonomy output
# example: python MostWanted.py MostWantedList.txt 200mostAbunOTU_w_counts.txt uclust_assigned_taxonomy/MostWanted_tax_assignments.txt MostWantedOTUFinal.txt

import sys
import modules

fileOTU = sys.argv[1]
fileAbun = sys.argv[2]
fileTax = sys.argv[3]
fileout = sys.argv[4]
fwrite = open(fileout,'w')

OTU = modules.FileToTable(fileOTU,'\t')
Abun = modules.FileToTable(fileAbun,'\t')
Tax = modules.TaxTable(fileTax)
guide = modules.TaxToGuide(Tax)

for i in range(len(OTU)):
    for j in range(len(Abun)):
        if (OTU[i][0] == Abun[j][0]):
            for k in range(len(guide)):
                if (OTU[i][0] == guide[k][0]):
                    fwrite.write(OTU[i][0]+'\t'+Abun[j][1]+'\t'+guide[k][1]+'\n')
