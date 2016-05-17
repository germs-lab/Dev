#!/usr/bin/python
# this script get count for each ARG proteiin seq
# usage: python get_count_gene.py list mock_protein_with_prodcut.fa map

import sys
lis = {}
for line in open(sys.argv[1],'r'):
    lis[line.strip()] = line.strip()

for line in open(sys.argv[2],'r'):
    if (line[:1] == ">"):
        for keys in lis.keys():
            if(keys in line):
                print line,
    #else:
    #    print line,
