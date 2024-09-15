# Habiendo analizado el diagrama, genere la clase Mozo con los atributos y servicios
# mencionados en dicho diagrama.
# a. El atributo pizzas se inicializa como una lista vacía.
# b. El comando tomarPizzas agrega los objetos de la clase Pizza referenciados por
# el parámetro formal pizzas. El mozo puede tomar hasta un máximo de 2 pizzas.
# c. servirPizzas limpia la lista pizzas, haciendo entrega de los pedidos a los clientes.
# d. obtenerEstadoLibre debe retornar True si es que la lista referenciada por el
# atributo pizzastiene una longitud de entre 0 y 1. Así mismo, debe retornar False
# si su tamaño es igual a 2.

from maestro_pizzero import Maestro_pizzero
from mozo import Mozo
from pizza import Pizza

class TesterPizzeria:
    @staticmethod
    def main():
        # a) Se crean los objetos de tipo MaestroPizzero y Mozo
        pizzero = Maestro_pizzero("PIPO")
        # mozo1 = Mozo("Gustavo")
        # mozo2 = Mozo("Leonardo")

# Para realizar el ejercicio 4 del TP2 se instancian los objetos y se contestan las preguntas solicitadas en el 
# archivo denominado integrantes.pdf:
        mozo1 = Mozo('Alfredo')
        mozo2 = Mozo('Alfredo')

# A continuación, se muestra el menú de opciones
        while True:
            print("\nMenu:")
            print(" 1. Tomar pedido Pizzero.")
            print(" 2. Ver pizzas por cocinar.")
            print(" 3. Cocinar pizzas.")
            print(" 4. Ver pizzas por entregar.")
            print(" 5. Entregar pizzas con mozo1.")
            print(" 6. Entregar pizzas con mozo2.")
            print(" 7. Salir.")

            # Validación de la entrada para evitar que un valor no numérico cause un error
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
                continue  # Regresa al inicio del loop para pedir la opción de nuevo

            if opcion == 1:
                pizzero.tomar_pedido()

            elif opcion == 2:
                pizzero.obtener_pizzas_por_cocinar()

            elif opcion == 3:
                pizzero.cocinar()

            elif opcion == 4:
                pizzero.obtener_pizzas_por_entregar()

            elif opcion == 5:
                mozo1.tomar_pizzas(pizzero.pizzas_por_entregar)
                mozo1.servir_pizzas()
                pizzero.obtener_pizzas_por_entregar()

            elif opcion == 6:
                mozo2.tomar_pizzas(pizzero.pizzas_por_entregar)
                mozo2.servir_pizzas()
                pizzero.obtener_pizzas_por_entregar()

            elif opcion == 7:
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida, por favor elija una opción del 1 al 7.")

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    TesterPizzeria.main()