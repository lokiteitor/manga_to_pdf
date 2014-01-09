#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# licenciado bajo GPL https://github.com/lokiteitor/manga_to_pdf/blob/master/LICENSE

import zipfile
import zlib
import os
import glob
import ManEnv
import shutil



def CheckZip(path=ManEnv.WORKING_DIR):
	"""filtra los resultados y permite la ejucucion en cada uno de los objetivos"""

	origin = os.getcwd()
	os.chdir(path)
	search = glob.glob('*.zip')

	for i in search:
		
		if zipfile.is_zipfile(i):


			UnCompress(i)

	os.chdir(origin)

	return



def UnCompress(obj):
	"""descomprime los archivos y crea la carpeta destino si es necesario"""


	with zipfile.ZipFile(obj,'r') as zip:

		path_final = (ManEnv.DESCOMPRESSED_ZIP + "/" + os.path.splitext(obj)[0] + '/')

		check  = zip.namelist()

		if zip.getinfo(check[0]).file_size == 0:

			zip.extractall(ManEnv.DESCOMPRESSED_ZIP + '/')

		else:

			zip.extractall(path_final)

	# error 008: mover este procedimento a nuevo modulo mencionado en FileImage		

	shutil.move(obj,ManEnv.LIBRARY_ZIP + '/')

	return

# error 006: implementar comprecion de manga una vez implementados
