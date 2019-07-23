# MinHash_PA2_535
2018 Fall CS535 Second Project Assignment

## Modify what?

1. numTerm = sum(max frequency of term)
2. minHash of multi-set not binary-set
3. return column of Doc Vector, not Row.
4. fileList[i].isFile() && !fileList[i].isHidden(), add hidden() file filter.
5. add result.
6. Set AB P after we get termDocumentMatrix.
7. Change variable type of hash function to BigInteger.

## problem

When there are a lot document, really a lot, it will over flow. Because we store termDocumentMatrix in memory. 

