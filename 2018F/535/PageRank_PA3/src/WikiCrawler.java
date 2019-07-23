import java.io.*;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashSet;

public class WikiCrawler {
    public static final String BASE_URL = "https://en.wikipedia.org";

    public static HashSet<String> discovered = new HashSet<String>();
    public static HashSet<String> visited = new HashSet<String>();
    public static WeightedQueue queue = new WeightedQueue();
    private static String seed;
    private static int max = 0;
    private static String[] topics = null;
    private static String filename = "";
    private boolean isTopicSensitive;
    private static ArrayList<ArrayList<String>> edgeSet;

    // constructor
    public WikiCrawler(String seed, int max, String[] topics, String output, boolean isTopicSensitive){
        //discovered.add(BASE_URL+seed);
        this.seed = seed;
        this.max = max;
        this.topics = topics;
        filename = output;
        this.isTopicSensitive = isTopicSensitive;
        this.edgeSet = new ArrayList<ArrayList<String>>();
    }

    public String getContent(String url) throws FileNotFoundException {
        String thisPage = "";
        BufferedReader bufferedReader = null;

        try {
            URL realURL = new URL(BASE_URL + url);
            InputStream inputStream = realURL.openStream();
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

            String line = "";
            while ((line = bufferedReader.readLine()) != null) {
                thisPage += line;
            }
        } catch (Exception e) {
            return "";
//            e.printStackTrace();
        }
        // close
        finally {
            try {
                if (bufferedReader != null){
                    bufferedReader.close();
                }
            } catch (Exception e2){
                e2.printStackTrace();
            }
        }
        return thisPage;
    }

    public void crawl() {
/*        for (int i = 0; i < 1000; i ++) {
            queue.add(new Node<String>("1", (float) 0.2));
            queue.printQueue();
            queue.add(new Node<String>("/wiki/Grand_Slam_(tennis)", (float)0.4));
            queue.printQueue();
            queue.add(new Node<String>("1", 1));
            queue.extract();
            queue.printQueue();
            queue.add(new Node<String>("1", 1));
            queue.printQueue();
            queue.add(new Node<String>("/wiki/Grand_Slam_(tennis)", 1));
            queue.printQueue();
            queue.add(new Node<String>("2", 1));
            queue.printQueue();
        }*/
        queue.add(new Node<String>(seed, 1));
        Node<String> node;
        String url;
        String content;
        int count = 1;
        System.out.println("crawling ... ");
        while (!queue.isEmpty() && visited.size() < this.max) {
            //System.out.println(queue.size());
            node = queue.extract();
            url = node.getIndex();
            content = "";
            try {
                content = getContent(url);
            } catch (Exception e) {
                e.printStackTrace();
            }
            if (content.equals("")) {
                continue;
            }
            visited.add(url);

            System.out.print("\r");
            System.out.print(visited.size() + " / " + max);
            analyseContent(content, node.getIndex());
            try {
                if (count % 10 == 0) {
                    Thread.sleep(2000);
                    count = 0;
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            count += 1;
        }

        // drop edges we don't need
        ArrayList<Integer> indexToRemove = new ArrayList<>();
        for (int j = 0; j < edgeSet.size(); j ++) {
            if (!(visited.contains(edgeSet.get(j).get(0)) && visited.contains(edgeSet.get(j).get(1)))) {
                indexToRemove.add(j);
            }
        }

        for (int i = indexToRemove.size()-1; i >= 0; i--) {
            int pos = indexToRemove.get(i);
            edgeSet.remove(pos);
        }

        // Write to file
        ArrayList<String> nodeArray = new ArrayList<>(visited);
        try {
            File file = new File(filename);
            Writer out = new FileWriter(file);
            //File fileNum = new File(filename + "num.txt");
            //Writer outNum = new FileWriter(fileNum);
            out.write(max + "\n");
            for (int i = 0; i < edgeSet.size(); i++) {
                out.write(edgeSet.get(i).get(0) + " " + edgeSet.get(i).get(1) + "\n");
                //outNum.write(nodeArray.indexOf(edgeSet.get(i).get(0)) + " " + nodeArray.indexOf(edgeSet.get(i).get(1)) + "\n");
            }
            out.close();
            //outNum.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void analyseContent(String content, String source) {
        HtmlParser htmlParser = new HtmlParser(content);

        try {
            htmlParser.getBody();
            htmlParser.getPlainText();
            htmlParser.getLinks();
            htmlParser.calculateTopicPosition(topics);
        } catch (Exception e) {
            //e.printStackTrace();
            return;
        }
        String address;
        float weight;
        for (int i = 0; i < htmlParser.links.size(); i++) {
            if (htmlParser.getAnchorTextFromLink(htmlParser.links.get(i)).length() == 0) {
                continue;
            }
            address = htmlParser.getAddressFromLink(htmlParser.links.get(i));
            if (isDisallow(address)) {
                continue;
            }
            if (address.equals("") || address.contains("#") || address.contains(":")) {
                continue;
            }
            ArrayList<String> edge = new ArrayList<>();
            edge.add(source);
            edge.add(address);
            if (!edgeSet.contains(edge)) {
                edgeSet.add(edge);
            }
            if (visited.contains(address)) {
                continue;
            }
            //discovered.add(address);
            weight = htmlParser.calculateLinkWeight(htmlParser.links.get(i), topics, this.isTopicSensitive);
            queue.add(new Node<String>(address, weight));
        }
    }

    public boolean isDisallow(String address) {
        String[] disAllow = {
                "/w/",
                "/api/",
                "/trap/",
                "/wiki/Special:",
                "/wiki/Spezial:",
                "/wiki/Spesial:",
                "/wiki/Special%3A",
                "/wiki/Spezial%3A",
                "/wiki/Spesial%3A"};

        for (int i = 0; i < disAllow.length; i ++) {
            if (address.contains(disAllow[i])) {
                return true;
            }
        }
        return false;
    }
}
