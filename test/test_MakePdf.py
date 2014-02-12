#!/usr/bin/env python2.7

import MakePdf
import Mensaje
import FileImage


def main():
    
    men = Mensaje.Mensaje()
    men = Mensaje.Mensaje()
    
    img =  FileImage.ManipulateImg(men)

    img.manipulate()


    mk = MakePdf.MakePdf(men)

    mk.checklist()

if __name__ == '__main__':
    main()