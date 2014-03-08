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

import ManEnv
import os
import shutil
from reportlab.pdfgen import canvas

def order(dsd,lst):
    aqui = dsd
    min = "1000.jpg"
    lon = dsd
    while lon < len(lst):

        if lst[lon] < min:
            min = lst[lon]
        lon = lon + 1
    return min , aqui


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
        #################
        listimg =self.orderlst(listimg)
        # debo de incluir un metodo de ordenamiento correcto en esta parte



        if self.mensaje.othersize.has_key(title):
            special = self.mensaje.othersize[title].keys()
        else:
            special = []

        for i in listimg:
            print "agregando %s al pdf" %i

            if special.count(i) > 0:

                Document.setPageSize(self.mensaje.othersize[title][i])

            image = path + i
            Document.drawImage(image,0,0)
            Document.showPage()

        Document.save()
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

        # aplicar un filtro para solo las imagenes

        for i in range(len(lst)):
            min , dst = order(i,lst)

            if min != "1000.jpg":
                lst.remove(min)
                lst.insert(dst,min)

        return lst



