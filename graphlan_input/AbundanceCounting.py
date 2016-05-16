#python
# python AbundanceCounting.py inpu1 input2 output
# example: python AbundanceCounting.py refsoil.out.txt out abunTable.txt
import sys
filein1 = sys.argv[1]
filein2 = sys.argv[2]
fileout = sys.argv[3]

fread1 = open(filein1,'r')
fread2 = open(filein2,'r')
fwrite = open(fileout,'w')

# make table
AbunTable = []
for line in fread2:
    tempcol = line.split(':')
    tempTable = [tempcol[0][1:],tempcol[1][1:-1]]            
    AbunTable.append(tempTable)

   
# matching
for line in fread1:
    tempcol = line.split('\t')
    for i in range(len(AbunTable)):
        if (tempcol[1] == AbunTable[i][0]):
            incase = tempcol[0].split(':')
            fwrite.write(incase[0]+'\t'+tempcol[1]+'\t'+AbunTable[i][1]+'\n')
            break
