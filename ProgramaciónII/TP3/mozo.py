from pizza import Pizza

class Mozo:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPizzas(self, pizzas: list[Pizza]):
        if len(pizzas) > 2:
            raise ValueError("El mozo solo puede tomar 2 pizzas a la vez")
        self.pizzas = pizzas

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPizzas(self):
        return self.__pizzas
    
    def servirPizzas(self):
        servidas = self.pizzas[:]
        self.pizzas.clear()
        return servidas

    def obtenerEstadoLibre(self):
        return len(self.pizzas) == 0
