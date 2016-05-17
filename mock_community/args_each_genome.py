#!/usr/bin/python
# 
#usage: python args_each_genome.py map hmmout/*.hmm.out > output

import sys
map = {}
mapfile =open(sys.argv[1],'r')
for line in mapfile:
    spl = line.rstrip().split('\t')
    #print spl
    #print spl[1][1:]
    map[spl[1]] = spl[0]
#print len(map)
genome = {}
for f in sys.argv[2:]:
    for line in open(f,'r'):
        if(line[:1]=="#"):
            continue
        spl = line.rstrip().split(" - ")
        query = spl[1].strip()
        hit = spl[0].strip()
        #print query, hit
        #arg = f.split('.')[0].split('/')[1]
        gen = map[query]
        #print gen
        if(genome.has_key(gen)):
            temp = genome[gen]
            if(temp.has_key(hit)):
                tetemp = temp[hit]
                tetemp += 1
                temp[hit] = tetemp
                genome[gen] = temp
            else:
                temp[hit] = 1
                genome[gen] = temp
        else:
            temp = {}
            temp[hit] = 1
            genome[gen]=temp

for item in genome.items():
    for res in item[1].items():
        print '\t'.join([item[0],res[0],str(res[1])])
