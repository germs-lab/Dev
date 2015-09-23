# RAST command tool

this script help to make massive upload to RAST.

## GenbankToUploadCommand.py

usage:

```
python GenbankToUploadCommand.py genbankfilename yourID yourPassword
```

for massive upload,:

```
for x in *.gbk;do python GenbankToUploadCommand.py $x yourID Password;done
cat *.out > RASTupload.sh
cat RASTupload.sh | parallel
```

## RASTdeleteCommand.sh

if RAST shows error, you want to delete job then upload again. This script will generate two files: jobDelete.sh, jobAdd.sh

usage:

```
bash RASTdeleteCommand.sh yourID password jobList.txt RASTupload.sh
cat jobDelete.sh | parallel
cat jobAdd.sh | parallel
```

Note: This tutorial use parallel. To install; sudo apt-get install parallel

## svr_subsystem_classification

to use those file it shold be place in appropriate folder
sas/bin/svr_subsystem_classification
sas/plbin/svr_subsystem_classification.pl

change permission
chmod 755 svr_subsystem_classification