# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
Lista_obj = ["Carro", "moto", "barco", "lancha", "avião"]
print(Lista_obj)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
nome = "Vinycius "
sobre_nome = "Souza"
nome_completo = nome + sobre_nome
print (nome_completo)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 3, 4, 4, 4, 5)
print (tupla.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario = {}
print(dicionario)

estudantes = {"Vinycius": 21, "Lucas": 22, "Lucia": 23}
print(estudantes)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
estudantes['Maria'] = 25
print(estudantes)
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
mercado = {"Ovos":5, "Açucar":3, "Café":[1, 2]}
print(mercado)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista_completa = ["Teste", ("Geografia", "Historia"), {"Vinycius": 21, "Matheus":22}, 1.5]
print(lista_completa)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print (frase[0:18])
