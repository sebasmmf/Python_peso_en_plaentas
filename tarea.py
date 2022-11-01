fuerza_de_gravedad_en_la_tierra = 9.807
fuerza_de_gravedad_en_marte = 3.721
fuerza_de_gravedad_en_neptuno = 11.15

peso_en_tierra = float(input("Ingrese su peso en Kg... "))
peso_marciano = (peso_en_tierra/fuerza_de_gravedad_en_la_tierra)
peso_en_marte = (peso_marciano*fuerza_de_gravedad_en_marte)
peso_en_neptuno = (peso_marciano*fuerza_de_gravedad_en_neptuno)

print("Tu peso en marte es igual a ", peso_en_marte , "Kg")
print("Tu peso en neptuno es igual a ", peso_en_neptuno , "Kg")
