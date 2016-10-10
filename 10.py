#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

hora = str(input("Em que turno voce estuda? : M- Matutino, V- Vespertino, N- Noturno."))

if "M" in hora:
    print("(+) Matutino  (Bom Dia!) ")

elif "V" in hora:
    print("(+) Vespertino    (Boa Tarde!)")

elif "N" in hora:
    print("(+) Noturno (Boa Noite!)")

else:
    print("(-) Invalidos")


