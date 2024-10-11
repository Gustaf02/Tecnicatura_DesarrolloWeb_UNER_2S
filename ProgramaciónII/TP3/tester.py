


from mozo import Mozo
from maestropizzero import MaestroPizzero
from pizza import Pizza
from orden  import Orden
from pizza_variedad import Pizza_variedad 


class Tester:
    carta = []
    ver_ordenes = []
   
    def main(self):
        pizzero = MaestroPizzero("walter")
        mozo_1 = Mozo('Gustavo')
        mozo_2 = Mozo('Leonardo')
        
        
       

        def crear_pizza_usuario (self, str_var, float_pre):
                str_var = input("Ingrese el nombre de la pizza: ")
                float_pre = int(input("Ingrese el precio de la pizza: "))
                var_pizz = Pizza_variedad(str_var, float_pre)
                self.carta.append(var_pizz)
            

        def crear_orden_usuario (self, int_ord): 
            int_ord = int(input("Ingrese el numero de orden: "))
            nu_or = Orden(int_ord, self.carta[0])
            self.ver_ordenes.appen(nu_or)
    
        def ver_carta (self):
            return self.carta
    
        def ver_ordenes (self):
            return self.ver



        while True:
            print("\nMenu:")
            print(" 1. Tomar pedido Pizzero.")
            print(" 2. Agregar pizza a la orden.")
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
                pizzero.tomar_pedido(2)
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

