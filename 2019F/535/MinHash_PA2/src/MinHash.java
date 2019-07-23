import java.io.File;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class MinHash {

    File folder;
    ArrayList<File> fileList;
    int numPermutations;
    int numUniqueTerms;
    int numTerms;
    int mod;
    int[] a,b;
    ArrayList<String> termsUnique;

    public MinHash(String folder, int numPermutations) throws IOException {
        this.folder = new File(folder);
        this.numPermutations = numPermutations;

        this.termsUnique = new ArrayList<String>(PreProcess.termsUnique(this.folder));
        this.numUniqueTerms = this.termsUnique.size();
        
        this.a = new int[this.numPermutations];
        this.b = new int[this.numPermutations];
        
        fileList = new ArrayList<File>();
        //get file list
        File[] tempList = this.folder.listFiles();

        for (int i = 0; i < tempList.length; i++)
            if (tempList[i].isFile() && !tempList[i].isHidden())
            	fileList.add(tempList[i]);
//
//        System.out.println("Total number of files: " + fileList.size());
//
//        termDocumentMatrix = new int[this.numUniqueTerms][fileList.size()];
//
//        computeTermDocumentMatrix();
//
//        minHashMatrix = new int[this.numPermutations][fileList.size()];
//
//        computeMinHashMatrix();
        
    }

    /**
     * Set mod and a,b according to the prime we pick.
     * @param mod
     */
    public void setABP(int mod) {
        this.mod = mod;

        // We chose 1 as the seed of random. change the seed if you want to.
        Random random = new Random(1);
        for (int i = 0; i < this.numPermutations; i++) {
            this.a[i] = random.nextInt(this.mod - 1) + 1;
            this.b[i] = random.nextInt(this.mod - 1) + 1;
        }
    }

    public int[][] termDocumentMatrix() throws IOException {

        int[][] termDocumentMatrix = new int[this.numUniqueTerms][this.fileList.size()];

        int[] docVector;
        for (int i = 0; i < fileList.size(); i++) {
            docVector = PreProcess.DocVector(fileList.get(i), this.numUniqueTerms, this.termsUnique);
            for (int j = 0; j < docVector.length; j ++) {
                termDocumentMatrix[j][i] = docVector[j];
            }
            
            if(i % 1000 == 0)
            	System.out.println(i);
        }
        
        System.out.println("Term Document Matrix completed.");

        return termDocumentMatrix;
    }

    public int[][] minHashMatrix() throws IOException {

        int minHashMatrix[][] = new int[this.numPermutations][this.fileList.size()];

        int[] maxNumEachTerm = new int[this.numUniqueTerms];
        Arrays.fill(maxNumEachTerm, 0);

        int[] docVector;
        for (int i = 0; i < fileList.size(); i++) {
            docVector = PreProcess.DocVector(fileList.get(i), this.numUniqueTerms, this.termsUnique);
            for (int j = 0; j < docVector.length; j ++) {
                maxNumEachTerm[j] = Math.max(maxNumEachTerm[j], docVector[j]);
            }
            if(i % 1000 == 0)
                System.out.println("Calculate max frequency of term: " + i + "\tth doc.");
        }

        // numTerms is the sum of max frequency of each term in Term set of All documents.
        int sum = 0;
        for (int i = 0; i < maxNumEachTerm.length; i ++) {
            sum += maxNumEachTerm[i];
        }
        this.numTerms = sum;
        // P is the prime no less than numTerm.
        setABP(PreProcess.nextPrime(sum));

        int[] minHashDocVector;
        for (int i = 0; i < fileList.size(); i++) {
            docVector = PreProcess.DocVector(fileList.get(i), this.numUniqueTerms, this.termsUnique);
            minHashDocVector = getMinHash(docVector, maxNumEachTerm);
            for (int j = 0; j < this.numPermutations; j ++) {
                minHashMatrix[j][i] = minHashDocVector[j];
            }
            if(i % 1000 == 0)
            	System.out.println("Calculate minHash: " + i + "\tth doc.");
        }
        
        System.out.println("Min Hash Matrix completed.");
        return minHashMatrix;
    }

    /**
     * Get MinHash of each Document. We do change below:
     *
     *      D1 D2   max             D1 D2
     * t1   2   1    2     -->  t1  1   1
     *                          t1  1   0
     *
     * @param docVector term frequency vector of one document
     * @param maxNumEachTerm Max term frequency vector of all document
     * @return
     */
    public int[] getMinHash(int[] docVector, int[] maxNumEachTerm) {
        // index is the position of term
        int index = 0;
        int[] hashed = new int[this.numPermutations];
        Arrays.fill(hashed, Integer.MAX_VALUE);
        for (int i = 0; i < maxNumEachTerm.length; i ++) {
            for (int j = 0; j < maxNumEachTerm[i]; j ++) {
                if (j < docVector[i]) {
                    for (int k = 0; k < this.numPermutations; k ++) {
                        hashed[k] = Math.min(hash(index, k), hashed[k]);
                    }
                }
                index += 1;
            }
        }
        return hashed;
    }

    /**
     * hash function of permutation, (ax + b) / p. We use big integer to avoid overflow.
     * @param x
     * @param index
     * @return
     */
    public int hash(int x, int index) {
        //return (int)((this.a[index] * x + this.b[index]) % this.mod);
        return  ((new BigInteger("" + this.a[index]))
                .multiply(new BigInteger("" + x)).subtract(new BigInteger("" + this.b[index])))
                .mod(new BigInteger("" + this.mod)).intValue();
    }
    
//    public int[][] termDocumentMatrix() { return termDocumentMatrix;}
//
//    public int[][] minHashMatrix() { return minHashMatrix;}

    public String[] allDocs() {
    	
    	String[] result = new String[fileList.size()];
    	
    	for(int i = 0; i < result.length; i++)
    		result[i] = fileList.get(i).getName();
    	
    	return result;
    }

    public int numTerms() { return this.numTerms; }

    public int getNumUniqueTerms() { return this.numUniqueTerms; }

    public int numPermutations() { return this.numPermutations; }
}
