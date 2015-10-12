#python
#python MakeAnno.py rep_set_tax_assignments.txt DefaultAnno.txt anno.txt
import sys
import modules
filein = sys.argv[1]
filedefault =  sys.argv[2]
fileout = sys.argv[3]

deread = open(filedefault,'r')
fwrite = open(fileout,'w')

#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table
Tax = modules.TaxTable(filein)

# class color assignment
phylum = []
Family = []
Class = []
genus = []
for i in range(len(Tax)):
	phylum.append(Tax[i][1])
	Family.append(Tax[i][4])
	Class.append(Tax[i][2])
	genus.append(Tax[i][5])
uniqPhylum = list(set(phylum))
uniqFamily = list(set(Family))
uniqClass = list(set(Class))
uniqGenus = list(set(genus))

color = ['r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#800080','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1','#D15FEE','#FFC0CB','#800000','#808080','#B0171F','r','g','b','#FFC0CB','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#8000\
80','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1','r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#8000\
80','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1','r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#8000\
80','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1']

classColor = []
for i in range(len(uniqClass)):
    tempClassColor = [uniqClass[i],color[i]]
    classColor.append(tempClassColor)
KingdomColor = [["Bacteria",'#EE6A50'],["Archaea",'#9ACD32']]

# Write annotation
for i in range(len(Tax)):
    tempColor = "k"
    kingColor = "k"
    for j in range(len(classColor)):
        if (classColor[j][0]==Tax[i][2]):
            tempColor = classColor[j][1]
    if (Tax[i][0] == KingdomColor[0][0]):
        kingColor = KingdomColor[0][1]
    elif(Tax[i][0] == KingdomColor[1][0]):
        kingColor = KingdomColor[1][1]
    if (Tax[i][5] != ""):
        fwrite.write(Tax[i][2]+'\t'+"annotation"+'\t'+"*:"+Tax[i][2]+'\n')
        fwrite.write(Tax[i][2]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
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
