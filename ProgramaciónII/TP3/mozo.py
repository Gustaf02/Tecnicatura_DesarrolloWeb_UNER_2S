class Mozo:
    
    # Constructor correcto para la clase Mozo (no MaestroPizzero)
    def __init__(self, nombre: str):
        # Atributo de instancia para el nombre del mozo
        self.nombre = nombre
        # Atributo de instancia para las pizzas asignadas al mozo (inicialmente vacío)
        self.pizzas = []

    # Comando para establecer el nombre del mozo
    def establecerNombre(self, nombre: str):
        self.nombre = nombre

    # Comando para que el mozo tome pizzas (máximo 2)
    def tomarPizzas(self, pizzas: list):
        if pizzas:
            # El mozo puede tomar hasta 2 pizzas máximo
            max_pizzas = min(2, len(pizzas))
            self.pizzas = pizzas[:max_pizzas]
            print(f"{self.nombre} ha tomado las pizzas: {[pizza.obtenerVariedad() for pizza in self.pizzas]}")
            # Se eliminan las pizzas tomadas de la lista original
            del pizzas[:max_pizzas]
        else:
            print(f"No hay pizzas para que {self.nombre} las tome.")

    # Comando para servir las pizzas que tiene el mozo
    def servirPizzas(self):
        if self.pizzas:
            print(f"{self.nombre} ha servido las pizzas: {[pizza.obtenerVariedad() for pizza in self.pizzas]}")
            # Limpiamos la lista de pizzas después de servirlas
            self.pizzas = []
        else:
            print(f"{self.nombre} no tiene pizzas para servir.")

    # Consulta para verificar si el mozo está librre para tomar más pizzas
    # Únicamente se modifica para retornar True si la lista de pizzas está vacía
    def obtenerEstadoLibre(self):
        return len(self.pizzas) == 0

    # Consulta para obtener el nombre del mozo
    def obtenerNombre(self):
        return self.nombre

    # Consulta para otbener la lista de pizzas asignadas al mozo
    def obtenerPizzas(self):
        return self.pizzas
