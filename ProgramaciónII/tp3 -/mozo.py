from pizza import Pizza

class Mozo:
    # Constructor
    def __init__(self, nom: str):
        """Inicializa al mozo con su nombre y una lista vacía de pizzas."""
        self.__nombre = nom
        self.__pizzas = []  # Lista de objetos Pizza

    # Comandos
    def establecerNombre(self, nom: str):
        """Establece el nombre del mozo."""
        self.__nombre = nom

    def tomarPizzas(self, pizzas: list):
        """
        Toma una lista de pizzas si hay espacio disponible.
        El mozo puede llevar como máximo dos pizzas a la vez.
        """
        if len(pizzas) <= 2:
            self.__pizzas.extend(pizzas)
        else:
            raise ValueError("Un mozo no puede llevar más de dos pizzas a la vez.")

    def servirPizzas(self):
        """Sirve las pizzas que lleva y las marca como entregadas."""
        for pizza in self.__pizzas:
            pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)
        entregadas = self.__pizzas.copy()  # Copia las pizzas a entregar
        self.__pizzas.clear()  # Vacía la lista de pizzas
        return entregadas  # Devuelve las pizzas entregadas

    def mostrarEstado(self):
        """Muestra el estado de las pizzas que lleva el mozo."""
        print(f"Mozo: {self.__nombre}")
        print("=" * 30)
        print("Pizzas entregadas:")
        for pizza in self.__pizzas:
            print(f"- Pizza: {pizza.obtenerNombre()} | Precio: {pizza.obtenerPrecio()} | Estado: {pizza.obtenerEstado()}")
        print("-" * 30)

    # Consultas
    def obtenerNombre(self) -> str:
        """Devuelve el nombre del mozo."""
        return self.__nombre

    def obtenerPizzas(self) -> list:
        """Devuelve la lista de pizzas que lleva el mozo.""" 
        return self.__pizzas

    def obtenerEstadoLibre(self) -> bool:
        """Devuelve True si el mozo no lleva ninguna pizza, False en caso contrario."""
        return len(self.__pizzas) == 0

    def llevarPizzasDeOrden(self, orden):
        """
        Lleva pizzas de la orden dada. 
        El mozo puede llevar hasta 2 pizzas.
        """
        if orden.pizzas:
            # Lleva hasta 2 pizzas
            pizzas_a_llevar = orden.pizzas[:2]  # Toma hasta 2 pizzas
            self.tomarPizzas(pizzas_a_llevar)  # Toma las pizzas
            orden.pizzas = orden.pizzas[2:]  # Elimina las pizzas que ha tomado

