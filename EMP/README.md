# EMP

This scripts help to convert EMP full table into soil specific

## full table to soil table
EMPsubsample.py

#usage: python EMPsubsample.py input input_to_remove output

```
python EMPsubsample.py ../EMPsampleInfoMerge/EMP_10k_merged_mapping_final.txt IDtoRemoveUnix.txt EMPsubSoilMapping.txt
```

## Soil table to each different soil enviromental matter
ENV_matter.py 

#usage: python ENV_matter.py input

```
python ENV_matter.py EMPsubSoilMapping.txt
```