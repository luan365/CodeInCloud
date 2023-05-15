# -*- coding: utf-8 -*-

print("-" * 20, " Conversão de número Decimal para extenso com casas flutuantes", "-" * 20)

#Declaração de variáveis
x = 0
continuar = "s"

while continuar == "s" and "S":
        
    cen = ""
    dez = ""
    num = ""
    uni = "" 
    dezDecimal = ""
    uniDecimal = ""
    numDecimal = ""
    numero = ""
    
    #Entrada de dados
    x = float(input("Digite um número: "))
    if(x < 0):
        numero = "Menos "
        x = -x
    
    #Cálculo
    u = int(x % 10)
    d = int(((x - u) % 100) / 10)
    c = int(((x - d - u) % 1000) / 100)
    dezDec = int((x * 10) % 10)
    uniDec = int((x * 100) % 10)
    
    #Condicional para unidade flutuante
    if (uniDec == 1): uniDecimal = "Um"
    elif (uniDec == 2): uniDecimal = "Dois"
    elif (uniDec == 3): uniDecimal = "Três"
    elif (uniDec == 4): uniDecimal = "Quatro"
    elif (uniDec == 5): uniDecimal = "Cinco"
    elif (uniDec == 6): uniDecimal = "Seis"
    elif (uniDec == 7): uniDecimal = "Sete"
    elif (uniDec == 8): uniDecimal = "Oito"
    elif (uniDec == 9): uniDecimal = "Nove"
    
    #Condicional para dezena flutuante
    if (dezDec == 1): 
        if(uniDec == 1): numDecimal = "Onze"
        elif (uniDec == 2): numDecimal = "Doze"
        elif (uniDec == 3): numDecimal = "Treze"
        elif (uniDec == 4): numDecimal = "Quatorze"
        elif (uniDec == 5): numDecimal = "Quinze"
        elif (uniDec == 6): numDecimal = "Dezesseis"
        elif (uniDec == 7): numDecimal = "Dezessete"
        elif (uniDec == 8): numDecimal = "Dezoito"
        elif (uniDec == 9): numDecimal = "Dezenove"
        
    if(uniDec != 0):
        if(dezDec == 2): dezDecimal = "Vinte"
        elif (dezDec == 3): dezDecimal = "Trinta"
        elif (dezDec == 4): dezDecimal = "Quarenta"
        elif (dezDec == 5): dezDecimal = "Cinquenta"
        elif (dezDec == 6): dezDecimal = "Sessenta"
        elif (dezDec == 7): dezDecimal = "Setenta"
        elif (dezDec == 8): dezDecimal = "Oitenta"
        elif (dezDec == 9): dezDecimal = "Noventa"
    else:
        if (dezDec == 1): dezDecimal = "Um"
        elif (dezDec == 2): dezDecimal = "Dois"
        elif (dezDec == 3): dezDecimal = "Três"
        elif (dezDec == 4): dezDecimal = "Quatro"
        elif (dezDec == 5): dezDecimal = "Cinco"
        elif (dezDec == 6): dezDecimal = "Seis"
        elif (dezDec == 7): dezDecimal = "Sete"
        elif (dezDec == 8): dezDecimal = "Oito"
        elif (dezDec == 9): dezDecimal = "Nove"
        
    #Condicional para unidade
    if (u == 0): uni = "Zero"
    elif (u == 1): uni = "Um"
    elif (u == 2): uni = "Dois"
    elif (u == 3): uni = "Três"
    elif (u == 4): uni = "Quatro"
    elif (u == 5): uni = "Cinco"
    elif (u == 6): uni = "Seis"
    elif (u == 7): uni = "Sete"
    elif (u == 8): uni = "Oito"
    elif (u == 9): uni = "Nove"
    
    #Condicional para números de 10 a 19
    if (d == 1): 
        if (u == 0): num = "Dez"
        if (u == 1): num = "Onze"       
        if (u == 2): num = "Doze"      
        if (u == 3): num = "treze"
        if (u == 4): num = "quatorze"
        if (u == 5): num = "Quinze"
        if (u == 6): num = "Dezesseis"
        if (u == 7): num = "Dezessete"
        if (u == 8): num = "Dezoito"
        if (u == 9): num = "Dezenove"        

    #Condicional para Dezena
    if (d == 2): dez = "Vinte"
    elif (d == 3): dez = "Trinta"
    elif (d == 4): dez = "Quarenta"
    elif (d == 5): dez = "Cinquenta"
    elif (d == 6): dez = "Sessenta"
    elif (d == 7): dez = "Setenta"
    elif (d == 8): dez = "oitenta"
    elif (d == 9): dez = "Noventa"
    
    #Condicional para centena
    if ((c == 1) and (d != 0)) or ((c == 1) and (u != 0)): cen = "Cento"
    elif (c == 2): cen = "Duzentos"
    elif (c == 3): cen = "Trezentos"
    elif (c == 4): cen = "Quatrocentos"
    elif (c == 5): cen = "Quinhentos"
    elif (c == 6): cen = "Seissentos"
    elif (c == 7): cen = "Setessentos"
    elif (c == 8): cen = "Oitocentos"
    elif (c == 9): cen = "Novecentos"
    else: cen = "Cem"
    
    """
    
    SAÍDA DE DADOS
    
    """
    
    #Saída de dados para dezena e unidade
    if (d >= 2):
        numero += f"{dez}" 
        if (u != 0): numero += f" e {uni}"
    else: numero += f"{num}"
    
    if(d == 0) and (u != 0): numero += f"{uni}"    
    
    #Saída de dados para casas flutuantes
    if (dezDec >= 2): 
        numero += f" ponto {dezDecimal}"
        if (uniDec != 0): numero += f" e {uniDecimal}"
    elif (dezDec == 0) and (uniDec != 0): numero += f" ponto zero {uniDecimal}"
    elif (numDecimal != ""): numero += f" ponto {numDecimal}"
    
    #Saída de dados para centena
    if (c >= 1):
        if(numero == ""): numero += cen
        else: numero = f"{cen} e " + numero
        
    #Impressão do número
    print(numero)
    
    #Verificação se o usuário deseja continar com o programa
    continuar = input("Deseja escolher outro número? (S ou N): ")
    
print("-" * 30, " Fim do programa ", "-" * 30)