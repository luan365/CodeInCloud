import pandas as pd

nomes = [
    {   "Nome" : "Rogério", "Turma" : "Eng. de Computador", "RA" : 23001839, 
        "Notas" : {"Álgebra": 7, "Ap (prática)": 8, "Bd": 8.7}
        },
    {   "Nome" : "Antenora", "Turma" : "Direito", "RA" : 23009170, 
        "Notas" : {"Álgebra": 9, "Ap (prática)": 7.5, "Bd": 6.6}
        },
    {   "Nome" : "Mendeleck", "Turma" : "Análise e dev. de sitemas", "RA" : 23007114, 
        "Notas" : {"Álgebra": 6, "Ap (prática)": 10, "Bd": 7.8}
        }
]

for i in nomes:
    st = i["Notas"]
    nomeAlunos = i["Nome"]
    soma = 0
    for j in st:
        soma += st[j]
    print(f"Total notas de {nomeAlunos} é {soma}")
    print(f"Media de {nomeAlunos} é {soma / 3:.1f}")

