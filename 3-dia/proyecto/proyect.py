texto = input("ingresa un texto a eleccion: ")
letras = []

texto = texto.lower()

letras.append(input("ingresa la primera letra: ").lower())
letras.append(input("ingresa la segunda letra: ").lower())
letras.append(input("ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantida_de_letras1 = texto.count(letras[0])
cantida_de_letras2 = texto.count(letras[1])
cantida_de_letras3 = texto.count(letras[2])

print(f"hemos encontrado la letra '{letras[0]}' repetida {cantida_de_letras1} veces")
print(f"hemos encontrado la letra '{letras[1]}' repetida {cantida_de_letras2} veces")
print(f"hemos encontrado la letra '{letras[2]}' repetida {cantida_de_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabra = texto.split()
print(f"hemos encontrado '{len(palabra)}' palabras en tu texto")


print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"la letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")


print("\n")
print("TEXTO INVERTIDO")
palabra.reverse()
texto_invertido = " ".join(palabra)
print(f"si ordenas tu texto al reves va a decir: '{texto_invertido}'")


print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True : 'si', False : 'no'}
print(f"la palabra 'python' {dic[buscar_python]} se encuentra en el texto" )