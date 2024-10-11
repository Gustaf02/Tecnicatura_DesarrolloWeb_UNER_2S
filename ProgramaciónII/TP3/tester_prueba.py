from mozo import Mozo
from maestropizzero import MaestroPizzero
from pizza import Pizza
from orden  import Orden
from pizza_variedad import Pizza_variedad 


class Tester:
    
   
    def main(self):
        #CARTA DE LA PIZZERIA
        self.carta = []
        #TOTAL DE ORDENES EXISTENTES
        self.ver_ordenes = []

        #OBJETOS MaestroPizzero Y Mozo   
        pizzero = MaestroPizzero("walter")
        mozo_1 = Mozo('Gustavo')
        mozo_2 = Mozo('Leonardo')

        #CREO VARIEDADES DE PIZZA
        variedad_1 = Pizza_variedad("muzzaaaa", 5000)
        variedad_2 = Pizza_variedad("napo", 7000)
        variedad_3 = Pizza_variedad("crudo", 10000)

        #OBJETOS Pizza
        pizza_1 = Pizza(variedad_1)
        pizza_2 = Pizza(variedad_2)
        pizza_3 = Pizza(variedad_3)
        
        #OBJETOS Orden MIREN LOS ARGUMETOS QUE LE PUSE AL PARAMETRO self.pizza 
        orden_1 = Orden(1111, pizzas="")
        self.ver_ordenes.append(orden_1.num_orden)
        
        #DIFERENTE PARAMETRO O EL MISMO PORQUE ES UN STR VACIO NO SE SI VA  PERO FUNCIONA
        orden_2 = Orden(2, "")
        self.ver_ordenes.append(orden_2.num_orden)
        
        orden_3 = Orden(3, "")
        self.ver_ordenes.append(orden_3.num_orden)
       
        orden_4 = Orden(444, "")
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

        #IMPRIMO LA CARTA CON LAS VARIEDADES DE PIZZAS CREADAS
        print("--------------------------------------------------------------------")
        print("Lista de variedad y precio: ")
        print(self.carta)

        #VER LOS NUMEROS DE ORDEN
        print("--------------------------------------------------------------------")
        print("Lista total de ordenes num_orden : Orden: ")
        print(self.ver_ordenes)

        #AGREGO PIZZAS A LA LISTA self.pizza DE Ordenes
        #   orden 1
        orden_1.pizzas.append(pizza_1.obtener_variedad().obtener_nombre())
        orden_1.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_1.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())

        #   orden 2
        orden_2.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_2.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())

        #   orden 3
        orden_3.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_3.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_3.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())

        #   orden 4
        orden_4.pizzas.append(pizza_3.obtener_variedad().obtener_nombre())
        orden_4.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())
        orden_4.pizzas.append(pizza_2.obtener_variedad().obtener_nombre())

        print("--------------------------------------------------------------------") 
        print(f"Nro de orden {orden_1.num_orden}, estado {orden_1.ESTADO_INICIAL}")
        print(orden_1.obtener_pizzas())
        print("--------------------------------------------------------------------")
        print(f"Nro de orden {orden_4.num_orden}, estado {orden_4.ESTADO_INICIAL}")
        print(orden_2.obtener_pizzas())
        print("--------------------------------------------------------------------")
        print(f"Nro de orden {orden_3.num_orden}, estado {orden_3.ESTADO_INICIAL}")
        print(orden_3.obtener_pizzas())
        print("--------------------------------------------------------------------")
    
        #CLASE Maestro_pizzero 
        pizzero.tomar_pedido(orden_1.num_orden)
        pizzero.tomar_pedido(orden_1.pizzas)
        pizzero.tomar_pedido(orden_1.ESTADO_INICIAL)
        pizzero.tomar_pedido(orden_4.num_orden)
        pizzero.tomar_pedido(orden_1.ESTADO_INICIAL)
        pizzero.tomar_pedido(orden_3.num_orden)
        pizzero.tomar_pedido(orden_1.ESTADO_INICIAL)
        #pizzero.obtener_ordenes_por_cocinar()
        print(pizzero.obtener_ordenes_por_cocinar())

        #COCINAR
        #pizzero.cocinar()

        orden_1.establecer_nro_orden(num_orden=200)

        
      

if __name__ == '__main__':
    tester = Tester()
    tester.main()   

