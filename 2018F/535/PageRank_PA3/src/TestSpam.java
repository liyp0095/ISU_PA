import java.io.IOException;

public class TestSpam {
	
	public static void main(String[] args) throws IOException {
		
		//SpamFarm(input file name, vertex you wish to increase)
//		SpamFarm sp = new SpamFarm("b.txt",2);
		SpamFarm sp = new SpamFarm("a500.txtnum.txt", 2);
		
		//output file name
		sp.CreateSpam("c.txt");
	}

}
