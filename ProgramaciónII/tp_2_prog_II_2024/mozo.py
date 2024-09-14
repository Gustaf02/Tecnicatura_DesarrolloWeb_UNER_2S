
# Habiendo analizado el diagrama, genere la clase Mozo con los atributos y servicios
# mencionados en dicho diagrama.
# a. El atributo pizzas se inicializa como una lista vacía.
# b. El comando tomarPizzas agrega los objetos de la clase Pizza referenciados por
# el parámetro formal pizzas. El mozo puede tomar hasta un máximo de 2 pizzas.
# c. servirPizzas limpia la lista pizzas, haciendo entrega de los pedidos a los clientes.
# d. obtenerEstadoLibre debe retornar True si es que la lista referenciada por el
# atributo pizzastiene una longitud de entre 0 y 1. Así mismo, debe retornar False
# si su tamaño es igual a 2.

from pizza import Pizza  

class Mozo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas = []  # a) Se inicializa la lista de pizzas como vacía.

    # Establecer el nombre del mozo
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    # Se toman 1 o 2 pizzas de la lista de pizzas por entregar.
    def tomar_pizzas(self, pizzas):
        if pizzas:  
            max_pizzas = min(2, len(pizzas))  # El mozo puede llevar 1 o 2 pizzas como máximo.
            self.pizzas = pizzas[:max_pizzas]  
            print(f"{self.nombre} ha tomado las pizzas: {[pizza.obtener_variedad() for pizza in self.pizzas]}.")
            del pizzas[:max_pizzas]  # Se eliminan las pizzas tomadas de la lista de pizzas por entregar.
        else:
            print(f"No hay pizzas para que {self.nombre} las tome.")  

    # c) Se sirven las pizzas a los clientes.
    def servir_pizzas(self):
        if self.pizzas:
            print(f"{self.nombre} ha servido las pizzas: {[pizza.obtener_variedad() for pizza in self.pizzas]}")
            self.pizzas = []  # Limpiamos la lista de pizzas después de servir.
        else:
            print(f"{self.nombre} no tiene pizzas para servir.")

    # d) Se verifica si el mozo está libre para tomar más pizzas.
    def obtener_estado_libre(self):
        return len(self.pizzas) == 0  # Está libre si no tiene pizzas en las manos

    # Consultas
    def obtener_nombre(self):
        return self.nombre

    def obtener_pizzas(self):
        return self.pizzas
