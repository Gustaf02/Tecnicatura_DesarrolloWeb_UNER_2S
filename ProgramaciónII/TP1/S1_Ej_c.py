'''c. Escriba un procedimiento procesar_palabras(entrada) que acepte una 
secuencia de palabras separadas por coma, las ordene y las imprima. 
Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te'''

# # Sin ingreso del usuario 

# def procesar_palabras(entrada):
#     palabras = entrada.split(',')
#     palabras_ordenadas = sorted(palabras)
#     print(', '.join(palabras_ordenadas))

# entrada_usuario = "te,felicito,que,bien,actuas"
# procesar_palabras (entrada_usuario)

# A continuación se presenta el ejercicio de otra manera, donde el usuario ingresa la palabra

def procesar_palabras(entrada):
    # Separar las palabras usando la coma como delimitador y eliminar espacios adicionales
    palabras = [palabra.strip() for palabra in entrada.split(',')]

    # Ordenar las palabras alfabéticamente
    palabras_ordenadas = sorted(palabras)

    # Unir las palabras ordenadas en una sola cadena, separadas por comas
    resultado = ','.join(palabras_ordenadas)

    # Imprimir el resultado
    print("Palabras ordenadas:", resultado)

# Solicitar la secuencia de palabras al usuario
entrada = input("Ingresa una secuencia de palabras separadas por comas: ")

# Procesar las palabras ingresadas
procesar_palabras(entrada)
