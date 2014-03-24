#!/usr/bin/env python2.7


cadena = "00a.jpg"

sub = cadena.split('.')[0]
print sub
print '#################'

ent = '001 '

ent = int(ent)

print ent
print '#################'



if sub.isdigit():
    print 'ok'
else:
    print 'caracter'
print '#################'

lst = ['23 .jpg', '14 .jpg', '00a .jpg', '27 .jpg', '15 .jpg', '30 .jpg', '35 .jpg', '08 .jpg', '02 .jpg', '05 .jpg', '33 .jpg', '00b .jpg', '00c .jpg', '28 .jpg', '22 .jpg', '38 .jpg', '000 .jpg', '04 .jpg', '09 .jpg', '07 .jpg', '37 .jpg', '17 .jpg', '16 .jpg', '29 .jpg', '19 .jpg', '01a .jpg', '32 .jpg', '01b .jpg', '18 .jpg', '06 .jpg', '10 .jpg', '39 .jpg', '34 .jpg', '21 .jpg', '25 .jpg', '11 .jpg', '26 .jpg', '12 .jpg', '13 .jpg', '24 .jpg', '31 .jpg', '03 .jpg', '20 .jpg', '36 .jpg']
otherlst = []

cont = 2
while cont > 0:
    for i in lst:

        x = i.replace(' ','')
        print x

        if not x.split('.')[0].isdigit():
            print '1'
            print i

            otherlst.append(i)
            lst.remove(i)
    cont = cont - 1

print lst.sort()
print lst
print '############'
print otherlst
print '##########'
for x in lst:
    tr = int(x.split('.')[0])
    print tr



