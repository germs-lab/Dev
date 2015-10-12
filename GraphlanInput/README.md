# Graplan

Graplan is a program that help you to draw a tree. [Here is the Graplan website](http://segatalab.cibio.unitn.it/tools/graphlan/).
You can download the program [here](https://bitbucket.org/nsegata/graphlan/src/c93d0d3739e6?at=default). To download and install

```
$ hg clone https://hg@bitbucket.org/nsegata/graphlan
$ export PATH='pwd'/graphlan/:$PATH
```
Note: 'pwd' means where you download the program.

There is the [tutorial](https://bitbucket.org/nsegata/graphlan/wiki/Home).

This repository have scripts can generate input file for Graplan

## Basic of Graplan

To draw a tree with Graplan, you will need following:

* Tree file (.dnd, .xml or guide) - Requied

Using [ClustalO](http://www.clustal.org)
```
$ clustalo -i fasta.fa --guidetree-out=treefilename.dnd
```
* (option) Taxonomy assignment to generage annotation file - This option make tree more informative.

Using [Qiime](http://qiime.org)
```
$ assign_taxonomy.py -i fasta.fa
```
* (option) Abundance file

The scripts below help you to write annotation file that add taxomony information and abundance on the tree.

## Make tree with tree file (.dnd or .xml)

If you have a tree file, you can draw the tree with following: 
```
graphlan.py RefSoil16sHMMFastaNS.dnd RefSoilPlain.png 
```

Now, let's add more information on the tree. We can add taxonomy information. Let's put color by class.
### MakeAnno.py
This script make an annotation file that is colored by 'class'
```
python MakeAnno.py RefSoil16sHMMFastaNS_tax_assignments.txt anno.txt
```

### MakeAnnoXML.py

This script make annotation file for each end of clade with ID

```
python MakeAnnoXML.py rep_set_tax_assignments.txt annoXML.txt
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

### MakeAnno_w_ring.py
This script make annotation file with abundance

```
python MakeAnno_w_ring.py Refsoil16scompRe_tax_assignments.txt DefaultAnno.txt Annotation.txt
```

### log transformation

```
python LogTransform.py abunTable.txt abunTable.log.txt
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


```
graphlan_annotate.py --annot anno.txt guide.txt RefSoilGuide.xml
graphlan.py RefSoilGuide.xml RefSoilGuide.png --dpi 300 --size 15 --pad 0.6 --external_legends
```

### Finally, make a tree
```
export PATH=~/graphlan:$PATH
graphlan_annotate.py --annot anno.txt guide.txt RefSoilGuide.xml
graphlan.py RefSoilGuide.xml RefSoilGuide.png --dpi 300 --size 15 --pad 0.6 --external_legends
```

##Makee tree with guide file

### TaxonToGuide.py
```
python TaxonToGuide.py rep_set_tax_assignments.txt output.txt
```

After this, you can make a tree

```
graphlan_annotate.py --annot anno.txt guide.txt RefSoilGuide.xml
graphlan.py RefSoilGuide.xml RefSoilGuide.png --dpi 300 --size 15 --pad 0.6