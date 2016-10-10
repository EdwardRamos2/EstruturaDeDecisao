#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

n1 = float(input("Valor1: "))
n2 = float(input("Valor2: "))
n3 = float(input("Valor3: "))


if n1 < n2 < n3:
    print(n1)

if n1 < n3 < n2:
    print(n1)

if n2 < n1 < n3:
    print(n2)

if n2 < n3 < n1:
    print(n2)

if n3 < n1 < n2:
    print(n3)

if n3 < n2 < n1:
    print(n3)

if n1 == n2 == n3:
   print("invalido")
