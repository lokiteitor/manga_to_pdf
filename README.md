acerca de:
----------

manga to pdf es un sencillo script para sistemas basados en unix  que te permite
gestionar tu manga de forma totalmente autonoma. Desde la descomprecion del
archivo .zip hasta la conversion en formato pdf para ofrecer una total
portabilidad de tu manga

2014 David Delgado - lokiteitor513@gmail.com GPL license



puedes obtener la ultima version en desarrollo desde el repositorio git alogado
en:

https://github.com/lokiteitor/manga_to_pdf

Instalacion:
------------

las depencias necesarias para el funcionamiento de este programa son:

reportlab
pil o pillow dependiendo de tu distro (pil = debian/ubuntu, pillow = archlinux )
python2.7

para poder instalarlo:

En Debian/ubuntu y derivadas:

apt-get install python-reportlab
apt-get install python-imaging

En archlinux:

python2-reportlab
python2-pillow


Una vez satisfechas estas dependencias solo debes de ejecutar en el directorio
donde descomprimiste el programa:

$python2.7 setup.py install 


Como usarlo:
------------

el procedimiento es sencillo

una vez instalado se generara el directorio ~/Documentos/Manga_to_pdf

en donde debes de pegar tus archivos .zip o carpetas con las imagenes del manga
en formatos .jpg .jpeg y .png.
seguido de esto solo deberas de ejecutar:

$mangatopdf.py

en la terminal he iniciara el proceso de conversion. Una vez finalizado esto en
la carpeta anteriormente mencionada se encontrara tu manga listo en formato pdf

ademas se genera el directorio library donde encontraras tus archivos .zip y/o
tus directorios que hallas ingresado para su conversion



