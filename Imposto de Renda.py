# -*- coding: utf-8 -*-

print("-" * 30, " Calculo de salário Bruto ", "-" * 30)

# Salário
S = float(input("Digite o salário base: "))

# Percentual do imposto de renda
PIR = float(input("Percentual do imposto de renda: "))

# Imposto de Renda
IR = S * (PIR / 100)

# SB
SB = S + IR

# Salário líquido
SL = S - IR

print(f"Salário: R${S:.2f}")
print(f"Percentual do Imposto de renda: R${PIR:.2f}")
print(f"Imposto de renda: R${IR:.2f}")
print(f"Salário bruto: R${SB:.2f}")
print(f"Salário líquido: R${SL:.2f}")
