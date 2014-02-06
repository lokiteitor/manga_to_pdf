#!/usr/bin/env python2.7

class primero():

    def __init__(self):
        
        self.re = [[1,234,4,4,5,65]]

    def res(self,ls):

        for i in self.re:
            ls.append(i)

        return ls

class segundo():

    def __init__(self,men):
        self.obj = men

    def pre(self):

        lst = [12,2343,454,54,2323]

        lt = self.obj.res(lst)

        for i in lt:
            print str(i)

p  = primero()

s = segundo(p)

s.pre()