#!/usr/bin/python
#python count_map.py summaryfile mapfile > output
import sys

sumread = open(sys.argv[1],'r')
mapread = open(sys.argv[2],'r')
dict = {}
line = sumread.next()
while (line.strip() != 'Counts/sample detail:'):
    line = sumread.next()
print line
#for line in sumread:
    
