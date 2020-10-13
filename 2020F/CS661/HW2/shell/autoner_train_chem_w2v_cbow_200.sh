MODEL_NAME="CHEMPROT"
RAW_TEXT="data/${MODEL_NAME}/train_raw.txt"
DICT_CORE="data/${MODEL_NAME}/dict_core.txt"
DICT_FULL="data/${MODEL_NAME}/dict_full.txt"
EMBEDDING_TXT_FILE="embedding/word2vec_200_cbow.txt"
# EMBEDDING_TXT_FILE="embedding/bio_embedding.txt"
MUST_RE_RUN=0
SUFFIX="word2vec_cbow200"

WORD_DIM=200

green=`tput setaf 2`
reset=`tput sgr0`

DEV_SET="data/${MODEL_NAME}/valid.txt"
TEST_SET="data/${MODEL_NAME}/test.txt"

MODEL_ROOT=./models/${MODEL_NAME}_${SUFFIX}
TRAINING_SET=$MODEL_ROOT/annotations.ck

mkdir -p $MODEL_ROOT

echo ${green}=== Compilation ===${reset}
make

if [ $MUST_RE_RUN == 1 ] || [ ! -e $MODEL_ROOT/embedding.pk ]; then
    echo ${green}=== Encoding Embeddings ===${reset}
    ml-gpu python3 preprocess_partial_ner/save_emb.py --input_embedding $EMBEDDING_TXT_FILE --output_embedding $MODEL_ROOT/embedding.pk
    # python preprocess_partial_ner/save_emb.py --input_embedding $EMBEDDING_TXT_FILE --output_embedding $MODEL_ROOT/embedding.pk
fi

echo ${green}=== Generating Distant Supervision ===${reset}
bin/generate $RAW_TEXT $DICT_CORE $DICT_FULL $TRAINING_SET

if [ DEV_SET == "" ]; then
    DEV_SET=$TRAINING_SET
fi

if [ TEST_SET == "" ]; then
    TEST_SET=$TRAINING_SET
fi

mkdir -p $MODEL_ROOT/encoded_data

if [ $MUST_RE_RUN == 1 ] || [ ! -e $MODEL_ROOT/encoded_data/test.pk ]; then
    echo ${green}=== Encoding Dataset ===${reset}
    ml-gpu python3 preprocess_partial_ner/encode_folder.py --input_train $TRAINING_SET --input_testa $DEV_SET --input_testb $TEST_SET --pre_word_emb $MODEL_ROOT/embedding.pk --output_folder $MODEL_ROOT/encoded_data/
    # python preprocess_partial_ner/encode_folder.py --input_train $TRAINING_SET --input_testa $DEV_SET --input_testb $TEST_SET --pre_word_emb $MODEL_ROOT/embedding.pk --output_folder $MODEL_ROOT/encoded_data/
fi

CHECKPOINT_DIR=$MODEL_ROOT/checkpoint/
CHECKPOINT_NAME=autoner

echo ${green}=== Training AutoNER Model ===${reset}
# python train_partial_ner.py \
ml-gpu python3 train_partial_ner.py \
    --cp_root $CHECKPOINT_DIR \
    --checkpoint_name $CHECKPOINT_NAME \
    --eval_dataset $MODEL_ROOT/encoded_data/test.pk \
    --train_dataset $MODEL_ROOT/encoded_data/train_0.pk \
    --update SGD --lr 0.05 --hid_dim 300 --droprate 0.5 \
    --sample_ratio 1.0 --word_dim $WORD_DIM --epoch 50

echo ${green}Done.${reset}

RAW_TEXT="data/${MODEL_NAME}/test_raw.txt"
CHECKPOINT=$MODEL_ROOT/checkpoint/autoner/

ml-gpu python3  preprocess_partial_ner/encode_test.py --input_data $RAW_TEXT --checkpoint_folder $CHECKPOINT --output_file $MODEL_ROOT/encoded_test.pk
ml-gpu python3 test_partial_ner.py --input_corpus $MODEL_ROOT/encoded_test.pk --checkpoint_folder $CHECKPOINT --output_text $MODEL_ROOT/decoded.txt --hid_dim 300 --droprate 0.5 --word_dim $WORD_DIM
