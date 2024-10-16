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


    def obtenerNombre(self):
        return self.__nombre
    
    def entregar(self, orden: Orden):
        if orden.estadoOrden == Orden.ESTADO_PARA_ENTREGAR:
            entregadas = [pizza for pizza in orden.pizzas if pizza.estado == Pizza.ESTADO_COCINADA][:2]
            for pizza in entregadas:
                pizza.entregar()
            
            if orden.todas_pizzas_entregadas():
                orden.estadoOrden = Orden.ESTADO_ENTREGADA

            return entregadas
        else:
            raise ValueError("La orden no está lista para entregar")

    def obtenerOrdenes(self):
        return self.ordenes
    
    
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar
    





