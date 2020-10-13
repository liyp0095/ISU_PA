#!/bin/python
# -*- coding: utf8 -*-

'''
Description: generate dictionary
Auther: Yuepei Li
Date: 2020-09-06
'''

import random

book = set()

def load_data(fname):
    label_dict = {}
    with open(fname, encoding="utf-8") as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            doc_id = int(aLine[0])
            entity_label = aLine[2]
            start_idx = int(aLine[3])
            end_idx = int(aLine[4])
            entity_name = aLine[5]

            if entity_name.lower() in book:
                continue
            label_dict[entity_name] = entity_label
            book.add(entity_name.lower())

            # break
    return label_dict


def write_core_dict(wfile):
    label_dict = {}
    d1 = load_data("data/chemprot/chemprot_training/chemprot_training_entities.tsv")
    d2 = load_data("data/chemprot/chemprot_test/chemprot_test_entities.tsv")
    d3 = load_data("data/chemprot/chemprot_development/chemprot_development_entities.tsv")
    label_dict.update(d1)
    label_dict.update(d2)
    label_dict.update(d3)

    wfp = open(wfile, "w")
    for entity_name, entity_label in random.sample(label_dict.items(), int(0.6*len(label_dict))):
        wfp.write(entity_label + "\t" + entity_name + "\n")
    wfp.close()


def write_full_dict(wfile, filename, theta):
    wfp = open(wfile, "a+")
    with open(filename, encoding="utf-8") as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            score = float(aLine[0])
            name = aLine[1]
            if score > theta:
                wfp.write(name + "\n")
    wfp.close()


def main():
    write_core_dict("data/dict_core.txt")
    write_full_dict("data/dict_full.txt", "data/autophrase/AutoPhrase_multi-words.txt", 0.35)
    write_full_dict("data/dict_full.txt", "data/autophrase/AutoPhrase_single-word.txt", 0.7)
    pass


if __name__ == "__main__":
    main()
