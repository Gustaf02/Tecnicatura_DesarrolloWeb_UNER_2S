from pizza import Pizza

class Maestro_pizzero :
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def establecer_nombre (self, nombre):
        self.nombre = nombre

    def tomar_pedido (self, var):
        var = (input("opcion 1 tomar pedido: "))
        self.piz = Pizza(var)
        self.pizzas_por_cocinar.append(self.piz.var)
        print(f"Pizzas por cocinar: {self.pizzas_por_cocinar}")
        
        print(self.piz)
        print(id(self.piz))

    def cocinar (self ):
        orden_pizzas = self.pizzas_por_cocinar[0]
        if len(self.pizzas_por_cocinar) > 2:
            self.pizzas_por_cocinar.remove(orden_pizzas)
            self.pizzas_por_entregar.append(orden_pizzas)
            print(f"Pizzas por entregar: {self.pizzas_por_entregar}")
        
    def entregar (self):
        self.pizzas_por_entregar = self.pizzas_por_entregar

    def obtener_nombre (self):
        self.nombre = self.nombre
        print(self.nombre)

    def obtener_pizzas_por_cocicar (self):
        """Pizza[]"""
        return self.pizzas_por_cocicar
    
    """def obtener_pizzas_por_entregar (self):
        #Pizza []
        self.pizzas_entregadas = []
        pizzas = self.pizzas_por_entregar[0]
        if len(self.pizzas_por_entregar) > 4:
            self.pizzas_por_entregar.remove(pizzas)
            self.pizzas_entregadas.append(pizzas)
        print(f"Las pizzas entregadas son: {self.pizzas_entregadas}")

        #return self.pizzas_entregadas"""
    








