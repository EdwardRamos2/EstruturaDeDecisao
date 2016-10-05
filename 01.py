#!/usr/bin/env python
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/04/2016 U.S.A

#Faça um Programa que peça dois números e imprima o maior deles. 

valor1 = raw_input("Enter o primeiro valor: ")
valor2 = raw_input('Enter o segundo valor: ')

if valor1 == valor2:
    print("Valores iguais!!")
    print("(+) Primeiro valor: %s") % (str(valor1))
    print("(+) Segundo valor: %s") % (str(valor2))
elif valor1 >= valor2:
    print("(+) Primeiro valor e maior: %s") % (str(valor1))
elif valor1 <= valor2:
    print("(+) Segundo valor e maior: %s") % (str(valor2))

else:
    ("(-) error")
