#!/usr/bin/env python2.7
from Filemanga import FileMan,FileImage,Mensaje,ManEnv
import glob
import os
class salida():

    def __init__(self):
        pass

    def manipulate(self,path):

        print path

        listimg = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.jpeg")

        if len(listimg):

            key = (True,path)
            print listimg

        else:
            key = (False,path)

        return key


    def exploreimgdir(self):

        for root, dirs, files in os.walk(ManEnv.MODIFIED_IMAGES, topdown=False):

            for name in dirs:
                print os.path.join(root,name)






def main():

    men = Mensaje.Mensaje()

    fl = FileMan.Manage()

    testMan = salida()

    fl.CheckImgDir(testMan)

    img = FileImage.ManipulateImg(men)

    fl.CheckImgDir(img)

    testMan.exploreimgdir()





main()