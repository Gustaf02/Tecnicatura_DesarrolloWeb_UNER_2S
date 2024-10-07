from pizza import Pizza
from orden import Orden

class MaestroPizzero:

    def __init__(self, nom: str):
        self.nombre = nom
        self.ordenes_por_cocininar = []
        

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomar_pedido(self, orden):
        nro = int(input ("Igrese el numero de orden: "))
        var = input("Ingrese la variedad: ")
        var = Pizza(var)
        orden = Orden(nro,var)
        orden.establecer_nro_orden(nro)
        orden.establecer_pizzas(var.obtener_variedad)
        self.ordenes_por_cocininar.append(orden)

        print(orden.obtener_nro_order, orden.pizzas)
        print(nro)
        print(var)
        print(orden.ESTADO_INICIAL)
     


    def cocinar(self):
        for pizza in self.__pizzasPorCocinar:
            print(self.__nombre + ": cocinando una pizza de " + pizza.obtenerVariedad())
            self.__pizzasPorEntregar.append(pizza)

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
    
    def obtenerPizzasPorCocinar(self):
        return self.__pizzasPorCocinar
    
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar
    
pi = MaestroPizzero("walter")

pi.tomar_pedido(1)


