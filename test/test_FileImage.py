#!/usr/bin/env python2.7

import FileImage
import Mensaje

def main():

    men = Mensaje.Mensaje()
    
    img =  FileImage.ManipulateImg(men)

    img.manipulate()

    print men.othersize


if __name__ == '__main__':
    main()