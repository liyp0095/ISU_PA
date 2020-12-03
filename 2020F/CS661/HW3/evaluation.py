#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
'''

def read_tsv(f_name):
    entity_dict = {}
    with open(f_name) as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 5 or len(aLine) >= 6:
                continue
            if aLine[0] == "":
                continue
            doc_id = int(aLine[0])
            entity_type = aLine[1]
            entity_name = aLine[4]
            start_idx = int(aLine[2])
            end_idx = int(aLine[3])

            key = str(doc_id) + "_" + entity_type + "_" + str(start_idx) + "_" + str(end_idx)
            entity_dict[key] = line
    return entity_dict


def calc_prf(entity_pred, entity_test):
    # pp: positive, np_:
    # tp: true positive
    tp = 0
    pp = len(entity_pred)
    np_ = len(entity_test)
    for entity in entity_pred:
        if entity in entity_test:
            tp += 1
    # print(pp, tp, np_)
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
    f_name = "out.tsv"
    f_test = "chemprot_test_entities.tsv"
    entity_pred = read_tsv(f_name)
    entity_test = read_tsv(f_test)
    pre, rec, f1 = calc_prf(entity_pred, entity_test)
    print("precision: %f\nrecall: %f\nF1: %f" % (pre, rec, f1))

    pass


if __name__ == "__main__":
    main()
