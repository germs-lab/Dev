#!/usr/bin/python

def ReadTable(filename):
    fread = open(filename,'r')
    SC = []
    for line in fread:
        tempcol = line.strip().split('\t')
        tempSC = []
        for i in range(len(tempcol)):
            tempSC.append(tempcol[i])
        SC.append(tempSC)
    return SC

def ReadTableSemi(filename):
    fread = open(filename,'r')
    SC = []
    for line in fread:
        tempcol= line.strip().split(";")
        tempSC = []
    for i in range(len(tempcol)):
        tempSC.append(tempcol[i])
        SC.append(tempSC)
    return SC

def ReadTableSemiOne(filename,num):
    fread = open(filename,'r')
    vector = []
    for line in fread:
        tempcol= line.strip().split(";")
        vector.append(tempcol[num])
    return vector
