# -*- coding: utf-8 -*-

print("-" * 30, " Cálculo de imc ", "-" * 30) 

#Entrada de dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura: "))

#Cálculo
imc = peso / (altura ** 2)

#Saída de dados
print(f"\nSeu imc é de: {imc:.2f}\n")

#Condicionais
if (imc < 18.5):
    print("Abaixo do Ideal")
elif (imc >= 18.5) and (imc <= 24.9):
    print("Peso Ideal")
elif (imc >= 25) and (imc <= 29.9):
    print("Levemente acima do ideal")
elif (imc >= 30) and (imc <= 34.9):
    print("Peso Obesidade grau I")
elif (imc >= 35) and (imc <= 39.9):
    print("Obesidade grau II (severa)")
elif (imc >= 40):
    print("Obesidade grau III (mórbida)")

print("-" * 30, " Fim do programa ", "-" * 30) 