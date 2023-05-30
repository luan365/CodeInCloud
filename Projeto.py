"""
Created on Mon Mar 3 09:21:14 2023

@Author: Luan de Campos Ferreira
"""

#Declaração de variáveis
continuar = "s"
senhaTemp = 0
produtos = 0

#Cadastro da senha
senha = input("Digite a senha para cadastro: ")
while continuar == "s":
    #Menu
    print("\n\n", "-" * 5, " Menu ", "-" * 5)
    escolha = input("1- Acesso ao sistema \n2- Redefinir senha \n3- Sair do sistema\n ")

    s = 0
    tentativas = 0

    if(escolha == "1"):
        while (s != senha) and (tentativas < 3):
            #Tela de acesso ao sistema
            s = input("Digite sua senha para acesso ao sistema: ")
            if (s != senha): 
                tentativas += 1
                print(f"Senha incorreta\nTentativas = {tentativas}/3")
            else: break

    elif(escolha == "2"):
        #Tela de redifinição de senha
        while (senhaTemp != senha) and (tentativas < 3):
            senhaTemp = input("Digite sua senha anterior: ")
            if(senhaTemp == senha): senha = input("Digite sua nova senha: ")
            else:
                tentativas += 1
                print(f"Senha incorreta\nTentativas = {tentativas}/3")

    elif (escolha == "3"): 
        #Sair do sistema
        exit()
    else: print ("Digite uma opção válida")

    if(tentativas >= 3):
        print("Máximo de tentativas alcançado, tente novamente mais tarde")
        exit()

    if(s == senha):
        while True:
            try:
                saldoInicial = float(input("Digite o valor do saldo incial do caixa: "))
                break
            except: print("Informe o valor em números")
            
        while True:
            try:
                produtos = float(input("Digite o valor total dos produtos: "))
                break
            except: print("Informe o valor em números")
            if(produtos < 0): print("Valor não pode ser negativo")
            else: break

        while True:
            pagamento = int(input("Qual a forma de pagamento? \n1- Cartão \n2- Dinheiro \n3- Pix\n "))
            
            if (pagamento == 1):
                print("1- Crédito \n2- Débito \n ")
                print("Efetuando pagamento...")
                break

            elif (pagamento == 2):

                while True:
                    tentativas = 0
                    dinheiro = float(input("Quantia recebida pelo cliente: "))
                    if(dinheiro >= produtos): break
                    else: 
                        print("Quantia insuiciente para pagar pelos produtos")
                        tentativas += 1
                        print(f"Tentativas = {tentativas}/3\n")
                        if (tentativas >= 3): print("Sinto muito mas você não tem como pagar pelos "
                                                    "produtos, peço para que tente novamente mais tarde")
                        exit()
                
                troco = dinheiro - produtos
                if(dinheiro != produtos):
                    print("Troco = R$", troco)
                saldoInicial -= troco + dinheiro
                break
            elif (pagamento == 3):
                print("Exibir código Qr ou chave CNPJ")
                print("Efetuando pagamento...")
                break

            else:
                print("Digite uma opção válida")

        print("Pagamento efetuado")

        continuar = input("Deseja reiniciar o programa(s/n)? \n ").lower()

print("Obrigado pela pregerência! \nVolte Sempre :)")
