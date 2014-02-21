#!/usr/bin/python2.7

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
import sys
import getopt
from Filemanga import FileZip,FileImage,MakePdf,FileMan,Mensaje


def main(argv):
	"""maneja los argumentos y los asigna a variables para su posterior manejo"""
	try:
		options , arg = getopt.getopt(argv, "d:t:",["directorio=","title="])
	except getopt.GetoptError:
		print "el argumento no es valido"
	

	for opt , arg in options:
		if opt in ("-d" , "--directorio"):
			pass

		elif opt in ("-t" , "--title"):
			pass

	print "iniciando proceso"


	# esta funcion de momento es inutil debido a la reimplementacion 
	# por lo que se redisenara de acuerdo a las nuevas capacidades de la 
	# reimplementacion

	fl = FileMan.Manage()

	men = Mensaje.Mensaje()
	
	img = FileImage.ManipulateImg(men)

	fl.CheckPdfExist(men)
	fl.CheckImgDir(img)

	des = FileZip.Descompress(men)

	des.UnComMult(fl.SearchCompress())
	img.manipulate()

	mk = MakePdf.MakePdf(men)

	mk.checklist()


if __name__ == '__main__':
	main(sys.argv[1:])