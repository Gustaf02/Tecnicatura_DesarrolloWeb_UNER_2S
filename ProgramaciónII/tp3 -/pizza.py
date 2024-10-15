from pizzavariedad import PizzaVariedad

class Pizza:
    # Atributos de clase (constantes de estado)
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    # Constructor
    def __init__(self, var: 'PizzaVariedad'):
        """Inicializa una pizza con su variedad y estado inicial."""
        self.__variedad = var  # Objeto de tipo PizzaVariedad
        self.__estado = Pizza.ESTADO_POR_COCINAR  # Estado inicial

    # Comandos
    def establecerVariedad(self, var: 'PizzaVariedad'):
        """Establece la variedad de pizza."""
        self.__variedad = var

    def establecerEstado(self, est: int):
        """Establece el estado de la pizza si la transición es válida."""
        if (self.__estado == Pizza.ESTADO_POR_COCINAR and est == Pizza.ESTADO_COCINADA) or \
           (self.__estado == Pizza.ESTADO_COCINADA and est == Pizza.ESTADO_ENTREGADA):
            self.__estado = est
        else:
            raise ValueError("Transición de estado no válida.")

    # Consultas
    def obtenerVariedad(self) -> 'PizzaVariedad':
        """Devuelve la variedad de la pizza."""
        return self.__variedad

    def obtenerEstado(self) -> int:
        """Devuelve el estado actual de la pizza."""
        return self.__estado

    def obtenerNombre(self) -> str:
        """Devuelve el nombre de la variedad de la pizza."""
        return self.__variedad.obtenerNombre() if self.__variedad else "Sin variedad"
