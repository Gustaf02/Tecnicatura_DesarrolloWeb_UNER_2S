# c. Tal como sucede con la lógica proposicional, en Python muchas veces las expresiones booleanas pueden ser simplificadas manteniendo el valor de
# verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente # a a and b.
# A continuación, intente simplificar las siguientes expresiones y escriba un procedimiento procesar_sentencias(a, b,
# c) que permita evaluar el # valor de verdad de las expresiones ya simplificadas:
# i. (a or b) or (b and c)
# ii. b and c or False
# iii. a and b or c or (b and a)
# iv. a == True or b == False

# Procedimiento que evalúa el valor de verdad de las expresiones ya simplificadas:
# def procesar_sentencias(a, b, c):
#     # Expresiones originales
#     original_1 = (a or b) or (b and c)
#     original_2 = b and c or False
#     original_3 = a and b or c or (b and a)
#     original_4 = a == True or b == False

#     # Expresiones simplificadas
#     simplificado_1 = a or b
#     simplificado_2 = b and c
#     simplificado_3 = a and b or c
#     simplificado_4 = a or not b

#     return (original_1, simplificado_1), (original_2, simplificado_2), (original_3, simplificado_3), (original_4, simplificado_4)

# # Ejemplos para testear. Si se cambia el valor del booleano cambia el resultado en la operación original y la simplificada:
# a = True
# b = False
# c = True

# resultados = procesar_sentencias(a, b, c)

# for i, (original, simplificado) in enumerate(resultados, 1):
#     print(f"Resultado {i} (Original): {original}")
#     print(f"Resultado {i} (Simplificado): {simplificado}")
#     print("----")

# EJERCICIO SIGUIENDO EL FORMATO SUGERIDO EN CLASES ADOPTANDO TODAS LAS COMBINACIONES POSIBLES:

def procesar_sentencias(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
    # i. (a or b) or (b and c)
    sentencia = (a or b) or (b and c)
    sentencia_reducida = a or b
    print(f'i. {sentencia} | {sentencia_reducida}')
    
    # ii. b and c or False
    sentencia = b and c or False
    sentencia_reducida = b and c
    print(f'ii. {sentencia} | {sentencia_reducida}')
    
    # iii. a and b or c or (b and a)
    sentencia = a and b or c or (b and a)
    sentencia_reducida = a and b or c
    print(f'iii. {sentencia} | {sentencia_reducida}')
    
    # iv. a == True or b == False
    sentencia = (a == True) or (b == False)
    sentencia_reducida = a or not b
    print(f'iv. {sentencia} | {sentencia_reducida}')
    print('')  # Se coloca línea en blanco para separar cada conjunto de resultados


# Generar todas las combinaciones posibles de a, b, c
from itertools import product

valores = [True, False]

# Evaluar todas las combinaciones de a, b, c
for a, b, c in product(valores, repeat=3):
    procesar_sentencias(a, b, c)
