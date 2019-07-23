import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Scanner;

//converts string vertices to number vertices
public class Convert {

	public static void main(String[] args) throws IOException {
		
		HashMap hashmap = new HashMap();
		
		String inFileName = "a.txt";
		String outFileName = "b.txt";
		
		Scanner inFile = new Scanner(new File(inFileName));
		PrintWriter outFile = new PrintWriter(new FileWriter(outFileName));
		
		int count = 0;
		
		//number of vertices
		outFile.println(inFile.nextLine());
		
		while(inFile.hasNext())
		{
			String page1 = inFile.next();
			String page2 = inFile.next();
			
			if(!hashmap.containsKey(page1))
			{
				count ++;
				hashmap.put(page1, count);
			}
			
			if(!hashmap.containsKey(page2))
			{
				count ++;
				hashmap.put(page2, count);
			}
			
			outFile.println(hashmap.get(page1) + " " + hashmap.get(page2));
			
		}

		inFile.close();
		outFile.close();
	}

}
