#!/usr/bin/env python2.7

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