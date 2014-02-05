#!/usr/bin/env python2.7
import os

class Mensaje():
    """clase encargada de manejar todas las eventualidades entre el programa y 
    el usuario"""
    def __init__(self):
        self.blacklist = []


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
        print "aqui"

        if len(self.blacklist) > 0:

            for i in lst:

                if self.blacklist.count(os.path.basename(i)):

                    lst.remove(i)

        return lst





