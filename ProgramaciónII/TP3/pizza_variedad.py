class PizzaVariedad:
    def __init__(self, nomVar: str, pre: float):
        if pre <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.nombreVariedad = nomVar
        self.precio = pre

    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombreVariedad} - {self.precio}$"

    def establecer_nombre_variedad (self, nom_var : str):
        self.nomVar = nom_var
    
    def establecer_precio (self, pre : int):
        self.pre = pre
    
    def obtener_nombre (self):
        return self.nombre_var
    
    def obtener_precio (self):
        return self.pre