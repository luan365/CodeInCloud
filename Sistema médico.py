print("{:-^40}".format("Sistema médico"))

dados = [{ "Doença": "Gripe", "Sintomas" : ["Tosse", "Febre" , "Dor Garganta"]},
         { "Doença": "Malaria", "Sintomas" : ["Suor", "Febre" , "Dor Corpo"]},
         { "Doença": "Covid", "Sintomas" : ["Tosse", "Febre" , "Dor Peito"]},     
         { "Doença": "Dengue", "Sintomas" : ["Tosse", "Dor Muscular"]}     
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

s1 = input("Digite o sintoma: ")
s2 = input("Digite o sintoma: ")
total = []
for i in dados:
    st = i["Sintomas"]
    ns = len(st)
    total.append(ns)
    soma = 0
    for j in st:
        if s1 == j: soma += 1
        if s2 == j: soma += 1
    total.append(soma)
#
aux = input("Digite o sintoma: ")
print("\nVerifica as doenças pelo sintoma")
flag = True
txt = ""
for i in dados:
    st = i["Sintomas"]
    for j in st:
        if(aux == j):
            txt += i["Doença"] + " "
            flag = True
print(f"{txt} " if flag else "Não encontrado")

