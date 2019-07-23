
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MinHashSimilarities {

    int[][] termDocumentMatrix;
    int[][] minHashMatrix;

    String[] fileNames;
    int numUniqueTerms;
    int numPermutations;

    public MinHashSimilarities(String folder, int numPermutations) throws IOException {
        MinHash minHash = new MinHash(folder, numPermutations);
        this.termDocumentMatrix = minHash.termDocumentMatrix();
        this.minHashMatrix = minHash.minHashMatrix();
        this.fileNames = minHash.allDocs();
        this.numUniqueTerms = minHash.getNumUniqueTerms();
        this.numPermutations = numPermutations;
    }

    public double exactJaccard(String file1, String file2) {
        List<String> files = Arrays.asList(this.fileNames);

        double Intersection = 0;
        double Union = 0;

        int index1 = files.indexOf(file1);
        int index2 = files.indexOf(file2);
        for (int i = 0; i < this.numUniqueTerms; i ++) {
            if (this.termDocumentMatrix[i][index1] < this.termDocumentMatrix[i][index2]) {
                Intersection += this.termDocumentMatrix[i][index1];
                Union += this.termDocumentMatrix[i][index2];
            } else {
                Intersection += this.termDocumentMatrix[i][index2];
                Union += this.termDocumentMatrix[i][index1];
            }
        }
        return Intersection / Union;
    }

    public double approximateJaccard(String file1, String file2) {
        List<String> files = Arrays.asList(this.fileNames);

        int equ = 0;

        int index1 = files.indexOf(file1);
        int index2 = files.indexOf(file2);
        for (int i = 0; i < this.numPermutations; i++) {
            if (this.minHashMatrix[i][index1] == this.minHashMatrix[i][index2]) {
                equ += 1;
            }
        }
        return (double)equ / this.numPermutations;
    }

    public int[] minHashSig(String fileName) {
        List<String> files = Arrays.asList(this.fileNames);
        System.out.println(files.indexOf(fileName));
        return PreProcess.getMatrixCol(this.minHashMatrix, files.indexOf(fileName));
    }

    public int[] termDocVec(String fileName) {
        List<String> files = Arrays.asList(this.fileNames);
        return PreProcess.getMatrixCol(this.termDocumentMatrix, files.indexOf(fileName));
    }
}
