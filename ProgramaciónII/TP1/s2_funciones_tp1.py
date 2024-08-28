# A continuación, se presenta el código de un programa que, ante la edad ingresada por el usuario, # este presenta el equivalente en días, meses y años. Se solicita al alumno que lo refactorice de
# manera tal que: 
# # a. Se elimine la sentencia if / else de la función anio_bisiesto.
# b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de # varias cláusulas or.
# c. Se agregue una sentencia que valide que la edad ingresada por el usuario es# numérica.
# d. Se agregue una función que encapsule el cálculo del equivalente de la edad en # días y que tome como parámetros las variables hora_local, anio_comienzo y anio_fin.
# e.Todas las funciones sean transportadas a un archivo auxiliar de funciones
# llamado funciones.py, y este sea importado desde el programa principal.

import time
from calendar import isleap

# Calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)

# Calcular el número de días de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28

# Calcular el equivalente de la edad en días
def calcular_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        dias += 366 if anio_bisiesto(a) else 365
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    dias += hora_local.tm_mday
    return dias

# Validar que la edad ingresada sea numérica
def validar_edad(edad):
    if not edad.isdigit():
        raise ValueError("La edad debe ser un número.")
    return int(edad)
