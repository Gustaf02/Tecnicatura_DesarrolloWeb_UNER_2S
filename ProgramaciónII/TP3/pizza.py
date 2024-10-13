

class Pizza:

    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: str):
        self.__variedad = var
        self.estado = 1
        self.pizzas_obj = []

    def crear_pizza(self,var):
        refe_obj = input("Ingrese ")
        pizza = Pizza(var)
        
        self.pizzas_obj.append(self.estado)
        self.pizzas_obj.append(self.__variedad)
        

        

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