import javafx.scene.transform.MatrixType;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.math.BigDecimal;
import java.util.*;

public class PositionalIndex {
    File folder;
    PostingArray postingArray;
    Map<String, Double> docVd;
    ArrayList<String> docNames;
    long N;

    public PositionalIndex(String folder){
        this.folder = new File(folder);
        this.postingArray = new PostingArray();
        this.docVd = new HashMap<>();
        this.docNames = new ArrayList<>();
        this.read_file();
        this.calculateVd();
    }

    public void read_file() {
        File[] fileList = folder.listFiles();
        N = fileList.length;

        FileReader fileReader;
        BufferedReader bufferedReader;
        for (int i = 0; i < fileList.length; i ++) {
            if (i % 1000 == 0)
                System.out.println(i);
            if (fileList[i].isFile()) {
                String filename = fileList[i].getName();
                docNames.add(filename);
                try {
                    fileReader = new FileReader(fileList[i]);
                    bufferedReader = new BufferedReader(fileReader);

                    String line;
                    String[] words;
                    int pos = 1;        // position starts from 1
                    while ((line = bufferedReader.readLine()) != null) {
                        words = line.replaceAll("[.,\\[\\]'{}:;()]", " ").toLowerCase().split("\\s+");
                        String w;
                        for (int j = 0; j < words.length; j++) {
                            w = wordTransform(words[j]);
                            if (w.length() < 1)
                                continue;
                            postingArray.add(w, filename, pos);
                            pos += 1;
                        }
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
//        postingArray.print();
    }

    public int termFrequency(String term, String Doc) {
        return postingArray.termFrequency(term, Doc);
    }

    public int docFrequency(String term) {
        return postingArray.docFrequency(term);
    }

    public String postingsList(String term) {
        if (postingArray.postingsList(term) == null) {
            return "";
        }
        Map<String, ArrayList<Integer>> postingsWord = postingArray.postingsList(term);
        String rst = "";
        for (String docName: postingsWord.keySet()) {
            String positions;

            positions = postingsWord.get(docName).get(0).toString();

            for (int j = 1; j < postingsWord.get(docName).size(); j ++) {
                positions += ",";
                positions += postingsWord.get(docName).get(j).toString();
            }
            rst += "<" + docName + ":" + positions + ">";
        }
        return "[" + rst + "]";
    }

    public double weight(String t, String d) {
        int termF = termFrequency(t, d);
        int docF = docFrequency(t);

        if (termF == 0) {
            return 0;
        }

        return Math.sqrt((double)termF) * Math.log10((double)N / (double)docF);
    }

    public double TPScore(String query, String doc) {
        String[] words = query.replaceAll("[,\\[\\]'{}:;()]", " ").toLowerCase().split("\\s+");

        if (words.length <= 1)
            return 0;

        String w0;
        String w1;
        int dis = 0;
        for (int j = 0; j < words.length - 1; j++) {
            w0 = wordTransform(words[j]);
            w1 = wordTransform(words[j + 1]);
            dis += termDistance(w0, w1, doc);
        }

        return (double)words.length / dis;
    }

    public double VSScore(String query, String doc) {
        String[] words = query.replaceAll("[,\\[\\]'{}:;()]", " ").toLowerCase().split("\\s+");
        if (words.length < 1)
            return 0;

        Map<String, Integer> wordList = new HashMap<>();
        String w;
        for (int i = 0; i < words.length; i++) {
            w = wordTransform(words[i]);
            if (wordList.containsKey(w)) {
                wordList.put(w, wordList.get(w) + 1);
            } else {
                wordList.put(w, 1);
            }
        }

        double tmp1 = 0;
        double tmp2 = 0;
        for (String word: wordList.keySet()) {
            int tf = wordList.get(word);
            double weightWD = weight(word, doc);

            tmp1 += (double)tf * weightWD;
            tmp2 += (double)tf * tf;
        }
/*        System.out.println("tmp1:" + tmp1);
        System.out.println("tmp2:" + tmp2);
        System.out.println("docVd:" + docVd.get(doc));*/
        if (tmp1 == 0) {
            return 0;
        }

        return tmp1 / Math.sqrt(tmp2 * docVd.get(doc).doubleValue());
    }

    public int termDistance(String w1, String w2, String docName) {
        ArrayList<Integer> postingW1 = postingArray.termPosInDoc(w1, docName);
        ArrayList<Integer> postingW2 = postingArray.termPosInDoc(w2, docName);

        if (postingW1 == null || postingW2 == null)
            return 17;

        int rst = Integer.MAX_VALUE;
        for (int i = 0; i < postingW1.size(); i++) {
            for (int j = 0; j < postingW2.size(); j++) {
                if (postingW1.get(i) < postingW2.get(j)) {
                    rst = Integer.min(rst, postingW2.get(j) - postingW1.get(i));
                }
            }
        }
        return Integer.min(rst, 17);
    }

    public double Relevance(String query, String doc) {
        return 0.6 * TPScore(query, doc) + 0.4 * VSScore(query, doc);
    }

    public void calculateVd() {
        int i = 0;
        for (String term: postingArray.postings.keySet()) {
            if (i % 100 == 0)
                System.out.println("vd:" + i);
            i++;
            Map<String, ArrayList<Integer>> postingsWord = postingArray.postings.get(term);
            for (String docName: postingsWord.keySet()) {
                if (!docVd.containsKey(docName)) {
                    docVd.put(docName, 0.0);
                }
                double value = docVd.get(docName) + Math.pow(weight(term, docName), 2);

                docVd.replace(docName, value);
            }
        }
    }

    public ArrayList<String> getTopK(String query, int k) {
        ArrayList<String> topK = new ArrayList<>();
        Map<String, BigDecimal> docRelevence = new HashMap<>();
        Map<String, BigDecimal> docTPS = new HashMap<>();
        Map<String, BigDecimal> docVSS = new HashMap<>();

        for (String docName: docNames) {
            docRelevence.put(docName, new BigDecimal(Relevance(query, docName)));
            docTPS.put(docName, new BigDecimal(TPScore(query, docName)));
            docVSS.put(docName, new BigDecimal(VSScore(query, docName)));
        }

        Set<Map.Entry<String, BigDecimal>> set = docRelevence.entrySet();

        List<Map.Entry<String, BigDecimal>> list = new ArrayList<Map.Entry<String, BigDecimal>>(set);

        Collections.sort(list, new Comparator<Map.Entry<String, BigDecimal>>() {
            @Override
            public int compare(Map.Entry<String, BigDecimal> o1,
                               Map.Entry<String, BigDecimal> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });

        List<Map.Entry<String, BigDecimal>> sublist;

        if(k > list.size()) {
            sublist = list;
        } else {
            sublist = list.subList(0, k);
        }
        for (int i = 0; i < sublist.size(); i++) {
            String name = sublist.get(i).getKey();
            System.out.println(name + ": " + sublist.get(i).getValue().toString()
                    + "\tVSS: " + docVSS.get(name).toString()
                    + "\tTPS: " + docTPS.get(name).toString());
        }

        return topK;
    }

    public String wordTransform(String word) {
        if (word.length() > 1 && word.charAt(word.length()-1) == '.') {
            try {
                word = word.substring(0, word.length() - 2);
            } catch (Exception e) {
                return "";
            }
        }
        for (int i = 0; i < word.length(); i ++) {
            if (!(Character.isDigit(word.charAt(i)) || word.charAt(i) == '.' || word.charAt(i) == '-' || word.charAt(i) == '+')) {
                return word.replaceAll("[,.\"\'?]", "");
            }
        }
        return word.replaceAll("[,\"\'?]", "");
    }
}
