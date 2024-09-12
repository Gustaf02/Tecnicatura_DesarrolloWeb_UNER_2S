from pizza import Pizza

class Maestro_pizzero :
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def establecer_nombre (self, nombre):
        self.nombre = nombre

    def tomar_pedido (self, variedad):
        self.variedad = variedad
        variedad = input("opcion 1 tomar pedido: ")
        variedad = Pizza(variedad)
        self.pizzas_por_cocinar.append(self.variedad)
        print(variedad)
        print(id(variedad))

    def cocinar (self ):
        self.pizzas_por_entregar.append(self.pizzas_por_cocinar)
        if  self.pizzas_por_entregar > self.pizzas_por_entregar[0:1:2]:
            print("en el horno solo se pueden cocinar 5 pizzas.")
        else:
            print("?????")

    def entregar (self):
        self.pizzas_por_entregar = self.pizzas_por_entregar

    def obtener_nombre (self):
        self.nombre = self.nombre

    def obtener_pizzas_por_cocicar (self):
        """Pizza[]"""
        return self.pizzas_por_cocicar
    
    def obtener_pizzas_por_entregar (self):
        """Pizza []"""
        pass
        #return self.pizzas_por_entregar
    








