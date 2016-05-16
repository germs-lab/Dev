//
import java.io.*;
import java.util.*;
import java.util.HashSet;

class BuildRepSet2 {
    public static void main(String[] args) {
	try{ 
		//argument check 
	    if (args.length != 3) {
	    System.err.println("usage: java BuildRepSet2 ID.txt rep_set.fna result_rep_set.fna "+ "");
	    System.exit(0);
	    }
		//get two files
		File idFile = new File(args[0]);
		File seqFile = new File(args[1]);

		//if argument are 3, remove
		
		//store ID in HashSet <- this is the reason make it faster
		Set<String> ids = new HashSet<String>();


	    //result file
	    String resultFile = args[2];
	    PrintStream resultOut = new PrintStream(resultFile);
	    
	    //read ID file
	    Scanner idFile1 = new Scanner(idFile);
	    //Vector<String> v = new Vector<String>();
	    while (idFile1.hasNextLine()){
			ids.add(idFile1.nextLine());
	    }
	    idFile1.close();
	    //read rep_set file and write
	   
	    Scanner seqFile1 = new Scanner(seqFile);
	    while (seqFile1.hasNextLine()){
		String line = seqFile1.nextLine();
		String[] parts = line.split(" ");
		String temp = parts[0].substring(1,parts[0].length());
			if (ids.contains(temp)){
		    	resultOut.println(line);
		    	resultOut.println(seqFile1.nextLine());
			}else{
		    	seqFile1.nextLine();
			}

	    }//end while

	   // v.removeAllElements();
	} catch (FileNotFoundException e) {
	    e.printStackTrace();
	}//end try
    }
}