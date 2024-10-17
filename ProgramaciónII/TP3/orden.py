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

    def entregar_pizzas(self):
        for pizza in self.pizzas:
            pizza.entregar()

    def todas_pizzas_entregadas(self):
        return all(pizza.estado == Pizza.ESTADO_ENTREGADA for pizza in self.pizzas)

    def __str__(self):
        estado = {1: "Inicial", 2: "Para Entregar", 3: "Entregada"}
        return f"Orden {self.nroOrden} - Estado: {estado[self.estadoOrden]} - Pizzas: {len(self.pizzas)}"
    
    def precio_total(self):
        return sum(pizza.variedad.precio for pizza in self.pizzas)
    
    def entregar_pizzas(self):
        for pizza in self.pizzas:
            pizza.entregar()

    def todas_pizzas_entregadas(self):
        return all(pizza.estado == Pizza.ESTADO_ENTREGADA for pizza in self.pizzas)

    def __str__(self):
        estado = {1: "Inicial", 2: "Para Entregar", 3: "Entregada"}
        return f"Orden {self.nroOrden} - Estado: {estado[self.estadoOrden]} - Pizzas: {len(self.pizzas)}"
    
    def precio_total(self):
        return sum(pizza.variedad.precio for pizza in self.pizzas)
    



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




    
