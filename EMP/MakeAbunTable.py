#!/usr/bin/python
#this script make an abundance table from each soil type on RefSoil
#python MakeAbunTable.py input output

import sys
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
fread_soil = open("soilSoil.summary",'r')
fread_sedi = open("soilSediment.summary",'r')
fread_peat = open("soil_peatsoil.biom.summary",'r')
fread_rocky = open("soil_rockysand.biom.summary",'r')
fread_ag = open("soil_agriculturalsoil.biom.summary",'r')
fread_silt = open("soil_silt.biom.summary",'r')
fread_loam = open("soil_loam.biom.summary",'r')

soil = []
readflag = 0
for line in fread_soil:
    if (readflag == 0):
        if(line.strip()== "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        soil.append(tempcol)

sedi = []
readflag = 0
for line in fread_sedi:
    if (readflag == 0):
        if(line.strip()== "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        sedi.append(tempcol)

readflag = 0
peat = []
for line in fread_peat:
    if (readflag == 0):
        if(line.strip() == "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        peat.append(tempcol)

rocky = []
readflag = 0
for line in fread_rocky:
    if (readflag == 0):
        if(line.strip()== "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        rocky.append(tempcol)

ag = []
readflag = 0
for line in fread_ag:
    if (readflag == 0):
        if(line.strip()== "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        ag.append(tempcol)

silt = []
readflag = 0
for line in fread_silt:
    if (readflag == 0):
        if(line.strip()== "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        silt.append(tempcol)

loam = []
readflag = 0
for line in fread_loam:
    if (readflag == 0):
        if(line.strip()== "Counts/sample detail:"):
            readflag = 1
    elif (readflag == 1):
        tempcol = line.strip().split(': ')
        loam.append(tempcol)


fwrite.write("refsoilID"+'\t'+"OTU"+'\t'+"soil"+'\t'+"sediment"+'\t'+"peat"+'\t'+"rocky"+'\t'+"ag"+'\t'+"silt"+'\t'+"loam"+'\n')
for line in fread:
    tempcol = line.split('\t')
    tempsoil = "1"
    tempsedi = "1"
    temppeat = "1"
    temprocky = "1"
    tempag = "1"
    tempsilt = "1"
    temploam = "1"
    for i in range(len(soil)):
        if(tempcol[1]==soil[i][0]):
            tempsoil = soil[i][1]
    for i in range(len(sedi)):
        if(tempcol[1]==sedi[i][0]):
            tempsedi = sedi[i][1]
    for i in range(len(peat)):
        if(tempcol[1]==peat[i][0]):
            temppeat = peat[i][1]
    for i in range(len(rocky)):
        if(tempcol[1]==rocky[i][0]):
            temprocky = rocky[i][1]
    for i in range(len(ag)):
        if(tempcol[1]==ag[i][0]):
            tempag = ag[i][1]
    for i in range(len(silt)):
        if(tempcol[1]==silt[i][0]):
            tempsilt = silt[i][1]
    for i in range(len(loam)):
        if(tempcol[1]==loam[i][0]):
            temploam = loam[i][1]
    fwrite.write(tempcol[0]+'\t'+tempcol[1]+'\t'+tempsoil+'\t'+tempsedi+'\t'+temppeat+'\t'+temprocky+'\t'+tempag+'\t'+tempsilt+'\t'+temploam+'\n')
