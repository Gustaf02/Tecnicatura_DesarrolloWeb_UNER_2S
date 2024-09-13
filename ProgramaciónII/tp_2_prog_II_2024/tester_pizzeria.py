from  maestro_pizzero import  Maestro_pizzero
from  mozo import Mozo
from pizza import Pizza
class Tester_pizzeria:
    def main():
       
        pizzero = Maestro_pizzero("PIPO")
        #mozo1 = Mozo("CARLOS")
        #mozo2 = Mozo("JUAN")
        #print(f"El nombre del pizzero es {pizzero.nombre}")
        #print(f"El nombre del mozo es {mozo1.nombre}")
        #print(f"El nombre del mozo es {mozo2.nombre}")
        #print(pizzero)
        #pizzero.pizzas_por_cocinar.append(crear_pizza.variedad)
                #print(f"Las pizzas por cocinar : {pizzero.pizzas_por_cocinar}")
                #order_de_pizzas = pizzero.pizzas_por_cocinar[0]
                #pizzero.pizzas_por_cocinar.remove(order_de_pizzas)
                #pizzero.pizzas_por_entregar.append(order_de_pizzas)
                #print(f"Las pizzas por cocinar : {pizzero.pizzas_por_cocinar}")
                #print(f"Las pizzas por entregar: {pizzero.pizzas_por_entregar}")
            

        while True:
            print(" 1 Tomar pedido Pizzero. ","\n"
                  " 2 Pizzas a cocinar. ""\n"
                  " 3 Cocinar pizzas. ""\n"
                  " 4 Pizzas por entregar. ""\n"
                  " 5 Entregar pizzas. ""\n")
            
            opciones = int(input("Ingrese una opcion: "))

            if opciones == 1:
                pizzero.tomar_pedido("")
                
            elif opciones == 2:
                pizzero.obtener_pizzas_por_cocicar()

            elif opciones == 3:
                pizzero.obtener_pizzas_por_entregar()

            elif opciones == 4:
                pizzero.cocinar()
                 
            elif opciones == 5:
                pizzero.entregar()
               
            else:
                break






if __name__ == '__main__':
    tester_pizeria = Tester_pizzeria
    tester_pizeria.main()
