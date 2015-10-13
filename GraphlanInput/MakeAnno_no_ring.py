#!/usr/bin/python
# This script make annotation file
#python MakeAnno_no_ring.py rep_set_tax_assignments.txt Annotation.txt
# print Legends part may not useful
import sys, os
import modules
filein = sys.argv[1]
fileout = sys.argv[2]
full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/DefaultAnnoNoRing.txt"

deread = open(filedefault,'r')
fwrite = open(fileout,'w')
lewrite = open("Legends.txt",'w')
#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table
Tax = modules.TaxTable(filein)

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
        fwrite.write(Tax[i][7]+'\t'+"ring_width"+'\t'+"1"+'\t'+"4"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
        if(Tax[i][6] != ""):
            fwrite.write(Tax[i][7]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
            fwrite.write(Tax[i][7]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
            fwrite.write(Tax[i][7]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        
#print Legends
for i in range(len(KingdomColor)):
    lewrite.write(KingdomColor[i][0]+":"+KingdomColor[i][1]+'\n')

lewrite.write('\n')

for i in range(len(classColor)):
    lewrite.write(classColor[i][0]+":"+classColor[i][1]+'\n')
