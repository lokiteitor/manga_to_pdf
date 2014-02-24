#!/usr/bin/python2.7
from distutils.core import setup

import os
import re
import shutil


"""definimos el tipo de distro y su respectivo modulo FileImage que abra de utilizar"""

distro = os.uname()[2]

if re.search("ARCH",distro):
    os.remove('Filemanga/FileImage.py')
    shutil.move('parches/FileImage.py','Filemanga/')


"""prepara el area de trabajo en cada llamada"""

WORKING_DIR = os.environ['HOME'] + '/Documentos/Manga_to_pdf'

TMP = os.environ['HOME'] + '/.manga_to_pdf/tmp'

LIBRARY_ZIP = os.environ['HOME'] + '/Documentos/Manga_to_pdf/library/zip'
DESCOMPRESSED_ZIP = os.environ['HOME'] + '/.manga_to_pdf/tmp/images'

MODIFIED_IMAGES = os.environ['HOME'] + '/.manga_to_pdf/tmp/images_modified'


IMGDIR = LIBRARY_ZIP = os.environ['HOME'] + '/Documentos/Manga_to_pdf/library/directory'


l_path = [TMP,LIBRARY_ZIP,DESCOMPRESSED_ZIP,MODIFIED_IMAGES]


if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

for i in l_path:
    if not os.path.exists(i) and not os.path.isdir(i):
        os.makedirs(i)

setup(
    name='manga_to_pdf'
    , url='http://www.desarrolloslkt.tk'
    , author='David Delgado'
    , author_email='lokiteitor513@gmail.com'
    , version='2.0.0a_build_130' # remember to change me for new versions!
    , description='sencillo programa que gestina el manga del usuario de forma totalmente autonoma'
    , long_description=open('README.txt').read()
    , scripts=['mangatopdf.py']
    , packages=['Filemanga','parches']
    , license='GPL'

    )