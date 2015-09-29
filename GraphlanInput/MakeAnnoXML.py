#python
#python MakeAnno.py rep_set_tax_assignments.txt DefaultAnno.txt Annotation.txt
import sys
filein = sys.argv[1]
fileout = sys.argv[3]
filedefault = sys.argv[2]
fread = open(filein,'r')
deread = open(filedefault,'r')
fwrite = open(fileout,'w')
lewrite = open("Legends.txt",'w')
#write default
for line in deread:
    fwrite.write(line)
fwrite.write('\n')

#Make Tax table
Kingdom = []
phylum = []
Class = []
Order = []
Family = []
genus = []
Sp = []
Tax = []
ID = []
for line in fread:
    tempLine = line.split(';')
    tempTax = []
    tempKingdom = ""
    tempPhylum = ""
    tempClass = ""
    tempOrder = ""
    tempFamily = ""
    tempGenus = ""
    tempSp = ""
    tempID = ""
    for i in range(len(tempLine)):
        tempcol = tempLine[i].split('__')
        if (tempcol[0][-1:]=="k"):
            incase = tempcol[1].split('\t')
            fortempID = tempcol[0].split('\t')
            if(len(incase)==1):
                Kingdom.append(tempcol[1])
                tempKingdom = tempcol[1]
                tempID = fortempID[0]
        elif (tempcol[0]==" p"):
            incase = tempcol[1].split('\t')
            if(len(incase)==1):
                phylum.append(tempcol[1])
                tempPhylum = tempcol[1]
        elif (tempcol[0]==" c"):
            incase = tempcol[1].split('\t')
            if(len(incase)==1):
                Class.append(tempcol[1])
                tempClass = tempcol[1]
        elif (tempcol[0]==" o"):
            incase = tempcol[1].split('\t')
            if(len(incase)==1):
                Order.append(tempcol[1])
                tempOrder = tempcol[1]
        elif (tempcol[0]==" f"):
            incase = tempcol[1].split('\t')
            if(len(incase)==1):
                Family.append(tempcol[1])
                tempFamily = tempcol[1]
        elif (tempcol[0]==" g"):
            incase = tempcol[1].split('\t')
            if(len(incase)==1):
                genus.append(tempcol[1])
                tempGenus = tempcol[1]
        elif (tempcol[0]==" s"):
            incase = tempcol[1].split('\t')
            if(len(incase)==3):
                
                Sp.append(incase[0])
                tempSp = incase[0]
    tempTax = [tempKingdom,tempPhylum,tempClass,tempOrder,tempFamily,tempGenus,tempSp,tempID]
    Tax.append(tempTax)

#print Tax
uniqPhylum = list(set(phylum))
uniqFamily = list(set(Family))
uniqClass = list(set(Class))
uniqGenus = list(set(genus))

color = ['r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#800080','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1','r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#8000\
80','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1','r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#8000\
80','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1','r','g','b','#EE6A50','#9ACD32','#87CEFA','#FFC125','#8DEEEE','#006400','#8000\
80','#191970','#7B68EE','#00CD00','#8B4513','#BC8F8F','#303030','#8E8E38','#CDCDC1']
classColor = []
#class color assignment
for i in range(len(uniqClass)):
    tempClassColor = [uniqClass[i],color[i]]
    classColor.append(tempClassColor)
KingdomColor = [["Bacteria",'#EE6A50'],["Archaea",'#9ACD32']]
#print classColor
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
        #fwrite.write(Tax[i][7]+'\t'+"annotation"+'\t'+Tax[i][2]+'\n')
        fwrite.write(Tax[i][7]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_width"+'\t'+"1"+'\t'+"4"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
        #fwrite.write(Tax[i][5]+'\t'+"ring_shape"+'\t'+"1"+'\t'+"v"+'\n')
        fwrite.write(Tax[i][7]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
        
#print Legends
for i in range(len(KingdomColor)):
    lewrite.write(KingdomColor[i][0]+":"+KingdomColor[i][1]+'\n')

lewrite.write('\n')

for i in range(len(classColor)):
    lewrite.write(classColor[i][0]+":"+classColor[i][1]+'\n')
