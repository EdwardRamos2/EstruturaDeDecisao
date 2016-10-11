#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A

#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:

#      Média de Aproveitamento  Conceito
#      Entre 9.0 e 10.0        A
#      Entre 7.5 e 9.0         B
#      Entre 6.0 e 7.5         C
#      Entre 4.0 e 6.0         D
#      Entre 4.0 e zero        E

#    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO”$


print("      Média de Aproveitamento  Conceito")
print("      Entre 9.0 e 10.0        A")
print("      Entre 7.5 e 9.0         B")
print("      Entre 6.0 e 7.5         C")
print("      Entre 4.0 e 6.0         D")
print("      Entre 4.0 e zero        E")


nota1 = float(input("Insira primeira nota: "))
nota2 = float(input("Insira segunda nota: "))



soma = (nota1 + nota2)
media = (soma / 2)
print(media)

if media >= 9.0 and media <= 10.0:
    print("Primeira Nota: " + str(nota1))
    print("Segunda Nota: " + str(nota2))    
    print("Sua media: " + str(media))
    print("(+) Conceito (A)")
    print("Parabens!!! APROVADO")

if media >= 7.5 and media <= 9.0:
    print("Primeira Nota: " + str(nota1))
    print("Segunda Nota: " + str(nota2))    
    print("Sua media: " + str(media))
    print("(+) Conceito (B)")
    print("Parabens!!! APROVADO")


if media >= 6.0 and media <=7.5:
    print("Primeira Nota: " + str(nota1))
    print("Segunda Nota: " + str(nota2))    
    print("Sua media: " + str(media))
    print("(+) Conceito (C)")
    print("Parabens!!! APROVADO")

if media >= 4.0 and media <=6.0:
    print("Primeira Nota: " + str(nota1))
    print("Segunda Nota: " + str(nota2))    
    print("Sua media: " + str(media))
    print("(+) Conceito (D)")
    print("(-) REPROVADO")

if media <= 4.0 and media >= 0:
    print("Primeira Nota: " + str(nota1))
    print("Segunda Nota: " + str(nota2))    
    print("Sua media: " + str(media))
    print("(+) Conceito (E)")
    print("(-) REPROVADO")


