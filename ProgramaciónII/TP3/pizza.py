

from pizza_variedad import PizzaVariedad

class Pizza:
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: PizzaVariedad):
        self.variedad = var
        self.estado = Pizza.ESTADO_POR_COCINAR

    
    def establecer_variedad(self, var: str):
        self.__variedad = var

    def establecer_estado_interno (self, estado: int):
        self.estado = estado

    def obtener_variedad(self):
        return self.__variedad
    
    def  obtener_estado_interno (self):
        return self.estado
    def __repr__(self):
        return self.__variedad
    def cocinar(self):
        self.estado = Pizza.ESTADO_COCINADA

    def entregar(self):
        self.estado = Pizza.ESTADO_ENTREGADA

    def __str__(self):
        estados = {1: "Por Cocinar", 2: "Cocinada", 3: "Entregada"}
        return f"Pizza de {self.variedad.nombreVariedad} - Estado: {estados[self.estado]}"
