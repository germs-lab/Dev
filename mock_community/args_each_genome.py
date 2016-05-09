#!/usr/bin/python
# 
#usage: python args_each_genome.py map hmmout/*.hmm.out > output

import sys
map = {}
mapfile =open(sys.argv[1],'r')
for line in mapfile:
    spl = line.rstrip().split('\t')
    #print spl[1][1:]
    map[spl[1]] = spl[0]
#print len(map)
genome = {}
for f in sys.argv[2:]:
    for line in open(f,'r'):
        if(line[:1]=="#"):
            continue
        spl = line.rstrip().split(" ")
        arg = f.split('.')[0].split('/')[1]
        #print spl
        if(genome.has_key(map[spl[0]])):
            temp = genome[map[spl[0]]]
            if(temp.has_key(arg)):
                tetemp = temp[arg]
                tetemp += 1
                temp[arg] = tetemp
            else:
                temp[arg] = 1
            
        else:
            temp = {}
            temp[arg] = 1
            genome[map[spl[0]]]=temp

for item in genome.items():
    for res in item[1].items():
        print item[0],res[0],res[1]
