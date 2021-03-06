#!/usr/bin/env python2.7


import os

"""prepara el area de trabajo en cada llamada"""

WORKING_DIR = os.environ['HOME'] + '/Documentos/Manga_to_pdf'

TMP = os.environ['HOME'] + '/.manga_to_pdf/tmp'

LIBRARY_ZIP = os.environ['HOME'] + '/Documentos/Manga_to_pdf/library/zip'
DESCOMPRESSED_ZIP = os.environ['HOME'] + '/.manga_to_pdf/tmp/images'

MODIFIED_IMAGES = os.environ['HOME'] + '/.manga_to_pdf/tmp/images_modified'


IMGDIR  = os.environ['HOME'] + '/Documentos/Manga_to_pdf/library/directory'

LIBRARY = '/home/lokiteitor/Documentos/Manga_to_pdf/library'


l_path = [TMP,LIBRARY_ZIP,DESCOMPRESSED_ZIP,MODIFIED_IMAGES]


if not os.path.exists(WORKING_DIR):
	os.mkdir(WORKING_DIR)

for i in l_path:
	if not os.path.exists(i):
		os.makedirs(i)