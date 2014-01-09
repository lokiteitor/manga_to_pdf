#!/usr/bin/env python2.7

import os
import ManEnv



def DeleteTrash(path=ManEnv.TMP):

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            obj =  os.path.join(root, name)
            os.remove(obj)
        for name in dirs:
            if not os.path.islink(name):
                os.rmdir(os.path.join(root, name))
            else:
                problem = os.path.join(root,name)
                print "se ha encontrado un enlace simbolico en el directorio se recomienda que revice en archivo %s" %problem





