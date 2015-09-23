#bash
#usage: bash BuildRASTdownloadCommand.sh yourID password jobList2.txt
grep -B 1 complete $3 > completeList.txt
cat completeList.txt | cut -f1 -s | sed -n "p;N;" > completeJobID.txt

for line in $(cat completeJobID.txt);
do
    echo "~ubuntu/sas/bin/svr_retrieve_RAST_job $1 $2 $line rast_tarball > $line.tar.gz";
done > RASTdownloadCommand.sh