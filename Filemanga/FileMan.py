#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# licenciado bajo GPL https://github.com/lokiteitor/manga_to_pdf/blob/master/LICENSE

import os
import sys
import glob
import ManEnv
import FileImage


def DeleteTrash(path=ManEnv.TMP):

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            obj =  os.path.join(root, name)
            os.remove(obj)
        for name in dirs:
            if not os.path.islink(name):
                os.rmdir(os.path.join(root, name))
            else:
                problem = os.path.join(root,name)
                print "se ha encontrado un enlace simbolico en el directorio se recomienda que revice en archivo %s" %problem
                print "ubicado en %s" %path


def CheckPdfExist():

    origin = os.getcwd()

    os.chdir(ManEnv.WORKING_DIR)

    search = glob.glob('*.pdf')

    posibility = glob.glob('*.zip')


    for i in posibility:


        name = os.path.splitext(i)[0]
        name = name + ".pdf"

        if search.count(name):
            print "el archivo %s ya existe desea sobrescribirlo?" %name
            print "(s/n)"

            res = raw_input()

            if res == "s":
                continue

            elif res == "n":
                print "deseas renombrar el archivo %s" %i
                print "(s/n)"
                ren = raw_input()

                if ren == "s":
                    print "introduce el nuevo nombre"
                    nom = raw_input()
                    os.rename(i,nom + '.zip')

                elif ren == "n":
                    sys.exit()

                else:
                    pass

            else:
                pass

    os.chdir(origin)


def ComparateImagePdf(dirname):

    origin = os.getcwd()
    os.chdir(ManEnv.WORKING_DIR)

    pdf = glob.glob('*.pdf')

    checklist = [True,False,""]


    for i in pdf:
        if os.path.splitext(i)[0] == dirname:
            checklist[0] = False
            print "el archivo %s ya existe desea sobrescribirlo?" %i
            print "(s/n)"
            
            res = raw_input()

            if res == "s":
                checklist[1] = False

            elif res == "n":
                checklist[1] = True
                print "introduce el nuevo nombre "
                nom = raw_input()

                redirect = ManEnv.DESCOMPRESSED_ZIP + '/' + nom

                checklist[2] = redirect


    os.chdir(origin)
    return checklist


def CheckImgDir():
    origin = os.getcwd()
    os.chdir(ManEnv.WORKING_DIR)

    for root, dirs, files in os.walk(ManEnv.WORKING_DIR):
        for name in dirs:
            if not os.path.islink(name) and name != "zip" and "library":
                FileImage.Manage_Image(os.path.join(root,name))

    os.chdir(origin)
