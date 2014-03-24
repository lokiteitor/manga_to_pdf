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
import commands

import FileMan

class Descompress():
	"""encargada de descomprimir cualquier archivo comprimido sin importar el tipo
	asi como tambien comprimir archivos y administrarlos"""
	def __init__(self,mensaje,indexdir):
		self.indexdir = indexdir

		self.mensaje = mensaje

	def UnComMult(self,lst):

		self.valid = self.mensaje.getValidList(lst)

		for i in self.valid:

			tp = self.getType(i)

			if tp == "zip":

				self.UnCompressZip(i)
				name = os.path.basename(i)
				self.MoveToLibrary(i,name)

			if tp == "rar":
				self.UnCompressRar(i)
				mov = os.path.basename(i)
				self.MoveToLibrary(i,mov)

	def getType(self,archive):
		"""devuelve el tipo de comprecion"""
		
		if zipfile.is_zipfile(archive):
			typ = "zip"

		elif os.path.splitext(archive)[1] == ".rar":

			typ = "rar"

		else:
			typ =self.getOtherType(archive)

			if typ == "unsoported":
				print "tipo de archivo no soportado"
		return 	typ


	def UnCompressZip(self,zp):
		"""descomprime los zip de manera individual en el lugar indicado"""
		
		with zipfile.ZipFile(zp,'r') as zip:

			check  = zip.namelist()

			if zip.getinfo(check[0]).file_size == 0:

				valid = FileMan.ComparateImagePdf(os.path.split(check[0])[0]) #atencion a esta funcion al traducir

				if valid[0] or valid[0] == valid[1] == False:

					zip.extractall(self.indexdir.DESCOMPRESSED_ZIP + '/')
				else:

					zip.extractall(self.indexdir.DESCOMPRESSED_ZIP + '/')

					os.rename(self.indexdir.DESCOMPRESSED_ZIP + '/' + check[0],valid[2])

			else:
				destinyImg = self.indexdir.DESCOMPRESSED_ZIP + "/" + os.path.splitext(os.path.basename(zp))[0] + '/'

				zip.extractall(destinyImg)

	def UnCompressRar(self,path):

		destiny = self.getDestinyrar(path)

		path = path.replace(' ','\\ ')
		destiny = destiny.replace(' ','\\ ')

		orden = path + ' ' + destiny

		os.system('unrar x -r -inul %s'%orden)


	def MoveToLibrary(self,zp,name):
		"""gestiona los zip ya utilizados"""

		if os.path.exists(self.indexdir.LIBRARY_ZIP + '/' + name):
			
			print "el archivo ya existe en la libreria zip"
			os.remove(zp)

		else:	
			
			shutil.move(zp,self.indexdir.LIBRARY_ZIP + '/')
			print "se ha reubicado el archivo %s a /library/zip" %name

	def getDestinyrar(self,path):

		name = os.path.basename(path)
		name = os.path.splitext(name)[0]

		name = self.indexdir.DESCOMPRESSED_ZIP + '/' + name + '/'

		os.mkdir(name)

		return name

	def getOtherType(self,path):

		path = path.replace(' ','\\ ')

		typ = commands.getoutput("file %s"%path)

		if typ.find("RAR"):
			output = "rar"
		else:
			output = "unsoported"

		return output


class ExaileCompress(Descompress):
	"""descomprime los archivos perdidos encontrados en las busquedas recursivas"""
	def __init__(self):
		pass