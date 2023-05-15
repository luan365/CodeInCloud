# -*- coding: utf-8 -*-

x = 0
y = 0

print(10 * "-", " ler dois valores e imprimir os valores inteiros no intervalo. ", "-" * 10)
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if(x < y):
    for k in range(x, y + 1):
        print(k)
else:
    for k in reversed(range(y, x + 1)):
        print(k)


print("\n" * 5)

print(10 * "-", " Valor médio ", "-" * 10)
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
print("Media = ",(x + y) / 2)
print(f"maior = {x} menor = {y}" if x > y else f"maior = {y} menor = {x}")

print("\n" * 5)

print(10 * "-", " Cálculo de fatorial ", "-" * 10)
x = int(input("Fatorial: "))
fact = 1

for k in range (1, x + 1):
    fact *= k

    print(k, " ", fact)

print("\n" * 5)


print(10 * "-", " Tabuáda ", "-" * 10)
x = int(input("Digite a quantidade de dias: "))
for k in range(0, 10 + 1): print(f"{x} * {k} = ", x * k)

print("\n" * 5)


print(10 * "-", " Fermentação de vinho ", "-" * 10)
x = int(input("Digite um número: "))
menor = 0

for k in range (0, x + 1):
    Td = 0.011 * (k ** 3) - 0.3 * (k ** 2) + (0.04 * k)
    if(Td < menor): menor = Td
print(f"O dia com a menor temperatura precista é de {menor:.2f}°C")

print("\n" * 5)


print(10 * "-", " Advinhe o número do computador ", "-" * 10)

import random

num = 0
tentativa = 0
parar = "s"
print("Advinhe um numéro entre 0 e 100\n\n")
while parar == "s":
    parar = "n"
    numComp = random.randint(0,100)
    while (num != numComp) and (parar == "n"): 
        tentativa += 1
        num = int(input("DIGITE UM NÚMERO: "))
        print(numComp)
        if(num == numComp): print("\nVocê acertou o número")
        else:
            print("O seu número é maior que o do computador" if num > numComp else "O seu número é menor que o do computador")
            parar = input("Deseja parar?(s/n) ")
            parar = parar.lower()
    parar = input("Deseja iniciar uma nova partida? ")

print("\n" * 5)


print(10 * "-", " Diviíveis por x em um intervalo ", "-" * 10)
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
div = int(input("Por qual número quer verificar se é divisivel: "))

for k in range(x, y + 1):
    if (k % div == 0): print(k)

print("\n" * 5)


print(10 * "-", " Listagem ", "-" * 10)
lista=["GUARANI", "SÃO PAULO", "PALMEIRAS", "CRUZEIRO",
"SANTOS", "FERROVIÁRIA", "JUVENTUS", "GOIÁS",
"ÍBIS", "SINOP"]
x = 0
try:
    while x <= len(lista):
        print(x, " - ", lista[x])
        x += 1
except:
    input("Aperte [ENTER] para continuar: ")
print("\n" * 5)


print(10 * "-", " Jokenpô ", "-" * 10)
parar = "s"
pntPlayer = 0
pntComp = 0
parar = "n"
while(parar == "n"): 
    x = 5
    if(x > 2) or (x < 0): x = int(input("Digite um número \n0 - Pedra\n1 - Papel\n2 - Tesoura\n"))
    else:
        y = random.randint(0, 2)
        if(x == y): print("Empate")
        elif(x == 0):
            if(y == 2): 
                print("Você ganhou")
                pntPlayer += 1
        elif(x == 1):
            if(y == 0): 
                print("Você ganhou")
                pntPlayer += 1
        elif(x == 2):
            if(y == 1): 
                print("Você ganhou")
                pntPlayer += 1
            else:
                print("Você perdeu")
                pntComp += 1
        else:
            print("Você perdeu")
            pntComp +=1
        print(f"Pontuação\n{pntPlayer:2d}   |   {pntComp:1}")
        parar = input("Deseja parar?(s/n) ")

nome = "Luan Ferreira"

iniciais = ""
for k in nome.split():
    iniciais += k[0]
print (iniciais)