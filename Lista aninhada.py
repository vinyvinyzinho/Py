Listas = [[1,2,3], [10,15,14], [10,15,25,35,0]]

print(Listas)

a = Listas[0]

print (a)

b = a[0]

print (b)

lista1 = Listas [1]

print(lista1)

valor_1_0 = lista1[0]

print (valor_1_0)

#calculo com listas

print (Listas)

a = Listas [0] [0]

print (a)

b = Listas [1] [2]

print (b)

c = Listas [0] [2] + 10

print (c)

d = 10 

print (d)

e = d * Listas[2] [0]

print (e)

# concatenando listas

Listas_s1 = [34, 32, 36]
Listas_s2 = [77, 50, 13]

print (Listas_s1)
print (Listas_s2)

listas_total = Listas_s1 + Listas_s2
print (listas_total)

lista_teste_op = [100, 2, -5, 3.4]

print (10 in lista_teste_op)
print (100 in lista_teste_op)

print (len(lista_teste_op))
print (max(lista_teste_op))
print (min(lista_teste_op))

lista_mercado2 = ["ovos", "leite", "farinha", "maças"]
print (lista_mercado2)

lista_mercado2.append("carne")
print(lista_mercado2)

lista_mercado2.append("carne")
print(lista_mercado2)

print (lista_mercado2.count("carne"))

a = []

print (a)

print (type(a))

a.append (50)
a.append(10)

print (a)

old_list = [1,2,3,4,5]

new_list = []

for item in old_list:
    new_list.append(item)

print(new_list)

c = []

c.append(70)
c.append(50)
c.append(30)
c.append(20)

print (c.count(20))

cidade = ['Recife', 'Manaus', 'Salvador', 'São Paulo']
cidade.extend (['Fortaleza', 'Palmas'])
print(cidade)

print (cidade.index('Salvador'))

print(cidade)

cidade.insert(2, 110)

print(cidade)

cidade.remove (110)

print(cidade)

cidade.reverse()

print(cidade)

x = [3,4,2,1]

print (x)

x.sort()

print (x)
