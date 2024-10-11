from pizza import Pizza
#from pizza_variedad import Pizza_variedad

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

    def establecer_nro_orden (self, num_orden: int):
        num_orden = int(input("Ingrese numero de orden: "))
        self.num_orden = num_orden
        print(str(f"se establecio el numero de orden: {self.num_orden}"))

    def establecer_pizzas (self, pizzas: Pizza):
        self.pizzas = pizzas
     
    def establecer_estado (self, estado: int):
        self.estado = estado
 
    """CONSULTAS"""

    def obtener_nro_order (self):
        
        return self.num_orden

    def obtener_pizzas (self): 
        return self.pizzas

    def obtener_estado(self):
        return self.estado
    
    #def calcular_total (self):
        #return total_calcuado # total_calculado(int)
      
    


