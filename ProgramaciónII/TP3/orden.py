from pizza import Pizza

class Orden:
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, nro: int, pizzas: list[Pizza]):
        self.nroOrden = nro
        self.pizzas = pizzas
        self.estadoOrden = Orden.ESTADO_INICIAL

    def agregar_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def cambiar_estado_para_entregar(self):
        self.estadoOrden = Orden.ESTADO_PARA_ENTREGAR

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
      
    


