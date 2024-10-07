from mozo import Mozo
from maestropizzero import MaestroPizzero
from pizza import Pizza
from orden  import Orden
#from pizza_vaierdad import PizzaVariedad

class Tester:
   
    def main(self):
        pizzero = MaestroPizzero("walter")
        mozo_1 = Mozo('Gustavo')
        mozo_2 = Mozo('Leonardo')

        pizzero.establecerNombre('WALTER')
        mozo_1.establecerNombre('GUSTAVO')
        mozo_2.establecerNombre('LEONARDO')
        pizzero.establecerNombre('WALTERrrrrr')

        print(pizzero)
        print (mozo_1)
        print (mozo_2) 

        print(pizzero.obtenerNombre())

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
                pizzero.tomar_pedido(1)
            elif opcion == 2:
                pizzero.obtener_pizzas_por_cocinar()

            elif opcion == 3:
                pizzero.cocinar()

            elif opcion == 4:
                pizzero.obtener_pizzas_por_entregar()

            elif opcion == 5:
                mozo_1.tomar_pizzas(pizzero.pizzas_por_entregar)
                mozo_1.servir_pizzas()
                pizzero.obtener_pizzas_por_entregar()

            elif opcion == 6:
                mozo_2.tomar_pizzas(pizzero.pizzas_por_entregar)
                mozo_2.servir_pizzas()
                pizzero.obtener_pizzas_por_entregar()

            elif opcion == 7:
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida, por favor elija una opción del 1 al 7.")

       
    

if __name__ == '__main__':
    tester = Tester()
    tester.main()   

