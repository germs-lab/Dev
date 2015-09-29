# Graplan Input

This script generate input file for Graplan

## TaxonToGuide.py
```
python TaxonToGuide.py rep_set_tax_assignments.txt output.txt
```

## MakeAnno.py
```
python MakeAnno.py rep_set_tax_assignments.txt anno.txt
```

## MakeAnnoXML.py

This script make annotation file for each end of clade with ID

```
python MakeAnnoXML.py rep_set_tax_assignments.txt annoXML.txt
```

## AbundanceCounting.py
This script make aboundance file from blast result and Abundance of OTU

```
bash GrepFromFile.sh otu.txt full_emp_table_w_tax.hdf5.summary > grepbash.sh
bash grepbash.sh
python AbundanceCounting.py refsoil.out.txt out abunTable.txt
```