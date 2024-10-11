from pizza import Pizza
from orden import Orden

class MaestroPizzero:

    def __init__(self, nom: str):
        self.nombre = nom
        self.ordenes_por_cocininar = []
        

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomar_pedido(self, orden): 
        self.ordenes_por_cocininar.append(orden)
        #print (f"orden por cocinar: {self.ordenes_por_cocininar }")
        """nro = int(input ("Igrese el numero de orden: "))
        var = input("Ingrese la variedad: ")
        variedad = Pizza(var)
        orden = Orden(nro,variedad.establecer_variedad(var))
        orden.establecer_nro_orden(nro)
        orden.establecer_pizzas(variedad)
        orden.ESTADO_INICIAL
        print(f"variedad de pizza de la orden {nro}: Estado: INICIAL {orden.ESTADO_INICIAL} {orden.pizzas}")
        self.ordenes_por_cocininar.append(nro)
        print(f"Los numeros de orden a cocinar son: {self.ordenes_por_cocininar}")
        #print(orden.obtener_nro_order, orden.pizzas)
        #print(orden.num_orden, orden.pizzas)
      
        #print(orden.ESTADO_INICIAL)"""
     


    def cocinar(self):
        for pizza in self.__pizzas_por_cocinar:
            print(self.__nombre + ": cocinando una pizza de " + pizza.obtenerVariedad())
            self.__pizzas_por_entregar.append(pizza)

    def entregar(self, pizzas: int):
        pizzasAEntregar = []
        i = 0
        for pizza in self.__pizzasPorEntregar:
            pizzasAEntregar.append(pizza)
            self.__pizzasPorEntregar.remove(pizza)
            i += 1
            if i == pizzas:
                break
        return pizzasAEntregar

    def obtenerNombre(self):
        return self.__nombre
    
    def obtener_ordenes_por_cocinar(self):
        print("Desde obtener_ordenes... Maestro_pizzero: ")
        return self.ordenes_por_cocininar
    
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar
    





