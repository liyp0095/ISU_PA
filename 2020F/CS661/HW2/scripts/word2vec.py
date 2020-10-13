#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
Date: 2020-10-11
'''

# from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec


def load_data(f_name):
    data = []
    corpus = []
    data_raw = []
    with open(f_name) as fp:
        sent_data = ["<s> O None"]
        sent_data_raw = []
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) == 0 or aLine[0] == "":
                data.append(sent_data + ["<eof> I None"])
                sent_data = ["<s> O None"]
                data_raw.append(sent_data_raw)
                corpus.append(" ".join(sent_data_raw))
                sent_data_raw = []
                continue
            word = aLine[0]
            w_type = aLine[1]
            spe = "I" if "B-" in w_type or w_type == "O" else "O"
            w_type = w_type.replace("B-", "")
            w_type = w_type.replace("I-", "")
            w_type = w_type if not w_type == "O" else "None"
            sent_data.append(" ".join([word, spe, w_type]))
            sent_data_raw.append(word)
    return data, corpus, data_raw


def main():
    train, train_corpus, train_raw = load_data("data/conll/train.txt")
    valid, valid_corpus, valid_raw = load_data("data/conll/valid.txt")
    test, test_corpus, test_raw = load_data("data/conll/test.txt")
    print(len(train))
    print(len(valid))
    print(len(test))
    common_texts = train_raw + valid_raw + test_raw

    # sg ({0, 1}, optional) – Training algorithm: 1 for skip-gram; otherwise CBOW.
    model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4, sg=1, iter=20)
    with open("embedding/word2vec_100_skip.txt", "w") as fp:
        line = []
        for x in model.wv.vocab:
            line.append(x)
            for d in model.wv[x]:
                line.append(str(d))
            fp.writelines(" ".join(line) + "\n")
            line = []
    # model.wv.save("embedding/word2vec_200_cbow.kv")
    # write_raw("data/train_raw.txt", [train_raw[:6000], valid_raw[:2000], test_raw[:2000]])
    # write_raw("data/train_embedding.txt", [train_raw, valid_raw, test_raw])
    # write_raw("data/test_raw.txt", [test_raw[:2000]])
    pass


if __name__ == "__main__":
    main()
