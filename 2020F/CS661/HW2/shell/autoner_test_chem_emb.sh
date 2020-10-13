MODEL_NAME="CHEMPROT"
GPU_ID=0
RAW_TEXT="data/CHEMPROT/test_raw.txt"
WORD_DIM=100
SUFFIX="word2vec_skip100"

green=`tput setaf 2`
reset=`tput sgr0`

MODEL_ROOT=./models/${MODEL_NAME}_${SUFFIX}
CHECKPOINT=$MODEL_ROOT/checkpoint/autoner/

ml-gpu python3  preprocess_partial_ner/encode_test.py --input_data $RAW_TEXT --checkpoint_folder $CHECKPOINT --output_file $MODEL_ROOT/encoded_test.pk

ml-gpu python3 test_partial_ner.py --input_corpus $MODEL_ROOT/encoded_test.pk --checkpoint_folder $CHECKPOINT --output_text $MODEL_ROOT/decoded.txt --hid_dim 300 --droprate 0.5 --word_dim $WORD_DIM
