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
import glob

import Image #cambiar esto por pil
from reportlab.lib.pagesizes import A4

import ManEnv

class ManipulateImg():
    def __init__(self,mensaje):
        self.origin = os.getcwd()
        self.mensaje = mensaje

        os.chdir(ManEnv.DESCOMPRESSED_ZIP)

    def manipulate(self,other_path=None):

        if other_path != None:
            if other_path.find(ManEnv.LIBRARY) == -1:
                key = self.make_only_img(path=other_path)
                return key
        
        else:
            self.get_directory()


    def get_directory(self,path=ManEnv.DESCOMPRESSED_ZIP):

        os.chdir(path)

        #error path no valido o incompleto

        dirs  = os.listdir(path)

        for i in dirs:

            if os.path.isdir(i):
                
                os.chdir(i)

                file_valid = glob.glob('*.jpg') + glob.glob('*.png')\
                                     + glob.glob('*.jpeg')


                if len(file_valid) > 0:
                    destiny = self.getDestiny(i,os.getcwd())
                    print "los siguentes archivos estan listos \
                    para ser verificados" + str(file_valid)

                    self.manipulate_list_img(destiny,file_valid)
                else:

                    other_dirs = os.listdir(os.getcwd())

                    if len(other_dirs) > 0:
                        self.get_directory(os.getcwd())

                os.chdir(path)


    def getDestiny(self,nom,path):

        dest = ManEnv.MODIFIED_IMAGES + '/' + nom

        if re.match("\d+",nom):
            name = os.path.dirname(path)

            if name == ManEnv.MODIFIED_IMAGES:

                dest = ManEnv.MODIFIED_IMAGES + '/' + nom
            else:
                if name.find(nom):
                    dest = ManEnv.MODIFIED_IMAGES + '/' + os.path.basename(name)
                else:
                    dest = ManEnv.MODIFIED_IMAGES + '/' + os.path.basename(name) + '/' + nom


        if not os.path.exists(dest):
            os.makedirs(dest)

        return dest

    def manipulate_list_img(self,destiny,listfile):

        for i in listfile:

            ubi = os.getcwd() + '/' + i

            try:
                img = Image.open(ubi)
            except:

                self.mensaje.exception(01,i,ubi)
                # esta excepcion es debida a un archivo corrupto de origen 
                # y por lo tanto ajeno al programa 
                # el manejo de la excepcion deberia de ser un registro de 
                # esta en el log de eventos del programa

            if A4[0] < img.size[0] or A4[1] < img.size[1]:
                if img.size[0] > img.size[1]:

                    key = os.path.basename(os.getcwd())

                    # obtiene las medidas en puntos y la agraga a un diccionario
                    # bidimensional que esta identificado por el nombre del
                    # directorio
                    pt1 = img.size[0]
                    pt2 = img.size[1]

                    if self.mensaje.othersize.has_key(key):

                        self.mensaje.add_other_size(key,i,(pt1,pt2))

                    else:
                        self.mensaje.adddicc(key)
                        self.mensaje.add_other_size(key,i,(pt1,pt2))

                    img.save(destiny + '/' + i)

                else:
                    mod = img.resize((595,841))
                    mod.save(destiny + '/' + i)

            else:
                img.save(destiny + '/' + i)

    def make_only_img(self,path):

        origin = os.getcwd()

        os.chdir(path)

        for i in self.mensaje.blacklist:
            if path.find(i):
                return

        file_valid = glob.glob('*.jpg') + glob.glob('*.png')\
                        + glob.glob('*.jpeg')

        if len(file_valid) > 0:
            destiny = self.getDestiny(os.path.basename(path),path)
            print "los siguentes archivos estan listos \
            para ser verificados" + str(file_valid)

            self.manipulate_list_img(destiny,file_valid)

            key = (True,path)

        else:
            # en este momento abra que preever la indefinicion correcta del 
            # directorio hijo por lo que creo deberia de tomar el titulo del
            # padre y fusionarlo con el titulo del hijo
            
            other_format = glob.glob('*.*')
            print other_format

            for i in other_format:
                self.mensaje.makeManComp(i)

            key = (False,path)
            # obtenemos la bandera de confirmacion sobre recursividad y
            # los parametros necesarios en caso de ser requerida

        return key
        os.chdir(origin)
