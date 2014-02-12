#!/usr/bin/env python2.7

import FileZip as fz
import Mensaje
import FileMan


def main():

    men = Mensaje.Mensaje()

    sea = FileMan.Manage()

    des = fz.Descompress(men)

    des.UnComMult(sea.SearchCompress())






if __name__ == '__main__':
    main()