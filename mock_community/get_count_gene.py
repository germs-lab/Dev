#!/usr/bin/python
# this script get count for each ARG proteiin seq
# usage: python get_count_gene.py list mock_protein_with_prodcut.fa map

import sys
lis = {}
for line in open(sys.argv[1],'r'):
    lis[line.strip()] = line.strip()
#print lis
map = {}
for line in open(sys.argv[3],'r'):
    spl = line.rstrip().split('\t')
    map[spl[1]] = spl[0]
genome = {}
for line in open(sys.argv[2],'r'):
    if (line[:1] == ">"):
        for keys in lis.keys():
            if(" "+keys.upper()+" " in line.upper()):
                locus = line.split(' ')[0][1:]
                gen = map[locus]
                arg = keys
                result = [map[locus],line.strip(),"::",keys]
                #print '\t'.join(result)
                if (genome.has_key(gen)):
                    temp = genome[gen]
                    if (temp.has_key(arg)):
                        tetemp = temp[arg]
                        tetemp += 1
                        temp[arg] = tetemp
                        genome[gen] = temp
                    else:
                        temp[arg] = 1
                        genome[gen] = temp
                else:
                    temp = {}
                    temp[arg] = 1
                    genome[gen] = temp


for item in genome.items():
    for res in item[1].items():
        print '\t'.join([item[0],res[0],str(res[1])])
