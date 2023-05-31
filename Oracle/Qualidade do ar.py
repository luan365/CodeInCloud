
# Coding: utf-8
"""
Created on Tue Mar 28 08:11:01 2023

@author:
Arthur Magalhâes Peixoto de Oliveira
Arthur Martins Parmeggiani
Isbella Maria Tressino Bruno
Jose Eduardo Cunha Roppa
Luan de Campos Ferreira
Luigi Mazzoni Targa
"""

# Importações usadas
import pandas as pd #pip3 install pandas
import numpy as num #pip install scilab2py
import msvcrt
import oracledb 
from time import sleep
from os import system

def TextoFormatado(texto):
        print("-" * 80)
        print("{:^80}".format(texto))
        print("-" * 80)

system("CLS")
sleep(1)

TextoFormatado("Bem vindo ao nosso software sobre amostras de ar")
print("\n")

#Limpa Terminal
sleep(3)
system("CLS")
sleep(1)

while True:
    # Input do usuario da conta do oracle
    TextoFormatado("Conta Oracle")

    us = input("\nUsuario: ")
    pw = input("Senha: ")

    try:
        # Realiza a conexão do banco de dados
        connection = oracledb.connect(
            user=us,
            password=pw,
            dsn="172.16.12.14/XE"
        )
        break
    except: 
        TextoFormatado("Erro ao se conectar. \nVerifique a senha, usuário ou a conexão")
        sleep(1)
        system("CLS")
        sleep(0.5)


system("CLS")
sleep(1)

# Imprime a mensagem de sucesso ao conectar o banco de dados
TextoFormatado("Sucesso ao conectar ao Oracle Database")


sleep(3)
system("CLS")
sleep(1)

# Cria uma variavel indicador/cursor
cursor = connection.cursor()

# Tenta criar uma tabela
try:
    # Executa o create table atraves do SQL
    cursor.execute("""
        CREATE TABLE parametros (
            ID_parametros number primary key,
            mp10 number,
            mp25 number,
            so2 number,
            no2 number,
            o3 number,
            co number,
            qualidade Varchar2(255)
        )
    """)

# Caso a tabela ja exista
except: sleep(0)

# Função que verifica os valores inseridos ao mp10, mp25, so2, no2 ,o3 e co *quando chamada*
def valorParametro(parametro):

    # Verifica a integridade do valor inserido
    while True:
        try:

            # Atribui a variavel valor o valor do parametro digitado
            valor = float(input(parametro))

            # Caso seja maior ou igual a 0, é permitido o uso
            if valor >= 0:
                return valor
            
            # Caso seja menor que 0, não é permitido o uso
            else:
 
                system("CLS")

                # Imprime mensagem de aviso sobre a integridade do valor
                print("O valor deve ser maior ou igual a zero.")
                
                sleep(3)
                system("CLS")
                sleep(1)
        
        # Caso o valor não seja numerico, não é permitido o uso
        except ValueError:

            system("CLS")

            # Imprime mensagem de aviso sobre a integridade do valor
            print("Valor inválido. Digite um número válido.")            
            
            sleep(3)
            system("CLS")
            sleep(1)

# Função para mostrar a tabela  de amostras usando a biblioteca pandas *quando chamada*
def mostrarTabela():
    # Verifica se a tabela contem algo
    cursor.execute("SELECT COUNT(*) FROM parametros")
    resultado = cursor.fetchone()[0]

    # Caso não tenha
    if resultado == 0:

        # Imprime a mensagem de que não foi encontrada nenhuma tabela
        print("Nenhuma tabela encontrada.\n")
    
    # Caso tenha
    else:
        # Executa o select atraves do SQL e imprime a tabela
        cursor.execute("SELECT id_parametros, mp10, mp25, so2, no2, o3, co FROM parametros ORDER BY id_parametros")
        colunas = [descricao[0] for descricao in cursor.description]
        valores = cursor.fetchall()
        nomeColunas = pd.DataFrame(valores, columns=colunas)
        print(nomeColunas)

# Função responsável por retornar o equivalente numérico para as letras do alfabeto
def equivalenteDecimal(letra):
    
    # definindo uma cadeia de caracteres com todas as letras do alfabeto
    alfabeto = "zabcdefghijklmnopqrstuvwxy"
    
    # encontra a posição da letra na string e a retorna
    return(alfabeto.find(letra))

# função responsável por retornar o equivalente alfabético para um valor numérico
def equivalenteAlfabetico(numero):

    
    # definindo uma cadeia de caracteres com todas as letras do alfabeto
    alfabeto = "zabcdefghijklmnopqrstuvwxy"
    
    # encontra o pedaço da string a qual o número correspondente indica
    return(alfabeto[numero])

#Matriz A responsável pela segurança da criptografia
A = num.array([[5,6],[2,3]]) 

# função responsável por codificar a matriz, dependendo da matriz inserida
def cifraHill(texto,chave):
    
    codigo = ""
    #Matriz responsável por receber o valor númerico equivalente ao alfabético
    valorNumerico = num.empty([2,1], dtype = int)
    #As inicializações indicam que ela será um vetor-coluna do tipo inteiro

    #Matriz responsável por receber o valor codificado equivalente ao alfabético
    valorCodificado = num.empty([2,1], dtype = int)
    #As inicializações indicam que ela será um vetor-coluna do tipo inteiro
    
    #Codificacao para cada par do texto formado
    for indice in range(0, len(texto)):
    
        #Adicionar o valor numérico para a primeira letra do par
        if(indice == 0 or indice % 2 == 0):
            
            #Pega exatamente a letra localizada no elemento numerico de 'indice'
            valor = equivalenteDecimal(texto[indice]) 
            #Adiciona na primeira linha da primeira coluna
            valorNumerico[0][0] = valor 
    
        #Adicionar o valor numérico para a segunda letra do par
        if(indice != 0 and indice % 2 != 0):
            
            #Pega exatamente a letra localizada no elemento numerico de 'indice'
            valor = equivalenteDecimal(texto[indice])  
            #Adiciona na segunda linha da primeira coluna
            valorNumerico[1][0] = valor 
        
        # estrutura de seleção responsável por calcular a multiplicação da matriz A pelo vetor-coluna 
        if(indice != 0 and indice % 2 != 0):
            #Multiplicação da matriz A com os pares de números equivalentes a letras
            valorCodificado = num.dot(chave, valorNumerico)
        
            #Se o valor do resultado codificado no primeiro par da letra seja maior que 25, substitui pelo valor do seu módulo por 26
            if(valorCodificado[0][0] > 25):
                valorCodificado[0][0] = (valorCodificado[0][0] % 26)
        
            #Se o valor do resultado codificado no segundo par da letra seja maior que 25, substitui pelo valor do seu módulo por 26
            if(valorCodificado[1][0] > 25):
                valorCodificado[1][0] = (valorCodificado[1][0] % 26)
        
            #Pega o equivalente alfabético para os novos números codificados, visando construir a frase codificada
            a = str(equivalenteAlfabetico(valorCodificado[0][0])) # primeira linha do vetor-coluna
            b = str(equivalenteAlfabetico(valorCodificado[1][0])) # segunda linha do vetor-coluna
        
            # adiciona letra por letra codificada a uma variável string para montar a frase
            codigo += a
            codigo += b
        
    # remove os caracteres desnecessários e mostra somente a parte codificada
    codigo = codigo[len(codigo) - len(texto): len(codigo)]
    
    # função retorna código criptografado
    return codigo

# função responsável por pegar o texto a ser encriptado
def inserirFrase(texto):
    texto = texto.replace(" ", "") # eliminando os espaços em branco do texto
    
    # caso o texto tenha uma quantidade ímpar de letras, adiciona mais uma letra arbitrária ao final
    if(len(texto) % 2 != 0):
        texto += "g"
    
    return texto # retorna a frase pronta para o sistema de criptografia


    residuo = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 26 
    # temos a.a^{-1} = 1 (mod 26)
    # residuo.reciproco = x  = 1 (mod 26)

    # definindo o reciproco
    reciproco = 9 
    # definindo o posicionamento da matriz invertível (mod 26)
    descriptografia = num.array([[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]) 
    # realizando a multiplicação com o recíproco
    descriptografia *= reciproco 
    # definindo o módulo 26 de cada elemento
    descriptografia %= 26 
    # definindo a cifra criptografada, dada anteriormente pela criptografia com A
    cifra = cifraHill(texto,A)
    # chamando a função responsável por criptografar/descriptografar
    print(cifraHill(cifra,descriptografia)) 

def DefineQualidade(mp10, mp25, so2, no2, o3, co):
    # Compara os parametros para definir a classificaçao da amostra
    if mp10 <= 50 and mp25 <= 25 and so2 <= 20 and no2 <= 200 and o3 <= 100 and co <= 9:
        texto = ("boa.")
    elif mp10 <= 120 and mp25 <= 60 and so2 <= 60 and no2 <= 240 and o3 <= 140 and co <= 11:
        texto = ("moderada.\n"
            "Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)"
            "podem apresentar sintomas como tosse seca e cansaço. \nA população, em geral, não é afetada.")
    elif mp10 <= 150 and mp25 <= 125 and so2 <= 365 and no2 <= 320 and o3 <= 160 and co <= 13:
        texto = ("ruim.\n"
            "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta."
            "\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)"
            "podem apresentar efeitos mais sérios na saúde.")
    elif mp10 <= 250 and mp25 <= 210 and so2 <= 800 and no2 <= 1130 and o3 <= 200 and co <= 15:
        texto = ("muito ruim.\n"
            "Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos,"
            "nariz e garganta e ainda falta de ar e respiração ofegante. \nEfeitos ainda mais graves à saúde de grupos sensíveis"
            "(crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    else:
        texto = ("péssima.\n"
            "Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias, cardiovasculares e \n"
            "aumento de mortes prematuras em pessoas de grupos sensíveis.")
    return texto

# While para possibilitar que o menu seja processado mais de uma vez
while True:
    # While para receber um caractere numérico (0 a 5) à variavel "escolha"
    while True:
        # Prints mostrando as funções do menu
        TextoFormatado("Menu")
        print("\n1 - Cadastrar Amostras")
        print("2 - Alterar Amostras")
        print("3 - Excluir Amostras")
        print("4 - Classificar Amostras")
        print("0 - Sair do Software\n")
        escolha = msvcrt.getch()   

        try:
            escolha = int(escolha)
            # Atribui à variavel qual funçao do menu foi escolhida
            break
        except:            
            system("CLS")
            sleep(0.5)

            # Imprime um aviso caso seja atribuido um valor invalido
            TextoFormatado("Escolha uma opção válida")
            
            sleep(2)
            system("CLS")

    # Função para inserir amostras
    if escolha == 1:
        system("CLS")
        sleep(1)

        # Imprime mensagem que explica como usar a função de inserir uma amostra
        TextoFormatado("Insira as amostras de cada parametro que deseja cadastrar")
        print("\n")

        # Chamando a função para inserir os valores
        mp10 = valorParametro("Digite a quantidade de partículas inaláveis: ")
        mp25 = valorParametro("Digite a quantidade de partículas inaláveis finas: ")
        so2 = valorParametro("Digite a quantidade de dióxido de enxofre: ")
        no2 = valorParametro("Digite a quantidade de dióxido de nitrogênio: ")
        o3 = valorParametro("Digite a quantidade de ozônio: ")
        co = valorParametro("Digite a quantidade de monóxido de carbono: ")

        # Pega o maior valor do id_parametros e soma 1 caso tenha alguma tabela, senão é 0
        cursor.execute("select max(id_parametros) from parametros")
        id_registro = cursor.fetchone()[0]
        id_registro = id_registro + 1 if id_registro is not None else 0

        # Insere os dados na tabela
        texto = inserirFrase(DefineQualidade(mp10, mp25, so2, no2, o3, co))
        try:
        # Inserindo os valores na tabela
            cursor.execute(f"""
                INSERT INTO parametros (ID_parametros, mp10, mp25, so2, no2, o3, co, qualidade)
                VALUES ({id_registro}, {mp10}, {mp25}, {so2}, {no2}, {o3}, {co}, '{cifraHill(texto,A)}')
            """)

        except Exception as e: TextoFormatado(f"Erro ao cadastrar amostra: {str(e)}")

        sleep(1)
        system("CLS")

        # Notificação de confirmação de atualização
        TextoFormatado("Registro cadastrado com sucesso!")
        
        sleep(3)
        system("CLS")

    # Função para alterar amostras
    if escolha == 2:

        system("CLS")
        sleep(1)

        # Imprime mensagem que explica como usar a função de alterar uma amostra cadastrada
        TextoFormatado("Consulte a tabela de amostras para ver o ID de qual deseja alterar.")
        print("\n")

        # Mostra a tabela de amostras cadastradas
        mostrarTabela()
        print("\n")

        # Input para definir o ID da amostra que sera alterada
        try:
            while True:
                id_registro = int(input("Digite o ID da amostra que deseja alterar: "))

                sleep(0.5)
                system("CLS")
                sleep(1)
                
                # Chama a função para alterar os valores
                mp10 = valorParametro("\nDigite a nova quantidade de partículas inaláveis: ")
                mp25 = valorParametro("Digite a nova quantidade de partículas inaláveis finas: ")
                so2 = valorParametro("Digite a nova quantidade de dióxido de enxofre: ")
                no2 = valorParametro("Digite a nova quantidade de dióxido de nitrogênio: ")
                o3 = valorParametro("Digite a nova quantidade de ozônio: ")
                co = valorParametro("Digite a nova quantidade de monóxido de carbono: ")

                # Executa o SQL com os valores substituídos
                texto = inserirFrase(DefineQualidade(mp10, mp25, so2, no2, o3, co))
                cifraHill(texto,A)
                try:
                    cursor.execute(f""" UPDATE parametros 
                        SET mp10 = {mp10}, 
                        mp25 = {mp25}, 
                        so2 = {so2}, 
                        no2 = {no2}, 
                        o3 = {o3}, 
                        co = {co},
                        qualidade = '{cifraHill(texto,A)}'
                        WHERE id_parametros = {id_registro}""")

                except Exception as e: TextoFormatado(f"Erro ao cadastrar amostra: {str(e)}")

                sleep(1)
                system("CLS")

                # Notificação de confirmação de atualização
                TextoFormatado("Registro alterado com sucesso!")

                sleep(3)
                system("CLS")
                break
        except: TextoFormatado("Digite um valor válido")


    # Função para excluir amostras
    if escolha == 3:
        
        sleep(1)
        system("CLS")

        # Imprime mensagem que explica como usar a função de excluir uma amostra cadastrada
        TextoFormatado("Consulte a tabela de amostras para ver o ID de qual amostra deseja excluir.")
        print("\n")

        # Mostra a tabela de amostras cadastradas
        mostrarTabela()
        print("\n")

        # Executa o SQL para excluir a amostra desejada
        id_registro = int(input("Digite o ID da amostra que deseja excluir: "))
        cursor.execute(f"DELETE FROM parametros WHERE id_parametros = {id_registro}")

        sleep(1)
        system("CLS")

        # Imprime a mensagem de confirmação que a amostra foi excluida
        TextoFormatado("Registro excluido com sucesso!")        
        
        sleep(3)
        system("CLS")

    # Função para classificar o uma amostra cadastrada
    if escolha == 4:
        
        system("CLS")
        sleep(1)

        # Imprime mensagem que explica como usar a função de classificar uma amostra cadastrada
        TextoFormatado("Consulte a tabela de amostras para ver o id de qual amostra deseja classificar")
        print("\n")

        # Mostra a tabela de amostras cadastradas
        mostrarTabela()
        print("\n")

        # Input para selecionar qual amostra sera consultada sua classificaçao
        try:
            while True:
                id_amostra = int(input("Digite o ID da amostra que deseja classificar: "))
                sleep(1)
                system("CLS")
                sleep(1)
                        # Imprime mensagem que explica como voltar para o menu
                TextoFormatado("Para voltar ao menu pressione qualquer tecla!")
                print("\n")

                # Executa o SQL com o valor atribuido ao id_amostra para que mostre apenas a amostra consultada
                cursor.execute(f"SELECT id_parametros, mp10, mp25, so2, no2, o3, co FROM parametros WHERE id_parametros = {id_amostra}")
                colunas = [descricao[0] for descricao in cursor.description]
                valores = cursor.fetchall()
                nomeColunas = pd.DataFrame(valores, columns=colunas)

                # Imprime a amostra consultada
                print(nomeColunas)
                print("\n")

                # Imprime os resultados de acordo com a amostra inserida
                print("A média da qualidade do ar está", end=" ")

                # Define cada parametro como zero para puxar os reais valores por meio de select do SQL
                mp10 = 0
                mp25 = 0
                so2 = 0
                no2 = 0
                o3 = 0
                co = 0

                # Pega cada valor a partir do 1 para tirar media
                cursor.execute(f"SELECT id_parametros, mp10, mp25, so2, no2, o3, co FROM parametros WHERE id_parametros = {id_amostra}")
                for row in cursor: 
                    mp10 = int(row[1])
                    mp25 = int(row[2])
                    so2 = int(row[3])
                    no2 = int(row[4])
                    o3 = int(row[5])
                    co = int(row[6])

                print(DefineQualidade(mp10, mp25, so2, no2, o3, co))
                break
        except: 
            TextoFormatado("Digite um valor correto")
            sleep(1)
            system("CLS")
            sleep(1)        

        # Função para voltar ao menu apertando qualquer tecla
        while True:
            sair = (msvcrt.getch())      
            break
    
    # Função para sair do sistema
    if escolha == 0:
        system("CLS")
        break

    # Confirma que todas mensagens sejam apagadas para mostar o menu novamente
    sleep(1)
    system("CLS")

    # Faz commit em todas transições de dados para o database
    connection.commit()

# Fecha a conexão
connection.close()