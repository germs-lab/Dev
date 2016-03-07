#!/usr/bin/python
#python add_ring_soil_type.py soil_type_abun.txt anno.soiltype.txt
import sys,os
import modules
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
dict={}
for line in fread:
    spl = line.strip().split('\t')
    temp = []
    for i in range(2,len(spl)):
        temp.append(spl[i])
    dict[spl[0]]=temp
color = ['r','g','b','#E80C7A','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#E80C7A','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#E80C7A','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125','r','g','b','#006400','#00CD00','#191970','#303030','#7B68EE','#800000','#800080','#808080','#87CEFA','#8B4513','#8DEEEE','#8E8E38','#9ACD32','#B0171F','#BC8F8F','#CDCDC1','#D15FEE','#EE6A50','#FFC0CB','#FFC125']

for item in dict.items():
    templist = []
    for x in item[1]:
        templist.append(float(x))
    tempsum = sum(list(templist))
    for i in range(0,len(item[1])):
        if (tempsum == 0.0):
            tempAlpha = 0.0
        else:
            tempAlpha = float(i)/tempsum
        #print tempAlpha
        fwrite.write(item[0]+'\t'+"ring_width"+'\t'+str(i+2)+'\t'+"1"+'\n')
        fwrite.write(item[0]+'\t'+"ring_height"+'\t'+str(i+2)+'\t'+"0.34"+'\n')
        fwrite.write(item[0]+'\t'+"ring_color"+'\t'+str(i+2)+'\t'+color[i]+'\n')
        fwrite.write(item[0]+'\t'+"ring_alpha"+'\t'+str(i+2)+'\t'+str(tempAlpha)+'\n')
