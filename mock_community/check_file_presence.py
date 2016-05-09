#!/usr/bin/python
# this script find if the file is presence 
# usage: python check_file_presence.py idfile folder

import sys
import os.path
for line in open(sys.argv[1],'r'):
    ids = line.strip()
    fname = sys.argv[2]+"/"+ids+".hmm"
    if not os.path.isfile(fname):
        print ids
