from itertools import count
"""
#tupla
tp = (2,3,4)

for i in tp:
    print(i)

#lista
lista_de_mercado = ["Leite", "Farinha", "Açucar", "Ovos", "Chocolate"]

for i in lista_de_mercado:
    print(i)

# imprimindo os valores por intervalo

for contador in range (1,6):
    print(contador)

# numeros pares
lista = [1,2,3,4,5,6,7,8,9,10]

for num in lista:
    if num % 2 == 0:
        print(num)

# listando os numeros no intervalo de 0 a 101, com incremento em 2

for i in range (0, 101, 2):
    print(i)


# string tambémm são sequencias
for caracter in 'python é uma linguagem de programação divertida!':
    print(caracter)
"""

"""
# loops aninhados

from tokenize import Double


for i in range (0, 5):
    for a in range (0, 5):
        print (a)

# operando valores de umalista com loop for

listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    Double_i = i*2
    soma += Double_i

print(soma)

# loop em lista de listas

listas = [[1,2,3], [10,15,14],[10.1,8.7,2.3]]

for valor in listas:
    print(valor)


# contando os itens de uma lista




lista = [5,6,10,13,17]
count = 0 
for item in lista:
    count += 1

print (count)

# contando o numero de colunas

lst = [[1,2,3],[4,5,6],[7,8,9]]
primeira_linha = lst[0]
count = 0
for column in primeira_linha:
    count = count +1
print (count)
""" 
# pesquisando em listas

listac = [5,6,7,10,50]
#loop atráves da lista

for item in listac:
    if item == 5:
        print("Número encontrado na lista")

"""
#listando chaves de um dicionario

dicionario = {'k1': 'python', 'k2':'R', 'k3':'scala'}
for item in dicionario:
    print (item)

#imprimindo chave e valor do dicionario. Usando o metodo item() oara retornar os itens de um dicionario

for k,v in dicionario.items():
    print(k,v,)
"""

