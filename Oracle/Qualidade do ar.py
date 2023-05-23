# -- coding: utf-8 --
"""
Created on Tue Mar 28 08:11:01 2023

@author: Arthur Magalhâes Peixoto de Oliveira
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

#pw = getpass.getpass("Enter password: ")
pw = "Qvuvw6"

connection = oracledb.connect(
    user="bd240223131",
    password=pw,
    dsn="172.16.12.14/XE")

print("Sucesso ao conectar ao Oracle Database")

cursor = connection.cursor() #cria conexão para executar e manipular dos dados SQL

try:    
    cursor.execute("""
        create table parametros (
            mp10 number,
            mp25 number,
            so2 number,
            no2 number,
            o3 number,
            co number)""")
    print("Tabela criada\n")
except:
    print("Tabela já criada\n")


#While para rodar o programa mais de uma vez
while True:
    id_registro = 0

    while True:  
        registro_encontrado = False
        print("{:-^30}".format("Menu"))
        
        print("1- Inserir Dados \n2- Atualizar Dados \n3- Excluir Dados \n0- Sair")
        
        # Ler uma tecla pressionada e converte para inteiro
        escolha = int(msvcrt.getch())
        print(escolha)
        
        if(escolha == 1): break

        elif(escolha == 2 or escolha == 3): 
            cursor.execute(""" SELECT COUNT(*) FROM parametros """)

            resultado = cursor.fetchone()

            if(resultado[0] == 0): break
            else:
                cursor.execute("""SELECT ROWNUM as ID_PARAMETROS, mp10, mp25, so2, no2, o3, co FROM parametros""")
                # Obter os nomes das colunas
                colunas = [descricao[0] for descricao in cursor.description]    
                # Obter os valores da tabela
                valores = cursor.fetchall() 
                # Criar um DataFrame do Pandas
                nomeColunas = pd.DataFrame(valores, columns=colunas) 
                # Imprimir o DataFrame
                print(nomeColunas)
                
                # Loop até que um ID válido seja fornecido
                while not registro_encontrado:
                    print("Digite o ID_PARAMETROS do registro a ser", end = " ")
                    print("alterado" if (escolha == 2) else "excluído", end = "")
                    id_registro = input(": ")

                    # Verificar se o ID fornecido é um valor numérico
                    if not id_registro.isdigit():
                        print("ID inválido. O ID deve ser um valor numérico.")
                    else:
                        # Executar uma consulta para verificar se o registro com o ID fornecido existe
                        cursor.execute("SELECT ROWNUM as ID_PARAMETROS, mp10, mp25, so2, no2, o3, co FROM parametros")

                        # Verificar se o registro com o ID fornecido existe
                        for i in cursor:
                            if i[0] == int(id_registro):
                                registro_encontrado = True
                        else: print("\nTabela não encontrada")
                        
                if(registro_encontrado): break
                else: print("Id não encontrado")
                
        elif(escolha == 0):
            exit()
        
        else:
            print("Escolha um valor válido")


    if(escolha != 3):

        def valorParametro(parametro):
            while True:
                try:
                    valor = float(input(parametro))
                    if valor >= 0:
                        return valor
                    else:
                        print("Valor não pode ser menor que zero.")
                except ValueError:
                    print("Somente valores numéricos são aceitos.")
        
        # Obter valores para cada coluna
        mp10 = valorParametro("\nDigite a quantidade de partículas inaláveis: ")
        mp25 = valorParametro("\nDigite a quantidade de partículas inaláveis finas: ")
        so2 = valorParametro("\nDigite a quantidade de dióxido de enxofre: ")
        no2 = valorParametro("\nDigite a quantidade de dióxido de nitrogênio: ")
        o3 = valorParametro("\nDigite a quantidade de ozônio: ")
        co = valorParametro("\nDigite a quantidade de monóxido de carbono: ")

        if(escolha == 1):
            #inserir dados na tabela
            cursor.execute(f"""insert into parametros (mp10, mp25, so2, no2, o3, co) values({mp10},{mp25},{so2},{no2},{o3},{co}) """)

            print("\nA média da qualidade do ar está", end = " ")

            if ((mp10 <= 50) and (mp25 <= 25) and (so2 <= 20) and (no2 <= 200) and (o3 <= 100) and (co <= 9)):
                print("boa\n")

            elif ((mp10 <= 120) and (mp25 <= 60) and (so2 <= 60) and (no2 <= 240) and (o3 <= 140) and (co <= 11)):
                print("""moderada\n
                    Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)
                    podem apresentar sintomas como tosse seca e cansaço. \nA população, em geral, não é afetada.\n""")
                
            elif ((mp10 <= 150) and (mp25 <= 125) and (so2 <= 365) and (no2 <= 320) and (o3 <= 160) and (co <= 13)):
                print("""ruim\n
                    "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta.
                    \nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) 
                    podem apresentar efeitos mais sérios na saúde.\n""")
                
            elif ((mp10 <= 250) and (mp25 <= 210) and (so2 <= 800) and (no2 <= 1130) and (o3 <= 200) and (co <= 15)):
                print("""muito ruim\n
                    Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos,
                    nariz e garganta e ainda falta de ar e respiração ofegante. \nEfeitos ainda mais graves à saúde de grupos sensíveis
                    (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n""")
                
            else:
                print("""péssima\n
                    Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. \n
                    aumento de mortes prematuras em pessoas de grupos sensíveis.\n""")
                
        elif(escolha == 2):
            # Construir a consulta SQL com os valores substituídos
            cursor.execute(f""" UPDATE parametros 
                SET mp10 = {mp10}, 
                mp25 = {mp25}, 
                so2 = {so2}, 
                no2 = {no2}, 
                o3 = {o3}, 
                co = {co}
                WHERE ROWNUM = {id_registro}""")

    else: 
        print("Apagar linha")
        # Excluir a linha desejada
        cursor.execute(f"""
            DELETE FROM parametros
                WHERE ID_PARAMETROS = (
                    SELECT ID_PARAMETROS
                    FROM (
                        SELECT ID_PARAMETROS, ROWNUM AS rn
                        FROM parametros
                        -- Aqui você pode adicionar outras condições
                        ORDER BY ID_PARAMETROS
                    )
                    WHERE rn = {id_registro} )
        """)

        # Atualizar os valores da coluna ID_PARAMETROS usando a sequência
        cursor.execute(f"""UPDATE parametros SET ID_PARAMETROS = ID_PARAMETROS - 1 WHERE ROWNUM > {id_registro}""")

    cursor.execute(""" SELECT COUNT(*) FROM parametros """)
    resultado = cursor.fetchall()[0][0]
    print(resultado)

    if (resultado == 0):
        print("Nenhuma tabela encontrada")

    else:
        cursor.execute("""SELECT ROWNUM as ID_PARAMETROS, mp10, mp25, so2, no2, o3, co FROM parametros""")
        colunas = [descricao[0] for descricao in cursor.description]    
        valores = cursor.fetchall() 
        nomeColunas = pd.DataFrame(valores, columns=colunas) 
        print(nomeColunas)
    connection.commit()

