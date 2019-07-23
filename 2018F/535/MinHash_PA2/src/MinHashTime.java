
import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class MinHashTime {
    long nowTime;
    public void timer(String folder, int numPermutations) throws IOException {
        this.nowTime = System.nanoTime();
        MinHashSimilarities minHashSimilarities = new MinHashSimilarities(folder, numPermutations);
        myPrint("Time to initial MinHashSimilarities");
        for (int i = 0; i < minHashSimilarities.fileNames.length; i++) {
            for (int j = i + 1; j < minHashSimilarities.fileNames.length; j ++) {
                double e = minHashSimilarities.exactJaccard(minHashSimilarities.fileNames[i], minHashSimilarities.fileNames[j]);
            }
        }
        myPrint("Time to compare every pair of files with exact Jaccard");
        for (int i = 0; i < minHashSimilarities.fileNames.length; i++) {
            for (int j = i + 1; j < minHashSimilarities.fileNames.length; j ++) {
                double a = minHashSimilarities.approximateJaccard(minHashSimilarities.fileNames[i], minHashSimilarities.fileNames[j]);
            }
        }
        myPrint("Time to compare every pair of files with approximate Jaccard");
    }

    public void myPrint(String s) {
        long duration = System.nanoTime() - this.nowTime;
        System.out.println(s + ": " + TimeUnit.MILLISECONDS.convert(duration, TimeUnit.NANOSECONDS) / 1000.0 + " s");
        this.nowTime = System.nanoTime();
    }
}
