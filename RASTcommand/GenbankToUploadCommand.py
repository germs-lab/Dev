# This script extract information from Genbank file to write command for RAST
# requirement: pip install biopython, (or apt-get install python-biopython), apt-get install parallel
# usage: python GenbankToUploadCommand.py genbankfilename yourID yourPassword
# python GenbankToUploadCommand.py CP001220.gbk yourID Password
# for massive upload:
# $for x in *.gbk;do python GenbankToUploadCommand.py $x yourID Password;done
# $cat *.out > RASTupload.sh
# $cat RASTupload.sh | parallel (or $bash RASTupload.sh)
from Bio import SeqIO
import sys
gbk_filename = sys.argv[1]
output_filename = gbk_filename+".out"
input_handle =  open(gbk_filename,"r")
output_handle = open(output_filename,"w")
yourID = sys.argv[2]
yourPass = sys.argv[3]

for seq_record in SeqIO.parse(input_handle,"genbank") :
    print "Dealing with GenBank record %s" % seq_record.id
    for seq_feature in seq_record.features :
        if seq_feature.type == "source" :
            taxonClass = seq_feature.qualifiers['db_xref']
            taxonID = taxonClass[0].split(':')
            output_handle.write("svr_submit_RAST_job --user='%s' --passwd=%s --genbank=%s --taxon_ID=%s --bioname='%s'" %(yourID,yourPass,gbk_filename,taxonID[1],seq_feature.qualifiers['organism'][0]))

output_handle.close()
input_handle.close()
