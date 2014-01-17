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
from Filemanga import FileZip,FileImage,MakePdf,FileMan


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

	FileMan.CheckPdfExist()

	FileMan.CheckImgDir()
	FileZip.CheckZip()
	FileImage.Manage_Image()
	MakePdf.Check()
	FileMan.DeleteTrash()



if __name__ == '__main__':
	main(sys.argv[1:])