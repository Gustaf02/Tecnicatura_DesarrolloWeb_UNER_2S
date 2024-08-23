# c. Se agregue una sentencia que valide que la edad ingresada por el usuario es
# numérica.
#d. Se agregue una función que encapsule el cálculo del equivalente de la edad en 
#días y que tome como parámetros las variables hora_local, anio_comienzo y
#anio_fin.



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

def equivalente_en_dias(hora_local, anio_comienzo, anio_fin):
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
    return dias
dias = equivalente_en_dias(hora_local, anio_comienzo, anio_fin)

# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))

####### PUNTO D ENCAMPSULAR FUNCION ########
"""def equivalente_en_dias(hora_local, anio_comienzo, anio_fin):
    print("####### punto d ######")
    hora_local = time.localtime(time.time())
    bisiesto = 0
    for a_bisiesto in range(anio_comienzo, anio_fin):
        if isleap(a_bisiesto): bisiesto = bisiesto + 1
    print(f"Desde el año {anio_comienzo} hasta el {anio_fin} hay {bisiesto} año bisiestos")
    print(f"En {bisiesto} años bisiestos hay {bisiesto * 366} dias.")
    años_no_bi = edad - bisiesto
    print(f"En {años_no_bi} años hay {años_no_bi * 365} dias.")
    print(f"Total de dias {(bisiesto * 366)+ (años_no_bi * 365)+(hora_local.tm_mday)}")
    return (bisiesto * 366) + ((anio_fin - anio_comienzo) * 365) 

dias = equivalente_en_dias(hora_local, anio_comienzo, anio_fin) + hora_local.tm_mday
print(f"En {edad} años transcurrieron {meses} y  {dias} dias!!")
print(f"El año  de inicio es: {anio_comienzo} y el año actual es {anio_fin}")
print("###### fin punto d ######")"""











