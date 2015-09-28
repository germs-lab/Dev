#python
#
# python TaxonToGuide.py rep_set_tax_assignments.txt output.txt
import sys
filein = sys.argv[1]
fileout = sys.argv[2]

fread = open(filein,'r')
fwrite = open(fileout,'w')

for line in fread:
    tempLine = line.split(';')
    dotFlag = 0
    for i in range(0,len(tempLine)):
        tempcol = tempLine[i].split('__')
        if (len(tempcol) > 1):
            if (len(tempcol[1]) > 0): #skip for non-annotated 
                tempData = tempcol[1].split('\t')
                if(len(tempData[0])>0): #treat for last argument
                    if (dotFlag == 1):
                        fwrite.write(".")
                    if (len(tempData) == 1):
                        fwrite.write(tempData[0])
                        dotFlag = 1
                    elif(len(tempData) == 3):
                        fwrite.write(tempData[0])
    fwrite.write('\n')
