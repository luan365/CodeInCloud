# -*- coding: utf-8 -*-

print("-" * 30, " Ano Bissexto ", "-" * 30)

ano = int(input("Digite um ano: "))

if((ano % 4) == 0): print(f"O ano {ano} é bissxeto")
else: print(f"O ano {ano} não é bissexto")

print("\n\n")


print("-" * 30, " Data válida ", "-" * 30)

ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (de 1 a 12): "))
dia = int(input("Digite o dia: "))

diasTotal = 0
bissexto = False
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    bissexto = True

if (mes == 2):
    if bissexto: diasTotal = 29
    else: diasTotal = 28
elif mes in (4, 6, 9, 11): diasTotal = 30
else: diasToal = 31

if (dia >= 1) and (dia <= diasTotal): print("Data válida")
else: print("Data inválida")


