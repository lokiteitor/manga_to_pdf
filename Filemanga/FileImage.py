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

from PIL import Image #cambiar esto por pil
import ManEnv
import os
import glob
from reportlab.lib.pagesizes import A4

class ManipulateImg():
	def __init__(self,mensaje):
		self.origin = os.getcwd()
		self.mensaje = mensaje

		os.chdir(ManEnv.DESCOMPRESSED_ZIP)

	def manipulate(self):
		self.get_directory


	def get_directory(self):

		dirs  = os.listdir(ManEnv.DESCOMPRESSED_ZIP)

		for i in dirs:

			if os.path.isdir(i):
				
				os.chdir(i)

				file_valid = glob.glob('*.jpg') + glob.glob('*.png')\
									 + glob.glob('*.jpeg')

				if len(file_valid) > 0:
					destiny = self.getDestiny(i)
					print "los siguentes archivos estan listos \
								para ser verificados" + str(file_valid)

					self.manipulate_list_img(destiny,file_valid)

				os.chdir(ManEnv.DESCOMPRESSED_ZIP)


	def getDestiny(self,nom):

		dest = ManEnv.MODIFIED_IMAGES + '/' + nom

		if not os.path.exists(dest):
			os.mkdir(dest)

		return dest

	def manipulate_list_img(self,destiny,listfile):

		for i in listfile:

			ubi = os.getcwd() + '/' + i

			img = Image.open(ubi)

			if A4[0] < img.size[0] or A4[1] < img.size[1]:
				if img.size[0] > img.size[1]:

					# obtiene las medidas en puntos y la agraga a un diccionario
					# bidimensional que esta identificado por el nombre del
					# directorio
					pt1 = img.size[0] * 0.75
					pt2 = img.size[1] * 0.75

					if self.mensaje.othersize.has_key(os.getcwd()):

						self.mensaje.add_other_size(os.getcwd(),i,(pt1,pt2))

					else:
						self.mensaje.adddicc(os.getcwd())
						self.mensaje.add_other_size(os.getcwd(),i,(pt1,pt2))

					img.save(destiny + '/' + i)

				else:
					mod = img.resize((595,841))
					mod.save(destiny + '/' + i)

			else:
				img.save(destiny + '/' + i)
