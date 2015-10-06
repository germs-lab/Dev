//This script makes subset of rep_set.fna 
// Note: Fna file should have one line of sequences each
// usage:  g++ BuildRepSetv2.cpp -o BuildRepSetv2
// ./BuildRepSetv2 input1 input2 output
// example: ./BuildRepSetv2 rep_set.fna ID.txt subset_rep_setv2.fna
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
  int ReadVector (string filenameDIR,vector <string> &data);
  void printMatrix(vector <string>  &dad);

  //check if the command correct
  if (argc!=4){
    cout<<"usage: ./BuildRepSet input1 input2 output"<< endl <<flush;
    return 1;
  }

  //read ID
  string filename = argv[2];
  vector <string>  data1;
  ReadVector(filename,data1);

  //file for result
  ofstream myfile;
  myfile.open (argv[3]);

  //now read file
  ifstream inputTable;
  inputTable.open(argv[1]);
  checkFile(inputTable);
  string table;
  while(getline(inputTable,table))
    {
      istringstream ss (table);
      vector <string> record;
      while (ss)
	{
	  string s1;
	  if(!getline(ss,s1,' ')) break;
	  if(s1!=""){
	    record.push_back(s1);
	  }
	}
      
      if (find(data1.begin(),data1.end(),record[0].substr(1,record[0].size()))!= data1.end()){
	  cout<<table<<endl<<flush;
	  getline(inputTable,table);
	  cout<<table<<endl<<flush;
      }else{
	getline(inputTable,table);
      }
    }
  inputTable.close();
  

  return 0;
}


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
int ReadVector (string filenameDIR,vector <string>  &data){
  char const* fin = filenameDIR.c_str();
  ifstream input;
  string s;
  input.open(fin);
  checkFile(input);
  while(getline(input,s))
    {
      data.push_back(s);
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
