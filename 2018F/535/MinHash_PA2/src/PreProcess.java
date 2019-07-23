import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class PreProcess {
    static final List<String> stopWords = new ArrayList<String>(Arrays.asList("the"));

    public static boolean isPrime(int n) {
        if (n == 1) return false;
        else {
            for (int i = 2; i < n; i ++) {
                if (n % i == 0) return false;
            }
            return true;
        }
    }

    public static int nextPrime(int n) {
        boolean isPrime = false;
        while (!isPrime) {
            isPrime = isPrime(++n);
        }
        return n;
    }

    public static boolean isStopWord(String s) {
        if (stopWords.contains(s) || s.length() < 3)
            return true;
        return false;
    }

    /**
     * Get unique word set of documents in one directory.
     * @param folder
     * @return  Unique word set
     * @throws IOException
     */
    public static Set<String> termsUnique(File folder) throws IOException {
        Set<String> s = new HashSet<String>();
        File[] fileList = folder.listFiles();

        FileReader fileReader;
        BufferedReader bufferedReader;
        for (int i = 0; i < fileList.length; i ++) {
            if (fileList[i].isFile() && !fileList[i].isHidden()) {
                fileReader = new FileReader(fileList[i]);
                bufferedReader = new BufferedReader(fileReader);

                String line;
                String[] words;
                while((line = bufferedReader.readLine()) != null) {
                    words = line.replaceAll("[,.:;']", "").toLowerCase().split("\\s+");
                    for (int j = 0; j < words.length; j ++) {
                        if (!isStopWord(words[j])) {
                            s.add(words[j]);
                        }
                    }
                }
                bufferedReader.close();
            }
        }

        return s;
    }

    /**
     * Get word frequency vector of one document
     * @param file  The file need to read
     * @param numUniqueTerms Unique term set size
     * @param termsList Unique term list
     * @return
     * @throws IOException
     */
    public static int[] DocVector(File file, int numUniqueTerms, ArrayList<String> termsList) throws IOException {
        int[] docVector = new int[numUniqueTerms];
        Arrays.fill(docVector, 0);

        FileReader fileReader = new FileReader(file);
        BufferedReader bufferedReader = new BufferedReader(fileReader);

        String line;
        String[] words;
        while ((line = bufferedReader.readLine()) != null) {
            words = line.replaceAll("[.,:;']", "").toLowerCase().split("\\s+");
            for (int j = 0; j < words.length; j ++) {
                if (!isStopWord(words[j])) {
                    docVector[termsList.indexOf(words[j])] += 1;
                }
            }
        }
        return docVector;
    }

    /**
     *  Get max value in each row of Matrix
     * @param Matrix
     * @return
     */
    public static int[] rowMaxMatrix(int[][] Matrix) {
    	int m = Matrix.length;
    	int n = Matrix[0].length;
    	
        int[] rowMax = new int[m];
        for (int i = 0; i < m; i ++) {
            int max = 0;
            for (int j = 0; j < n; j ++) {
                if (max < Matrix[i][j]) {
                    max = Matrix[i][j];
                }
            }
            rowMax[i] = max;
        }
        return rowMax;
    }

    /**
     * Get max value in each column of Matrix
     * @param Matrix
     * @return
     */
    public static int[] colMaxMatrix(int[][] Matrix) {
    	int m = Matrix.length;
    	int n = Matrix[0].length;
    	
        int[] colMax = new int[n];
        for (int i = 0; i < n; i ++) {
            int max = 0;
            for (int j = 0; j < m; j ++) {
                if (max < Matrix[j][i]) {
                    max = Matrix[j][i];
                }
            }
            colMax[i] = max;
        }
        return colMax;
    }

    /**
     * Get one row of Matrix
     * @param Matrix
     * @param index
     * @return
     */
    public static int[] getMatrixRow(int[][] Matrix,int index) {
    	int m = Matrix.length;
    	int n = Matrix[0].length;
    	
        int[] row = new int[n];
        for (int i = 0; i < n; i ++) {
            row[i] = Matrix[index][i];
        }
        return row;
    }

    /**
     * Get one column of Matrix
     * @param Matrix
     * @param index
     * @return
     */
    public static int[] getMatrixCol(int[][] Matrix, int index) {
    	int m = Matrix.length;
    	int n = Matrix[0].length;
    	
        int[] row = new int[m];
        for (int i = 0; i < m; i ++) {
            row[i] = Matrix[i][index];
        }
        return row;
    }
}
