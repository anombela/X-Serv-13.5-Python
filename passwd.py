#!/usr/bin/python
#Alfosno Nombela Moreno

#abrir fichero
fich=open("/etc/passwd","r")
#leer lineas
lineas = fich.readlines()
dicc = {}

for linea in lineas:
    conf = linea.split(':')
    #me quedo primer y ultimo elemento
    username = conf[0]
    shell=conf[-1][:-1]  # para quitar el \ el -1
    dicc[username] = shell

##print dicc
print dicc["root"]
print len (dicc)

try:
    print dicc["imaginario"]   #no existe
except KeyError:
    print "Usuario imaginario no existe"