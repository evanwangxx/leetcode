/*
Data Structure - Homework 3
Programming Problem_2
*/

import java.util.Scanner;
import java.io.*;


public class Problem2{

	public static void main(String [] args){

		try{

			BufferedReader br = new BufferedReader(new FileReader(args[0])); 

            String lineread;
            String[] wordList;
            AvlTree<String> tree = new AvlTree<>();
            
            
            int lineCount = 1;      // start from 1
			while((lineread = br.readLine()) != null){
                
                String linereadRemovePunctions = lineread.replaceAll("\\p{P}", "");
                wordList = linereadRemovePunctions.split("\\s+");                                   // one or many whitespaces
                
                for(int i = 0; i <= wordList.length - 1; i++){
                	
                	tree.indexWord(wordList[i].replace("\\n",""), lineCount);
                }
                lineCount++;
            }

        br.close();
        tree.printIndex();

		} catch(IOException error){
			System.out.println(error.getMessage());
		}
	}

}
