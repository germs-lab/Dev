//This script makes subset of rep_set.fna 
// Note: Fna file should have one line of sequences each
// usage:  g++ BuildRepSet.cpp -o BuildRepSet
// ./BuildRepSet input1 input2 output
// example: ./BuildRepSet rep_set.fna ID.txt subset_rep_set.fna
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <dirent.h>
#include <vector>
#include <sstream>

using namespace std;

int main(int argc, char *argv[])
{
int checkFile(ifstream &input); 
int fileToDataAllLine (string filenameDIR,vector <vector <string> > &data);
void printMatrix(vector <vector <string> > &dad);

//check if the command correct
if (argc!=4){
	cout<<"usage: ./BuildRepSet input1 input2 output"<< endl <<flush;
	return 1;
}

//read rep_set.fna file
string filename = argv[1];
vector <vector <string> > data1;
fileToDataAllLine(filename,data1);

//file for result
ofstream myfile;
myfile.open (argv[3]);

//open file: your ID file
ifstream inputTable;
inputTable.open(argv[2]);
checkFile(inputTable);
string table;

while(getline(inputTable,table))
{
	//cout<<table<<endl<<flush;	
	for (int i=0;i<data1.size();i++){
		if(table == data1[i][0].substr(1,table.length())){
			myfile<<data1[i][0]<<endl<<flush;
			myfile<<data1[i+1][0]<<endl<<flush;
			break;
		}//if
	}//for
}//while

return 0;
}
//this is end of main

// check openfile
int checkFile(ifstream &input)
{
	if(input.fail()){                           //    Check open
       cerr << "Can't open file\n";
       exit(EXIT_FAILURE);
       //return 1;
	}else{return 0;}
}

//file contents to data-vector
int fileToDataAllLine (string filenameDIR,vector <vector <string> > &data){
	char const* fin = filenameDIR.c_str();
	ifstream input;
	string s;
	input.open(fin);
	checkFile(input);
	while(getline(input,s))
	{
		vector <string> record;
		record.push_back(s);
		data.push_back(record);
	}//while
	input.close();
	return 0;
}

void printMatrix(vector <vector <string> > &dad){
	for (int i=0;i<dad.size();i++){
		for (int j=0;j<dad[i].size();j++){
			cout<<dad[i][j]+" "<<flush;
		}
	cout<<endl<<flush;
	}
}