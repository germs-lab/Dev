#!/usr/bin/python
#usage: python MakeAnnoGuide_w_ring.py taxonomyFile outputFile
#python MakeAnnoGuide_w_ring.py RefSoil16sHMMFastaNS_tax_assignments.txt soil.abundance.txt anno.guide.ring.txt
# This script may not useful
import sys, os
import modules
filein = sys.argv[1]
fileAbun = sys.argv[2]
fileout = sys.argv[3]

full_path = os.path.realpath(__file__)
filedefault = os.path.dirname(full_path)+"/DefaultAnnoNoRing.txt"
AbunRead = open(fileAbun,'r')
deread = open(filedefault,'r')
fwrite = open(fileout,'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table
Tax = modules.TaxTable(filein)

#Make abundance table
AbunTable = modules.ReadSummaryAbun(AbunRead)

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
        fwrite.write(Tax[i][1]+'\t'+"annotation"+'\t'+"*:"+Tax[i][1]+'\n')
        fwrite.write(Tax[i][1]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][5]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][5]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"ring_width"+'\t'+"1"+'\t'+"2"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
        if(Tax[i][6] != ""):
            fwrite.write(Tax[i][6]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
            fwrite.write(Tax[i][6]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
            fwrite.write(Tax[i][6]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        for k in range(len(AbunTable)):
            if (Tax[i][7] == AbunTable[k][0]):
                fwrite.write(Tax[i][5]+'\t'+"ring_color"+'\t'+"9"+'\t'+tempColor+'\n')
                fwrite.write(Tax[i][5]+'\t'+"ring_height"+'\t'+"9"+'\t'+AbunTable[k][1]+'\n')
