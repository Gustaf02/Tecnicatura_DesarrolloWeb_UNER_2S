def procesar_palabras(entrada):
    palabras = entrada.split(',')
    palabras_ordenadas = sorted(palabras)
    print(', '.join(palabras_ordenadas))

entrada_usuario = "manzana,pera,banana,uva"
procesar_palabras (entrada_usuario)