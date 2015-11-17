#!/usr/bin/python
# python RASTdownloadCommad.py inpufile ID password

import sys
fread = open(sys.argv[1],'r')
id = sys.argv[2]
passwd = sys.argv[3]

for line in fread:
    if(line.strip()[:1]=="["):
        continue
    tempcol = line.strip().split('\t')
    print "~/sas/bin/svr_retrieve_RAST_job "+id+" "+passwd+" "+tempcol[0]+" rast_tarball > "+tempcol[2]+".tar.gz"
