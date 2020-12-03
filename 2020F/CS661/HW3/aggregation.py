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


def main():
    entity_dicts = []
    for i in range(1, 8):
        entity_dicts.append(read_tsv(str(i) + ".tsv"))

    entity_freq = {}
    entity_cont = {}
    for entity_dict in entity_dicts:
        for entity in entity_dict:
            if not entity in entity_freq:
                entity_freq[entity] = 0
            entity_freq[entity] += 1

            if not entity in entity_cont:
                entity_cont[entity] = entity_dict[entity]

    wfp = open("out.tsv", "w")
    for entity in entity_freq:
        if entity_freq[entity] > 2:
            # print(entity, entity_freq[entity])
            # print(entity_cont[entity])
            wfp.writelines(entity_cont[entity])
    wfp.close()
    pass


if __name__ == "__main__":
    main()
