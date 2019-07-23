import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class SpamFarm {
	
	String inputFile;
	int target;
	
	public SpamFarm(String fileName, int target)
	{
		this.inputFile = fileName;
		this.target = target;
	}
	
	//writes to fileName
	public void CreateSpam(String fileName) throws IOException
	{
		Scanner inFile = new Scanner(new File(inputFile));
		PrintWriter outFile = new PrintWriter(new FileWriter(fileName));
		
		int N = Integer.parseInt(inFile.nextLine());
		int newN = (int) (N + Math.floor(N/10));
		
		outFile.println(newN);
		
		//copy the original edges
		while(inFile.hasNextLine())
			outFile.println(inFile.nextLine());

		//add new edges
		for(int i = N+1; i <= newN; i++)
		{
			//from new page i to the target 
			outFile.println(i + " " + target);
		}
		
		inFile.close();
		outFile.close();
		
	}
}
