#!/usr/bin/python

def TaxTable(filename):
    fread = open(filename,'r')
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
    return Tax

def AssignColor(Tax):
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
    return classColor
