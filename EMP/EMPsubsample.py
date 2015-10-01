#this code find list of sample that only from soil habitate in EMP
#usage: python EMPsubsample.py input input_to_remove output
#example: python EMPsubsample.py ../EMPsampleInfoMerge/EMP_10k_merged_mapping_final.txt IDtoRemoveUnix.txt EMPsubSoilMapping.txt

import sys
filein = sys.argv[1]
fileindelist = sys.argv[2]
fileout = sys.argv[3]

fread = open(filein,'r')
freaddelist = open(fileindelist,'r')
fwrite = open(fileout,'w')

#read ID to remove
idlist = []
for line in freaddelist:
    myline = line.split('\n')
    idlist.append(myline[0])

headertemp = fread.readline()
fwrite.write(headertemp)
header = headertemp.split('\t')
colnum = 0
for i in range(len(header)):
    if (header[i]=='ENV_MATTER'):
        colnum=i

for line in fread:
    tempcol = line.split('\t')
    if(tempcol[colnum]=='ENVO:Agricultural soil')or(tempcol[colnum]=='ENVO:loam')or(tempcol[colnum]=='ENVO:peat soil')or(tempcol[colnum]=='ENVO:rocky sand')or(tempcol[colnum]=='ENVO:sandstone')or(tempcol[colnum]=='ENVO:sediment')or(tempcol[colnum]=='ENVO:silt')or(tempcol[colnum]=='ENVO:soil'):
        flag = 0
        for i in range(len(idlist)):
            if(idlist[i]==tempcol[0]):
                flag = 1
        if(flag==0):
            fwrite.write(line)
