'''Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y
cuando las letras que componen dicha palabra estén en orden alfabético, y False
en caso contrario'''

def es_abc (palabra):
    palabra = palabra.lower()
    return palabra == "".join(sorted(palabra))

print (es_abc("gft"))
print (es_abc("abc"))
print (es_abc("str"))
