#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
Date: 2020-04-26
'''

from Util import point_cmp

class EventNode:
    is_site_event = True
    site = (0, 0)
    lowest_point = [0, 0]
    dis_leaf_pointer = None

    def __init__(self, ise, site, lp, dlp):
        self.is_site_event = ise
        self.site = site
        self.lowest_point = lp
        self.dis_leaf_pointer = dlp

    def show(self):
        print(self.site, end=" ")

    def is_site_event(self):
        return True


class EventQueue:
    def __init__(self):
        self.q = []

    def add(self, s):
        n = EventNode(True, s, (0,0), None)
        self.q.append(n)

    def show(self):
        for n in self.q:
            n.show()

    def not_empty(self):
        return True


class Voronoi:
    def construct(self):
        sites = [(0,0), (0,1), (1,0)]
        sites = sorted(sites, key=lambda x: (x[1], -x[0]), reverse=True)
        event_q = EventQueue()
        for site in sites:
            event_q.add(site)
        event_q.show()
        # while event_q.not_empty():
        #     e = event_q.get_next()
        #     if e.is_site_event():
        #         HandleSiteEvent(e.p)
        #     else:
        #         HandleCircleEvent(e.p)


def main():
    v = Voronoi()
    v.construct()


if __name__ == "__main__":
    main()
