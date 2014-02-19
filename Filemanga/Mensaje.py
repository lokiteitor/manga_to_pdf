#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
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

        self.othersize[dicc][clave] = tam
