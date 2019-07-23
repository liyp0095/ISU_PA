import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

//implement it as random walk
public class PageRank {

	private Page[] graph;		//graph G
	
	private int numEdges;		//number of edges
	private int N;				//number of nodes
	
	private double[] ranks;		//page rank
	
	double epsilon;				//approximation parameter
	double beta;				//teleportation parameter

	//Constructor
	public PageRank(String fileName, double epsilon, double beta) throws IOException
	{
		Scanner inFile = new Scanner(new File(fileName));
		
		this.epsilon = epsilon;
		this.beta = beta;
		
		//number of nodes in total
		
		N = inFile.nextInt();
		numEdges = 0;
		
		//initialize graph
		graph = new Page[N];
		
		for(int i = 0; i < N; i++)
			graph[i] = new Page(i+1);
		
		//add all edges
		while(inFile.hasNextInt())
		{
			int fromPage = inFile.nextInt();
			int toPage = inFile.nextInt();
			graph[fromPage].addChild(graph[toPage]);
			numEdges ++;
		}
		
		//initialize ranks
		ranks = new double[N];
		
		for(int i = 0; i < N; i++)
			ranks[i] = (double)1/N;
		
		
		
		//printRanks();
		
		
		boolean converged = false;
		
		int count = 0;
		
		while(!converged)
		{	
			double[] nextRanks = getNextRanks(ranks);
			
			if(getNorm(ranks, nextRanks) <= epsilon)
				converged = true;
			
			ranks = nextRanks;
			//printRanks();
			count ++;
		}
		
		System.out.println("converge after " + count + " iterations");
		//printRanks();
		
	}
	
	//get next page ranks
	private double[] getNextRanks(double[] currentRanks)
	{
		double[] nextRanks = new double[N];
		
		for(int i = 0; i < N; i++)
			nextRanks[i] = (double)(1-beta)/N;
		
		//for every node in the graph
		for(int i = 0; i < N; i++)
		{
			Page page = graph[i];
			
			//contains children
			if(page.getOutdegree() != 0)
			{
				//for every child of the current page
				for(int j = 0; j < page.getOutdegree(); j++)
				{
					int childPage = page.getChildNameAt(j);
					nextRanks[childPage-1] += beta * (currentRanks[page.getName()-1]/page.getOutdegree());
				}
			}
			else		//do not have children
			{
				//for every page in graph
				for(int j = 0; j < N; j++)
					nextRanks[j] += beta * (currentRanks[page.getName()-1]/N);
			}
		}
		
		return nextRanks;
		
	}
	
	//Norm(M) as sum absolute values of all entries of M
	//return Norm(ranks1 - ranks2)
	private double getNorm(double[] ranks1, double[] ranks2)
	{
		double result = 0;
		
		for(int i = 0; i < N; i++)
			result += Math.abs(ranks1[i] - ranks2[i]);
		
		return result;
	}
	
	public double pageRankOf(int vertex)
	{
		return ranks[vertex-1];
	}
	
	public int outDegreeOf(int vertex)
	{
		return graph[vertex-1].getOutdegree();
	}
	
	public int inDegreeOf(int vertex)
	{
		return graph[vertex-1].getIndegree();
	}
	
	public int numEdges()
	{
		return numEdges;
	}
	
	public int[] topKPageRank(int k)
	{
		ArrayList<Page> nodes = new ArrayList<Page>();
		
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < k; j++)
			{
				if(j >= nodes.size() || ranks[i] > ranks[nodes.get(j).getName()-1])
				{
					nodes.add(j, graph[i]);
					break;
				}
			}
		}
		
		
		int[] result = new int[k];
		
		int min = Math.min(k, nodes.size());
		
		for(int i = 0; i < min; i++)
			result[i] = nodes.get(i).getName();
		
		return result;
	}
	
	public int[] topKInDegree(int k)
	{
		ArrayList<Page> nodes = new ArrayList<Page>();
		
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < k; j++)
			{
				if(j >= nodes.size() || graph[i].getIndegree() > nodes.get(j).getIndegree())
				{
					nodes.add(j, graph[i]);
					break;
				}
			}
		}
		
		
		int[] result = new int[k];
		
		int min = Math.min(k, nodes.size());
		
		for(int i = 0; i < min; i++)
			result[i] = nodes.get(i).getName();
		
		return result;
	}
	
	public int[] topKOutDegree(int k)
	{
		ArrayList<Page> nodes = new ArrayList<Page>();
		
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < k; j++)
			{
				if(j >= nodes.size() || graph[i].getOutdegree() > nodes.get(j).getOutdegree())
				{
					nodes.add(j, graph[i]);
					break;
				}
			}
		}
		
		
		int[] result = new int[k];
		
		int min = Math.min(k, nodes.size());
		
		for(int i = 0; i < min; i++)
			result[i] = nodes.get(i).getName();
		
		return result;
	}
	
	public int getMinPRNode()
	{
		int result = -1;
		double minValue = Double.MAX_VALUE;
		for(int i =0; i<ranks.length; i++)
			if(ranks[i] < minValue)
			{
				result = i;
				minValue = ranks[i];
			}
		return result+1;
	}
	
	public void printRanks()
	{
		System.out.println("----------------------------");
		for(int i = 0; i < N; i++)
			System.out.println((i+1) + ": " + ranks[i]);
		System.out.println("----------------------------");
	}
	
}
