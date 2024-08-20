# c. Se agregue una sentencia que valide que la edad ingresada por el usuario es
# numérica.

import time
from calendar import isleap

# calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)

# calcular el número de días de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28

# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")

# Validación de la edad ingresada
while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("Por favor, ingrese un valor numérico para la edad.")

# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = edad
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = 0

# calcular los días
for a in range(anio_comienzo, anio_fin):
    if anio_bisiesto(a):
        dias += 366
    else:
        dias += 365

# agregar los días transcurridos en este año
for m in range(1, hora_local.tm_mon):
    dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

# agregar los días transcurridos en este mes
dias += hora_local.tm_mday

# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))






