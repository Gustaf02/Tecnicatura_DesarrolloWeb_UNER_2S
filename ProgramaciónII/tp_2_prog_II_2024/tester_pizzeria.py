from  maestro_pizzero import  Maestro_pizzero
from  mozo import Mozo
from pizza import Pizza
class Tester_pizzeria:
    def main():

        mozo1 = Mozo("CARLLOS")
        
       
        pizzero = Maestro_pizzero("PIPO")
       
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
                pizzero.obtener_pizzas_por_cocinar()

            elif opciones == 3:
                pizzero.cocinar()
                

            elif opciones == 4:
                pizzero.obtener_pizzas_por_entregar()
                
                 
            elif opciones == 5:
                pizzero.entregar()

            elif opciones == 6:
                mozo1.tomar_pizzas()

               
            else:
                break

  


if __name__ == '__main__':
    tester_pizeria = Tester_pizzeria
    tester_pizeria.main()
