class PizzaVariedad:
    # Constructor
    def __init__(self, nomVar: str, pre: float):
        """Inicializa una nueva variedad de pizza con su nombre y precio."""
        if pre <= 0.0:
            raise ValueError("El precio debe ser mayor que 0.0")
        self.__nombreVariedad = nomVar
        self.__precio = pre

    # Comandos
    def establecerNombreVariedad(self, nomVar: str):
        """Establece el nombre de la variedad de pizza."""
        self.__nombreVariedad = nomVar

    def establecerPrecio(self, pre: float):
        """Establece el precio de la pizza. Tiene que ser mayor a 0.0."""
        if pre <= 0.0:
            raise ValueError("El precio debe ser mayor que 0.0")
        self.__precio = pre

    # Consultas
    def obtenerNombreVariedad(self) -> str:
        """Devuelve el nombre de la variedad de pizza."""
        return self.__nombreVariedad

    def obtenerPrecio(self) -> float:
        """Devuelve el precio de la variedad de pizza."""
        return self.__precio

