#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
Date: 2020-10-12
'''

import re

def load_abstract(f_name):
    doc2Id = {}
    id2Doc = {}
    with open(f_name) as fp:
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 3:
                continue
            doc_id = int(aLine[0])
            title = aLine[1]
            abstract = aLine[2]
            clean_key = re.sub('\W+', '', title + abstract[:80])
            doc2Id[clean_key[:80]] = doc_id
            id2Doc[doc_id] = title + "\t" + abstract
    return doc2Id, id2Doc


def main():
    doc2Id, id2Doc = load_abstract("data/chemprot/chemprot_test/chemprot_test_abstracts.tsv")
    # print(doc2Id)
    # exit()
    with open("result/decoded.txt") as fp:
        key_str = ""
        doc_str = ""
        entities = []
        types = []
        doc_id = 0
        doc_index = 0
        entity_id = 1
        for line in fp.readlines():
            aLine = line.strip("\n").split("\t")
            if len(aLine) < 5:
                # sentence_start = index_end + 1
                # match docstr and result
                if doc_str == "":
                    continue
                for i, e in enumerate(entities):
                    # print(doc_str)
                    if e in doc_str and doc_str.index(e) < 10:
                        e_start = doc_str.index(e)
                        offset = e_start + len(e)
                        if doc_str == e:
                            doc_str = ""
                        else:
                            doc_str = doc_str[offset:]
                        if not types[i] == "None":
                            # print(doc_id, e, types[i], doc_index + e_start, doc_index + offset)
                            print("\t".join([str(doc_id), "T"+str(entity_id), types[i], str(doc_index + e_start), str(doc_index + offset), e]))
                            entity_id += 1
                        doc_index += offset
                    else:
                        if " " in e:
                            es = e.split(" ")
                            for et in es:
                                e_start = doc_str.index(et)
                                offset = e_start + len(et)
                                if doc_str == et:
                                    doc_str = ""
                                else:
                                    doc_str = doc_str[offset:]
                                if not types[i] == "None":
                                    print("\t".join([str(doc_id), "T"+str(entity_id), types[i], str(doc_index + e_start), str(doc_index + offset), et]))
                                    entity_id += 1
                                    # print(doc_id, et, types[i], doc_index + e_start, doc_index + offset, T)
                                doc_index += offset
                        else:
                            print(doc_str)
                            print(e)
                    # print(e)
                    # print(doc_str)
                entities = []
                types = []
                key_str = ""
                continue
            # index_start = int(aLine[0])
            # index_end = int(aLine[1])
            entity_name = aLine[2]
            entity_type = aLine[4]
            entities.append(entity_name)
            types.append(entity_type)
            # print(entity_name)

            clean_name = re.sub('\W+', '', entity_name)
            key_str += clean_name
            if doc_str == "" and key_str[:80] in doc2Id:
                # print(key_str[:50])
                doc_id = doc2Id[key_str[:80]]
                doc_str = id2Doc[doc_id]
                doc_index = 0
                entity_id = 1
                # print(doc_id)
                # exit()
    pass


if __name__ == "__main__":
    main()
