
from pizza import Pizza 

class Maestro_pizzero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas_por_cocinar = []
        self.pizzas_por_entregar = []

    def establecer_nombre (self, nom):
        self.nom = nom

    def tomar_pedido(self):
        variedad = input("Ingrese la variedad de pizza: ")  
        pizza = Pizza(variedad)  
        self.pizzas_por_cocinar.append(pizza)
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

    def cocinar(self):
        if self.pizzas_por_cocinar:
            pizza_cocinada = self.pizzas_por_cocinar.pop(0)
            self.pizzas_por_entregar.append(pizza_cocinada)
            print(f"Se ha cocinado: {pizza_cocinada.obtener_variedad()}")

    def obtener_nombre (self):
        self.nombre = self.nombre
        return print(self.nombre)   

    def obtener_pizzas_por_cocinar(self):
        print(f"Pizzas por cocinar: {[p.obtener_variedad() for p in self.pizzas_por_cocinar]}")

    def obtener_pizzas_por_entregar(self):
        print(f"Pizzas por entregar: {[p.obtener_variedad() for p in self.pizzas_por_entregar]}")







