"""b. Escribir un programa que resuelva la secuencia de Fibonacci a pedido del
usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro
numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio
anterior, validado. La función debe encargarse de calcular la secuencia para
dicho número. A continuación, una descripción matemática de la famosa
secuencia:"""


def fibonacci(numero):

    if numero == 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]

    secuencia = [0, 1]
    while len(secuencia) < numero:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia


def obtener_numero():

    while True:
        entrada = input("Por favor, ingresa un número entero positivo: ")
        try:
            numero = int(entrada)
            if numero < 0:
                print("El numero debe ser positivo")
            else:
                return numero
        except ValueError:
            print("Entrada invalida ingresa un numero entero.")


def main():
    numero = obtener_numero()
    secuencia_fibonacci = fibonacci(numero)
    print(f"La secuencia de Fibonacci hasta el término {numero} es:")
    print(secuencia_fibonacci)


main()


