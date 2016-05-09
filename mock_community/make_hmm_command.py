#!/usr/bin/python
#usage: python make_hmm_command.py input
import sys
import os.path
for line in open(sys.argv[1],'r'):
    ids = line.strip()
    fname = "hmm/"+ids+".hmm"
    print "hmmsearch -E 1e-5 --tblout hmmout/"+ids+".hmm.out hmm/"+ids+".hmm mock_all_protein.fa"
    if not os.path.isfile(fname):
        print fname
