import java.io.IOException;

public class MinHashAccuracy {
    public void accuracy(String folder, int numPermutation, double eta) throws IOException {
        int numWrong = 0;

        MinHashSimilarities minHashSimilarities = new MinHashSimilarities(folder, numPermutation);
        System.out.println("NumPermutations: " + numPermutation);
        for (int i = 0; i < minHashSimilarities.fileNames.length; i++) {
            for (int j = i + 1; j < minHashSimilarities.fileNames.length; j ++) {
                double e = minHashSimilarities.exactJaccard(minHashSimilarities.fileNames[i], minHashSimilarities.fileNames[j]);
                double a = minHashSimilarities.approximateJaccard(minHashSimilarities.fileNames[i], minHashSimilarities.fileNames[j]);
                double d = Math.abs(e - a);
                
                if (d > eta) {
                    System.out.println(minHashSimilarities.fileNames[i] + " & " +
                            minHashSimilarities.fileNames[j] + ": " + d + " ; " + e + " ; " + a);
                    numWrong += 1;
                }
            }
        }
        System.out.println("eta is : " + eta + "Num of over diff: " + numWrong);
    }

    /**
     * just for convenience to calculate result. ignore it please
     * @param folder
     * @param numPermutation
     * @param eta
     * @throws IOException
     */
    public void myaccuracy(String folder, int numPermutation, double eta) throws IOException {
        int numWrong4 = 0;
        int numWrong7 = 0;
        int numWrong9 = 0;
        int total = 0;
        MinHashSimilarities minHashSimilarities = new MinHashSimilarities(folder, numPermutation);
        System.out.println("NumPermutations: " + numPermutation);
        for (int i = 0; i < minHashSimilarities.fileNames.length; i++) {
            for (int j = i + 1; j < minHashSimilarities.fileNames.length; j ++) {
                double e = minHashSimilarities.exactJaccard(minHashSimilarities.fileNames[i], minHashSimilarities.fileNames[j]);
                double a = minHashSimilarities.approximateJaccard(minHashSimilarities.fileNames[i], minHashSimilarities.fileNames[j]);
                double d = Math.abs(e - a);
                if (d > 0.04) {
                    //System.out.println(minHashSimilarities.fileNames[i] + " & " +
                    //        minHashSimilarities.fileNames[j] + ": " + d + " ; " + e + " ; " + a);
                    numWrong4 += 1;
                }
                if (d > 0.07 ) {
                    numWrong7 += 1;
                }
                if (d > 0.09) {
                    numWrong9 += 1;
                }
                total += 1;
            }
        }
        System.out.println("Num of total: " + total);
        System.out.println("Num of over diff4: " + numWrong4);
        System.out.println("Num of over diff7: " + numWrong7);
        System.out.println("Num of over diff9: " + numWrong9);
    }
}
