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
            print(" 1 Tomar pedido Mozo 1","\n")
                 # " 2 ??????","\n", 
                  #" 4 o mas Salir")
            
            opciones = int(input("Ingrese una opcion: "))

            if opciones == 1:

                pizzero.tomar_pedido("")
                pizzero.cocinar()
                pizzero.entregar()

            elif opciones == 2:
                pass
            elif opciones == 3:
               pass
            elif opciones == 4:
                pass

            else:
                break






if __name__ == '__main__':
    tester_pizeria = Tester_pizzeria
    tester_pizeria.main()
