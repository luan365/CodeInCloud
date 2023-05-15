# -*- coding: utf-8 -*-

print("-" * 30, " Par ou ímpar ", "-" * 30)

x = int(input("Digite um número: "))

if (x % 2 == 0):
    print("par")
else:
    print("impar")


print("-" * 60, "\n\n")


print("-" * 30, " Se iguais ou diferentes ", "-" * 30)
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if(a == b):
    c = a + b
    print(c)
else: 
    c = a * b
    print(c)
        
print("-" * 60, "\n\n")


print("-" * 30, " Classificação de um triângulo ", "-" * 30)

x = int(input("Digite um lado do triângulo: "))
y = int(input("Digite outro do triângulo: "))
z = int(input("Digite outro do triângulo: "))

if (a == b == c): print("triângulo equilátero")
elif (a == b) or (b == c) or (c == a): print("triângulo isóceles")
else: print("triângulo escaleno")

print("-" * 60, "\n\n")

print("-" * 30, " Válido em um intervalo ", "-" * 30)
x = int(input("Digite um número"))
y = int(input("Digite outro número"))

if (x < y): z = int(input("Digite um número"))
elif z == y: print("limite superior")
elif z == x: print("limite inferior")
elif x < z < y: print("dentro do intervalo")
elif z < x: print("abaixo do inferior")
elif z > y: print("acima do intervalo")
else: print("erro")

print("-" * 60, "\n\n")


print("-" * 30, " Equação de segundo grau ", "-" * 30)
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

d = (b ** 2) - (4 * a * c)

if d < 0: print("Erro")
elif a == 0:
    x = -b / (2*a)
    print(f"x = {x}")
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f"Ax1 = {x1} e x2 = {x2}")

print("-" * 60, "\n\n")


print("-" * 30, " Cálculo de média ", "-" * 30)
ax = float(input("Digite a nota 1: "))
x1 = float(input("Digite o peso da nota 1: "))

x = float(input("Digite a nota 2: "))
x2 = float(input("Digite o peso da nota 2: "))
media = ((x * x1) + (x * x2)) / 2
if (c == 10): print("Aprovado com Distinção")
elif(c >= 7): print("Aprovado")
else: print("Reprovado")

print("-" * 60, "\n\n")


print("-" * 30, " Dia da semana ", "-" * 30)

dia = int(input("Digite um número inteiro de 1 à 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Número inválido. Digite um número de 1 à 7.")















