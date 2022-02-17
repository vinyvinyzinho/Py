Nota1 = float (input("Informe a primeira nota : "))
Nota2 = float (input("Informe a segunda nota : "))

#calculo
mediafinal = (Nota1 + Nota2) / 2

#verificação
if mediafinal >= 7.0:
    print ("A média: %.1f - Aprovado" % mediafinal)
else:
    print ("A média: %.1f - Reprovado" % mediafinal)
