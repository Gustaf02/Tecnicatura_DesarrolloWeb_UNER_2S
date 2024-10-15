from orden import Orden
from pizza import Pizza

class MaestroPizzero:
    # Constructor
    def __init__(self, nom: str):
        """Inicializa al maestro pizzero con su nombre y una lista vacía de órdenes."""
        self.__nombre = nom
        self.__ordenes = []  # Lista de objetos Orden

    # Comandos
    def establecerNombre(self, nom: str):
        """Establece el nombre del maestro pizzero."""
        self.__nombre = nom

    def tomarPedido(self, orden: 'Orden'):
        """Agrega una orden a la lista de órdenes si está en estado inicial."""
        if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
            self.__ordenes.append(orden)
        else:
            raise ValueError("La orden debe estar en estado inicial para ser tomada.")

    def cocinar(self):
        """Cocina todas las órdenes en estado inicial y cambia su estado a para entregar."""
        for orden in self.__ordenes:
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)
                for pizza in orden.obtenerPizzas():
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)

    def entregar(self, orden: 'Orden') -> list:
        """
        Entrega hasta dos pizzas de una orden en estado para entregar.
        Cambia el estado de cada pizza entregada a entregada.
        Si todas las pizzas de la orden están entregadas, cambia el estado de la orden.
        """
        if orden.obtenerEstadoOrden() != Orden.ESTADO_PARA_ENTREGAR:
            raise ValueError("La orden debe estar en estado para entregar.")

        pizzas_entregadas = []
        for pizza in orden.obtenerPizzas():
            if len(pizzas_entregadas) < 2 and pizza.obtenerEstado() != Pizza.ESTADO_ENTREGADA:
                pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)
                pizzas_entregadas.append(pizza)

        # Verificar si todas las pizzas están entregadas
        if all(pizza.obtenerEstado() == Pizza.ESTADO_ENTREGADA for pizza in orden.obtenerPizzas()):
            orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)

        return pizzas_entregadas

    def mostrarEstado(self):
        """Muestra el estado de todas las órdenes y sus pizzas."""
        print(f"Maestro Pizzero: {self.__nombre}")
        print("=" * 30)
        for orden in self.__ordenes:
            print(f"Estado de la Orden: {orden.obtenerEstadoOrden()}")
            for pizza in orden.obtenerPizzas():
                print(f"- Pizza: {pizza.obtenerNombre()} | Precio: {pizza.obtenerPrecio()} | Estado: {pizza.obtenerEstado()}")
            print("-" * 30)

    # Consultas
    def obtenerNombre(self) -> str:
        """Devuelve el nombre del maestro pizzero."""
        return self.__nombre

    def obtenerOrdenes(self) -> list:
        """Devuelve la lista de órdenes."""
        return self.__ordenes
