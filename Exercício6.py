# Definir o dataset contendo os efeitos e suas causas com pesos
dataset = {
    'Má qualidade de sono': {'Atividade física': (0, 4), 'Alimentação': (0, 6), 'Quantidade de água bebida': (0, 2)},
    'Boa qualidade de sono': {'Atividade física': (6, 10), 'Alimentação': (7, 10), 'Quantidade de água bebida': (5, 10)},
    'Regular qualidade de sono': {'Atividade física': (4, 7), 'Alimentação': (4, 7), 'Quantidade de água bebida': (3, 6)},
    'Insônia': {'Atividade física': (0, 4), 'Alimentação': (0, 5), 'Quantidade de água bebida': (0, 2)},
    'Sonolência excessiva': {'Atividade física': (0, 4), 'Alimentação': (0, 4), 'Quantidade de água bebida': (0, 3)},
    'Pesadelos frequentes': {'Atividade física': (0, 4), 'Alimentação': (0, 3), 'Quantidade de água bebida': (0, 1)},
    'Dificuldade de concentração': {'Atividade física': (0, 4), 'Alimentação': (0, 5), 'Quantidade de água bebida': (0, 3)},
    'Pouca disposição durante o dia': {'Atividade física': (0, 4), 'Alimentação': (0, 3), 'Quantidade de água bebida': (0, 5)},
    'Despertares noturnos frequentes': {'Atividade física': (0, 4), 'Alimentação': (0, 3), 'Quantidade de água bebida': (0, 2)},
    'Qualidade de sono variável': {'Atividade física': (4, 7), 'Alimentação': (4, 7), 'Quantidade de água bebida': (3, 6)},
}

# Função para calcular a probabilidade de associação entre causas e efeitos
def calcular_probabilidade(causas):
    probabilidade = {}
    for efeito, causas_peso in dataset.items():
        prob_total = 0
        for causa, peso in causas_peso.items():
            if causa in causas:
                valor = causas[causas.index(causa) + 1]
                if peso[0] <= valor <= peso[1]:
                    prob_total += peso[1]
        if prob_total > 0:
            probabilidade[efeito] = prob_total / len(causas)
    return probabilidade

# Causas de consulta (atividade física, alimentação e quantidade de água bebida)
causas_consulta = [
    'Atividade física',
    int(input("Informe o nível de atividade física (0 a 10): ")),
    'Alimentação',
    int(input("Informe o nível de alimentação (0 a 10): ")),
    'Quantidade de água bebida',
    int(input("Informe a quantidade de água bebida (0 a 10): "))
]

# Calcular a probabilidade de associação com os efeitos
probabilidade_assoc = calcular_probabilidade(causas_consulta)

# Apresentar os efeitos com suas respectivas probabilidades
print("Probabilidade de associação entre as causas e os efeitos:")
for efeito, probabilidade in probabilidade_assoc.items():
    print(f"{efeito}: {probabilidade}")
