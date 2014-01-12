#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# licenciado bajo GPL https://github.com/lokiteitor/manga_to_pdf/blob/master/LICENSE

import Image
import ManEnv
import shutil
import os
import glob
from reportlab.lib.pagesizes import A4


def Manage_Image(path = ManEnv.DESCOMPRESSED_ZIP):
	"""proporciona un filtro de archivos y directorios candidatos para el 
	posterior manejo por la funcion Manipulate"""

	origin = os.getcwd()

	os.chdir(path)

	members = os.listdir(os.getcwd())

	for i in members:

		if os.path.isdir(i):
			os.chdir(i)

			dest = ManEnv.MODIFIED_IMAGES + '/' + i

			if not os.path.exists(dest):
				os.mkdir(ManEnv.MODIFIED_IMAGES + '/' + i)


			file_valid = glob.glob('*.jpg') + glob.glob('*.png') + glob.glob('*.jpeg')

			print "los siguentes archivos estan listos para ser verificados" + str(file_valid)


			# error 008: las funciones embebidas en otras podrian causar
			# futuros errores derivados de sus dependecias
			if len(file_valid) > 0:
				Manipulate(file_valid,i)

			os.chdir(path)

	os.chdir(origin)

	return


def Manipulate(candidate,path):
	"""manipula las imagenes de tal forma que puedan caber en un documento pdf
	en caso de que no las redimensiona y las reemplaza 
	acepta como arguementos un directorio y una lista de archivos que solo
	debe contener imagenes"""

	for i in candidate:
		ubi = os.getcwd() + '/' + i
		im = Image.open(ubi)

		if A4[0] < im.size[0] or A4[1] < im.size[1]:
			print "modificando el archivo %s" %i
			if im.size[0] > im.size[1]:

				mod = im.rotate(90)

				if mod.size[0] > A4[0] or mod.size[1] > A4[1]:
					ult = mod.resize((595,841))

					ult.save(ManEnv.MODIFIED_IMAGES + '/' + path + '/' + i)
				else:
					mod.save(ManEnv.MODIFIED_IMAGES + '/' + path + '/' + i)

			else:
				mod = im.resize((595,841))
				mod.save(ManEnv.MODIFIED_IMAGES + '/' + path + '/' + i)

		else:
			shutil.move(i,ManEnv.MODIFIED_IMAGES + '/' + path + '/' + i)

	return

