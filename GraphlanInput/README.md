# Graplan

Graplan is a program that help you to draw a tree. [Here is the Graplan website](http://segatalab.cibio.unitn.it/tools/graphlan/).
You can download the program [here](https://bitbucket.org/nsegata/graphlan/src/c93d0d3739e6?at=default). To download and install

```
$ hg clone https://hg@bitbucket.org/nsegata/graphlan
$ export PATH='pwd'/graphlan/:$PATH
```
Note: 'pwd' means where you download the program.

For example, if I install graphlan on my home directory, path will be:
```
$ export PATH=~/graphlan/:$PATH
```
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
#### Step 1: Make tree with plain tree file
If you have a tree file, you can draw the tree with following: 
```
graphlan.py RefSoil16sHMMFastaNS.dnd RefSoilPlain.png 
```

Now, let's add more information on the tree. We can add taxonomy information. Let's put color by class.

#### Step 2: Add color of taxonomy
### MakeAnno_no_ring.py
This script make an annotation file that is colored by 'Phylum'

```
python MakeAnno_no_ring.py RefSoil16sHMMFastaNS_tax_assignments.txt Annotation_no_ring.txt
```
To run Graphlan
```
graphlan_annotate.py --annot Annotation_no_ring.txt RefSoil16sHMMFastaNS.dnd RefSoil_no_ring.xml
graphlan.py RefSoil_no_ring.xml RefSoil_no_ring.png --dpi 300 --size 15 --pad 0.6
```
#### Step 3: Add ring
You need a file 'abuntTable.txt'. The file is provided here, but there is a description how I made this file bellow (AbundanceCounting.py)

### MakeAnno_w_ring.py
This script make annotation file with abundance

```
python MakeAnno_w_ring.py RefSoil16sHMMFastaNS_tax_assignments.txt abunTable.txt Annotation_w_ring.txt
```
Then, run
```
graphlan_annotate.py --annot Annotation_w_ring.txt RefSoil16sHMMFastaNS.dnd RefSoil_w_ring.xml
graphlan.py RefSoil_w_ring.xml RefSoil_w_ring.png --dpi 300 --size 15 --pad 0.6 --external_legends
```


### (option) log transformation
If you compare big numbers, it is resonable to use log scale.
```
python LogTransform.py abunTable.txt abunTable.log.txt
```
Then,
```
python MakeAnno_w_ring.py RefSoil16sHMMFastaNS_tax_assignments.txt abunTable.log.txt Annotation_w_ring.log.txt
graphlan_annotate.py --annot Annotation_w_ring.log.txt RefSoil16sHMMFastaNS.dnd RefSoil_w_ring.log.xml
graphlan.py RefSoil_w_ring.log.xml RefSoil_w_ring.log.png --dpi 300 --size 15 --pad 0.6 --external_legends
```
### (option) Add more rings
You can add additional rings. The script write additional annotation file from abundance file.

```
python MakeAbunRing.py SoilAbundance.txt SoilAbunAnno.txt
```
Then, you can add additional annotation into annotated XML file
```
graphlan_annotate.py --annot SoilAbunAnno.txt RefSoil_w_ring.log.xml RefSoil_w_additional_ring.xml
graphlan.py RefSoil_w_additional_ring.xml RefSoil_w_add_ring.png --dpi 300 --size 15 --pad 0.6 --external_legends
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
python TaxonToGuide.py rep_set_tax_assignments.txt EMP_soil.guide.txt
python MakeAnnoGuide_no_ring.py RefSoil16sHMMFastaNS_tax_assignments.txt anno.guide.txt
```
If you want to add ring,
```
python MakeAnnoGuide_w_ring_SingleCell.py RefSoil16sHMMFastaNS_tax_assignments.txt singlecell.txt anno.guide.ring.txt
```

After this, you can make a tree

```
graphlan_annotate.py --annot anno.guide.txt EMP_soil.guide.txt RefSoilGuide.xml
graphlan.py RefSoilGuide.xml RefSoilGuide.png --dpi 300 --size 15 --pad 0.6 --external_legends
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

## Example1: RefSoil tree
You need 16s file, here is the description how to get 16s sequences. https://github.com/germs-lab/ref_soil

### step1: Alignment using infernal with RDP's bacterial model
```
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/cmalign bacteria_model.cm RefSoil16sGenbank_HMM_clean.fa > RefSoil_bac_ali.sto
$ ~/infernal-1.1.1-linux-intel-gcc/binaries/esl-reformat afa RefSoil_bac_ali.sto > RefSoil_bac_ali.afa
```
### step2: build tree using Fasttree
```
$ wget http://www.microbesonline.org/fasttree/FastTree
$ chmod 655 FastTree
$ ./FastTree -nt < RefSoil_bac_ali.afa > RefSoil_bac.tree
```
### step3: plot tree using Graphlan
This step add color for phylum
```
python MakeAnno_RefSoil_no_ring.py RefSoil_v1.txt.split.bacteria.txt RefSoil_bacAnno.txt
graphlan_annotate.py --annot RefSoil_bacAnno.txt RefSoil_bac.tree step2.xml
```
This step add first ring
```
python MakeAnno_RefSoil_first_ring.py RefSoil_v1.txt.split.bacteria.txt RefSoilAnno_ring1.txt
graphlan_annotate.py --annot RefSoilAnno_ring1.txt step2.xml step3.xml
```
This step add legend
```
python MakeAnno_RefSoil_legend.py RefSoil_v1.txt.split.bacteria.txt legend_anno.txt
graphlan_annotate.py --annot legend_anno.txt step3.xml step4.xml
```
Finally generate tree figure
```
graphlan.py step4.xml step4.png --dpi 300 --size 15 --pad 0.6 --external_legends
```
## Example2: If you use RDP claassifier
Running RDP classifier
```
java -Xmx1g -jar ~/RDPTools/classifier.jar classify -o EMP_soil_RDP_taxonomy.txt -h EMP_soil_RDP_hier.txt JavaNewSoilRepSet.fna
```
You will have Taxonomy file

Then, make guide file
```
python rdp_to_guide.py EMP_soil_RDP_taxonomy.txt > EMP_soil_guide_uniq.txt
```
You are ready to draw tree

step1: plain tree
```
graphlan.py EMP_soil_guide_uniq.txt EMP.step1.png --dpi 300 --size 15 --pad 0.6
```
step2: add color for phylum
Make annotation file
```
python MakeAnno_rdp_guide.py EMP_soil_guide_uniq.txt EMP_soil_anno.txt
graphlan_annotate.py --annot EMP_soil_anno.txt EMP_soil_guide_uniq.txt EMP_step2.xml
graphlan.py EMP_step2.xml EMP.step2.png --dpi 300 --size 15 --pad 0.6
```
step3: add refsoil ring
```
python ../Dev/GraphlanInput/add_refsoil_ring.py RefSoil_guide_ar_bac.txt anno_step3.txt
graphlan_annotate.py --annot anno_step3.txt EMP_step2.xml EMP_step3.xml
graphlan.py EMP_step3.xml EMP_step3.png --dpi 300 --size 15 --pad 0.6
```
step4: add single cell ring
```
python ../Dev/GraphlanInput/Guide_Add_Ring_SingleCell.py /mnt/data2/jin_emp/emp/Dev/GraphlanInput/singlecell.unix.txt anno_step4.txt
graphlan_annotate.py --annot anno_step4.txt EMP_step3.xml EMP_step4.xml
graphlan.py EMP_step4.xml EMP.step4.png --dpi 300 --size 15 --pad 0.6
```