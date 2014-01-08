#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# licenciado bajo GPL https://github.com/lokiteitor/manga_to_pdf/blob/master/LICENSE

import sys
import getopt
import FileZip
import FileImage
import MakePdf


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


	FileZip.CheckZip()
	FileImage.Manage_Image()
	MakePdf.Check()





if __name__ == '__main__':
	main(sys.argv[1:])