import java.io.IOException;
import java.util.ArrayList;

public class NearDuplicates {
	
	LSH lsh;
	
	
	public NearDuplicates(String folder, int numPermutation, double s) throws IOException
	{
		MinHash minHash = new MinHash(folder, numPermutation);
		
		int[][] minHashMatrix = minHash.minHashMatrix();
		
		//calculate bands based on k and s
		int bands = getOptimalBands(numPermutation, s);
		
		lsh = new LSH(minHashMatrix, minHash.allDocs(), bands);
	}
	
	public ArrayList<String> nearDuplciateDetector(String docName)
	{
		return lsh.nearDuplicatesOf(docName);
	}
	
	public int getOptimalBands(int numPermutation, double s)
	{
		double optS = Double.MAX_VALUE;
		int optBands = -1;
		
		for(int bands = 1; bands < numPermutation; bands ++)
		{
			int r = numPermutation/bands;
			
			double tempS = Math.pow((double)1/bands, (double)1/r); 
			
			if(Math.abs(tempS-s) < Math.abs(optS-s))
			{
				optS = tempS;
				optBands = bands;
			}
		}
		
		System.out.println("optS " + optS);
		
		return optBands;
	}
}
