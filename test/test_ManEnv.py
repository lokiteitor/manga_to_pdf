#!/usr/bin/env python2.7

import ManEnv
import os

print ManEnv.l_path

for i in ManEnv.l_path:
    if os.path.exists(i):
        print i