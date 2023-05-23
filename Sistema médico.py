print("{:-^40}".format("Sistema médico"))

dados = [{ "Doença": "Gripe",   "Sintomas" : {"Tosse": 6, "Febre": 5 , "Dor Garganta": 4}},
         { "Doença": "Malaria", "Sintomas" : {"Suor": 4, "Febre": 6 , "Dor Corpo": 7}},
         { "Doença": "Covid",   "Sintomas" : {"Tosse": 5, "Febre": 9, "Dor Peito": 5}},     
         { "Doença": "Dengue",  "Sintomas" : {"Tosse": 3, "Dor Muscular": 9}}     
]
"""

print("Imprime tudo")
for i in dados:
    print(i)


print("\nImpreme somente as doenças")
for i in dados:
    print(i["Doença"], end=" ")


print("\n\n\nImprime as doenças e os sitomas")
for i in dados:
    print(i["Doença"],"\t",i["Sintomas"])


print("\nVerifica se há alguma uma doença cadastrada")
aux = input("Doença:")
flag = False
for i in dados:
    if(aux == i["Doença"]): print(f"{aux} Está cadastrado e apresenta sintomas como ", i["Sintomas"])
if(not flag): print("Não encontrada")
"""

for i in dados:
    st = i["Sintomas"]
    doenca = i["Doença"]
    soma = 0
    for j in st:
        soma += st[j]
    print(f"Total peso de {doenca} é {soma}")

