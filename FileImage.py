#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# licenciado bajo GPL https://github.com/lokiteitor/manga_to_pdf/blob/master/LICENSE

import Image
import config
import shutil
import os
import glob
from reportlab.lib.pagesizes import A4


def Manage_Image():
	origin = os.getcwd()

	os.chdir(config.DESCOMPRESSED_ZIP)

	members = os.listdir(os.getcwd())

	for i in members:

		if os.path.isdir(i):
			os.chdir(i)

			dest = config.MODIFIED_IMAGES + '/' + i

			if not os.path.exists(dest):
				os.mkdir(config.MODIFIED_IMAGES + '/' + i)


			file_valid = glob.glob('*.jpg') + glob.glob('*.png') + glob.glob('*.jpeg')

			Manipulate(file_valid,i)

			os.chdir(config.DESCOMPRESSED_ZIP)

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
			if im.size[0] > im.size[1]:

				mod = im.rotate(90)

				if mod.size[0] > A4[0] or mod.size[1] > A4[1]:
					ult = mod.resize((595,841))

					ult.save(config.MODIFIED_IMAGES + '/' + path + '/' + i)
				else:
					mod.save(config.MODIFIED_IMAGES + '/' + path + '/' + i)

			else:
				mod = im.resize((595,841))
				mod.save(config.MODIFIED_IMAGES + '/' + path + '/' + i)

		else:
			shutil.move(i,config.MODIFIED_IMAGES + '/' + path + '/' + i)

	return


# error 007 implementar funcion encargada de limpiar basura





