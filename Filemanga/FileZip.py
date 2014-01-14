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
import zipfile
import zlib
import os
import glob
import ManEnv
import shutil
import FileMan


def CheckZip(path=ManEnv.WORKING_DIR):
	"""filtra los resultados y permite la ejucucion en cada uno de los objetivos"""

	origin = os.getcwd()
	os.chdir(path)
	search = glob.glob('*.zip')

	if len(search) == 0:
		print "no se han encontrado archivos .zip en manga_to_pdf porfavor ingrese los ficheros a descomprimir en manga_to_pdf"


	elif len(search) > 0:

		print "se han encontrado los siguientes archivos listos para ser descomprimidos"
		for i in search:
			print i

	for i in search:
		
		if zipfile.is_zipfile(i):

			print "descomprimiendo el archivo " + i
			UnCompress(i)

	os.chdir(origin)

	return



def UnCompress(obj):
	"""descomprime los archivos y crea la carpeta destino si es necesario"""


	with zipfile.ZipFile(obj,'r') as zip:


		path_final = (ManEnv.DESCOMPRESSED_ZIP + "/" + os.path.splitext(obj)[0] + '/')

		check  = zip.namelist()

		if zip.getinfo(check[0]).file_size == 0:

			valid = FileMan.ComparateImagePdf(os.path.split(check[0])[0])

			if valid[0] or valid[0] == valid[1] == False:

				zip.extractall(ManEnv.DESCOMPRESSED_ZIP + '/')
			else:

				zip.extractall(ManEnv.DESCOMPRESSED_ZIP + '/')

				os.rename(ManEnv.DESCOMPRESSED_ZIP + '/' + check[0],valid[2])

		else:

			zip.extractall(path_final)

	# error 008: mover este procedimento a nuevo modulo mencionado en FileImage	

	if os.path.exists(ManEnv.LIBRARY_ZIP + '/' + obj):
		print "el archivo ya existe en la libreria zip"
		os.remove(obj)
	else:	

		shutil.move(obj,ManEnv.LIBRARY_ZIP + '/')
		print "se ha reubicado el archivo %s a /library/zip" %obj

	return

# error 006: implementar comprecion de manga una vez implementados
