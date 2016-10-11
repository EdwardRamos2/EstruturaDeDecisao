#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A

#Faça um Programa que leia três números e mostre o maior e o menor deles. 

n1 = input("Valor 1: ")
n2 = input("Valor 2: ")
n3 = input("Valor 3: ")

if n1 > n2 > n3:
   print(n1,n3)
if n1 > n3 > n2:
   print(n1,n2)
if n2 > n1 > n3:
   print(n2,n3)
if n2 > n3 > n1:
   print(n2,n1)
if n3 > n1 > n2:
   print(n3,n2)
if n3 > n2 > n1:
   print(n3,n1)
if n1 == n2 == n3:
   print("Numero repetidos sao invalidos!")
