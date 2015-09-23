#this script deal with erroed job in RAST
#usage: bash RASTdeleteCommand.sh RASTID RASTpassword JobList OriginalUploadingcommand
#example: bash RASTdeleteCommand.sh yourID password jobList.txt RASTcommand.sh

#copy and paste joblist then save as jobList.txt

#get List of taxon ID has error
grep -B 1 error $3 > errorList.txt
cat errorList.txt |cut -f3 -s|sed -n "p;N;"|cut -f1 -s -d '.' > errorTaxon.txt

#get jobID has error
grep -f errorTaxon.txt $3 | cut -f1 > errorJobID.txt

#make sh for deleting
for line in $(cat errorJobID.txt);                                                                                                                              
do                                                                                                                                                                
    echo "~ubuntu/sas/bin/svr_delete_RAST_job $1 $2 $line" ;                                                                                                    
done > jobDelete.sh 

#make sh for adding
grep -f errorTaxon.txt $4 > jobAdd.sh

#remove temporary files
rm errorList.txt errorTaxon.txt errorJobID.txt