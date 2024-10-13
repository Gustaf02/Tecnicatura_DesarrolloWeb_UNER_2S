from mozo import Mozo
from maestropizzero import MaestroPizzero
from pizza import Pizza
from orden  import Orden
from pizza_variedad import Pizza_variedad 


class Tester:
    
   
    def main(self):
        #CARTA DE LA PIZZERIA
        self.carta = []
        #TOTAL DE ORDENES CREADAS
        self.ver_ordenes = []


        #OBJETOS MaestroPizzero Y Mozo   
        pizzero = MaestroPizzero("walter")
        mozo_1 = Mozo('Gustavo')
        mozo_2 = Mozo('Leonardo')

        #CREO VARIEDADES DE PIZZA
        gerente_variedad = Pizza_variedad("gerente", 100000000000)
        variedad_1 = Pizza_variedad("muzza", 5000)
        variedad_2 = Pizza_variedad("napo", 7000)
        variedad_3 = Pizza_variedad("crudo", 10000)
        variedad_4 = Pizza_variedad("rucula", 7000)
        variedad_5 = Pizza_variedad("azul", 8000)
       

        #OBJETOS Pizza
        gerente_pizza = Pizza(gerente_variedad)
        pizza_1 = Pizza(variedad_1)
        pizza_2 = Pizza(variedad_2)
        pizza_3 = Pizza(variedad_3)
        pizza_4 = Pizza(variedad_4)
        pizza_5 = Pizza(variedad_5)
      
        
        #OBJETOS Orden
        gerente_orden = Orden(1,[pizza_3.obtener_estado_interno(), pizza_1, pizza_2,pizza_2])
        print(gerente_orden)

        """orden_1 = Orden(1,"")
        self.ver_ordenes.append(orden_1.num_orden)
        
        orden_2 = Orden(2, "")
        self.ver_ordenes.append(orden_2.num_orden)
        
        orden_3 = Orden(3, "")
        self.ver_ordenes.append(orden_3.num_orden)
       
        orden_4 = Orden(4, "")
        self.ver_ordenes.append(orden_4.num_orden)

        #AGREGO VARIEDAD DE PIZA Y SU PRECIO A LA CARTA DE LA PIZZARIA
        self.carta.append(variedad_1.nombre_var)
        self.carta.append(variedad_1.pre)
        self.carta.append(variedad_2.nombre_var)
        self.carta.append(variedad_2.pre)
        self.carta.append(variedad_3.nombre_var)
        self.carta.append(variedad_3.pre)
        #self.carta.append(variedad_4.nombre_var)
        #self.carta.append(variedad_4.pre)

       

        #AGREGO PIZZAS A LA LISTA self.pizza DE Ordenes
        #   orden 1
        orden_1.pizzas.append(pizza_1.obtener_variedad().obtener_nombre())
        orden_1.pizzas.append(pizza_1.ESTADO_POR_COCINAR)
        orden_1.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_1.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        orden_1.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_1.pizzas.append(pizza_3.ESTADO_POR_COCINAR)

        #   orden 2
        orden_2.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_3.ESTADO_POR_COCINAR)
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        orden_2.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_3.ESTADO_POR_COCINAR)
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        
        #   orden 3
        orden_3.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_3.pizzas.append(pizza_3.ESTADO_POR_COCINAR)
        orden_3.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_3.pizzas.append(pizza_2.ESTADO_POR_COCINAR)
        orden_3.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_3.pizzas.append(pizza_2.ESTADO_POR_COCINAR)

        #   orden 4
        orden_4.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_4.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_4.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())

        # print("--------------------------------------------------------------------") 
        # print(f"Nro de orden {orden_1.num_orden}, estado {orden_1.ESTADO_INICIAL}")
        # print(orden_1.obtener_pizzas())
        # print("--------------------------------------------------------------------")
        # print(f"Nro de orden {orden_4.num_orden}, estado {orden_4.ESTADO_INICIAL}")
        # print(orden_2.obtener_pizzas())
        # print("--------------------------------------------------------------------")
        # print(f"Nro de orden {orden_3.num_orden}, estado {orden_3.ESTADO_INICIAL}")
        # print(orden_3.obtener_pizzas())
        # print("--------------------------------------------------------------------")
    
        #CLASE Maestro_pizzero 
        pizzero.tomar_pedido(orden_1.num_orden)
        pizzero.tomar_pedido(orden_1.ESTADO_INICIAL)
        pizzero.tomar_pedido(orden_1.pizzas)
       
        
        pizzero.tomar_pedido(orden_2.num_orden)
        pizzero.tomar_pedido(orden_2.ESTADO_INICIAL)
        pizzero.tomar_pedido(orden_2.pizzas)
        

        pizzero.tomar_pedido(orden_3.num_orden)
        pizzero.tomar_pedido(orden_3.ESTADO_INICIAL)
        pizzero.tomar_pedido(orden_3.pizzas)

        #SALIDAS POR CONSOLA
        #IMPRIMO LA CARTA CON LAS VARIEDADES DE PIZZAS CREADAS
        print("--------------------------------------------------------------------")
        print("Carta. ")
        print(self.carta)

        #VER LOS NUMEROS DE ORDEN
        print("--------------------------------------------------------------------")
        print("Ordenes creadas: ")
        print(self.ver_ordenes)
        
        # #pizzero.obtener_ordenes_por_cocinar()
        print("--------------------------------------------------------------------")
        print("Ordenes tomadas:")
        print(pizzero.obtener_ordenes_por_cocinar())#[int+["",int]]
        print("--------------------------------------------------------------------")
        print( orden_1.obtener_nro_orden())#int
        print( orden_1.obtener_pizzas())#[""]
        print("--------------------------------------------------------------------")
        print( orden_2.obtener_nro_orden())
        print( orden_2.obtener_pizzas())
        print("--------------------------------------------------------------------")
        print( orden_3.obtener_nro_orden())
        print( orden_3.obtener_pizzas())


        #COCINAR
        #pizzero.cocinar()"""

        #VARIEDAD
        while True:
            print("Comience creando una carta de pizzas.\n"
                  "1. Crear pizza: \n"
                  "2. Ver carta de pizzas\n"
                  "3. Genere una orden\n"
                  "4. Agregar pizzas a la orden")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                gerente_variedad.crear_variedad("walter", 100000000)
                gerente_variedad.obtener_set()

            elif opcion == 2:
                pass
                

            elif opcion == 3:
                gerente_orden.crear_orden(1,[])

            elif opcion == 4:
                print("Agregue una pizza de la lista a la oden:")
                gerente_pizza.crear_pizza()
  










        #Orden
        # def crear_orden(num_orden):
        #     num_orden = int(input("Ingrese numero de orden: "))
        #     pizzas = []
        #
        #     pizza = input("Ingrese ")
        #     orden = Orden(num_orden, "")
        #

if __name__ == '__main__':
    tester = Tester()
    tester.main()   

