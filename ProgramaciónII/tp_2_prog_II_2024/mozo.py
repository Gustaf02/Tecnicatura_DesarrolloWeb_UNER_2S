
from  pizza import Pizza
from maestro_pizzero import Maestro_pizzero

class Mozo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas = []

    def establecer_nombre (self, nombre):
        nombre = self.nombre

    def tomar_pizzas (self, pizzas):
        pizzas = Pizza(Maestro_pizzero.entregar)
        #pizzas = pizzas.cocinar
        self.pizzas.append(pizzas)
        print(self.pizzas)
        return print(f"Inprime desde tomar_pizza: {pizzas}")
       
    
        
        
      





    def obtener_nombre (nombre):
        return  nombre

    def obtener_pizzas (self, pizza):
        return pizza

    def obtener_estado_libre ():
        return
    pass













