#bash
#usage: bash GrepFromFile.sh listfile file
for line in $(cat $1);
do
    echo "grep ^' $line:' $2 >> out";
done