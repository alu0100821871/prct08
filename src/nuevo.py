#!/usr/bin/python
#!encoding:UTF-8
import modulo
import moduloerror

n_test = (10, 100, 1000, 10000, 100000)
umbral = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)

intervalo = 10
fichero = open('comprobar_moduloerror.txt', 'w')
for u in umbral:
  for n in n_test:
    s = moduloerror.error (intervalo, n, u)
    fichero.write ( str(s) + '\n')
fichero.close()