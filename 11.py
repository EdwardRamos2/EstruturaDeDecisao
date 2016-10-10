#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A



#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa 
#que calculará os reajustes.

#    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento. 

salario = (input("Insira o salario: "))

if float(salario) <= 280:
    aumento = (float(salario) * 0.20)
    total = (float(aumento) + float(salario))
    print("Salario antes do reajuste: %r" % salario)
    print("Houve aumento de 20% ") 
    print("Valor aumento: %r" % aumento)
    print("Valor total: %r" % total)

if float(salario) > 280 and float(salario) <= 700:
    aumento = (float(salario) * 0.15)
    total = (float(aumento) + float(salario))
    print("Salario antes do reajuste: %r" % salario)
    print("Houve aumento de 15% ") 
    print("Valor aumento: %r" % aumento)
    print("Valor total: %r" % total)

if float(salario) > 700 and float(salario) <= 1500:
    aumento = (float(salario) * 0.10)
    total = (float(aumento) + float(salario))
    print("Salario antes do reajuste: %r" % salario)
    print("Houve aumento de 10% ") 
    print("Valor aumento: %r" % aumento)
    print("Valor total: %r" % total)

if float(salario) >= 1500.00:
    aumento = (float(salario) * 0.05)
    total = (float(aumento) + float(salario))
    print("Salario antes do reajuste: %r" % salario)
    print("Houve aumento de 5% ") 
    print("Valor aumento: %r" % aumento)
    print("Valor total: %r" % total)

