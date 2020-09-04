#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
Date: 2020-04-28
'''

from Util import find_intersect

class BstNode:
    def __init__(self, is_leaf, pi, pj):
        self.is_leaf = is_leaf
        self.pi = pi
        self.pj = pj
        self.left = None
        self.right = None

    def show_tree(self):
        if self.left:
            self.left.show_tree()
        print(self.pi, self.pj, end="||")
        if self.right:
            self.right.show_tree()


class BalancedBst:
    def __init__(self):
        self.root = None

    def search(self, node, p, ly):
        if node.is_leaf:
            return node
        else:
            breakpoint = find_intersect(node.pi, node.pj, ly)
            if breakpoint[0] > p[0]:
                return self.search(node.left, p, ly)
            else:
                return self.search(node.right, p, ly)

    def balance(self):
        pass

    def insert(self, p):
        if self.root == None:
            self.root = BstNode(True, p, None)
        else:
            insert_position = self.search(self.root, p, p[1]+0.01)
            print(insert_position.pi, insert_position.pj, p)
            pi = insert_position.pi
            pj = p
            insert_position.left = BstNode(False, pj, pi)
            insert_position.right = BstNode(True, pj, None)
            insert_position.left.left = BstNode(True, pj, None)
            insert_position.left.right = BstNode(True, pi, None)
            insert_position.pi = pi
            insert_position.pj = pj
            insert_position.is_leaf = False
        self.show()

    def show(self):
        self.root.show_tree()
        print()


def main():
    b = BalancedBst()
    b.insert((0,3))
    b.insert((1,2))
    b.insert((2,1))
    b.insert((4,0))
    b.show()
    pass


if __name__ == "__main__":
    main()
