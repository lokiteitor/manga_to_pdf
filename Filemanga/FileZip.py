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

import os

import shutil
import FileMan

import ManEnv


#debe de crearse una clase encargada de buscar los archivos candidatos de cualquier tipo



#------------------------------------------------------------------------------
class Descompress():
	"""encargada de todas las tareas de descompresion de ficheros dependiendo
	del tipo de estos """
	def __init__(self,path,des=ManEnv.LIBRARY_ZIP):
		self.pathOriginal = path
		self.destinozip = des + os.path.splitext(path)[0] + '/'
		self.destinyImg = ManEnv.DESCOMPRESSED_ZIP + "/" + os.path.splitext(os.path.basename(self.pathOriginal))[0] + '/'

		self.name = os.path.basename(path)
		self.type = ""


	def get_Type(self):

		if zipfile.is_zipfile(self.pathOriginal):
			self.type = "zip"

		elif os.path.splitext(self.pathOriginal)[1] == ".rar":

			self.type = "rar"
			# ejecutar comando de descomprecion de rar

		return self.type

	def Uncompress(self):

		if self.type == "zip":

			self.UnCompressZip()

	def UnCompressZip(self):


		with zipfile.ZipFile(self.pathOriginal,'r') as zip:

			check  = zip.namelist()

			if zip.getinfo(check[0]).file_size == 0:

				valid = FileMan.ComparateImagePdf(os.path.split(check[0])[0]) #atencion a esta funcion al traducir

				if valid[0] or valid[0] == valid[1] == False:

					zip.extractall(ManEnv.DESCOMPRESSED_ZIP + '/')
				else:

					zip.extractall(ManEnv.DESCOMPRESSED_ZIP + '/')

					os.rename(ManEnv.DESCOMPRESSED_ZIP + '/' + check[0],valid[2])

			else:

				zip.extractall(self.destinyImg)

	def MoveToLibrary(self):
		# este metodo no guarda el archivo en el lugar correcto
		if os.path.exists(ManEnv.LIBRARY_ZIP + '/' + self.name):
			print "el archivo ya existe en la libreria zip"
			os.remove(self.pathOriginal)
		else:	
			shutil.move(self.pathOriginal,ManEnv.LIBRARY_ZIP + '/')
			print "se ha reubicado el archivo %s a /library/zip" %self.name
