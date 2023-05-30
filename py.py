def getLinha(matriz, n):
    return [i for i in matriz[n]]  

def getColuna(matriz, n):
    return [i[n] for i in matriz]

# matriz chave
mat1 = [[11, 13], [2, 3]]            
mat1lin = len(mat1)                
mat1col = len(mat1[0])             

# matriz do codigo cripitografado
mat2 = [[4, 18, 14, 7, 20], [1, 11, 9, 8, 20]]    
mat2lin = len(mat2)                
mat2col = len(mat2[0])             

matRes = []                        
for i in range(mat1lin):           
    matRes.append([])

    for j in range(mat2col):
        # multiplica cada linha de mat1 por cada coluna de mat2
        listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]

        matRes[i].append(sum(listMult))

print(matRes[0])
print(matRes[1])


#resto da multiplicaçao das matrizes
matF1 = []
for i in matRes[0]:
  i = i % 26
  matF1.append(i)
  
matF2 = []
for i in matRes[1]:
  i = i % 26
  matF2.append(i)

#dado criptografado
print("\n", matF1)
print(matF2)