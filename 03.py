#!/usr/bin/env python
#*-*coding: utf-8 *-*

#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite F Feminino ou M Masculino: ')
print(sexo)

if sexo.upper() == 'M':
    print ('(+) Sexo escolhido: Masculino')
elif sexo.upper() == 'F':
    print('(+) Sexo escolhido: Feminino')
else:
    print('(-) Caractere invalido! Tente novamente')

