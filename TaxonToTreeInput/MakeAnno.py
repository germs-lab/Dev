#python
#python MakeAnno.py rep_set_tax_assignments.txt anno.txt
import sys
filein = sys.argv[1]
fileout = sys.argv[2]

fread = open(filein,'r')
deread = open("DefaultAnno.txt",'r')
fwrite = open(fileout,'w')

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

#print classColor
for i in range(len(Tax)):
    tempColor = "k"
    kingColor = "k"
    for j in range(len(classColor)):
        if (classColor[j][0]==Tax[i][2]):
            tempColor = classColor[j][1]
    if (Tax[i][0] == "Bacteria"):
        kingColor = '#EE6A50'
    elif(Tax[i][0] == "Archaea"):
        kingColor = '#9ACD32'
    if (Tax[i][5] != ""):
        fwrite.write(Tax[i][2]+'\t'+"annotation"+'\t'+"*:"+Tax[i][2]+'\n')
        fwrite.write(Tax[i][2]+'\t'+"annotation_background_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][5]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
        fwrite.write(Tax[i][5]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"ring_width"+'\t'+"1"+'\t'+"2"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"ring_height"+'\t'+"1"+'\t'+"0.35"+'\n')
        #fwrite.write(Tax[i][5]+'\t'+"ring_shape"+'\t'+"1"+'\t'+"v"+'\n')
        fwrite.write(Tax[i][5]+'\t'+"ring_color"+'\t'+"1"+'\t'+kingColor+'\n')
        if(Tax[i][6] != ""):
            fwrite.write(Tax[i][6]+'\t'+"clade_marker_color"+'\t'+tempColor+'\n')
            fwrite.write(Tax[i][6]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
            fwrite.write(Tax[i][6]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
            #fwrite.write(Tax[i][5]+'\t'+"ring_width"+'\t'+"2"+'\t'+"4"+'\n')
            #fwrite.write(Tax[i][5]+'\t'+"ring_height"+'\t'+"2"+'\t'+"0.35"+'\n')
            #fwrite.write(Tax[i][5]+'\t'+"ring_color"+'\t'+"2"+'\t'+kingColor+'\n')

#for i in range(len(uniqPhylum)):
#    fwrite.write(uniqPhylum[i]+'\t'+"annotation"+'\t'+uniqPhylum[i]+'\n')
#    fwrite.write(uniqPhylum[i]+'\t'+"annotation_background_color"+'\t'+color[i]+'\n')
#    fwrite.write(uniqPhylum[i]+'\t'+"clade_marker_color"+'\t'+"k"+'\n')
#    fwrite.write(uniqPhylum[i]+'\t'+"clade_marker_size"+'\t'+"3"+'\n')

#for i in range(len(uniqFamily)):
#    fwrite.write(uniqFamily[i]+'\t'+"clade_marker_color"+'\t'+"b"+'\n')
#    fwrite.write(uniqFamily[i]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')

#for i in range(len(uniqClass)):
#    fwrite.write(uniqClass[i]+'\t'+"annotation"+'\t'+"*:"+uniqClass[i]+'\n')
#    fwrite.write(uniqClass[i]+'\t'+"annotation_background_color"+'\t'+"w"+'\n')
#    fwrite.write(uniqClass[i]+'\t'+"clade_marker_color"+'\t'+"k"+'\n')
#    fwrite.write(uniqClass[i]+'\t'+"clade_marker_size"+'\t'+"3"+'\n')
#    fwrite.write(uniqClass[i]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')

#for i in range(len(uniqGenus)):
#    fwrite.write(uniqGenus[i]+'\t'+"clade_marker_color"+'\t'+color[0]+'\n')
#    fwrite.write(uniqGenus[i]+'\t'+"clade_marker_size"+'\t'+"30"+'\n')
#    fwrite.write(uniqGenus[i]+'\t'+"clade_marker_edge_width"+'\t'+"0.1"+'\n')
