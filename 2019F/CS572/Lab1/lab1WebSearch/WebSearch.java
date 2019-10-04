import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.StringTokenizer;

import java.util.Collections;
import java.util.Comparator;


// You should call this code as follows:
//
//   java WebSearch directoryName searchStrategyName
//   (or jview, in J++)
//
//   where <directoryName> is the name of corresponding intranet
//   and <searchStrategyName> is one of {breadth, depth, best, beam}.

// The PARTIAL code below contains code for fetching and parsing
// the simple web pages we're using, as well as the fragments of
// a solution.  BE SURE TO READ ALL THE COMMENTS.

// Feel free to alter or discard whatever code you wish;
// the only requirement is that your main class be called WebSearch
// and that it accept the two arguments described above
// (if you wish you can add additional OPTIONAL arguments, but they
// should default to the values "hardwired" in below).

public class WebSearch
{
	static LinkedList<SearchNode> OPEN; // Feel free to choose your own data structures for searching,
	static HashSet<String> CLOSED;      // and be sure to read documentation about them.

	static final boolean DEBUGGING = false; // When set, report what's happening.
	// WARNING: lots of info is printed.

	static int beamWidth = 2; // If searchStrategy = "beam",
	// limit the size of OPEN to this value.
	// The setSize() method in the Vector
	// class can be used to accomplish this.

	static final String START_NODE     = "page1.html";

	// A web page is a goal node if it includes
	// the following string.
	static final String GOAL_PATTERN   = "QUERY1 QUERY2 QUERY3 QUERY4";

	public static void main(String args[])
	{
		if (args.length != 2)
		{
			System.out.println("You must provide the directoryName and searchStrategyName.  Please try again.");
		}
		else
		{
			String directoryName = args[0]; // Read the search strategy to use.
			String searchStrategyName = args[1]; // Read the search strategy to use.

			if (searchStrategyName.equalsIgnoreCase("breadth") ||
					searchStrategyName.equalsIgnoreCase("depth")   ||
					searchStrategyName.equalsIgnoreCase("best")    ||
					searchStrategyName.equalsIgnoreCase("beam"))
			{
				performSearch(START_NODE, directoryName, searchStrategyName);
			}
			else
			{
				System.out.println("The valid search strategies are:");
				System.out.println("  BREADTH DEPTH BEST BEAM");
			}
		}

		Utilities.waitHere("Press ENTER to exit.");
	}

	static void performSearch(String startNode, String directoryName, String searchStrategy)
	{
		int nodesVisited = 0;

		OPEN   = new LinkedList<SearchNode>();
		CLOSED = new HashSet<String>();

		OPEN.add(new SearchNode(startNode));

		while (!OPEN.isEmpty())
		{
			SearchNode currentNode = pop(OPEN);
			String currentURL = currentNode.getNodeName();

			nodesVisited++;

			// Go and fetch the contents of this file.
			String contents = Utilities.getFileContents(directoryName
					+ File.separator
					+ currentURL);

			if (isaGoalNode(contents))
			{
				// Report the solution path found
				// (You might also wish to write a method that
				// counts the solution-path's length, and then print that
				// number here.)
				currentNode.reportSolutionPath();
				break;
			}

			// Remember this node was visited.
			CLOSED.add(currentURL);

			addNewChildrenToOPEN(currentNode, contents, searchStrategy);

			// Provide a status report.
			if (DEBUGGING) System.out.println("Nodes visited = " + nodesVisited
					+ " |OPEN| = " + OPEN.size());
		}

		System.out.println(" Visited " + nodesVisited + " nodes, starting @" +
				" " + directoryName + File.separator + startNode +
				", using: " + searchStrategy + " search.");
	}

	// This method reads the page's contents and
	// collects the 'children' nodes (ie, the hyperlinks on this page).
	// The parent node is also passed in so that 'backpointers' can be
	// created (in order to later extract solution paths).
	static void addNewChildrenToOPEN(SearchNode parent, String contents, String searchStrategy)
	{
		// StringTokenizer's are a nice class built into Java.
		// Be sure to read about them in some Java documentation.
		// They are useful when one wants to break up a string into words (tokens).
		StringTokenizer st = new StringTokenizer(contents);
		LinkedList<SearchNode> topn = new LinkedList<>();

		while (st.hasMoreTokens())
		{
			String token = st.nextToken();

			// Look for the hyperlinks on the current page.

			// (Lots a print statments and error checks are in here,
			// both as a form of documentation and as a debugging tool should you
			// create your own intranets.)

			// At the start of some hypertext?  Otherwise, ignore this token.
			if (token.equalsIgnoreCase("<A"))
			{
				String hyperlink; // The name of the child node.

				if (DEBUGGING) System.out.println("Encountered a HYPERLINK");

				// Read: HREF = page#.html >

				token = st.nextToken();
				if (!token.equalsIgnoreCase("HREF"))
				{
					System.out.println("Expecting 'HREF' and got: " + token);
				}

				token = st.nextToken();
				if (!token.equalsIgnoreCase("="))
				{
					System.out.println("Expecting '=' and got: " + token);
				}

				// Now we should be at the name of file being linked to.
				hyperlink = st.nextToken();
				if (!hyperlink.startsWith("page"))
				{
					System.out.println("Expecting 'page#.html' and got: " + hyperlink);
				}

				token = st.nextToken();
				if (!token.equalsIgnoreCase(">"))
				{
					System.out.println("Expecting '>' and got: " + token);
				}

				if (DEBUGGING) System.out.println(" - found a link to " + hyperlink);

				//////////////////////////////////////////////////////////////////////
				// Have collected a child node; now have to decide what to do with it.
				//////////////////////////////////////////////////////////////////////

				if (alreadyInOpen(hyperlink))
				{ // If already in OPEN, we'll ignore this hyperlink
					// (Be sure to read the "Technical Note" below.)
					if (DEBUGGING) System.out.println(" - this node is in the OPEN list.");
				}
				else if (CLOSED.contains(hyperlink))
				{ // If already in CLOSED, we'll also ignore this hyperlink.
					if (DEBUGGING) System.out.println(" - this node is in the CLOSED list.");
				}
				else
				{ // Collect the hypertext if this is a previously unvisited node.
					// (This is only needed for HEURISTIC SEARCH, but collect in
					// all cases for simplicity.)
					String hypertext = ""; // The text associated with this hyperlink.

					do
					{
						token = st.nextToken();
						if (!token.equalsIgnoreCase("</A>")) hypertext += " " + token;
					}
					while (!token.equalsIgnoreCase("</A>"));

					if (DEBUGGING) System.out.println("   with hypertext: " + hypertext);

					//////////////////////////////////////////////////////////////////////
					// At this point, you have a new child (hyperlink) and you have to
					// insert it into OPEN according to the search strategy being used.
					// Your heuristic function for best-first search should accept as
					// arguments both "hypertext" (ie, the text associated with this
					// hyperlink) and "contents" (ie, the full text of the current page).
					//////////////////////////////////////////////////////////////////////

					// Technical note: in best-first search,
					// if a page contains TWO (or more) links to the SAME page,
					// it is acceptable if only the FIRST one is inserted into OPEN,
					// rather than the better-scoring one.  For simplicity, once a node
					// has been placed in OPEN or CLOSED, we won't worry about the
					// possibility of later finding of higher score for it.
					// Since we are scoring the hypertext POINTING to a page,
					// rather than the web page itself, we are likely to get
					// different scores for given web page.  Ideally, we'd
					// take this into account when sorting OPEN, but you are
					// NOT required to do so (though you certainly are welcome
					// to handle this issue).

					// HINT: read about the insertElementAt() and addElement()
					// methods in the Vector class.

					if (searchStrategy.equalsIgnoreCase("breadth")) {
						SearchNode searchNode = new SearchNode(hyperlink);
						searchNode.parent = parent;
						OPEN.addLast(searchNode);
					} else if (searchStrategy.equalsIgnoreCase("depth")) {
						SearchNode searchNode = new SearchNode(hyperlink);
						searchNode.parent = parent;
						OPEN.addFirst(searchNode);
					} else if (searchStrategy.equalsIgnoreCase("best")){
						SearchNode searchNode = new SearchNode(hyperlink, contents, GOAL_PATTERN, hypertext);
						searchNode.parent = parent;

						if (OPEN.size() == 0) {
							OPEN.add(searchNode);
						} else if (searchNode.getHvalue() < OPEN.peekLast().getHvalue()) {
							OPEN.addLast(searchNode);
						} else {
							for (int i = 0; i < OPEN.size(); i++) {
								if (searchNode.getHvalue() > OPEN.get(i).getHvalue()) {
									OPEN.add(i, searchNode);
									break;
								}
							}
						}
					} else if (searchStrategy.equalsIgnoreCase("beam")){
						SearchNode searchNode = new SearchNode(hyperlink, contents, GOAL_PATTERN, hypertext);
						searchNode.parent = parent;
						topn.add(searchNode);
					}
				}
			}
		}

		if (searchStrategy.equalsIgnoreCase("beam")) {
			// add topn to OPEN
			Collections.sort(topn, new Comparator<SearchNode>() {
				@Override
				public int compare(SearchNode s1, SearchNode s2) {
					if (s1.getHvalue() < s2.getHvalue()) {
						return 1;
					} else {
						return -1;
					}
				}
			});

			for (int i = 0; i < Math.min(topn.size(), beamWidth); i++) {
				// System.out.println(topn.get(i).getHvalue());
				// System.out.println(i);
				OPEN.add(topn.get(i));
			}

			Collections.sort(OPEN, new Comparator<SearchNode>() {
				@Override
				public int compare(SearchNode s1, SearchNode s2) {
					if (s1.getHvalue() < s2.getHvalue()) {
						return 1;
					} else {
						return -1;
					}
				}
			});
		}
	}

	// A GOAL is a page that contains the goalPattern set above.
	static boolean isaGoalNode(String contents)
	{
		return (contents != null && contents.indexOf(GOAL_PATTERN) >= 0);
	}

	// Is this hyperlink already in the OPEN list?
	// This isn't a very efficient way to do a lookup,
	// but its fast enough for this homework.
	// Also, this for-loop structure can be
	// be adapted for use when inserting nodes into OPEN
	// according to their heuristic score.
	static boolean alreadyInOpen(String hyperlink)
	{
		int length = OPEN.size();

		for(int i = 0; i < length; i++)
		{
			SearchNode node = OPEN.get(i);
			String oldHyperlink = node.getNodeName();

			if (hyperlink.equalsIgnoreCase(oldHyperlink)) return true;  // Found it.
		}

		return false;  // Not in OPEN.
	}

	// You can use this to remove the first element from OPEN.
	static SearchNode pop(LinkedList<SearchNode> list)
	{
		SearchNode result = list.removeFirst();




		return result;
	}
}

/////////////////////////////////////////////////////////////////////////////////

// You'll need to design a Search node data structure.

// Note that the above code assumes there is a method called getHvalue()
// that returns (as a double) the heuristic value associated with a search node,
// a method called getNodeName() that returns (as a String)
// the name of the file (eg, "page7.html") associated with this node, and
// a (void) method called reportSolutionPath() that prints the path
// from the start node to the current node represented by the SearchNode instance.
class SearchNode
{
	final String nodeName;
	SearchNode parent;
	String contents;
	double hValue;

	public SearchNode(String name) {
		nodeName = name;
	}

	public SearchNode(String name, String contents, String pattern, String hypertext) {
		nodeName = name;
		hValue = calculateHvalue(contents, pattern, hypertext);
	}

	public void reportSolutionPath() {
		SearchNode curNode = parent;
		String curName = nodeName;
		do {
			System.out.print(curName + "\t");
			curName = curNode.getNodeName();
			curNode = curNode.parent;
		} while (!curName.equalsIgnoreCase("page1.html"));
		System.out.println("page1.html");
	}

	public String getNodeName() {
		return nodeName;
	}

	public double getHvalue() {
		return hValue;
	}

	public double calculateHvalue(String contents, String pattern, String hypertext) {
		// Query words on page
		double score1 = getPageSimilarity(contents, pattern);
		// Query words in hypertext
		double score2 = getHyperLinkTermBagSimilarity(pattern, hypertext);
		// Consecutive similarity
		double score3 = getConsecutiveSimilarity(pattern, hypertext);
		// hypertext ranking
		double score4 = getPositionScore(contents, hypertext);

		return 0.2*score1 + 0.3*score2 + 0.8 * score3 + 0.2 * score4;
	}

	public double getPageSimilarity(String contents, String pattern) {
		String[] contentsList = contents.split("\\s");
		String[] patternList = pattern.split("\\s");
		double wordNum = 0.0;
		double queryNum = 0.0;

		for (int i = 0; i < contentsList.length; i++) {
			wordNum += 1;
			for (int j = 0; j < patternList.length; j++) {
				if (contentsList[i].equalsIgnoreCase(patternList[j])) {
					queryNum += 1;
				}
			}
		}
		return queryNum / wordNum;
	}

	public double getHyperLinkTermBagSimilarity(String pattern, String hypertext) {
		String[] hypertextList = hypertext.split("\\s");
		String[] patternList = pattern.split("\\s");
		double patternNum = 0.0;
		double queryNum = 0.0;

		for (int i = 0; i < patternList.length; i++) {
			patternNum += 1;
			for (int j = 0; j < hypertextList.length; j++) {
				if (patternList[i].equalsIgnoreCase(hypertextList[j])) {
					queryNum += 1;
				}
			}
		}
		return queryNum / patternNum;
	}

	public double getConsecutiveSimilarity(String pattern, String hypertext) {
		String[] hypertextList = hypertext.split("\\s");
		String[] patternList = pattern.split("\\s");
		double patternConsecutiveNum = 0.0;
		double hypertextConsecutiveNum = 0.0;
		HashSet<String> patternConsecutiveSet = new HashSet<>();

		for (int i = 0; i < patternList.length - 1; i++) {
			patternConsecutiveNum += 1;
			patternConsecutiveSet.add(patternList[i] + "-" + patternList[i+1]);
		}
		for (int i = 0; i < hypertextList.length - 1; i++) {
			if (patternConsecutiveSet.contains(hypertextList[i] + "-" + hypertextList[i+1])) {
					hypertextConsecutiveNum += 1;
			}
		}
		return hypertextConsecutiveNum / patternConsecutiveNum;
	}

	public double getPositionScore(String contents, String hypertext) {
		return 1 - (double) contents.indexOf(hypertext) / contents.length();
	}
}

/////////////////////////////////////////////////////////////////////////////////

// Some 'helper' functions follow.  You needn't understand their internal details.
// Feel free to move this to a separate Java file if you wish.
class Utilities
{
	// In J++, the console window can close up before you read it,
	// so this method can be used to wait until you're ready to proceed.
	public static void waitHere(String msg)
	{
		System.out.println("");
		System.out.println(msg);
		try { System.in.read(); } catch(Exception e) {} // Ignore any errors while reading.
	}

	// This method will read the contents of a file, returning it
	// as a string.  (Don't worry if you don't understand how it works.)
	public static synchronized String getFileContents(String fileName)
	{
		File file = new File(fileName);
		String results = null;

		try
		{
			int length = (int)file.length(), bytesRead;
			byte byteArray[] = new byte[length];

			ByteArrayOutputStream bytesBuffer = new ByteArrayOutputStream(length);
			FileInputStream       inputStream = new FileInputStream(file);
			bytesRead = inputStream.read(byteArray);
			bytesBuffer.write(byteArray, 0, bytesRead);
			inputStream.close();

			results = bytesBuffer.toString();
		}
		catch(IOException e)
		{
			System.out.println("Exception in getFileContents(" + fileName + "), msg=" + e);
		}

		return results;
	}
}
