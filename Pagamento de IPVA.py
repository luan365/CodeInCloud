# -*- coding: utf-8 -*-
import datetime

print("-" * 30, " Pagamento de IPVA ", "-" * 30) 

#Declaração de variáveis
data = datetime.datetime.now()
mes = ""
boole = True
placa = 0

while boole:
#Entrada de dados
    placa = int(input("Digite o ultimo número da placa do seu carro:  "))
#Cálculo
    if (placa >= 0) and (placa <= 9):
        boole = False
    if (placa == 1):
        mes = "janeiro"
    elif (placa == 2):
        mes = "fevereiro"
    elif (placa == 3):
        mes = "março"    
    elif (placa == 4):
        mes = "abril"
    elif (placa == 5):
        mes = "maio"
    elif (placa == 6):
        mes = "junho"
    elif (placa == 7):
        mes = "julho"
    elif (placa == 8):
        mes = "agosto"
    elif (placa == 9):
        mes = "setembro"
    elif (placa == 0):
        mes = "outubro"
    else:
        boole = True
        print("Valor incorreto, digite um número entre 0 e 9")
       
#Saída de dados
print(f"o mês do pagamento é {mes}\n")
if(placa < data.month):
    print("Pagamento atrasado")
elif (placa == data.month):
    print("Pagamento até este mês")
else:
    print("Sem atraso")


print("-" * 30, " Fim do programa ", "-" * 30) 
