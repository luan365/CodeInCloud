"""
print("-" * 10, " Olá mundo ", 10 * "-")

text = "Olá mundo"
print(f"{text:-^20}")

print("{:-^20}".format("Olá mundo"))

"""

import pandas as pd

produtos = [
    {"Nome" : "Ipad" , "Preço" : 1200, "Quantidade" : 500},
    {"Nome" : "Iphone 12" , "Preço" : 3500, "Quantidade" : 200},
    {"Nome" : "Nokia" , "Preço" : 120, "Quantidade" : 50}
]

tabela = pd.DataFrame(produtos)
print(tabela)

print(pd.DataFrame(produtos))