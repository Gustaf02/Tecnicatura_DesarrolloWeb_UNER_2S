class Orden:
    # Atributos de clase (constantes)
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3

    # Constructor
    def __init__(self, nro: int, pizzas: list):
        """Inicializa una nueva orden con un número y una lista de pizzas."""
        self.__nroOrden = nro
        self.__pizzas = pizzas  # Lista de objetos Pizza
        self.__estadoOrden = Orden.ESTADO_INICIAL  # Estado inicial

    # Comandos
    def establecerNroOrden(self, nro: int):
        """Establece el número de la orden."""
        self.__nroOrden = nro

    def establecerPizzas(self, pizzas: list):
        """Establece la lista de pizzas asociadas a la orden."""
        self.__pizzas = pizzas

    def establecerEstadoOrden(self, est: int):
        """Establece el estado de la orden solo si la transición es válida."""
        if (self.__estadoOrden == Orden.ESTADO_INICIAL and est == Orden.ESTADO_PARA_ENTREGAR) or \
           (self.__estadoOrden == Orden.ESTADO_PARA_ENTREGAR and est == Orden.ESTADO_ENTREGADA):
            self.__estadoOrden = est
        else:
            raise ValueError("Transición de estado no válida.")

    def cocinadas(self):
        """Marca la orden como cocinada, cambiando su estado a 'para entregar'."""
        self.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)

    # Consultas
    def obtenerNroOrden(self) -> int:
        """Devuelve el número de la orden."""
        return self.__nroOrden

    def obtenerPizzas(self) -> list:
        """Devuelve la lista de pizzas asociadas a la orden."""
        return self.__pizzas

    def obtenerEstadoOrden(self) -> int:
        """Devuelve el estado actual de la orden."""
        return self.__estadoOrden
    
    def eliminarPizzas(self, pizzas_a_eliminar: list):
        """Elimina las pizzas de la lista de pizzas asociadas a la orden."""
        self.__pizzas = [pizza for pizza in self.__pizzas if pizza not in pizzas_a_eliminar]

    def calcularTotal(self) -> float:
        """Calcula el costo total de la orden sumando el precio de cada pizza."""
        return sum(pizza.obtenerVariedad().obtenerPrecio() for pizza in self.__pizzas)

    def __str__(self):
        """Devuelve una representación en cadena de la orden."""
        estado = {
            Orden.ESTADO_INICIAL: "Por Cocinar",
            Orden.ESTADO_PARA_ENTREGAR: "Cocinada",
            Orden.ESTADO_ENTREGADA: "Entregada"
        }.get(self.__estadoOrden, "Estado Desconocido")
        
        pizzas_list = ', '.join(pizza.obtenerVariedad().nombre for pizza in self.__pizzas)
        return f"Orden #{self.__nroOrden} - Estado: {estado} - Pizzas: [{pizzas_list}]"
