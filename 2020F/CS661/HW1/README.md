# Experiments and Analysis of AutoNER

This projects apply [AutoNER](https://github.com/shangjingbo1226/AutoNER) on dataset [CHEMPROT](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vi/track-5/). By data format converting, we make the dataset of CHEMPROT runable on AutoNER. The f1 value very low now (f1=0.24) and it need further modification for the full schema.  

## Requirements

main function:
  - linux + python 3.x

AutoPhrase:
  - see the linke for details: https://github.com/shangjingbo1226/AutoPhrase

AutoNER:
  - see the link for details: https://github.com/shangjingbo1226/AutoNER

## How to Run

Process to run:
- copy following file to ```/data``` from [CHEMPROT](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vi/track-5/)
  - chemprot_training_entities.tsv
  - chemprot_training_abstracts.tsv
  - chemprot_test_entities.tsv
  - chemprot_test_abstracts.tsv
- run ```python data_preprocessing```, it will get following files
  - corpus.txt
  - test_labeled/raw.txt
  - train_labeled/raw.txt
- copy ```corpus.txt``` to [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase) and run to get result
- copy following files to ```/data``` from AutoPhrasse
  - AutoPhrase_multi-words.txt
  - AutoPhrase_single-word.txt
- run ```python generate_dictionary```, it will get following files
  - dict_full.txt
  - dict_core.txt
- copy following files to [AutoNER](https://github.com/shangjingbo1226/AutoNER) and run it on [pronto](https://researchit.las.iastate.edu/pronto).
  - dict_full.txt
  - dict_core.txt
  - train_raw.txt
  - test_raw.txt
- copy following files back and run ```python final_eval.py```
  - test_decoded.txt
  - train_decoded.txt

file in ```/data```:
- chemprot* : source data from [CHEMPROT](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vi/track-5/)
- train/test* : generated train and test set
- corpus.txt : corpus for AutoPhrase to learn dict_full.txt
- dict* : dictionaries for AutoNER task

## Problems  

- [ ] ```separators = [".", ",", "(", ")", "[", "]", "/", ":", "=", "+"]```, but there are some unexpected characters like ```'\u2002', '\u2009'```
