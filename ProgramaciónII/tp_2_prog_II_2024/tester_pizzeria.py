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
                  " 5 Entregar pizzas. ""\n"
                  " 6 Mozo tomar pizzas. ""\n")
                
            
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
                mozo1.tomar_pizzas([])  

            elif opciones == 7:
                mozo1.obtener_estado_libre()


               
            else:
                break

  


if __name__ == '__main__':
    tester_pizeria = Tester_pizzeria
    tester_pizeria.main()

"""pizzas = Pizza(Maestro_pizzero.entregar)
        #pizzas = pizzas.cocinar
        self.pizzas.extend(Maestro_pizzero.entregar.var)
        #pizzas.extend(self.pizzas
        return print(F"Inprime desde tomar_pizza: {self.pizzas}")"""
