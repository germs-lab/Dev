#!/usr/bin/python
#usage: python MakeAnnoGuide_w_ring.py taxonomyFile outputFile
#python MakeAnnoGuide_w_ringSingleCell.py singlecell.unix.txt anno.SingleCell.Ring.txt
# This script may not useful
import sys, os
import modules

fileAbun = sys.argv[1]
fileout = sys.argv[2]

full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/DefaultAnnoNoRing.txt"

deread = open(filedefault,'r')
fwrite = open(fileout,'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make singlecell table
AbunTable = []
Sep = "."
AbunTable = modules.ReadTableSep(fileAbun,Sep)

for i in range(len(AbunTable)):
    fwrite.write(AbunTable[i][12]+'\t'+"ring_width"+'\t'+"2"+'\t'+"1"+'\n')
    fwrite.write(AbunTable[i][12]+'\t'+"ring_height"+'\t'+"2"+'\t'+"0.35"+'\n')
    fwrite.write(AbunTable[i][12]+'\t'+"ring_color"+'\t'+"2"+'\t'+"b"+'\n')
