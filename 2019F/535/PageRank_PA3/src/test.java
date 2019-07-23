import java.net.MalformedURLException;

public class test {
    static public void main(String[] args) throws MalformedURLException {
/*        System.out.println("HelloWorld!");
        String[] relate = new String[1];
        relate[0] = "tennis";
        WikiCrawler wikiCrawler = new WikiCrawler("/wiki/Tennis", 10, relate, "a.txt");
        String rst = wikiCrawler.getContent("/wiki/Tennis");
        System.out.println(rst);
        wikiCrawler.extractLinks(rst);*/
        String[] relate = {"tennis", "grand slam"};
        WikiCrawler wikiCrawler = new WikiCrawler("/wiki/Tennis", 500, relate, "a500.txt", true);
        wikiCrawler.crawl();
    }
}
