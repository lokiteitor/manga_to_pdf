#!/usr/bin/env python2.7
import os


class delete():
    def __init__(self):
        pass

    def DeleteTrash(self):
        """metodo encargado de la recoleccion de basurae los archivos temporales"""
        for root, dirs, files in os.walk(os.environ['HOME'] + '/.manga_to_pdf/tmp', topdown=False):
            for name in files:
                obj =  os.path.join(root, name)
                os.remove(obj)
            for name in dirs:
                if not os.path.islink(name):
                    os.rmdir(os.path.join(root, name))
                else:
                    problem = os.path.join(root,name)
                    print "se ha encontrado un enlace simbolico en el directorio \
                    se recomienda que revice en archivo %s" %problem
                    print "ubicado en %s" %os.environ['HOME'] + '/.manga_to_pdf/tmp'

def main():
    fl = delete()

    fl.DeleteTrash()

if __name__ == '__main__':
    main()
