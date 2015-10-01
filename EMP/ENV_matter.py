#this script seperate soil map into different env_matters to return ID
#usage: python ENV_matter.py input
#example: python ENV_matter.py EMPsubSoilMapping.txt

import sys
filein = sys.argv[1]

fread = open(filein,'r')
fwriteSoil = open("soilsoil.txt",'w')
fwriteSediment = open("soilsediment.txt",'w')
fwritePeatsoil =  open("soilpeatsoil.txt",'w')
fwriteRockysand = open("soilrockysand.txt",'w')
fwriteAgriculturalsoil = open("soilagriculturalsoiil.txt",'w')
fwriteSilt = open("soilsilt.txt",'w')
fwriteLoam = open("soilloam.txt",'w')
fwritestat = open("stat.txt",'w')

headertemp = fread.readline()
header = headertemp.split('\t')
colnum = 0
for i in range(len(header)):
    if (header[i]=='ENV_MATTER'):
        colnum=i
soil=0
sediment=0
peatSoil=0
rockySand=0
AgSoil=0
silt=0
loam=0

for line in fread:
    tempcol = line.split('\t')
    if(tempcol[colnum]=='ENVO:soil'):
        soil += 1
        fwriteSoil.write(tempcol[0]+'\n')
    elif(tempcol[colnum]=='ENVO:sediment'):
        sediment += 1
        fwriteSediment.write(tempcol[0]+'\n')
    elif(tempcol[colnum]=='ENVO:peat soil'):
        peatSoil += 1
        fwritePeatsoil.write(tempcol[0]+'\n')
    elif(tempcol[colnum]=='ENVO:rocky sand'):
        rockySand += 1
        fwriteRockysand.write(tempcol[0]+'\n')
    elif(tempcol[colnum]=='ENVO:Agricultural soil'):
        AgSoil += 1
        fwriteAgriculturalsoil.write(tempcol[0]+'\n')
    elif(tempcol[colnum]=='ENVO:silt'):
        silt += 1
        fwriteSilt.write(tempcol[0]+'\n')
    elif(tempcol[colnum]=='ENVO:loam'):
        loam += 1
        fwriteLoam.write(tempcol[0]+'\n')

fwritestat.write("soil"+'\t'+"sediment"+'\t'+"peatSoil"+'\t'+"rockySand"+'\t'+"AgSoil"+'\t'+"silt"+'\t'+"loam"+'\n')
fwritestat.write(str(soil)+'\t'+str(sediment)+'\t'+str(peatSoil)+'\t'+str(rockySand)+'\t'+str(AgSoil)+'\t'+str(silt)+'\t'+str(loam))   

