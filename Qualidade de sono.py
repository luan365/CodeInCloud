print("{:-^40}".format("Qualidade de sono"))

dados = [{"Efeito": "Má qualidade de sono",            "Motivo"  : {"Atividade física": 4, "Alimentação": 5, "Quantidade de água bebida": 3, "Sobrecarga" : 8}},
         {"Efeito": "Insônia",                         "Motivo"  : {"Barulho": 6, "Alimentação": 5, "Trabalho Noturno": 8, "Estresse": 9}},
         {"Efeito": "Sonolência excessiva",            "Motivo"  : {"Atividade física": 2, "Estresse": 3, "Quantidade de água bebida": 3, "Noite mal dormida": 9}},
         {"Efeito": "Pesadelos frequentes",            "Motivo"  : {"Ansiedade": 9, "Estresse": 8, "Medo": 10}},
         {"Efeito": "Dificuldade de concentração",     "Motivo"  : {"Estresse": 8, "Sobrecarga": 7, "Alimentação": 3}},
         {"Efeito": "Pouca disposição durante o dia",  "Motivo"  : {"Atividade física": 3, "Alimentação": 2, "Noite mal dormida": 8}},
         {"Efeito": "Despertares noturnos frequentes", "Motivo"  : {"Atividade física": 4, "Alimentação": 3, "Estresse": 9, "Medo": 9}}
]


cons = [
    'Atividade física',
    int(input("Informe o nível de atividade física (0 a 10): ")),
    'Alimentação',
    int(input("Informe o nível de alimentação (0 a 10): ")),
    'Quantidade de água bebida',
    int(input("Informe a quantidade de água bebida (0 a 10): ")),
    'Sobrecarga',
    int(input("Informe o nível de sobrecarga (0 a 10): ")),
    'Estresse',
    int(input("Informe o nível de estresse (0 a 10): ")),
    'Noite mal dormida',
    int(input("Informe a quantidade de noite mal dormida (0 a 10): ")),   
    'Medo',
    int(input("Informe o nível de medo (0 a 10): ")),
    'Barulho',
    int(input("Informe a quantidade de barulho (0 a 10): ")),
    'Trabalho Noturno',
    int(input("Informe a quantidade de trabalho noturno (0 a 10): ")),
    'Ansiedade',
    int(input("Informe o nível de Ansiedade (0 a 10): ")),

]


def calculo():
    probabilidade = {}
    for i in range(0, len(dados)):
        motivo = dados[i]["Motivo"]
        efeito = dados[i]["Efeito"]
        soma = 0
        for j in motivo:
            soma += motivo[j] * cons[cons.index(j) + 1]
        prob = "{:.1f}".format(soma / (len(motivo)))
        probabilidade[efeito] = prob
    for efeito, prob in probabilidade.items():
        print(f"{efeito}: {prob}%")
calculo()