from pizza import Pizza

class Orden :
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, num_orden: int, pizzas: Pizza): 
        self.num_orden = num_orden
        self.pizzas = pizzas
        self.estado_orden = 1

    """COMANDOS"""

    def establecer_nro_orden (self, num_orden: int):
        self.num_orden = num_orden

    def establecer_pizzas (self, pizzas: Pizza):
        self.pizzas = pizzas

    def establecer_estado (self, estado: int):
        self.estado = estado
        if estado == 1:
            print("Orden: " + str(self.num_orden) + " (ESTADO_INICIAL):")
        elif estado == 2:
            print("Orden:" + str(self.num_orden) + " (ESTADO_PARA_ENTREGAR):")
        elif estado == 3:
            print("Orden: " + str(self.num_orden) + " (ESTADO_ENTREGADA):")

    """CONSULTAS"""


    def obtener_nro_order (self):
        return self.num_orden

    def obtener_pizzas (self): 
        return self.pizzas

    def obtener_lei (self):
        return self.estado
    
    def calcular_total (self):
        return self.pizzas.caKOlcular_total()
      
    


