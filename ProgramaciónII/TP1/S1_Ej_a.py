"""a. Escribir una función de nombre palabra_no_tiene_letras(palabra,
letras_prohibidas), la cual retorne True si es que los caracteres que componen
una palabra no se encuentran en una lista de caracteres prohibidos."""

print("###############")
print("### ejer. a ###")
print("###############")
def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

palabra = input("Ingrese una palabra: ")
letras_prohibidas = ['x', 'y', 'z']

resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)

print(resultado)
print("Fin de la ejecución")


    