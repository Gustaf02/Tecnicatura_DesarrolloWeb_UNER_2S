

from pizza_variedad import PizzaVariedad

class Pizza:
    # Estados posibles para una pizza
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    # CONSTRUCTOR: Inicializa una pizza con su variedad
    def __init__(self, var: PizzaVariedad):
        self.variedad = var
        self.estado = Pizza.ESTADO_POR_COCINAR  # Estado inicial

    # COMANDO: Cocina la pizza cambiando su estado
    def cocinar(self):
        self.estado = Pizza.ESTADO_COCINADA

    # COMANDO: Entrega la pizza cambiando su estado
    def entregar(self):
        self.estado = Pizza.ESTADO_ENTREGADA

    # CONSULTA: Devuelve una representación en texto de la pizza
    def __str__(self):
        estados = {1: "Por Cocinar", 2: "Cocinada", 3: "Entregada"}
        return f"Pizza de {self.variedad.nombreVariedad} - Estado: {estados[self.estado]}"
