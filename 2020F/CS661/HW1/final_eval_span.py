#!/bin/python
# -*- coding: utf8 -*-

'''
Description: word level f1 and span level f1
Auther: Yuepei Li
Date: 2020-09-07
'''


def compute_precision_recall_f1(fname, labels):
    tp = 0
    pp = 0
    np_ = len(labels)
    with open(fname, encoding="utf-8") as fp:
        sentences = []
        sent = []
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 5:
                sentence_start = index_end + 1
                continue
            index_start = int(aLine[0])
            index_end = int(aLine[1])
            entity_name = aLine[2]
            entity_type = aLine[4]
            if entity_type == "None":
                continue
            pp += 1
            if entity_name+entity_type+str(index_start)+str(index_end) in labels:
                tp += 1
    if pp == 0:
        p = 0
    else:
        p = float(tp) / float(pp)
    if np_ == 0:
        r = 0
    else:
        r = float(tp) / float(np_)
    if p == 0 or r == 0:
        f1 = 0
    else:
        f1 = float(2 * p * r) / float((p + r))
    return p, r, f1


def get_true_labels(fname):
    labels = {}
    index = 0
    with open(fname, encoding="utf-8") as fp:
        entity = []
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 2:
                index += 1
                continue
            name = aLine[0]
            type = aLine[1]

            if not type == "O":
                if last_type == type:
                    entity.append(name)
                else:
                    if len(entity) > 0:
                        labels["_".join(entity)+last_type+str(entity_start)+str(index)] = 1
                    entity = [name]
                    entity_start = index
            else:
                if len(entity) > 0:
                    labels["_".join(entity)+last_type+str(entity_start)+str(index)] = 1
                entity = []
            last_type = type
            index += 1
    return labels


def compute_precision_recall_f1_word(pred_file, label_file):
    labels = []
    with open(label_file) as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 2:
                continue
            labels.append(aLine[-1])
    preds = []
    with open(pred_file) as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 5:
                continue
            for i in range(int(aLine[1]) - int(aLine[0])):
                preds.append(aLine[-1] if not aLine[-1] == "None" else "O")

    tp = 0
    pp = 0
    np_ = 0
    for i in range(len(labels)):
        if not labels[i] == "O":
            np_ += 1
        if not preds[i] == "O":
            pp += 1
            if preds[i] == labels[i]:
                tp += 1
    if pp == 0:
        p = 0
    else:
        p = float(tp) / float(pp)
    if np_ == 0:
        r = 0
    else:
        r = float(tp) / float(np_)
    if p == 0 or r == 0:
        f1 = 0
    else:
        f1 = float(2 * p * r) / float((p + r))
    return p, r, f1


def main():
    labels = get_true_labels("data/train_labeled.txt")
    p, r, f = compute_precision_recall_f1("data/train_decoded.txt", labels)
    print(p,r,f)
    p, r, f = compute_precision_recall_f1_word("data/train_decoded.txt", "data/train_labeled.txt")
    print(p,r,f)
    pass


if __name__ == "__main__":
    main()
