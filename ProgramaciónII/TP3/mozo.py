
from pizza import Pizza

class Mozo:
     # CONSTRUCTOR: Inicializa al mozo con un nombre y una lista vacía de pizzas
    def __init__(self, nom: str):
        self.__nombre = nom
        self.pizzas = []

    # COMANDO: Establece el nombre del mozo
    def establecerNombre(self, nom: str):
        self.nombre = nom

    # COMANDO: El mozo toma hasta 2 pizzas para servir
    def tomarPizzas(self, pizzas: list[Pizza]):
        if len(pizzas) > 2:
            raise ValueError("El mozo solo puede tomar 2 pizzas a la vez")
        self.pizzas = pizzas

    # CONSULTA: Obtiene el nombre del mozo
    def obtenerNombre(self):
        return self.__nombre
    
    # CONSULTA: Devuelve las pizzas tomadas por el mozo
    def obtenerPizzas(self):
        return self.__pizzas
    
    # COMANDO: Sirve las pizzas tomadas y vacía la lista de pizzas
    def servirPizzas(self):
        servidas = self.pizzas[:]
        self.pizzas.clear()
        return servidas

    #def obtenerEstadoLibre(self):
        #return len(self.pizzas) == 0

    #def obtenerEstadoLibre(self):
        #return len(self.pizzas) == 0 or len(self.pizzas) < 0

  # CONSULTA: Verifica si el mozo está libre (menos de 2 pizzas tomadas)
    def obtenerEstadoLibre(self):
        pizzasTomadas = len(self.pizzas)
        return pizzasTomadas < 2