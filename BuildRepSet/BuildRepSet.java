//
import java.io.*;
import java.util.*;

class BuildRepSet {
    public static void main(String[] args) {
	try{  
	    if (args.length != 3) {
	    System.err.println("usage: java BuildRepSet rep_set.fna ID.txt result_rep_set.fna "+ "");
	    System.exit(0);
	    }

	    String RepSet = args[0];
	    String IDs = args[1];
	    String resultFile = args[2];

	    PrintStream resultOut = new PrintStream(resultFile);
	    File file2 = new File(IDs);
	    Scanner scanner2 = new Scanner(file2);
	    Vector<String> v = new Vector<String>();
	    while (scanner2.hasNextLine()){
		v.add(scanner2.nextLine());
	    }
	    scanner2.close();
	    File file1 = new File(RepSet);
	    Scanner scanner1 = new Scanner(file1);
	    while (scanner1.hasNextLine()){
		String line = scanner1.nextLine();
		String[] parts = line.split(" ");
		String temp = parts[0].substring(1,parts[0].length());
		if (v.contains(temp)){
		    resultOut.println(line);
		    resultOut.println(scanner1.nextLine());
		}else{
		    scanner1.nextLine();
		}

	    }


	    v.removeAllElements();

	    


	} catch (FileNotFoundException e) {
	    e.printStackTrace();
	}
    }
}