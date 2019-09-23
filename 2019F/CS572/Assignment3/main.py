#!/bin/python
#-*- coding: utf8 -*-

from node import Node


def find_path(node, node_dict):
    path = [node.six_tuple]
    while node.parent != node.index:
        node = node_dict[node.parent]
        path.append(node.six_tuple)
    print(path)


def main():
    index = 0
    n = Node(index, (0, 0, 0, 3, 3, 1))
    index += 1
    node_dict = {}
    node_dict[index] = n
    visited = set()
    visited.add(n.six_tuple)
    queue_list = [n]

    # bfs
    while len(queue_list) > 0:
        n = queue_list.pop(0);
        print(len(queue_list))
        for s in n.successors():
            node = Node(index, s)
            node.parrent = n.index
            if not n.valid():
                continue
            # print(node_dict)
            index += 1
            node_dict[index] = node
            queue_list.append(node)

            if node.six_tuple == (3,3,1,0,0,0):
                # print(node.six_tuple)
                find_path(node, node_dict)
                exit(0)


if __name__ == "__main__":
    main()
