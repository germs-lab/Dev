# Graplan Input

This script generate input file for Graplan

To draw a tree with Graplan, you will need following:

1. Tree file (.dnd, .xml or guide)
```
$ clustalo -i fasta.fa --guidetree-out=treefilename.dnd
```
2. Taxonomy assignment to generage annotation file
```
$ assign_taxonomy.py -i fasta.fa
```
3. (option) Abundance file

##Makee tree with guide file

### TaxonToGuide.py
```
python TaxonToGuide.py rep_set_tax_assignments.txt output.txt
```

After this, you can make a tree

```
graphlan_annotate.py --annot anno.txt guide.txt RefSoilGuide.xml
graphlan.py RefSoilGuide.xml RefSoilGuide.png --dpi 300 --size 15 --pad 0.6
```

## Make tree with tree file (.dnd or .xml)

### MakeAnno.py
This script make an annotation file that is colored by 'class'
```
python MakeAnno.py rep_set_tax_assignments.txt Default.txt anno.txt
```

### MakeAnnoXML.py

This script make annotation file for each end of clade with ID

```
python MakeAnnoXML.py rep_set_tax_assignments.txt DefaultAnno.txt annoXML.txt
```

### AbundanceCounting.py
This script make aboundance file from blast result and Abundance of OTU

To run, you need 

1. blast result
```
$ cat blastResultFile.txt | cut -f2 -s > otu.txt
```
2. otu count file (ex. full_emp_table_w_tax.hdf5.summary)

then,
```
bash GrepFromFile.sh otu.txt full_emp_table_w_tax.hdf5.summary > grepbash.sh
bash grepbash.sh
python AbundanceCounting.py blastResultFile.txt out abunTable.txt
```

Tip,

you can blast in this way:
```
blastn -db EMP -query fasta.fa -out result.txt -outfmt6
g++ DownstreamBlast.cpp -o DownstreamBlast
./Get_best_hit_blast_tabular/DownstreamBlast result.txt blastResultFile.txt
cat blastResultFile.txt | cut -f2 -s > otu.txt
```

FYI, Tools for make a tree file:

1. clustalo

2. Qiime (fasttree)

3. MEGA

Tools for visualizing a tree

1. Graplan

2. Tol (tree of life)

3. MEGA

4. FigTree