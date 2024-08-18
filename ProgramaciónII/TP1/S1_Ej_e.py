# Escribir un procedimiento numeros_par_impar(entrada) que, dada una lista de números, eleve cada elemento impar
# en ella al cuadrado y los mueva a otra lista e imprima ambas. La lista de números la ingresa el usuario en forma de números
# separados por coma.
# Suponiendo que el usuario ingresa la siguiente lista:
# 1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81

def numeros_par_impar(entrada):
    # Convertir la entrada en una lista de números enteros
    lista_numeros = [int(x) for x in entrada.split(',')]
    
    # Listas para números pares e impares elevados al cuadrado
    pares = []
    impares_cuadrados = []
    
    # Recorrer cada número en la lista original.
    # Si el número es par, se agrega a la lista de pares.
    # Si el número es impar, se eleva al cuadrado y se agrega a la lista de impares elevados al cuadrado.
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares_cuadrados.append(numero ** 2)
    
    # Imprimir las dos listas
    print(",".join(map(str, pares)))
    print(",".join(map(str, impares_cuadrados)))

# Solicitud de números al usuario
entrada = input("Ingresa una lista de números separados por coma: ")
numeros_par_impar(entrada)

