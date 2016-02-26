#!/usr/bin/python
#python count_map.py summaryfile mapfile > output
import sys

sumread = open(sys.argv[1],'r')
mapread = open(sys.argv[2],'r')

#read summaryfile
dict = {}
line = sumread.next()
while (line.strip() != 'Counts/sample detail:'):
    line = sumread.next()
line = sumread.next()
for line in sumread:
    splt = line.strip().split(': ')
    dict[splt[0]]=splt[1]
sumread.close()
#read map
for line in mapread:
    splt = line.strip().split('\t')
    ids = splt[1].split(',')
    for x in ids:
        print dict[x]

