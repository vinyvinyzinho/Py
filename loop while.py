# loop while
"""
#usando loop while para imprimir os valores de 0 a 9

counter = 0 
while counter < 10:
    print (counter)
    counter = counter +1

# usar a clausula else para encerrar o loop while

x = 0 

while x <= 10: 
    print('o valor de x nesta itereção é: ', x)
    print('x ainda é menor que 10, somando 1 a x')
    x += 1

else:
    print('loop concluido!')
    """


# --- pass, break, continue ---
"""
counter = 0
while counter < 100:
    if counter == 4 :
        break
    else:
        pass
    print (counter)
    counter = counter +1


#continue

for verificador in "python":
    if verificador =="h":
        continue
    print(verificador)
   
# while e for juntos

for i in range (2, 30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j = j + 1 
        else:
            j = j + 1
    if counter == 0:
        print(str(i) + " é um número primo")
        counter = 0
    else:
        counter = 0 
        """