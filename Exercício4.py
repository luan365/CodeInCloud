import pandas as pd

nomes = [
    {   "Nome" : "Rogério", "Turma" : "Eng. de Computador", "RA" : 23001839, 
        "Notas" : {"Álgebra": 7, "Ap (prática)": 7, "Bd": 7}
        },
    {   "Nome" : "Antenora", "Turma" : "Direito", "RA" : 23009170, 
        "Notas" : {"Álgebra": 9, "Ap (prática)": 7.5, "Bd": 6.6}
        },
    {   "Nome" : "Mendeleck", "Turma" : "Análise e dev. de sitemas", "RA" : 23007114, 
        "Notas" : {"Álgebra": 6, "Ap (prática)": 11, "Bd": 7.8}
        }
]

notas = []

for i in nomes:
    st = i["Notas"]
    nomeAlunos = i["Nome"]
    soma = 0
    for j in st:
        soma += st[j]
    media = soma / len(i["Notas"])
    print(f"\nTotal notas de {nomeAlunos} é {soma}")
    print(f"Média de {nomeAlunos} é {media:.1f}")
    
    notas.append({"Nome": nomeAlunos, "Total Notas": soma, "Média": f"{media:.1f}"})

print(pd.DataFrame(notas))

