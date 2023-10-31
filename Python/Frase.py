# Función para invertir las palabras de una frase
def invertir_palabras(frase):
    palabras = frase.split()  # Dividir la frase en palabras
    palabras_invertidas = palabras[::-1]  # Invertir la lista de palabras
    frase_invertida = " ".join(palabras_invertidas)  # Unir las palabras invertidas en una frase
    return frase_invertida

# Solicitar la entrada del usuario
frase_original = input("Ingrese una frase: ")

# Llamar a la función para invertir las palabras
frase_invertida = invertir_palabras(frase_original)

# Imprimir la frase invertida
print("Frase invertida:", frase_invertida)