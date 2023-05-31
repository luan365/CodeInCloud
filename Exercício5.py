dados = [
    {"Nome": "Andre", "Viagem": [50, 100, 70.21, 5.25, 10]},
    {"Nome": "Magal", "Viagem": [60, 110, 80.32, 6, 20]},
    {"Nome": "Pedro", "Viagem": [70, 120, 90.43, 7.25, 30]},
    {"Nome": "Leoncio", "Viagem": [50, 115, 70.21, 5.15, 15]},
    {"Nome": "Hercules", "Viagem": [66, 80, 80.32, 6.25, 8]},
    {"Nome": "Marileide", "Viagem": [33, 100, 90.43, 5.50, 30]},
    {"Nome": "Chiquinha", "Viagem": [42, 70, 90.43, 7.25, 17]},
    {"Nome": "Maurício", "Viagem": [56, 75, 70.21, 10, 18]},
    {"Nome": "Mendeleck", "Viagem": [100, 140, 80.32, 6.25, 20]},
    {"Nome": "Chacon", "Viagem": [83, 650, 90.43, 7.25, 30]},
    {"Nome": "Lúcia", "Viagem": [80, 65, 100.54, 8.25, 40]}
    # Distância | Vm | Pedágio | Combustível | Consumo Km/L
]

def Tempo(distancia, velocidade):
    return distancia / velocidade

def MostrarDados(nome, tempo, consumo, pedagio):
    print("-" * 30)
    print(f"\nNome: {nome}")
    print(f"Tempo de viagem: {tempo:.1f} horas")
    print(f"Preço de combustível = R${consumo:.2f}")
    print(f"Preço total de viagem = R${pedagio + consumo:.2f}\n")
    print("Valores Ordenados:")

def sort(parametros, caracteristicas):
    for i in range(len(parametros) - 1, 0, -1):
        for j in range(i):
            if parametros[j] > parametros[j + 1]:
                parametros[j], parametros[j + 1] = parametros[j + 1], parametros[j]
                caracteristicas[j], caracteristicas[j + 1] = caracteristicas[j + 1], caracteristicas[j]

def ConsumoTotal(i):
    distancia, _, pedagio, combustivel, consumo = i["Viagem"] #Um descarte para completar a quantidade de valores em viagem, porem desnecessária
    return ((distancia * consumo) / combustivel) + pedagio

ordemDados = sorted(dados, key=ConsumoTotal)

for i in ordemDados:
    nome = i["Nome"]
    tempo = Tempo(i["Viagem"][0], i["Viagem"][1])
    pedagio = i["Viagem"][2]
    MostrarDados(nome, tempo, ConsumoTotal(i), pedagio)
    parametros = i["Viagem"]
    caracteristicas = ["Distância", "Velocidade Média", "Pedágio", "Combustível", "Consumo Km/L"]
    sort(parametros, caracteristicas)
    for j in range(len(caracteristicas)):
        print(f"{caracteristicas[j]}: {parametros[j]}")
    print()
