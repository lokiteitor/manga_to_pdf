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
import re
import os
import shutil


import ManEnv

from reportlab.pdfgen import canvas

def order(dsd,lst):
    # ordena los numeros del tipo 001.jpg por simple comparacion
    aqui = dsd
    mn = "1000.jpg"
    lon = dsd
    while lon < len(lst):

        if lst[lon] < mn:
            mn = lst[lon]
        lon = lon + 1
    return mn , aqui

def orderint(dsd,lst):
    # ordena los numeros del tipo 10.jpg por simple comparacion
    # emplea una conversion a enteros por lo que puede gastar mas recursos

    aqui = dsd
    mn = 1000
    lon = dsd

    while lon < len(lst):
        can = int(os.path.splitext(lst[lon])[0])

        if can < mn:
            mn = can
            aqmn = lon
        lon = lon + 1
    mn = lst[aqmn]

    return mn , aqui


class MakePdf():
    """clase encargada de construir los pdf siguiendo la informacion
    proporcionada por el modulo Mensaje"""
    def __init__(self, mensaje):
        
        self.mensaje = mensaje

    def checklist(self):

        dirslist = os.listdir(ManEnv.MODIFIED_IMAGES)

        for i in dirslist:

            print "convirtiendo %s en pdf" %i

            path = ManEnv.MODIFIED_IMAGES + '/' + i
            title = i

            if os.path.isdir(path):
                listimg = os.listdir(path)
                self.Make_Document(path+'/',title,listimg)

        
    def Make_Document(self,path,title,listimg):

        Document = canvas.Canvas(title + '.pdf')
        listimg =self.orderlst(listimg)



        if self.mensaje.othersize.has_key(title):
            special = self.mensaje.othersize[title].keys()
        else:
            special = []

        for i in listimg:
            print "agregando %s al pdf" %i

            if special.count(i) > 0:
                # revisa si esa pagina en especial cuenta con una peticion 
                # de tamano personalizado lo busca y lo aplica
                # la busqueda se realiza desde el diccionario de mensaje

                Document.setPageSize(self.mensaje.othersize[title][i])

            image = path + i
            Document.drawImage(image,0,0)
            Document.showPage()

        Document.save()
        self.mensaje.exception(02,title)
        #retorna la ruta al documento generado
        search = os.getcwd() + '/' + title + '.pdf'

        self.movepdf(title,search)


    def movepdf(self,title,gen):

        if not os.path.exists(ManEnv.WORKING_DIR + '/' + title + '.pdf'):
            shutil.move(gen,ManEnv.WORKING_DIR + '/')
            print "se ha creado el archivo %s en el directorio de trabajo" %title

            print "tareas finalizadas satisfactoriamente"

        else:
            print "el archivo %s ya exite" %title
            os.remove(gen)

    def orderlst(self,lst):
        # metodo de ordenamiento revisa el formato de la cadena
        # y elige el proceso adecuado
        lst.sort()

        # aplicar un filtro para solo las imagenes
        for x in lst[0]:

            if re.match(x,"0\d\d.jpg"):
                for i in range(len(lst)):
                    mn , dst = order(i,lst)

                    if mn != "1000.jpg":
                        lst.remove(mn)
                        lst.insert(dst,mn)

            if re.match(x,"[1-9][0-9].jpg") or re.match(x,"[1-9].jpg"):
                #problema del hola
                #print "hola"
                for i in range(len(lst)):
                    mn , dst = orderint(i,lst)

                    if mn != 1000:
                        lst.remove(mn)
                        lst.insert(dst,mn)                

        return lst



