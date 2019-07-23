import java.io.IOException;
import java.util.ArrayList;

public class TestLSH {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		String folderName = "data//F17PA2";
//		String folderName = "data//space";
		int numPermutaiton = 800;
		double s = 0.9;
		NearDuplicates nearDuplicates = new NearDuplicates(folderName, numPermutaiton, s);
		
		String[] docNames = {"baseball50.txt","baseball150.txt","baseball250.txt",
				"baseball350.txt","baseball450.txt","hockey50.txt",
				"hockey150.txt", "hockey250.txt", "hockey350.txt","hockey450.txt"};
		
		//String[] docNames = {"baseball1.txt","baseball10.txt","baseball20.txt","baseball30.txt","baseball40.txt","baseball50.txt"};
//		String[] docNames = {"space-0.txt","space-1000.txt","space-200.txt" };

		for(int i = 0; i<docNames.length; i++)
		{
			String docName = docNames[i];
			ArrayList<String> result = nearDuplicates.nearDuplciateDetector(docName);
			System.out.println("-----------------------------------");
			System.out.println("Near Duplicates Of " + docName);
			System.out.println();
			for(int j = 0; j < result.size(); j++)
				System.out.println(result.get(j));
		}
		

	}

}
