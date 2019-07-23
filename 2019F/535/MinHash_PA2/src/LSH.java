import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LSH {
	
	int[][] minHashMatrix;
	String[] docNames;
	
	int bands;
	int r;
	int numPermutation;

	int hashTableSize;
	
	int sizeOfLastBand;
	
	ArrayList<String>[][] LSHMatrix;
	
	public LSH(int[][] minHashMatrix, String[] docNames, int bands)
	{
		this.minHashMatrix = minHashMatrix;
		this.docNames = docNames;
		
		//r = k/b
		this.bands = bands;
		numPermutation = minHashMatrix.length;
		
		
		r = numPermutation/bands;
		sizeOfLastBand = numPermutation - r*(bands-1);
		
		System.out.println("k = " + numPermutation);
		System.out.println("bands = " + bands);
		System.out.println("r = " + r);
		System.out.println("sizeOfLastBand = " + sizeOfLastBand);
		System.out.println();
		
		//size of each hash table = least prime that is greater than 4N
		hashTableSize = PreProcess.nextPrime(4 * docNames.length);

		LSHMatrix = new ArrayList[bands][hashTableSize];
		
		for(int i = 0; i < bands; i++)
			for(int j = 0; j < hashTableSize; j++)
				LSHMatrix[i][j] = new ArrayList<String>();
		
		//for each document, calculate the hash location using FNV for all bands
		for(int j = 0; j < docNames.length; j++)
		{
			for(int i = 0; i < bands; i++)
			{
				//string for i'th band  of j'th document
				String temp = getBandString(j, i);
				
				//System.out.println(temp);
				
				int location = hashFunction(temp);
				
				LSHMatrix[i][location].add(docNames[j]);
			}
			
			if(j %1000 ==0)
				System.out.println(j);
		}
		System.out.println("LSH Matrix completed.");
	}
	
	//get the string of i'th band of j'th document
	private String getBandString(int j, int i)
	{
		String temp = "";
		if(i != bands - 1)	//not the last band
			for(int k = 0; k < r; k++) {
				temp += minHashMatrix[k + i * r][j] + "$";
			}
		else	//it is the last band
			for(int k = 0; k < sizeOfLastBand; k++)
				temp += minHashMatrix[k+i*r][j] + "$";
		
		return temp;
	}
	
	public ArrayList<String> nearDuplicatesOf(String docName)
	{
		ArrayList<String> duplicates = new ArrayList<String>();
		
		List<String> docNamesList = Arrays.asList(docNames);
		int docNameIndex = docNamesList.indexOf(docName);
		
		//find location in each band
		for(int i = 0; i < bands; i++)
		{
			//string for i'th band 
			String temp = getBandString(docNameIndex, i);
			
			int location = hashFunction(temp);
			
			for(int j = 0; j < LSHMatrix[i][location].size(); j++)
			{
				String tempDoc = LSHMatrix[i][location].get(j);
				if(!tempDoc.equals(docName) && !duplicates.contains(tempDoc))
					duplicates.add(tempDoc);
			}
		}

		return duplicates;
	}
	
	//FNV
	 public int hashFunction(String s){
	    	
	 	BigInteger FNV64Prime = new BigInteger("1099511628211");
	    BigInteger FNV64Init = new BigInteger("14695981039346656037");
	    
        BigInteger offset_basis = FNV64Init;
        BigInteger hash = offset_basis;
        
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            hash = hash.xor(BigInteger.valueOf((long)c));
            hash = (hash.multiply(FNV64Prime)).mod (new BigInteger("2").pow(64));
        }
        return hash.mod(BigInteger.valueOf((long)hashTableSize)).intValue();
    }
	 
}
