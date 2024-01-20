texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\nCANTIDAD DE LETRAS")
cantidad_de_letras1 = texto.count(letras[0])
cantidad_de_letras2 = texto.count(letras[1])
cantidad_de_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_de_letras1} veces.")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_de_letras2} veces.")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_de_letras3} veces.")
