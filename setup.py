#!/usr/bin/env python2.7
from distutils.core import setup


setup(
    name='manga_to_pdf'
    , url='http://www.desarrolloslkt.tk'
    , author='David Delgado'
    , author_email='lokiteitor513@gmail.com'
    , version='1.1.0' # remember to change me for new versions!
    , description='sencillo programa que gestina el manga del usuario de forma totalmente autonoma'
    , long_description=open('README.txt').read()
    , scripts=['mangatopdf.py']
    , packages=['Filemanga']
    , license='GPL'

    )