import time
from s2_funciones_tp1 import calcular_dias, validar_edad

# Ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Validar la edad
try:
    anios = validar_edad(edad)
except ValueError as e:
    print(e)
    exit()

# Seteo inicial de variables
hora_local = time.localtime(time.time())
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon

# Calcular los días
dias = calcular_dias(hora_local, anio_comienzo, anio_fin)

# Imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))
