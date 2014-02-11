#!/usr/bin/env python2.7
import os

class Mensaje():
    """clase encargada de manejar todas las eventualidades entre el programa y 
    el usuario"""
    def __init__(self):
        self.blacklist = []
        self.othersize = {}


    def ExistPdf(self,problem,archive):
        
            print "el archivo %s ya existe desea sobrescribirlo?" %problem
            print "(s/n)"

            res = raw_input()

            if res == "s":
                return

            elif res == "n":
                print "deseas renombrar el archivo %s" %archive
                print "(s/n)"
                ren = raw_input()

                if ren == "s":
                    print "introduce el nuevo nombre"
                    nom = raw_input()
                    os.rename(archive,nom + '.zip')

                elif ren == "n":

                    # agrega el archivo a una lista para su omision
                    # se debe de categorizar esta lista para su posterior uso
                    self.blacklist.append(archive)

                    print "el archivo sera omitido"

    def getBlackList(self):

        return self.blacklist

    def getValidList(self,lst):

        if len(self.blacklist) > 0:

            for i in lst:

                if self.blacklist.count(os.path.basename(i)):

                    lst.remove(i)

        return lst

    # gestiona un diccionario con las medidas personalizadas de las imagenes
    # que haci lo requieran
    def adddicc(self,nom):

        self.othersize[nom] = {}

    def add_other_size(self,dicc,clave,tam):

        # error 010: ver issues

        self.othersize[dicc][clave] = tam



