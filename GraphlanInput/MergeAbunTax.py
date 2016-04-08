#!/usr/bin/python
# usage: python MergeAbunTax.py taxfile abundancefile outputfile
# example: python MergeAbunTax.py Refsoil16scomp_tax_assignments.txt abunTable.txt abun_w_tax.txt
import sys
fread1 = open(sys.argv[1],'r')
fread2 = open(sys.argv[2],'r')
fwrite = open(sys.argv[3],'w')

tax = []
for line in fread1:
    tempcol = line.strip().split('\t')
    temptax = [tempcol[0],line.strip()]
    tax.append(temptax)

for line in fread2:
    tempcol = line.strip().split('\t')
    for i in range(len(tax)):
        if(tempcol[0]==tax[i][0]):
            fwrite.write(line.strip()+'\t'+tax[i][1]+'\n')
