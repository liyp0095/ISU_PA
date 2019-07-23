import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;

public class MyWikiRanker {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

//		String fileName = "b.txt";
		String fileName = "a500.txtnum.txt";
		double[] eplison = {0.01, 0.005, 0.001};
		double[] deta = {0.85, 0.85, 0.85};
		
		System.out.print("first: ");
		PageRank pageRank1 = new PageRank(fileName, eplison[0], deta[0]);
		System.out.print("second: ");
		PageRank pageRank2 = new PageRank(fileName, eplison[1], deta[1]);
		System.out.print("third: ");
		PageRank pageRank3 = new PageRank(fileName, eplison[2], deta[2]);
		
		int k = 10;
		
		int[] A = pageRank1.topKOutDegree(k);
		System.out.println("A : top " + k + " outdegree");
		for(int i = 0; i < k; i ++)
			System.out.println(A[i]);
		System.out.println("-------------------");
		
		int[] B = pageRank1.topKInDegree(k);
		System.out.println("B : top " + k + " indegree");
		for(int i = 0; i < k; i ++)
			System.out.println(B[i]);
		System.out.println("-------------------");
		
		int[] C = pageRank1.topKPageRank(k);
		System.out.println("C: top " + k + " page ranks with eplison = " + eplison[0] + ", deta = " + deta[0]);
		for(int i = 0; i < k; i ++)
			System.out.println(C[i]);
		System.out.println("-------------------");
		
		int[] D = pageRank2.topKPageRank(k);
		System.out.println("D: top " + k + " page ranks with eplison = " + eplison[1] + ", deta = " + deta[1]);
		for(int i = 0; i < k; i ++)
			System.out.println(D[i]);
		System.out.println("-------------------");
		
		int[] E = pageRank3.topKPageRank(k);
		System.out.println("E: top " + k + " page ranks with eplison = " + eplison[2] + ", deta = " + deta[2]);
		for(int i = 0; i < k; i ++)
			System.out.println(E[i]);
		System.out.println("-------------------");
		
		int[][] temp = {A, B, C, D, E};
		
		for(int i = 0; i < temp.length; i++)
			for(int j = i+1; j < temp.length; j++)
			{
				char first = (char) (i + 'A');
				char second = (char) (j + 'A');
				System.out.println("Jac(" + first + ", " + second + ") = " + JaccardSimilarity(temp[i], temp[j]));
			}
		
		System.out.println("-------------------");
		int minNode = pageRank1.getMinPRNode();
		System.out.println("Vertex " + minNode + " has the min page rank" );
		System.out.println("The page rank is " + pageRank1.pageRankOf(minNode));
		
		
	}
	
	public static double JaccardSimilarity(int[] a, int[] b)
	{	
		int sum = 0;
		int common = 0;
		
		for(int i = 0; i < a.length; i++)
			for(int j = 0; j < b.length; j++)
			{
				if(a[i] != 0 && b[j] != 0 && a[i] == b[j])
				{
					common ++;
					break;
				}
			}
		
		sum = a.length + b.length - common;
		
		return (double) common/sum;
	}

}
