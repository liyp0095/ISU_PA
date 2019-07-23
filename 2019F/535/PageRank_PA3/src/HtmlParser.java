import java.util.*;

import static java.lang.Math.abs;
import static java.lang.Math.min;

public class HtmlParser {
    String page;
    String body;
    String plainText;
    ArrayList<String> links;
    ArrayList<String> words;
    Map<String, ArrayList<Integer>> topicsPosition;

    public HtmlParser(String page) {
        this.page = page;
        this.words = new ArrayList<String>();
        this.topicsPosition = new HashMap<String, ArrayList<Integer>>();
    }

    public String getBody() {
        int bodyStartIndex = page.indexOf("<p>", 0);
        int bodyEndIndex = page.indexOf("</body>", bodyStartIndex);

        if (bodyStartIndex < 0 || bodyEndIndex < 0)
            return  "";

        body = page.substring(bodyStartIndex, bodyEndIndex);
        return body;
    }

    public String getPlainText() {
        String rst = body;
        String text = "";

        int start = rst.indexOf("<p>", 0);
        int end = rst.indexOf("</p>", start+1);
        int i = 0;
        int j = 0;

        while (start >= 0) {
            String temp = rst.substring(start, end);
            i = temp.indexOf("<", 0);
            j = temp.indexOf(">", i+1);
            while (i >= 0) {
                String subtemp = temp.substring(i, j+1);
                temp = temp.replace(subtemp, "");
                i = temp.indexOf("<", 0);
                j = temp.indexOf(">", i+1);
            }
            text += temp;
            start = rst.indexOf("<p>", end + 1);
            end = rst.indexOf("</p>", start + 1);
        }
        plainText = text;
        Collections.addAll(words, plainText.split("\\s+"));
        return plainText;
    }

    public ArrayList<String> getLinks() {
        String str = body;
        links = new ArrayList<>();
        int start = str.indexOf("<p>", 0);
        int end = str.indexOf("</p>", start+1);

        while (start >= 0) {
            String passage = str.substring(start, end+4);
            int i = passage.indexOf("<a", 0);
            int j = passage.indexOf("</a>", i+1);
            while ( i >=0 && j >= 0) {
                String link = passage.substring(i, j+4);
                links.add(link);
                i = passage.indexOf("<a", j + 5);
                j = passage.indexOf("</a>", i + 1);
            }
            start = str.indexOf("<p>", end+5);
            end = str.indexOf("</p>", start+1);
        }
        return links;
    }

    public void calculateTopicPosition(String[] topics) {
        ArrayList<Integer> positions = new ArrayList<Integer>();
        for (int i = 0; i < topics.length; i++ ) {
            positions = getStringPosition(topics[i]);
            topicsPosition.put(topics[i], positions);
        }
    }

    public ArrayList<Integer> getStringPosition(String str) {
        ArrayList<Integer> strPos = new ArrayList<>();
        int pos = plainText.indexOf(str, 0);
        while (pos >= 0) {
            strPos.add(charNumber(plainText.substring(0, pos), ' '));
            pos = plainText.indexOf(str, pos+1);
        }
        return strPos;
    }

    public int charNumber(String str, char c) {
        int num = 0;
        for (int i = 0; i < str.length(); i ++){
            if (Character.isSpaceChar(str.charAt(i))) {
                num += 1;
            }
        }
        return num;
    }

    public float calculateLinkWeight(String link, String[] topics, boolean isTopicSensitive) {
        if (!isTopicSensitive)
            return 0;

        if (topicsPosition.size() == 0)
            return 0;

        String linkAnchorText = getAnchorTextFromLink(link);
        String linkAddress = getAddressFromLink(link);
        ArrayList<Integer> linkPosition = getStringPosition(linkAnchorText);
        Integer distance = Integer.MAX_VALUE;
        for (int i = 0; i < topics.length; i++) {
            if (linkAddress.toLowerCase().contains(topics[i]) || linkAnchorText.toLowerCase().contains(topics[i]))
                return 1;
            distance = min(distance, findMinDistance(linkPosition, topicsPosition.get(topics[i])));
        }
        if (distance > 17)
            return 0;
        return (float)1/(distance + 2);
    }

    public int findMinDistance(ArrayList<Integer> p1, ArrayList<Integer> p2) {
        int i = 0;
        int j = 0;
        Integer distance = Integer.MAX_VALUE;
        while (i < p1.size() && j < p2.size()) {
            distance = min(distance, abs(p1.get(i) - p2.get(j)));
            if (p1.get(i) < p2.get(j))
                i += 1;
            else
                j += 1;
        }
        return distance;
    }

    public String getAnchorTextFromLink(String link) {
        String rst = link;

        int start = link.indexOf("<", 0);
        int end = link.indexOf(">", start+1);

        while (start >= 0) {
            String temp = rst.substring(start, end+1);
            rst = rst.replace(temp, "");
            start = rst.indexOf("<", 0);
            end = rst.indexOf(">", start+1);
        }
        return rst;
    }

    public String getAddressFromLink(String link) {
        int start = link.indexOf("href=", 0);
        int end = link.indexOf("\"", start + 6);
        if (start < 0) {
            return "";
        }
        return link.substring(start + 6, end);
    }
}
