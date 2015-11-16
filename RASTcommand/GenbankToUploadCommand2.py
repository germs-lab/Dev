#!/usr/bin/pyton
# This script extract information from Genbank file to write command for RAST
# requirement: pip install biopython, (or apt-get install python-biopython), apt-get install parallel
# usage: python GenbankToUploadCommand.py genbankfilename yourID yourPassword
# python GenbankToUploadCommand2.py CP001220.gbk yourID Password
# for massive upload:
# $for x in *.gbk;do python GenbankToUploadCommand.py $x yourID Password;done
# $cat *.out > RASTupload.sh
# $cat RASTupload.sh | parallel (or $bash RASTupload.sh)
import sys

gbk_filename = sys.argv[1]
output_filename = gbk_filename+".out"
input_handle =  open(gbk_filename,"r")
output_handle = open(output_filename,"w")
yourID = sys.argv[2]
yourPass = sys.argv[3]
orga="null"

for line in input_handle:
    if("organism="in line):
        tempcol = line.strip().split("=")
        orga = tempcol[1][1:-1]
        break


for line in input_handle:
    if("taxon:" in line):
        tempcol = line.strip().split(":")
        output_handle.write("svr_submit_RAST_job --user='%s' --passwd=%s --genbank=%s --taxon_ID=%s --bioname='%s'" %(yourID,yourPass,gbk_filename,tempcol[1][:-1],orga))
        break
