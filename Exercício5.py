aux = []
dados  = [
    {"Nome" : "Andre", "Viagem" : [50, 100, 70.21, 5.25, 10]},
    {"Nome" : "Magal", "Viagem" : [60, 110, 80.32, 6.25, 20]},
    {"Nome" : "Pedro", "Viagem" : [70, 120, 90.43, 7.25, 30]},
    {"Nome" : "Lion", "Viagem"  : [80, 130, 100.54, 8.25, 40]}
#Distância | Vm | Pedágio | Combustível | Consumo Km/L
]

def Tempo(distancia, velocidade): return distancia / velocidade

def Consumo(distancia, combustivel, consumo): return distancia * consumo / combustivel

def MostrarDados():
    print("-" * 30)
    print(f"Nome: {nome}") 
    print(f"Tempo de viagem: {tempo:.1f} horas")
    print(f"Preço de combustível = R${consumo:.2f}")
    print(f"Preço total de viagem = R${pedagio + consumo:.2f}")

for i in dados:
    nome = i["Nome"]
    tempo = Tempo(i["Viagem"][0], i["Viagem"][1])
    pedagio = i["Viagem"][2]
    consumo = Consumo(i["Viagem"][0], i["Viagem"][3], i["Viagem"][4])
    total = consumo + pedagio
    aux.append(f"{consumo:.2f}")
print(sorted(aux))

    