
import java.io.IOException;

public class TestPageRank {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		//String fileName = "c.txt";
		String fileName = "a500.txtnum.txt";
		double eplison = 0.01;
		double deta = 0.85;
		
		PageRank pageRank = new PageRank(fileName, eplison, deta);
		
		int page = 2;
		System.out.println("-------------------");
		System.out.println("page rank of " + page + ": " + pageRank.pageRankOf(page));
		System.out.println("indegree of " + page + ": " + pageRank.inDegreeOf(page));
		System.out.println("outdegree of " + page + ": " + pageRank.outDegreeOf(page));
		System.out.println("Number of edges: " + pageRank.numEdges());
		System.out.println("-------------------");
		
		int k = 2;
		int[] topK = pageRank.topKPageRank(k);
		System.out.println("top " + k + " page ranks:");
		for(int i = 0; i < k; i ++)
			System.out.println(topK[i]);
		System.out.println("-------------------");
		
		topK = pageRank.topKInDegree(k);
		System.out.println("top " + k + " indegree::");
		for(int i = 0; i < k; i ++)
			System.out.println(topK[i]);
		System.out.println("-------------------");
		
		topK = pageRank.topKOutDegree(k);
		System.out.println("top " + k + " outdegree::");
		for(int i = 0; i < k; i ++)
			System.out.println(topK[i]);
		System.out.println("-------------------");
	}

}
