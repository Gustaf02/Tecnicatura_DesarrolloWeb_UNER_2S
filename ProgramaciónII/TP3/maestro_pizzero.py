from orden import Orden
from pizza import Pizza

class MaestroPizzero:
    
   # CONSTRUCTOR: Inicializa al maestro pizzero con un nombre y una lista vacía de órdenes
    def __init__(self, nom: str):
        self.__nombre = nom
        self.ordenes = []

# COMANDO: Establece el nombre del maestro pizzero
    def establecerNombre(self, nom: str):
        self.__nombre = nom

# COMANDO: El maestro toma un pedido solo si está en estado inicial
    def tomarPedido(self, orden: Orden):
        if orden.estadoOrden == Orden.ESTADO_INICIAL:
            self.ordenes.append(orden)
        else:
            raise ValueError("La orden no está en estado inicial")

# COMANDO: Cocina las pizzas de las órdenes pendientes
    def cocinar(self):
        for orden in self.ordenes:
            if orden.estadoOrden == Orden.ESTADO_INICIAL:
                for pizza in orden.pizzas:
                    pizza.cocinar()
                orden.cambiar_estado_para_entregar()

# CONSULTA: Devuelve el nombre del maestro pizzero
    def obtenerNombre(self):
        return self.__nombre
    
# COMANDO: Entrega las pizzas si están listas para entregar    
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

# CONSULTA: Devuelve la lista de órdenes pendientes
    def obtenerOrdenes(self):
        return self.ordenes
    
 # CONSULTA: Devuelve las pizzas por entregar
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar
    





