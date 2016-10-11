#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/10/2016 U.S.A


#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#            Salário Bruto: (5 * 220)        : R$ 1100,00
#            (-) IR (5%)                     : R$   55,00  
#            (-) INSS ( 10%)                 : R$  110,00
#            FGTS (11%)                      : R$  121,00
#            Total de descontos              : R$  165,00
#            Salário Liquido                 : R$  935,00

hora = float(input("Insira quantidade da hora trabalhada: "))
print(hora) #DEBUG
v_horas = float(input("Insira o valor da hora trabalhada: "))
print(v_horas) #DEBUG
salario = float(v_horas * hora)
print(salario) #DEBUG

if float(salario) <= 900:
    inss = (float(salario) * 0.10)
    sindicato = (float(salario) * 0.03)
    ir = (salario * 0.05)
    fgts = (salario * 0.11)
    total_desc = (inss)
    salario_desc = (salario - total_desc)   
    print(inss) #DEBUG
    print(sindicato) #DEBUG
    print(ir)   #DEBUG
    print(fgts) #DEBUG
    print(total_desc)  #DEBUG  
    print(salario_desc) #DEBUG    
    print("Salario Bruto: (5 * 220)   : R$ %r" % salario)
    print("(-) IR (5%)                : R$ ISENTO")
    print("(-) INSS (9%)              : R$ " + str(inss))
    print("FGTS (11%)                 : R$ " + str(fgts))   
    print("Total de descontos:        : R$ " + str(total_desc))    
    print("Salário Liquido:           : R$ " + str(salario_desc))
    print("(+) Valor referente ao sindicato: R$" + str(sindicato))
    
if float(salario) >= 900 and salario <= 1500:
    inss = (float(salario) * 0.10)
    sindicato = (float(salario) * 0.03)
    ir = (salario * 0.05)
    fgts = (salario * 0.11)
    total_desc = (ir + inss)
    salario_desc = (salario - total_desc)   

    print("Salario Bruto: (5 * 220)   : R$ %r" % salario)
    print("(-) IR (5%)                : R$ " + str(ir))
    print("(-) INSS (9%)              : R$ " + str(inss))
    print("FGTS (11%)                 : R$ " + str(fgts))   
    print("Total de descontos:        : R$ " + str(total_desc))    
    print("Salário Liquido:           : R$ " + str(salario_desc))
    print("(+) Valor referente ao sindicato: R$" + str(sindicato))


if float(salario) >= 1500 and salario <= 2500:
    inss = (float(salario) * 0.10)
    sindicato = (float(salario) * 0.03)
    ir = (salario * 0.10)
    fgts = (salario * 0.11)
    total_desc = (ir + inss)
    salario_desc = (salario - total_desc)   

    print("Salario Bruto: (5 * 220)   : R$ %r" % salario)
    print("(-) IR (5%)                : R$ " + str(ir))
    print("(-) INSS (9%)              : R$ " + str(inss))
    print("FGTS (11%)                 : R$ " + str(fgts))   
    print("Total de descontos:        : R$ " + str(total_desc))    
    print("Salário Liquido:           : R$ " + str(salario_desc))
    print("(+) Valor referente ao sindicato: R$" + str(sindicato))



if float(salario) >= 2500:
    inss = (float(salario) * 0.10)
    sindicato = (float(salario) * 0.03)
    ir = (salario * 0.20)
    fgts = (salario * 0.11)
    total_desc = (ir + inss)
    salario_desc = (salario - total_desc)   

    print("Salario Bruto: (5 * 220)   : R$ %r" % salario)
    print("(-) IR (5%)                : R$ " + str(ir))
    print("(-) INSS (9%)              : R$ " + str(inss))
    print("FGTS (11%)                 : R$ " + str(fgts))   
    print("Total de descontos:        : R$ " + str(total_desc))    
    print("Salário Liquido:           : R$ " + str(salario_desc))
    print("(+) Valor referente ao sindicato: R$" + str(sindicato))









