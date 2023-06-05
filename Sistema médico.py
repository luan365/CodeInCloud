print("{:-^40}".format("Qualidade de sono"))

dados = [{"Efeito": "Má qualidade de sono",            "Motivo"  : {"Atividade física": 4, "Alimentação": 5, "Quantidade de água bebida": 3, "Sobrecarga" : 8}},
         {"Efeito": "Boa qualidade de sono",           "Motivo"  : {"Atividade física": 9, "Alimentação": 9, "Quantidade de água bebida": 9, "Estresse": 0}},
         {"Efeito": "Insônia",                         "Motivo"  : {"Barulho": 6, "Alimentação": 5, "Trabalho Noturno": 8, "Estresse": 9}},
         {"Efeito": "Sonolência excessiva",            "Motivo"  : {"Atividade física": 2, "Estresse": 3, "Quantidade de água bebida": 3, "Noite mal dormida": 9}},
         {"Efeito": "Pesadelos frequentes",            "Motivo"  : {"Ansiedade": 9, "Estresse": 8, "Medo": 10}},
         {"Efeito": "Dificuldade de concentração",     "Motivo"  : {"Estresse": 8, "Sobrecarga": 7, "Alimentação": 3}},
         {"Efeito": "Pouca disposição durante o dia",  "Motivo"  : {"Atividade física": 3, "Alimentação": 2, "Noite mal dormida": 8}},
         {"Efeito": "Despertares noturnos frequentes", "Motivo"  : {"Atividade física": 4, "Alimentação": 3, "Estresse": 9, "Medo": 9}}
]


for i in dados:
    motivo = i["Motivo"]
    efeito = i["Efeito"]
    soma = 0
    for j in motivo:
        soma += motivo[j]
    print(f"Total peso de {efeito} é {soma}")


