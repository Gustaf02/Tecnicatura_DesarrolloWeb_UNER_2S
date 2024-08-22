# a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo
# que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro número.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a
# un dígito entero, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
# while).
# BONUS: Luego, codificar una función equivalente que utilice recursividad.
def suma(numero):
    total = 0
    for i in range(1, numero + 1):
        total += i
    return total

# Bloque principal
while True:
    numero = input("Ingresa un número entero (un solo dígito entre 0 y 9, incluyendo al 10): ")
    
    if numero.isdigit():  # Verifica si es un número entero positivo
        numero = int(numero)
        if 0 <= numero <= 10:  # Verifica que el número esté entre 0 y 10
            break
        else:
            print("Por favor, ingresa un dígito entre 0 y 10.")
    elif numero.replace('.', '', 1).isdigit() and numero.count('.') == 1:
        # Verifica si es un número decimal
        print("No se permiten números decimales. Por favor, ingresa un número entero.")
    else:
        print("Entrada inválida. No se permiten cadenas o caracteres especiales. Por favor, ingresa solo un dígito (0-10).")

resultado = suma(numero)
print(f"La suma de los números de 1 a {numero} es: {resultado}")

# A CONTINUACIÓN, FUNCIÓN EQUIVALENTE QUE UTILIZA RECURSIVIDAD

# def suma_recursiva(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero + suma_recursiva(numero - 1)

# def solicitar_numero():
#     numero = input("Ingresa un número entero (un solo dígito entre 0 y 9, incluyendo al 10): ")

#     if numero.isdigit():  # Verifica si es un número entero positivo
#         numero = int(numero)
#         if 0 <= numero <= 10:  # Verifica que el número esté entre 0 y 10
#             return numero
#         else:
#             print("Por favor, ingresa un dígito entre 0 y 10.")
#     elif numero.replace('.', '', 1).isdigit() and numero.count('.') == 1:
#         # Verifica si es un número decimal
#         print("No se permiten números decimales. Por favor, ingresa un número entero.")
#     else:
#         print("Entrada inválida. No se permiten cadenas o caracteres especiales. Por favor, ingresa solo un dígito (0-10).")
    
#     return solicitar_numero()  # Llama recursivamente hasta que la entrada sea válida

# # Bloque principal
# numero = solicitar_numero()  # Llama a la función recursiva para solicitar el número
# resultado = suma_recursiva(numero)  # Llama a la función recursiva para calcular la suma
# print(f"La suma recursiva de los números de 1 a {numero} es: {resultado}")
