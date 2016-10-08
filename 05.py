#!/usr/bin/env python
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/07/2016 U.S.A

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez. 

nota1 = input("Insira a primeira NOTA: ")
nota2 = input("Insira a segunda NOTA: ")

conv1 = float(nota1)
conv2 = float(nota2)

total = (conv1 + conv2)
media = (total / 2)

if media >= 7:
   print('(+) Aluno APROVADO')

elif media <= 7:
   print('(-) Aluno REPROVADO')

elif media == 10:
   print('(+) Aluno APROVADO com Disticao!')

