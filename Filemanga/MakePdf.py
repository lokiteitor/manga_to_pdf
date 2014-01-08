#!/usr/bin/env python2.7



import config
import os
import shutil
from reportlab.pdfgen import canvas



def Check(title=None):

    files = os.listdir(config.MODIFIED_IMAGES)

    for i in files:

        path = config.MODIFIED_IMAGES + '/' + i

        if os.path.isdir(path):
            Make_Document(os.listdir(path),path + '/',i)

    return


def Make_Document(files,path,title):
    Document = canvas.Canvas(title + '.pdf')
    files.sort()

    for i in files:
        print i
        image = path + i
        Document.drawImage(image,0,0)
        Document.showPage()

    Document.save()
    search = os.getcwd() + '/' + title + '.pdf'
    shutil.move(search,config.WORKING_DIR + '/')

    return