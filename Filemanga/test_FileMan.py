#!/usr/bin/env python2.7

import FileMan
import FileImage
import Mensaje
import ManEnv

def main():

    mnsg = Mensaje.Mensaje()

    fl =  FileMan.Manage()
    img = FileImage.ManipulateImg(mnsg)

    fl.DeleteTrash()
    fl.CheckPdfExist(mnsg)
    fl.CheckImgDir(img)


if __name__ == '__main__':
    main()