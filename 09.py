#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A


#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

n1 = int(input("Valor1: "))
n2 = int(input("Valor2: "))
n3 = int(input("Valor3: "))

if n1 > n2 > n3:
    print(n1,n2,n3)
if n1 > n3 > n2:
    print(n1,n3,n2)

if n2 > n1 > n3:
    print(n2,n1,n3)
if n2 > n3 > n1:
    print(n2,n3,n1)

if n3 > n2 > n1:
    print(n3,n2,n1)
if n3 > n1 > n2:
    print(n3,n1,n2)

