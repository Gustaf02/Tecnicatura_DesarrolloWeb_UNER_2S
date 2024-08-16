# Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
# que tome ambas como parámetros e imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']


def listas_diferencia(lista1, lista2):
    # Imprimir la llamada a la función como "listas"
    print(f'listas({lista1}, {lista2})')

    # Encontrar los elementos en común entre las dos listas
    comunes = list(set(lista1) & set(lista2))
    # Invertir el orden de los elementos comunes
    comunes.sort(reverse=True)
    
    # Encontrar los elementos no comunes
    no_comunes = list(set(lista1).union(set(lista2)) - set(comunes))
    # Ordenar los elementos no comunes en orden alfabético
    no_comunes.sort()

    # Imprimir los resultados
    print(comunes)
    print(no_comunes)

# Llamada a la función 
listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])





