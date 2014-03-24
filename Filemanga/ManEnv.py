#!/usr/bin/env python2.7
import os

class IndexDir():
    """encargada de la gestion y personalizacion de directorios"""
    def __init__(self):
        
        #prepara el area de trabajo en cada llamada

        self.WORKING_DIR = os.environ['HOME'] + '/Documentos/Manga_to_pdf'

        self.TMP = os.environ['HOME'] + '/.manga_to_pdf/tmp'
        
        self.LIBRARY_ZIP = os.environ['HOME'] + '/Documentos/Manga_to_pdf/library/zip'
        
        self.DESCOMPRESSED_ZIP = os.environ['HOME'] + '/.manga_to_pdf/tmp/images'

        self.MODIFIED_IMAGES = os.environ['HOME'] + '/.manga_to_pdf/tmp/images_modified'

        self.IMGDIR  = os.environ['HOME'] + '/Documentos/Manga_to_pdf/library/directory'

        self.LIBRARY = '/home/lokiteitor/Documentos/Manga_to_pdf/library'

        self.l_path = [self.TMP,self.LIBRARY_ZIP,self.DESCOMPRESSED_ZIP,self.MODIFIED_IMAGES]

    def MakeDirs(self):
        
        if not os.path.exists(self.WORKING_DIR):
        	os.mkdir(self.WORKING_DIR)

        for i in self.l_path:
        	if not os.path.exists(i):
        		os.makedirs(i)

    def SetWorkingDir(self,path):

        self.WORKING_DIR = path