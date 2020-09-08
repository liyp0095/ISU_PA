#!/bin/python
# -*- coding: utf8 -*-

'''
Description: This file change data format from relation to NER
Auther: Yuepei Li
Date: 2020-09-04
'''

'''
letters encoded with '\u2002' is a space?
'''

import random
import codecs


def load_dict(fname):
    label_dict = {}
    with codecs.open(fname, encoding="utf-8") as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            doc_id = int(aLine[0])
            entity_label = aLine[2]
            start_idx = int(aLine[3])
            end_idx = int(aLine[4])
            entity_name = aLine[5]

            if doc_id not in label_dict:
                label_dict[doc_id] = [{}, {}]
            label_dict[doc_id][0][start_idx] = [entity_label, entity_name]
            label_dict[doc_id][1][end_idx] = 1

            # break
    return label_dict


def get_label(index, idx_start_dict, idx_end_dict, label):
    if index in idx_start_dict:
        return idx_start_dict[index][0]
    if index in idx_end_dict:
        return "O"
    return label


def split_corpus(corpus, index, idx_start_dict, idx_end_dict, separators, splitters):
    label = "O"
    pre_label = "O"
    word = []
    rst = []
    for i, c in enumerate(corpus):
        index += 1
        label = get_label(index-1, idx_start_dict, idx_end_dict, label)
        # print(c, index, label)
        if c in separators + splitters:
            if len(word) > 0:
                # print(index)
                rst.append("".join(word) + "\t" + pre_label)
                # print("".join(word) + "\t" + pre_label)
            if c in separators:
                rst.append(c + "\t" + label)
                # print(c + "\t" + label)
            if c == "." and i < len(corpus)-1 and corpus[i+1] not in "0123456789":
                rst.append("")
                # print()
            word = []
            continue
        word.append(c)
        pre_label = label
    return index, rst


def standoff2conll(dataset_name):
    label_dict = load_dict("data/chemprot_" + dataset_name + "_entities.tsv")

    separators = [".", ",", "(", ")", "[", "]", "/", ":", "=", "+"]
    splitters = [" ", '\u2002', '\u2009']
    corpus = []
    with codecs.open("data/chemprot_" + dataset_name + "_abstracts.tsv", encoding="utf-8") as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            doc_id = int(aLine[0])
            title = aLine[1]
            abstract = aLine[2]

            index = 0
            word = []
            idx_start_dict = label_dict[doc_id][0]
            # print(idx_start_dict)
            idx_end_dict = label_dict[doc_id][1]

            index, rst = split_corpus(title, index, idx_start_dict, idx_end_dict, separators, splitters)
            # break
            corpus.append(rst)
            index += 1
            index, rst = split_corpus(abstract, index, idx_start_dict, idx_end_dict, separators, splitters)
            corpus.append(rst)
    return corpus


def write_corpus(wfile, diction_corpus):
    wfp = open(wfile, "w")
    for corpus in diction_corpus:
        for c in corpus:
            if c == "":
                wfp.write("\n")
            else:
                wfp.write(c.split("\t")[0] + " ")
    wfp.close()


def write_dataset(wfile, dataset_corpus):
    wfp_1 = open("data/" + wfile + "_raw.txt", "w")
    wfp_2 = open("data/" + wfile + "_labeled.txt", "w")
    for corpus in dataset_corpus:
        for c in corpus:
            wfp_1.write(c.split("\t")[0] + "\n")
            wfp_2.write(c + "\n")
    wfp_1.close()
    wfp_2.close()


def main():
    corpus = []
    corpus.extend(standoff2conll("training"))
    corpus.extend(standoff2conll("test"))

    diction_corpus = random.sample(corpus, int(0.5*len(corpus)))
    train_corpus = random.sample(corpus, int(0.4*len(corpus)))
    test_corpus = random.sample(corpus, int(0.1*len(corpus)))

    write_corpus("data/corpus.txt", diction_corpus)
    write_dataset("train", train_corpus)
    write_dataset("test", test_corpus)


            # if count == 0:
            #     break
            # count -= 1


if __name__ == "__main__":
    main()
