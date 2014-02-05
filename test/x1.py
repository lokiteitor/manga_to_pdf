#!/usr/bin/env python2.7

class hola():
    def __init__(self):
        pass
    def res(self):
        print "hola"

class saludo():
    def __init__(self):
        pass

    def mensaje(self,obj):

        obj.res()


i = saludo()
h = hola()

i.mensaje(h)