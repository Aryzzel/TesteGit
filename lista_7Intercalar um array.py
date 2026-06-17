# Descrição
# Você deve intercalar dois arrays de números inteiros.

# Formato de entrada

# Na primeira linha você receberá um número inteiro n indicando o tamanho de cada um dos arrays.

# As próximas n linhas correspondem aos elementos do primeiro array.

# Depois seguirão mais n linhas correspondendo aos elementos do segundo array.




def formarArrays(n):
    array1 = []
    array2 = []
    for i in range(1, n*2+1):
        elemento = int(input())
        if i < n+1:
            array1.append(elemento)
        else:
            array2.append(elemento)
    return array1, array2
def printArraysIntercalados(array1: list,array2: list):
    for i in range(0,len(array1)):
        print(array1[i])
        print(array2[i])

n = int(input())
array1, array2 = formarArrays(n)
printArraysIntercalados(array1, array2)