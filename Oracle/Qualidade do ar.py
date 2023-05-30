# -- coding: utf-8 --
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
import getpass
import oracledb
import pandas as pd
import msvcrt
import numpy as np

pw = "Qvuvw6"
#pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user="bd240223131",
    password=pw,
    dsn="172.16.12.14/XE"
)

print("Sucesso ao conectar ao Oracle Database") #cria conexão para executar e manipular dos dados SQL

cursor = connection.cursor()
#Tenta criar uma tabela, caso de erro = ja existe uma
try:
    cursor.execute("""
        CREATE TABLE parametros (
            id_parametros NUMBER,
            mp10 NUMBER,
            mp25 NUMBER,
            so2 NUMBER,
            no2 NUMBER,
            o3 NUMBER,
            co NUMBER,
            CONSTRAINT parametros_pk PRIMARY KEY (id_parametros)
        )
    """)
    print("Tabela criada\n")
except:
    print("Tabela já criada\n")

#Função para inserir os valores, sendo 'parametro' o mp10, mp25, so2, no2 ,o3 e co quando chamado
def valorParametro(parametro):
    while True:
        try:
            valor = float(input(parametro))
            if valor >= 0:
                return valor
            else:
                print("O valor deve ser maior ou igual a zero.")
        except ValueError:
            print("Valor inválido. Digite um número válido.")

#Função para mosdtrar a tabela usando a biblioteca pandas
def mostrarTabela():
    cursor.execute("""SELECT COUNT(*) FROM parametros""")
    resultado = cursor.fetchone()[0]
    if resultado == 0:
        print("Nenhuma tabela encontrada.\n")
    else:
        cursor.execute("SELECT * FROM parametros")
        colunas = [descricao[0] for descricao in cursor.description]
        valores = cursor.fetchall()
        nomeColunas = pd.DataFrame(valores, columns=colunas)
        print(nomeColunas)


#While para rodar o programa mais de uma vez
while True:
    print("{:-^30}".format("Menu"))
    print("1- Inserir Dados")
    print("2- Atualizar Dados")
    print("3- Excluir Dados")
    print("0- Sair")

    #While para receber um caractere numérico
    while True:
            try:
                escolha = int(msvcrt.getch())       
                break
            except ValueError: print("Digite um valor numérico")

    cursor.execute("""SELECT COUNT(*) FROM parametros""")
    resultado = cursor.fetchone()[0]

    if escolha == 1:
        #Chamando a função para inserir os valores
        mp10 = valorParametro("\nDigite a quantidade de partículas inaláveis: ")
        mp25 = valorParametro("\nDigite a quantidade de partículas inaláveis finas: ")
        so2 = valorParametro("\nDigite a quantidade de dióxido de enxofre: ")
        no2 = valorParametro("\nDigite a quantidade de dióxido de nitrogênio: ")
        o3 = valorParametro("\nDigite a quantidade de ozônio: ")
        co = valorParametro("\nDigite a quantidade de monóxido de carbono: ")

        #Pega o maior valor do id_parametros e soma 1 caso tenha alguma tabela, senão é 0
        cursor.execute("""select max(id_parametros) from parametros""")
        id_registro = cursor.fetchone()[0]
        id_registro = id_registro + 1 if id_registro is not None else 0

        print("\nA média da qualidade do ar está", end=" ")

        if mp10 <= 50 and mp25 <= 25 and so2 <= 20 and no2 <= 200 and o3 <= 100 and co <= 9:
            print("boa\n")
        elif mp10 <= 120 and mp25 <= 60 and so2 <= 60 and no2 <= 240 and o3 <= 140 and co <= 11:
            print("moderada\n"
                "Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)"
                "podem apresentar sintomas como tosse seca e cansaço. \nA população, em geral, não é afetada.\n")
        elif mp10 <= 150 and mp25 <= 125 and so2 <= 365 and no2 <= 320 and o3 <= 160 and co <= 13:
            print("ruim\n"
                "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta."
                "\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)"
                "podem apresentar efeitos mais sérios na saúde.\n")
        elif mp10 <= 250 and mp25 <= 210 and so2 <= 800 and no2 <= 1130 and o3 <= 200 and co <= 15:
            print("muito ruim\n"
                "Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos,"
                "nariz e garganta e ainda falta de ar e respiração ofegante. \nEfeitos ainda mais graves à saúde de grupos sensíveis"
                "(crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n")
        else:
            print("péssima\n"
                "Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. \n"
                "aumento de mortes prematuras em pessoas de grupos sensíveis.\n")
        mostrarTabela()
                
        #Definir a matriz de parâmetros
        mzParametros = np.array([[mp10, mp25, so2],
                                 [no2, o3, co],
                                 [0, 0, 0]])
        # Definir a matriz de criptografia
        mzCript = np.array([[15, 8, 7],
                            [26, 54, 13],
                            [23, 9, 6]])
        # Multiplicar as matrizes
        resultado = np.dot(mzParametros, mzCript)
        print(resultado)

        mzInv = np.linalg.inv(mzCript)

        # Multiplicar a matriz resultante pelo inverso da matriz de criptografia
        mzDescript = np.dot(resultado, mzInv)

        # Converter cada elemento individualmente em inteiros
        mzDescript = np.dot(resultado, mzInv)

        print(mzDescript)

        #inserir dados na tabela
        mp10 = resultado[0][0]
        mp25 = resultado[0][1]
        so2 = resultado[0][2]
        no2 = resultado[1][0]
        o3 = resultado[1][1]
        co = resultado[1][2]
        cursor.execute(f"""insert into parametros (id_parametros, mp10, mp25, so2, no2, o3, co) values({id_registro}, {mp10},{mp25},{so2},{no2},{o3},{co}) """)

    elif (escolha == 2 or escolha == 3) and resultado != 0:
        mostrarTabela()
        
        while True:
            try:
                #Se tiver escolhido 2 no menu, ira mostrar a palavra "alterada" no final do texto, senão (que no caso é se for 3), excluída
                id_registro = int(input("\nDigite o ID_PARAMETROS do registro a ser " + ("alterada" if escolha == 2 else "excluída") + ": "))
                break
            except:
                print("ID inválido. Digite um número inteiro válido.")

        cursor.execute("SELECT COUNT(*) FROM parametros")
        resultado = cursor.fetchone()[0]

        if resultado == 0: print("Nenhuma tabela encontrada.\n")
        else:
            cursor.execute("SELECT id_parametros FROM parametros ORDER BY id_parametros")
            
            ids = [row[0] for row in cursor]

            if id_registro not in ids:
                print("ID não encontrado.\n")

        if escolha == 2:
            mp10 = valorParametro("\nDigite a nova quantidade de partículas inaláveis: ")
            mp25 = valorParametro("\nDigite a nova quantidade de partículas inaláveis finas: ")
            so2 = valorParametro("\nDigite a nova quantidade de dióxido de enxofre: ")
            no2 = valorParametro("\nDigite a nova quantidade de dióxido de nitrogênio: ")
            o3 = valorParametro("\nDigite a nova quantidade de ozônio: ")
            co = valorParametro("\nDigite a nova quantidade de monóxido de carbono: ")

            # Construir a consulta SQL com os valores substituídos
            cursor.execute(f""" UPDATE parametros 
                SET mp10 = {mp10}, 
                mp25 = {mp25}, 
                so2 = {so2}, 
                no2 = {no2}, 
                o3 = {o3}, 
                co = {co}
                WHERE id_parametros = {id_registro}""")

            print("\nRegistro atualizado com sucesso!\n")

        elif escolha == 3:
            cursor.execute(f"""DELETE FROM parametros WHERE id_parametros = {id_registro}""")
            cursor.execute("""SELECT * FROM parametros""")
            print("\nRegistro excluído com sucesso!\n")

        cursor.execute(f""" UPDATE parametros SET id_parametros = id_parametros - 1 WHERE id_parametros > {id_registro} """)

        mostrarTabela()

    elif escolha == 0:
        break

    else: 
        print("Escolha um valor válido" if resultado != 0 else "Nenhuma tabela encontrada")

    connection.commit()
connection.close()
