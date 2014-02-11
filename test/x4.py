#!/usr/bin/env python2.7

class mensaje():

    def __init__(self):
        
        self.diccionario = {}

    def add_diccionario(self,nom):

        self.diccionario[nom] = {}

    def addkey(self,dicc,clave,valor):

        self.diccionario[dicc][clave] = valor

class emisor():
    def __init__(self,mensaje):

        self.mensaje = mensaje

    def getlist(self,dicc):

        for i in range(10):
            
            self.addkey(dicc,i,i)


    def addkey(self,dicc,clave,valor):

        self.mensaje.addkey(dicc,clave,valor)

    def getdicc(self):

        print self.mensaje.diccionario

    def otherdicc(self,nom):

        print self.mensaje.diccionario[nom]

men = mensaje()

emi = emisor(men)


men.add_diccionario('other')

emi.getlist('other')
emi.getdicc()
emi.otherdicc('other')