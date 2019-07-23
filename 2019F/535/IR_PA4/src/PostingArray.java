import javafx.scene.transform.MatrixType;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class PostingArray {
    Map<String, Map<String, ArrayList<Integer>>> postings;

    public PostingArray() {
        postings = new HashMap<>();
    }

    public void add(String word, String docName, int pos) {
        if (postings.containsKey(word)) {
            Map<String, ArrayList<Integer>> postingsWord = postings.get(word);
            if (postingsWord.containsKey(docName)) {
                postingsWord.get(docName).add(pos);
            } else {
                ArrayList<Integer> positions = new ArrayList<>();
                positions.add(pos);
                postingsWord.put(docName, positions);
            }

        } else {
            Map<String, ArrayList<Integer>> postingsWord = new HashMap<>();
            ArrayList<Integer> positions = new ArrayList<>();
            positions.add(pos);
            postingsWord.put(docName, positions);
            postings.put(word, postingsWord);
        }
    }

    public int termFrequency(String term, String docName) {
        if (!postings.containsKey(term)) {
            return 0;
        }
        Map<String, ArrayList<Integer>> postingsWord = postings.get(term);
        if (!postingsWord.containsKey(docName)) {
            return 0;
        }

        return postingsWord.get(docName).size();
    }

    public int docFrequency(String term) {
        if (!postings.containsKey(term)) {
            return 0;
        }
        Map<String, ArrayList<Integer>> postingsWord = postings.get(term);

        return postingsWord.size();
    }

    Map<String, ArrayList<Integer>> postingsList(String term) {
        if (!postings.containsKey(term)) {
            return null;
        }
        return postings.get(term);
    }

    ArrayList<Integer> termPosInDoc(String term, String docName) {
        if (!postings.containsKey(term)) {
            return null;
        }

        if (!postings.get(term).containsKey(docName)) {
            return null;
        }

        return postings.get(term).get(docName);
    }
}
