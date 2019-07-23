import java.util.ArrayList;

//represents graph
public class Page {
	private int name;
	private int indegree;
	private int outdegree;
	private ArrayList<Page> children;
	
	public Page(int name){
		indegree = 0;
		outdegree = 0;
		children = new ArrayList<Page>();
		this.name = name;
	}
	
	public void addChild(Page node)
	{	
		children.add(node);
		outdegree ++;
		node.addIndegree();
	}
	
	public int getName(){
		return name;
	}
	
	public int getChildNameAt(int index)
	{
		return children.get(index).getName();
	}
	
	private void addIndegree()
	{
		indegree ++;
	}
	
	public int getIndegree()
	{
		return indegree;
	}
	
	public int getOutdegree()
	{
		return outdegree;
	}
}
