#This script generate map: genome, gene_name(locus)
#usage: for x in *.gbk;do python get_map.py name $x;done > output 
from Bio import SeqIO
import sys
gb_file = sys.argv[2]
gb_record = SeqIO.read(open(gb_file,'r'),'genbank')

name = {}
for line in open(sys.argv[1],'r'):
    spl = line.rstrip().split('\t')
    name[spl[1]]=spl[0]

for record in gb_record.features:
    if (record.type == "CDS"):
        for x in record.qualifiers:
            if (x == "translation"):
                ids = [">",record.qualifiers["locus_tag"][0]]
                gene_name = "".join(ids)
                genome = gb_file.split('.')[0].split('/')[1]
                print '\t'.join([name[genome],gene_name])

