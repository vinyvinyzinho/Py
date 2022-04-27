estudante_lst = [ "Matheus",24, "Vinycius" , 7 , "Julia", 26, "Lidia", 25 ]

print (estudante_lst)

estudantes_dict = {"Matheus":24, "Vinycius": 7 , "Julia": 26, "Lidia": 25 }
print (estudantes_dict)

print (estudantes_dict["Matheus"])
estudantes_dict["Pedro"] = 23

print (estudantes_dict["Pedro"])


estudantes_dict.clear
print (estudantes_dict)

estudantes= {"Matheus":24, "Vinycius": 7 , "Julia": 26, "Lidia": 25 }
print (estudantes)

print (len(estudantes))

print (estudantes.keys())

print (estudantes.values())

print (estudantes.items())

estudantes2 = {"Maria":27, "Jamal": 28 , "Andressa": 20, "Lucas": 21 }
print (estudantes2)

estudantes.update(estudantes2)
print (estudantes)
