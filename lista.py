#nota = [10, 2, 9, 8]
media = 0
nota = []
k = int(input("Quantidade de provas realizadas: "))
for i in range(0, k): 
    nota.append(float(input(f"Digite a nota da: {i + 1}º prova: ")))
    media += nota[i]
print(f"Media = {media / len(nota):.1f}")