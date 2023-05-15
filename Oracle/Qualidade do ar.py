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


#pw = getpass.getpass("Enter password: ")
pw = "Qvuvw6"

connection = oracledb.connect(
    user="bd240223131",
    password=pw,
    dsn="172.16.12.14/XE")

print("Successfully connected to Oracle Database")

cursor = connection.cursor() #cria conexão para executar e manipular dos dados SQL

cursor.execute("""
    begin
        execute immediate 'drop table parametros';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute("""
    create table parametros (
        ID_parametros number generated always as identity,
        mp10 number,
        mp25 number,
        so2 number,
        no2 number,
        o3 number,
        co number)""")


while True:
#While para rodar o programa mais de uma vez
    while True:
            print("{:-^30}".format("Menu"))
            escolha = int(input("1- Inserir Dados \n2- Atualizar Dados \n3- Excluir Dados \n0- Sair"))
            
            if(escolha == 1 or 2): break

            elif(escolha == 3): break
                 
            elif(escolha == 0):
                exit()
            
            else:
                print("Escolha um valor válido")







    #ler numero de linhas da tabela
    cursor.execute('SELECT * FROM parametros')
    resultados = cursor.fetchall()
    num_linhas = cursor.rowcount

    print(pd.DataFrame(resultados))
    print("\n\n", resultados)


    if(escolha == 2):
        if(len(resultados) != 0):
            print("Para qual valores deseja atualizar: ")
            for i in range(len(resultados)):
                print(resultados[i])
        else: 
            print("Não existe uma tabela para alterar os valores")
            print(len(resultados))
        

    while True:
    #while para repitir valores caso não seja maior que zero ou numérico
        try:
        #try para conferir se valor é numérico
            mp10 = float(input("\nDigite a quantidade de partículas inaláveis: "))
            if (mp10 >= 0): 
                break
                #break para sair desse laço de repetição e ir para o3 próximo
            else:
            #else para informar erro caso valor seja menor que zero 
                print("Valor não pode ser menor que zero")
        except:
        #except para informar erro caso valor não seja numérico
            print("Somente valores númericos aceitos")
            
    while True:
        try:
            mp25 = float(input("\nDigite a quantidade de partículas inaláveis finas: "))
            if (mp25 >= 0): break
            else: print("Valor não pode ser menor que zero")
        except:
            print("Somente valores númericos aceitos")

    while True:
        try:
            so2 = float(input("\nDigite a quantidade de dióxido de enxofre: "))
            if (so2 >= 0): break
            else: print("Valor não pode ser menor que zero")
        except:
            print("Somente valores númericos aceitos")

    while True:
        try:
            no2 = float(input("\nDigite a quantidade de dióxido de nitrogênio: "))
            if (no2 >= 0): break
            else: print("Valor não pode ser menor que zero")
        except:
            print("Somente valores númericos aceitos")

    while True:
        try:
            o3 = float(input("\nDigite a quantidade de ozônio: "))
            if (o3 >= 0): break
            else: print("Valor não pode ser menor que zero")
        except:
            print("Somente valores númericos aceitos")

    while True:
        try:     
            co = float(input("\nDigite a quantidade de monóxido de carbono: "))
            if (co >= 0): break
            else: print("Valor não pode ser menor que zero")
        except:
            print("Somente valores númericos aceitos")


    #inserir dados na tabela
    cursor.execute(f"""
        insert into parametros (mp10, mp25, so2, no2, o3, co) values({mp10},{mp25},{so2},{no2},{o3},{co}) 
    """)

    connection.commit()  

    #ler numero de linhas da tabela
    cursor.execute('SELECT * FROM parametros')
    resultados = cursor.fetchone()
    num_linhas = cursor.rowcount

    print("A média da qualidade do ar está", end = " ")

    if ((mp10 <= 50) and (mp25 <= 25) and (so2 <= 20) and (no2 <= 200) and (o3 <= 100) and (co <= 9)):
        print("boa\n")

    elif ((mp10 <= 120) and (mp25 <= 60) and (so2 <= 60) and (no2 <= 240) and (o3 <= 140) and (co <= 11)):
        print("moderada\n")
        print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)"
            "podem apresentar sintomas como tosse seca e cansaço. \nA população, em geral, não é afetada.")
        
    elif ((mp10 <= 150) and (mp25 <= 125) and (so2 <= 365) and (no2 <= 320) and (o3 <= 160) and (co <= 13)):
        print("ruim\n")
        print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta." 
            "\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)" 
            "podem apresentar efeitos mais sérios na saúde.")
        
    elif ((mp10 <= 250) and (mp25 <= 210) and (so2 <= 800) and (no2 <= 1130) and (o3 <= 200) and (co <= 15)):
        print("muito ruim\n")
        print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos," 
            "nariz e garganta e ainda falta de ar e respiração ofegante. \nEfeitos ainda mais graves à saúde de grupos sensíveis"
            "(crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
        
    else:
        print("péssima\n")
        print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. \n" 
            "Aumento de mortes prematuras em pessoas de grupos sensíveis.")
    
    escolha = input("\nDeseja inserir outros valores? (s/n): ").lower()
    if((escolha != "s")):
        break