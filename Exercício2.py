# -*- coding: utf-8 -*-

print("-" * 30, " Cadastro ", "-" * 30)
tentativa = 0
x = 0
senha = -1
escolha = 0
while x != senha:
    if(escolha == 0):
        print("\n--- Menu ---")
        escolha = int(input("\n1- Cadastrar senha \n2- Acesso ao sistema: "))
    elif (escolha == 1): 
        senha = input("\nDigite sua senha: ")
        escolha = 0
    elif(escolha == 2):
        print("--- SISTEMA ---")
        x = input("Digite sua senha: ")
        print("Acesso Permitido" if x == senha else "Acesso negado\n\n")
        tentativa += 1
        print("tentativas = ", tentativa)
    else: 
        print("\nDigite um valor válido")
        escolha = 0
print("\n" * 5)


print("-" * 30, " Classificação de um triângulo ", "-" * 30)

a = int(input("Digite um lado do triângulo: "))
b = int(input("Digite outro do triângulo: "))
c = int(input("Digite outro do triângulo: "))

if (a == b == c): print("triângulo equilátero")
elif (a == b) or (b == c) or (c == a): print("triângulo isóceles")
else: print("triângulo escaleno")

print("\n" * 5)


print("-" * 30, " Par ou ímpar ", "-" * 30)

x = int(input("Digite um número: "))

if (x % 2 == 0):
    print("par")
else:
    print("impar")


print("\n" * 5)


print("-" * 30, " Se a é divisível por b ", "-" * 30)
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if(x % y == 0): print(f"{x} é divisivel por {y}")
else: print(f"{x} não é divisiel por {y}")

print("\n" * 5)


print("-" * 30, " Cálculo de média ", "-" * 30)
ax = float(input("Digite a nota 1: "))
x1 = float(input("Digite o peso da nota 1: "))

x = float(input("Digite a nota 2: "))
x2 = float(input("Digite o peso da nota 2: "))
media = ((x * x1) + (x * x2)) / 2
if (c == 10): print("Aprovado com Distinção")
elif(c >= 7): print("Aprovado")
else: print("Reprovado")

print("\n" * 5)


print("-" * 30, " Conversão de temperatura ", "-" * 30)

x = float(input("Digite a temperatura a ser convertida: "))
dec = int(input("Escolha de qual escala de temperatura deseja converter:\n1- Célsius\n2- Fahrenheit \n3- Rankine\n4- Réamur\n5- Kevin\n"))
dec2 = int(input("Escolha para qual escala de temperatura deseja converter:\n1- Célsius\n2- Fahrenheit\n3- Rankine\n4- Réamur\n5- Kevin\n"))

if (1 < dec > 5 or 1 < dec2 > 5): print("Escala inválida")

if (dec == 1):
    if (dec2 == 1): print(x)
    if (dec2 == 2): print((x * 1.8) + 32)
    if (dec2 == 3): print((x * 1.8) + 491.6)
    if (dec2 == 4): print((x * 4) / 5)
    if (dec2 == 5): print(x + 273.15)
elif (dec == 2):
    if (dec2 == 1): print((5 * (x - 32)) / 9) 
    if (dec2 == 2): print(x)
    if (dec2 == 3): print(x + 459.67)
    if (dec2 == 4): print((x - 32) * 0.4)
    if (dec2 == 5): print((x + 459.67) * 5 / 9)
elif (dec == 3):
    if (dec2 == 1): print(((5 * x) / 9) - 273.15)
    if (dec2 == 2): print(x - 459.67)
    if (dec2 == 3): print(x)
    if (dec2 == 4): print(((x * 9) / 4) + 491,67)
    if (dec2 == 5): print((x * 5) / 9)
elif (dec == 4):
    if (dec2 == 1): print((x + 5) / 4)
    if (dec2 == 2): print((x * 2.25) + 32)
    if (dec2 == 3): print(x * 2.25 + 491.67)
    if (dec2 == 4): print(x)
    if (dec2 == 5): print((x / 0.8) + 273.15)
elif (dec == 5):
    if (dec2 == 1): print(x - 273.15)
    if (dec2 == 2): print(x -459.67)
    if (dec2 == 3): print((x * 9) / 5)
    if (dec2 == 4): print((x - 273.15) * 0.8)
    if (dec2 == 5): print(x)

print("\n" * 5)


print("-" * 30, " Desconto de IPTU", "-" * 30)
ano = int(input("Digite a quantos anos da construção do imóvel: "))
if (ano < 5): print("0% de desconto")
elif(ano >= 5 < 20): print("15% de desconto")
elif(ano >= 20 < 40): print("25% de desconto")
else: print("30% de desconto")

print("\n" * 5)


print("-" * 30, " Cálculo de IMC ", "-" * 30) 

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"\nSeu imc é de: {imc:.2f}\n")

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

print("\n" * 5)


print("-" * 30, " 3 números em ordem crescente ", "-" * 30) 

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
z = int(input("Digite outro número: "))

if(x < y < z): print("Estão em ordem crescente")
else: print("Não estão em ordem crescente")

print("\n" * 5)


print("-" * 30, " Nota e frequência ", "-" * 30) 

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
freq = int(input("Digite a frequenência: "))

media = (nota1 + nota2) / 2
if(freq < 75): print("Reprovado")
elif(media < 6): print("Reprovado")
else: print("Aprovado")

print("\n" * 5)


print("-" * 30, " Cálculo da f(x) ", "-" * 30) 

x = int(input("Digite o valor de x: "))

if(x != 0) : print(((4 * x ** 2) - (3 * x) + 9) / x)
else: print("Naõ pode dividir por zero")