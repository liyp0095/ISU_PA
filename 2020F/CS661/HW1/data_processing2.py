#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
Date: 2020-10-10
'''

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


def write_data(f_name, data):
    with open(f_name, "w") as fp:
        for d in data:
            for t in d:
                fp.writelines(t + "\n")
            fp.writelines("\n")


def write_raw(f_name, data):
    with open(f_name, "w") as fp:
        for d in data:
            for s in d:
                for t in s:
                    fp.writelines(t + "\n")
                fp.writelines("\n")


def write_corpus(f_name, data):
    with open(f_name, "w") as fp:
        for d in data:
            for t in d:
                fp.writelines(t + "\n")


def main():
    train, train_corpus, train_raw = load_data("data/conll/train.txt")
    valid, valid_corpus, valid_raw = load_data("data/conll/valid.txt")
    test, test_corpus, test_raw = load_data("data/conll/test.txt")
    print(len(train))
    print(len(valid))
    print(len(test))

    # write_data("data/test.txt", test[:2000])
    # write_data("data/valid.txt", valid[:2000])
    #
    # write_corpus("data/autophrase/corpus.txt", [train_corpus, valid_corpus, test_corpus])
    #
    # write_raw("data/train_raw.txt", [train_raw[:6000], valid_raw[:2000], test_raw[:2000]])
    # write_raw("data/train_embedding.txt", [train_raw, valid_raw, test_raw)
    write_raw("data/test_raw_all.txt", [test_raw])
    pass


if __name__ == "__main__":
    main()
