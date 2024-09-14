from  maestro_pizzero import  Maestro_pizzero
from  mozo import Mozo
from pizza import Pizza

class TesterPizzeria:
    def main():
        
        pizzero = Maestro_pizzero("PIPO")
        mozo1 = Mozo("Gustavo")
        mozo2 = Mozo("Leonardo")

        while True:
            print(" 1. Tomar pedido Pizzero. ","\n"
                  " 2. Ver pizzas por cocinar. ","\n"
                  " 3. Cocinar pizzas. ","\n"
                  " 4. Ver pizzas por entregar. ","\n"
                  " 5. Entregar pizzas con Gustavo. ","\n"
                  " 6. Entregar pizzas con Luis. ","\n"
                  " 7. Salir. ")

            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                pizzero.tomar_pedido("")
                
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
                break

if __name__ == '__main__':
    tester_pizzeria = TesterPizzeria
    tester_pizzeria.main()
