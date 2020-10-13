# Experiments and Analysis of AutoNER

This work is next to [HW1]() and again we apply [AutoNER](https://github.com/shangjingbo1226/AutoNER) on dataset [CHEMPROT](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vi/track-5/).  By changing the embedding from [bio-embedding](http://bio.nlplab.org/) to embeddings shows below, we make a comparison of the effects of different embeddings.  

- word2vec_cbow100
- word2vec_cbow200
- word2vec_skip100
- word2vec_skip200
- FastText_cbow100
- FastText_cbow200
- FastText_skip100
- FastText_skip200

## Requirements

main function:
  - linux + python 3.x
  - python packages: [gensim](https://radimrehurek.com/gensim/)

AutoPhrase:
  - see the linke for details: https://github.com/shangjingbo1226/AutoPhrase

AutoNER:
  - see the link for details: https://github.com/shangjingbo1226/AutoNER

## How to Run

Process to run:
- convert [CHEMPROT](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vi/track-5/) to standoff with https://github.com/JohnGiorgi/ChemProt-to-Standoff
- convert standoff to conll with https://github.com/spyysalo/standoff2conll
- run ```data_preprocessing.py``` to get the dataset to train and test
- run ```fastvec.py``` and ```word2vec.py``` in ```/scripts``` to get the embedding files
- train and test AutoNER on the server
- run ```final_eval.py``` to get the final result

## Problems  

- [ ] f1 value (0.43) is still low
