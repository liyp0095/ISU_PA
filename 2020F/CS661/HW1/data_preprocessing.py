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


def load_dict(fname):
    label_dict = {}
    with open("data/chemprot_sample_entities.tsv") as fp:
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


def split_sentence(sentence, index, idx_start_dict, idx_end_dict, separators, splitters):
    label = "O"
    pre_label = "O"
    word = []
    for c in sentence:
        index += 1
        label = get_label(index-1, idx_start_dict, idx_end_dict, label)
        # print(c, index, label)
        if c in separators + splitters:
            if len(word) > 0:
                # print(index)
                print("".join(word) + "\t" + pre_label)
            if c in separators:
                print(c + "\t" + label)
            if c == ".":
                print()
            word = []
            continue
        word.append(c)
        pre_label = label
    return index


def main():
    label_dict = load_dict("")

    separators = [".", ",", "(", ")", "[", "]", "/"]
    splitters = [" ", '\u2002', '\u2009']
    count = 3
    with open("data/chemprot_sample_abstracts.tsv") as fp:
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

            index = split_sentence(title, index, idx_start_dict, idx_end_dict, separators, splitters)
            # break
            index += 1
            index = split_sentence(abstract, index, idx_start_dict, idx_end_dict, separators, splitters)

            # if count == 0:
            #     break
            # count -= 1


if __name__ == "__main__":
    main()
