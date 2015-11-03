#!/usr/bin/python
# python SC.py input1 input2 input3 output
# python SC.py fixrank_RS_garden_AG-212_16S.fasta_classified.unix.txt RS_blast.out.txt garden_soilEMP.out.txt RefSoilTaxFull.txt output.txt

import sys
import functions

fwrite =open(sys.argv[5],'w')

SC = []
SC = functions.ReadTable(sys.argv[1])

ref = []
ref = functions.ReadTable(sys.argv[2])

emp = []
emp = functions.ReadTable(sys.argv[3])

tax = []
tax = functions.ReadTableSemiOne(sys.argv[4],6)
for i in range(len(SC)):
    lin = ""
    for j in range(2,len(SC[i]),2):
        lin = lin+SC[i][j]+";"
    refper = "null"
    empper = "null"
    for k in range(len(ref)):
        if(SC[i][0]==ref[k][0]):
            refper = ref[k][2]
    for l in range(len(emp)):
        if(SC[i][0]==emp[l][0]):
            empper = emp[l][2]
    contains = "new genus"
    if(SC[i][12] in tax):
        contains = "existed"
    fwrite.write(SC[i][0]+'\t'+lin+'\t'+refper+'\t'+empper+'\t'+contains+'\n')
