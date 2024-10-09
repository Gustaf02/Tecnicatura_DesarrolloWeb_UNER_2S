class PizzaVariedad:
    
    # Constructor
    def __init__(self, nomVar: str, pre: float):
        # Requiere pre > 0.0 
        if pre <= 0.0:
            raise ValueError("El precio debe ser mayor a 0.0")
        self.nombreVariedad = nomVar
        self.precio = pre

    # Comando: establecer el nombre de la variedad
    def establecerNombreVariedad(self, nomVar: str):
        self.nombreVariedad = nomVar

    # Comando: establecer el precio
    def establecerPrecio(self, pre: float):
        # Requiere pre > 0.0
        if pre <= 0.0:
            raise ValueError("El precio debe ser mayor a 0.0")
        self.precio = pre

    # Consulta: obtener el nombre de la variedad
    def obtenerNombreVariedad(self) -> str:
        return self.nombreVariedad

    # Consulta: obtener el precio
    def obtenerPrecio(self) -> float:
        return self.precio
