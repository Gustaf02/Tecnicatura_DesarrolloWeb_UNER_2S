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
    
    # agregar los días transcurridos en este año
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))

# agregar los días transcurridos en este mes
    dias += hora_local.tm_mday
    return dias

def equivalente_en_dias(hora_local, anio_comienzo, anio_fin):
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


# Validación de la edad ingresada
'''def validar_edad():
  while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("Por favor, ingrese un valor numérico para la edad.")'''
