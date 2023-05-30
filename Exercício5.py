aux = []
dados = [
    {"Nome" : "Andre", "Viagem" : [50, 100, 70.21, 5.25, 10]},
    {"Nome" : "Magal", "Viagem" : [60, 110, 80.32, 6.25, 20]},
    {"Nome" : "Pedro", "Viagem" : [70, 120, 90.43, 7.25, 30]},
    {"Nome" : "Lion", "Viagem" : [80, 130, 100.54, 8.25, 40]}
    # Distância | Vm | Pedágio | Combustível | Consumo Km/L
]

def Tempo(distancia, velocidade):
    return distancia / velocidade

def Consumo(distancia, combustivel, consumo):
    return distancia * consumo / combustivel

def MostrarDados(nome, tempo, consumo, pedagio):
    print("-" * 30)
    print(f"Nome: {nome}") 
    print(f"Tempo de viagem: {tempo:.1f} horas")
    print(f"Preço de combustível = R${consumo:.2f}")
    print(f"Preço total de viagem = R${pedagio + consumo:.2f}\n")
    print("Valores Ordenados")

def sort(parametros, nomes):
    for i in range(len(parametros) - 1, 0, -1):
        for j in range(i):
            if parametros[j] > parametros[j + 1]:
                temp = parametros[j]
                parametros[j] = parametros[j + 1]
                parametros[j + 1] = temp
                temp = nomes[j]
                nomes[j] = nomes[j + 1]
                nomes[j + 1] = temp

for i in dados:
    nome = i["Nome"]
    tempo = Tempo(i["Viagem"][0], i["Viagem"][1])
    pedagio = i["Viagem"][2]
    consumo = Consumo(i["Viagem"][0], i["Viagem"][3], i["Viagem"][4])
    total = consumo + pedagio
    MostrarDados(nome, tempo, consumo, pedagio)
    parametros = i["Viagem"]
    nomes = ["Distância", "Vm", "Pedágio", "Combustível", "Consumo Km/L"]
    sort(parametros, nomes)
    for j in range(len(nomes)):
        print(f"{nomes[j]}: {parametros[j]}")
    print()
#!: PRINTAR EM ORDEM CRESCENTE APENAS O TOTAL
#? Mas vou printar os 2 :)