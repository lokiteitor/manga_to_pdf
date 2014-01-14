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




def Check(title=None):

    files = os.listdir(ManEnv.MODIFIED_IMAGES)


    for i in files:
        print "convirtiendo el archivo %s en pdf" %i

        path = ManEnv.MODIFIED_IMAGES + '/' + i

        if os.path.isdir(path):


            Make_Document(os.listdir(path),path + '/',i)

    return


def Make_Document(files,path,title):

    Document = canvas.Canvas(title + '.pdf')
    files.sort()

    for i in files:
        print "agregando %s al pdf" %i
        image = path + i
        Document.drawImage(image,0,0)
        Document.showPage()

    Document.save()
    #retorna la ruta al documento generado
    search = os.getcwd() + '/' + title + '.pdf'


    # error 008

    if not os.path.exists(ManEnv.WORKING_DIR + '/' + title + '.pdf'):
        shutil.move(search,ManEnv.WORKING_DIR + '/')
        print "se ha creado el archivo %s en el directorio de trabajo" %title

        print "tareas finalizadas satisfactoriamente"

    else:
        print "el archivo %s ya exite" %title
        os.remove(search)

    return