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

import glob
import ManEnv
import FileImage
import shutil


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
            if not os.path.islink(name):
                if not name == 'zip':
                    if not name == 'library':
                        if not name == 'directory':
                            f = FileImage.ManageImg(os.path.join(root,name))
                            f.Manipulate_Img()
                            if not os.path.join(root,name) == ManEnv.IMGDIR:
                                shutil.move(os.path.join(root,name),ManEnv.IMGDIR + '/' + name)

    os.chdir(origin)



class Manage():
    """clase principal encargada de todas las tareas de administracion de archivos"""
    def __init__(self):
        self.tmp = ManEnv.TMP
        self.origin = os.getcwd()

        os.chdir(ManEnv.WORKING_DIR)
        self.pdf = glob.glob("*.pdf")


    def DeleteTrash(self):
        """metodo encargado de la recoleccion de basurae los archivos temporales"""
        for root, dirs, files in os.walk(self.tmp, topdown=False):
            for name in files:
                obj =  os.path.join(root, name)
                os.remove(obj)
            for name in dirs:
                if not os.path.islink(name):
                    os.rmdir(os.path.join(root, name))
                else:
                    problem = os.path.join(root,name)
                    print "se ha encontrado un enlace simbolico en el directorio \
                    se recomienda que revice en archivo %s" %problem
                    print "ubicado en %s" %self.tmp



    def CheckPdfExist(self,mensaje):
        """metodo que se asegura de que los archivos candidatos no se repitan
         con aquellos existentes"""

        # analizamos las posibilidades en base a los archivos candidato
        posibility = glob.glob("*.zip")

        for root, dirs, files in os.walk(ManEnv.WORKING_DIR):
            for name in dirs:
                if not os.path.islink(name):
                    if not name == 'zip':
                        if not name == 'library':
                            posibility.append(name)

        # comparamos los archivos candidato con los pdf
        for i in posibility:

            name = os.path.splitext(i)[0]
            name = name + ".pdf"

            if self.pdf.count(name):
                # pasamos los errores a otro objeto que los maneje(Mensaje.Mensaje)
                mensaje.ExistPdf(name,i)