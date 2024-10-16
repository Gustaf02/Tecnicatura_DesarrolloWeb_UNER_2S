# maestro_pizzero.py
from orden import Orden
from pizza import Pizza

class MaestroPizzero:
    def __init__(self, nom: str):
        self.nombre = nom
        self.ordenes = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, orden: Orden):
        if orden.estadoOrden == Orden.ESTADO_INICIAL:
            self.ordenes.append(orden)
        else:
            raise ValueError("La orden no está en estado inicial")

    def cocinar(self):
        for orden in self.ordenes:
            if orden.estadoOrden == Orden.ESTADO_INICIAL:
                for pizza in orden.pizzas:
                    pizza.cocinar()
                orden.cambiar_estado_para_entregar()

    def entregar(self, pizzas: int):
        self.pizzasas_a_entregar = []
        i = 0
        for pizza in self.ordenes_por_cocininar:
            self.pizzas_a_entregar.append(pizza)
            self.pizzas_a_entregar.remove(pizza)
            i += 1
            if i == pizzas:
                break
        return self.pizzas_a_entregar

    def obtenerNombre(self):
        return self.__nombre
    
    def obtener_ordenes_por_cocinar(self):
        return self.ordenes_por_cocininar
        """print("Desde obtener_ordenes... Maestro_pizzero: ")
        print (f"Nro_ord: {self.ordenes_por_cocininar[0]}, Est_ord: {self.ordenes_por_cocininar[2]}, Pizas: {self.ordenes_por_cocininar[1]}")
        print (f"Nro_ord: {self.ordenes_por_cocininar[3]}, Est_ord: {self.ordenes_por_cocininar[4]}")
        print (f"Nro_ord: {self.ordenes_por_cocininar[5]}, Est_ord: {self.ordenes_por_cocininar[5]}")
        #print (f"Est_ord: {self.ordenes_por_cocininar[2:4]}")
        print (self.ordenes_por_cocininar[7:8])
        #print (self.ordenes_por_cocininar[:2])"""
    
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar
    





