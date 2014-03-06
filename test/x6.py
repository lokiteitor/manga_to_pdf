#!/usr/bin/env python2.7

def order(dsd):
    aqui = dsd
    min = 100000
    lon = dsd
    while lon < len(lst):

        if lst[lon] < min:
            min = lst[lon]
        lon = lon + 1
        print min
    if min != 100000:
        lst.remove(min)
        lst.insert(aqui,min)

    print lst


lst = [5,3,8,4,1,12,15,14,0,2,6]
print lst


for i in range(len(lst)):

    order(i)