from pizza import Pizza
from pizza_variedad import Pizza_variedad

class Orden :
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, num_orden: int, pizzas: Pizza): 
        self.num_orden = num_orden
        self.pizzas =[]
        #self.pizzas = pizzas
        self.estado_orden = 1

    """COMANDOS"""
    def crear_orden (self, num_orden, pizzas : Pizza):
        refe_obj = input("Cree una orden: ")
        num_orden = int(input("Ingrese un nro de orden: "))
        pizzas = self.pizzas
        refe_obj = Orden(num_orden, pizzas)
        self.pizzas.append(refe_obj.num_orden)
        self.pizzas.append(refe_obj.pizzas)


    def establecer_nro_orden (self, num_orden: int):
        #num_orden = int(input("Ingrese numero de orden: "))
        self.num_orden = num_orden
        #print(str(f"se establecio el numero de orden: {self.num_orden}"))

    def establecer_pizzas (self, pizzas: Pizza):
        self.pizzas = pizzas
        # n_ob_var = input("Nombre del objeto PizzaVar: ")
        # nom_var = input("Ingrese la variedad: ")
        # precio = int(input("Ingrese el precio"))
        # n_ob_var = Pizza_variedad(nom_var, precio)
        #pizzas = input("Agregar pizzas: ")
        # pizza_objeto = Pizza(n_ob_var)
        # self.pizzas.append(pizza_objeto.obtener_variedad())
    
    # def establecer_estado (self, estado: int):
    #     self.estado = estado
    #     if estado == 1:
    #         print("Orden: " + str(self.num_orden) + " (ESTADO_INICIAL):")
    #     elif estado == 2:
    #         self.ordenes_por_cocininar
    #         print("Orden:" + str(self.num_orden) + " (ESTADO_PARA_ENTREGAR):")
    #     elif estado == 3:
    #         print("Orden: " + str(self.num_orden) + " (ESTADO_ENTREGADA):")

    """CONSULTAS"""


    def obtener_nro_orden (self):
        
        return self.num_orden

    def obtener_pizzas (self): 
        return self.pizzas

    def obtener_lei (self):
        return self.estado
    
    def calcular_total (self):
        return self.pizzas.caKOlcular_total()
      
    


