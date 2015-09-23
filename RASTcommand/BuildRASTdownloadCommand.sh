#bash
#usage: bash BuildRASTdownloadCommand.sh yourID password jobList2.txt
grep -B 1 complete $3 > completeList.txt
cat completeList.txt | cut -f1 -s | sed -n "p;N;" > completeJobID.txt

for line in $(cat completeJobID.txt);
do
    echo "~ubuntu/sas/bin/svr_retrieve_RAST_job $1 $2 $line rast_tarball > $line.tar.gz";
done > RASTdownloadCommand.sh


cat completeList.txt | cut -f3 -s | sed -n "p;N;" > completeTaxonID.txt

for line in $(cat completeTaxonID.txt);
do
    echo "~ubuntu/sas/bin/svr_subsystem_classification --c=1 < $line/Subsystems/bindings > $line/Subsystems/bindings.plus.SS_categories";
done > RASTclassification.sh


cat RASTdownloadCommand.sh | parallel

for x in *.gar.gz;
do tar -xvf $x;
done

cat RASTclassification.sh | parallel

for line in $(cat completeTaxonID.txt);
do
    cat $line/EC_numbers >> allEC_numbers;
done

