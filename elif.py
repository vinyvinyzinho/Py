dia = "Terça"
"""
if dia == "Segunda":
    print("Hoje vai chover")
else:
    print("hoje vai fazer sol")

#ELIF
if dia == "Segunda":
    print("Hoje fará sol")
elif dia == "Terça":
    print("Hoje vai chover")
else:
    print("Sem previsão do tempo para o dia selecionado")
"""
#ELIF CONDICIONAIS, OPERADORES LOGICOS E PLACEHOLDERS
""""
disciplina = input('Digite o nome da materia: ')
nota_final = input('Digita a nota final (entre 0 e 100): ') 

if disciplina == 'Geografia' and nota_final >='70':
    print('vc foi aprovado!')
else:
    print('Vc não foi aprovado!')
"""
disciplina = input('Digite o nome da materia: ')
nota_final = input('Digita a nota final (entre 0 e 100): ') 
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >='50' and int(semestre) != 1:
    print('vc foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Vc não foi aprovado!')



