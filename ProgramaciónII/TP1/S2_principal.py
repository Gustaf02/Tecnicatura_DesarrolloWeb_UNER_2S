# c. Se agregue una sentencia que valide que la edad ingresada por el usuario es
# numérica.
#d. Se agregue una función que encapsule el cálculo del equivalente de la edad en 
#días y que tome como parámetros las variables hora_local, anio_comienzo y
#anio_fin.
#e. Todas las funciones sean transportadasa un archivo auxiliar de funciones
#llamado funciones.py, y este sea importado desde el programa 
#principal.
    


### Programa Principal ###

from funciones import*
import time
from S2_Ej_c import  equivalente_en_dias, anio_bisiesto, calcular_dias_mes

    
# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input ("Ingrese su edad: ")

if not edad.isdigit():
     print ("La edad igresada es invalida,debe ser un numero")
     exit()
edad= int(edad)

     
# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = edad
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon

dias = equivalente_en_dias(hora_local, anio_comienzo, anio_fin) + hora_local.tm_mday


# imprimir la edad del usuario
#print("La edad de %s es %d años o " % (nombre, anios), end="")
#print("%d meses o %d días" % (meses, dias))

print(f"En {edad} años transcurrieron {meses} y  {dias} dias!!")
print(f"El año  de inicio es: {anio_comienzo} y el año actual es {anio_fin}")












