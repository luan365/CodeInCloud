"""
print("-" * 10, " Olá mundo ", 10 * "-")

text = "Olá mundo"
print(f"{text:-^20}")
"""

print("{:-^20}".format("Olá mundo"))


import pandas as pd

produtos = [
    {"Nome" : "Ipad" , "Preço" : 1200, "Quantidade" : 500},
    {"Nome" : "Iphone 12" , "Preço" : 3500, "Quantidade" : 200},
    {"Nome" : "Nokia" , "Preço" : 120, "Quantidade" : 50}
]

print(pd.DataFrame(produtos))

import msvcrt

# Ler uma tecla pressionada
tecla = msvcrt.getch()

# Converter a tecla pressionada para uma string
valor = tecla.decode('utf-8')

# Imprimir o valor
print("Valor lido:", valor)