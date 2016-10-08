#!/usr/bin/env python
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/07/2016 U.S.A


#Faça um Programa que leia três números e mostre o maior deles.


num1 = int(input('Insira o primeiro numero: '))
num2 = int(input('Insira o segundo numero: '))
num3 = int(input('Insira o terceiro numero: '))


if num1 > num2 > num3:
    print('(+) Primeiro numero e o maior: %d' % num1)
    
if num1 > num3 > num2:
    print('(+) Primeiro numero e o maior: %d' % num1)
    
if num2 > num1 > num3:
    print('(+) Segundo numero e o maior: %d' % num2)
    
if num2 > num3 > num1:
    print('(+) Segundo numero e o maior: %d' % num2)
    
if num3 > num1 > num2:
    print('(+) Terceiro numero e o maior: %d' % num3)
    
if num3 > num2 > num1:
    print('(+) Terceiro numero e o maior: %d' % num3)
    
if num1 == num2 == num3:        
    print('(+) Numeros repetidos sao anulados')
