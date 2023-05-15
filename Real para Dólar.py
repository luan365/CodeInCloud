# -*- coding: utf-8 -*-

print("-" * 30, " Real para Dolar ", "-" * 30)

# Valor em real
preco = float(input("Digite o valor a ser convertido para dolar: "))

# Conversão para dólar
dolar = preco * 5.14

print(f"R${preco:.2f} em dolar é R${dolar:.2f}\n")
print("-" * 30, " Fim do programa ", "-" * 30)