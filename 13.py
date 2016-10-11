#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A


#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
#s digitar outro valor deve aparecer valor inválido. 


dia = int(input("Insira o dia da semana! -> 1-Domingo, 2- Segunda, etc: "))

if dia == 1:
    print("1 - Domingo")
elif dia == 2:
    print("2 - Segunda")
elif dia == 3:
    print("3 - Terca")
elif dia == 4:
    print("4 - Quarta")
elif dia == 5:
    print("5 - Quinta")
elif dia == 6:
    print("6 - Sexta")
elif dia == 7:
    print("7 - Sabado")
else:
    print("Invalido")
