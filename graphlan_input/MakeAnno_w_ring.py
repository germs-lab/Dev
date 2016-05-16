#!/usr/bin/python
# python MakeAnno_w_ring.py RefSoil16sHMMFastaNS_tax_assignments.txt abunTable.txt Annotation.txt
import sys, os
import modules
filein = sys.argv[1]
full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/DefaultAnnoNoRing.txt"
fileAbun = sys.argv[2]
fileout = sys.argv[3]

deread = open(filedefault,'r')
AbunRead = open(fileAbun,'r')
fwrite = open(fileout,'w')
lewrite = open("Legends.txt",'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table
Tax = modules.TaxTable(filein)

#Make abundance table
"""
AbunTable = []
for line in AbunRead:
    tempcol =  line.split('\t')
    tempAbunTable = [tempcol[0],tempcol[1],tempcol[2]]
    AbunTable.append(tempAbunTable)
bignumber = 0
amp = 1
for i in range(len(AbunTable)):
    if (float(AbunTable[i][2])>bignumber):
        bignumber = float(AbunTable[i][2])
for i in range(len(AbunTable)):
    AbunTable[i][2] = str(format(float(AbunTable[i][2])*amp/bignumber,'f'))
"""
AbunTable = modules.MakeAbunTable(AbunRead)

# class color assignment
classColor = modules.AssignColor(Tax)
KingdomColor = [["Bacteria",'#EE6A50'],["Archaea",'#9ACD32']]

# Write annotation
for i in range(len(Tax)):
    tempColor = "k"
    kingColor = "k"
    for j in range(len(classColor)):
        if (classColor[j][0]==Tax[i][1]):
            tempColor = classColor[j][1]
    if (Tax[i][0] == KingdomColor[0][0]):
        kingColor = KingdomColor[0][1]
    elif(Tax[i][0] == KingdomColor[1][0]):
        kingColor = KingdomColor[1][1]
    if (Tax[i][5] != ""):
        fwrite.write(Tax[i][7]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_width"+'\t'+"1"+'\t'+"3"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.34"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
        if(Tax[i][6] != ""):
            fwrite.write(Tax[i][7]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
            fwrite.write(Tax[i][7]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
            fwrite.write(Tax[i][7]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        for k in range(len(AbunTable)):
            if (Tax[i][7] == AbunTable[k][0]):
                fwrite.write(Tax[i][7]+'\t'+"ring_color"+'\t'+"9"+'\t'+tempColor+'\n')
                fwrite.write(Tax[i][7]+'\t'+"ring_height"+'\t'+"9"+'\t'+AbunTable[k][2]+'\n')

#print Legends
for i in range(len(KingdomColor)):
    lewrite.write(KingdomColor[i][0]+":"+KingdomColor[i][1]+'\n')

lewrite.write('\n')

for i in range(len(classColor)):
    lewrite.write(classColor[i][0]+":"+classColor[i][1]+'\n')
    fwrite.write(classColor[i][0]+'\t'+"annotation"+'\t'+classColor[i][0]+'\n')
    fwrite.write(classColor[i][0]+'\t'+"clade_marker_color"+'\t'+classColor[i][1]+'\n')
