#!/usr/bin/env python

valor1 = input('Enter o primeiro valor: ')
valor2 = input('Enter o segundo valor: ')

if valor1 == valor2:
    print("Valores iguais!!")
    print("(+) Primeiro valor: %d") % (valor1)
    print("(+) Segundo valor: %d") % (valor2)
elif valor1 >= valor2:
    print("(+) Primeiro valor e maior: %d") % (valor1)
elif valor1 <= valor2:
    print("(+) Segundo valor e maior: %d") % (valor2)

else:
    ("(-) error")
