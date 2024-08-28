'''Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y
cuando las letras que componen dicha palabra estén en orden alfabético, y False
en caso contrario'''

# def es_abc (palabra):
#     palabra = palabra.lower()
#     return palabra == "".join(sorted(palabra))

# print (es_abc("gft"))
# print (es_abc("abc"))
# print (es_abc("str"))

# A continuación, se presenta el mismo ejercicio donde se solicita que el usuario ingrese datos: 

def es_abc(palabra):
    # Convertimos la palabra a minúsculas para asegurar consistencia en la comparación
    palabra = palabra.lower()

    # Comparamos la palabra original con la misma palabra ordenada alfabéticamente
    return palabra == ''.join(sorted(palabra))

# Solicitar la palabra al usuario
palabra = input("Ingresa una palabra: ")

# Verificar si las letras de la palabra están en orden alfabético
resultado = es_abc(palabra)

# Mostrar el resultado
if resultado:
    print(f'Las letras de la palabra "{palabra}" están en orden alfabético.')
else:
    print(f'Las letras de la palabra "{palabra}" no están en orden alfabético.')

